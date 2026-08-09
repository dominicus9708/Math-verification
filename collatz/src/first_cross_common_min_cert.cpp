// Exact verifier for the correction-gap common-minimizer certificate.
//
// Scope: accelerated Collatz first coefficient crossings, 1 <= q <= 100.
// The program uses exact integer arithmetic for all coefficient/correction bounds
// and ordinary uint64_t trajectory arithmetic only after checking overflow.
// It is a finite verifier, not a proof for all q.

#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using boost::multiprecision::cpp_int;

static cpp_int pow2(int e) {
    cpp_int x = 1;
    for (int i = 0; i < e; ++i) x *= 2;
    return x;
}

static int bit_length(cpp_int x) {
    int b = 0;
    while (x > 0) {
        x /= 2;
        ++b;
    }
    return b;
}

static int ceil_log3(const cpp_int& n) {
    cpp_int p = 1;
    int k = 0;
    while (p < n) {
        p *= 3;
        ++k;
    }
    return k;
}

struct QData {
    int q = 0;
    int sigma = 0;
    int h = 0;
    cpp_int P;
    cpp_int M;
    cpp_int gap;
    std::vector<int> caps;
};

static QData make_qdata(int q) {
    QData d;
    d.q = q;
    d.P = 1;
    for (int i = 0; i < q; ++i) d.P *= 3;
    d.sigma = bit_length(d.P);  // ceil(q log_2 3), since 3^q is not a power of two
    d.M = pow2(d.sigma);
    d.gap = d.M - d.P;
    d.h = std::max(0, q - ceil_log3(d.gap));

    cpp_int p = 1;
    for (int i = 0; i < q; ++i) {
        d.caps.push_back(bit_length(p) - 1);  // floor(i log_2 3)
        p *= 3;
    }
    return d;
}

static void prefix_rec(const QData& d,
                       int i,
                       int prev,
                       std::vector<int>& cur,
                       std::vector<std::vector<int>>& out) {
    if (i == d.h) {
        out.push_back(cur);
        return;
    }
    for (int x = prev + 1; x <= d.caps[i]; ++x) {
        cur.push_back(x);
        prefix_rec(d, i + 1, x, cur, out);
        cur.pop_back();
    }
}

static std::vector<std::vector<int>> prefixes(const QData& d) {
    std::vector<std::vector<int>> out;
    std::vector<int> cur;
    prefix_rec(d, 0, -1, cur, out);
    return out;
}

static std::string class_key(int q, const std::vector<int>& pref) {
    std::string s = std::to_string(q) + ":";
    for (int x : pref) s += std::to_string(x) + ",";
    return s;
}

struct Cross {
    bool ok = false;
    int k = 0;
    int q = 0;
    std::uint64_t y = 0;
    std::int64_t z = 0;
    std::vector<int> odd_positions;
};

// a[k] is the least q with 3^q >= 2^k.  Thus the coefficient has crossed
// below one exactly when current_q < a[k].
static Cross first_cross(std::uint64_t n,
                         int max_k,
                         const std::vector<int>& a) {
    std::uint64_t x = n;
    int q = 0;
    std::vector<int> odd;

    for (int k = 1; k <= max_k; ++k) {
        if (x & 1ULL) {
            ++q;
            odd.push_back(k - 1);
            if (x > (UINT64_MAX - 1) / 3) {
                std::cerr << "trajectory overflow\n";
                std::exit(2);
            }
            x = (3 * x + 1) / 2;
        } else {
            x /= 2;
        }

        if (q < a[k]) {
            return {true,
                    k,
                    q,
                    x,
                    static_cast<std::int64_t>(n) - static_cast<std::int64_t>(x),
                    odd};
        }
    }
    return {};
}

static cpp_int prefix_rmax(const QData& d, const std::vector<int>& pref) {
    std::vector<int> ds = d.caps;
    for (std::size_t i = 0; i < pref.size(); ++i) ds[i] = pref[i];

    std::vector<cpp_int> p3(d.q);
    cpp_int p = 1;
    for (int i = d.q - 1; i >= 0; --i) {
        p3[i] = p;
        p *= 3;
    }

    cpp_int R = 0;
    for (int i = 0; i < d.q; ++i) R += pow2(ds[i]) * p3[i];
    return R;
}

struct Cert {
    int q = 0;
    std::vector<int> pref;
    std::uint64_t x = 0;
    std::uint64_t y = 0;
    std::int64_t z = 0;
    std::uint64_t U = 0;
    cpp_int Rmax;
    bool found = false;
    std::uint64_t window_hits = 0;
};

int main() {
    constexpr int QMAX = 100;
    constexpr int KMAX = 170;
    constexpr std::uint64_t DISCOVERY_LIMIT = 5000000;

    // Exact coefficient-barrier table.
    std::vector<int> a(KMAX + 1);
    cpp_int p3 = 1;
    cpp_int p2 = 1;
    int q_for_barrier = 0;
    for (int k = 1; k <= KMAX; ++k) {
        p2 *= 2;
        while (p3 < p2) {
            p3 *= 3;
            ++q_for_barrier;
        }
        a[k] = q_for_barrier;
    }

    std::map<int, QData> qdata;
    std::map<std::string, Cert> certs;

    for (int q = 1; q <= QMAX; ++q) {
        qdata.emplace(q, make_qdata(q));
        const QData& d = qdata.at(q);
        for (const auto& pref : prefixes(d)) {
            Cert c;
            c.q = q;
            c.pref = pref;
            c.Rmax = prefix_rmax(d, pref);
            certs.emplace(class_key(q, pref), c);
        }
    }

    // Ascending discovery scan.  The first member of each class is, by construction,
    // its smallest positive canonical start.
    for (std::uint64_t n = 1; n <= DISCOVERY_LIMIT; ++n) {
        Cross c = first_cross(n, KMAX, a);
        if (!c.ok || c.q < 1 || c.q > QMAX) continue;

        const QData& d = qdata.at(c.q);
        std::vector<int> pref(c.odd_positions.begin(),
                              c.odd_positions.begin() + d.h);
        auto it = certs.find(class_key(c.q, pref));
        if (it == certs.end()) continue;

        Cert& C = it->second;
        if (!C.found) {
            C.found = true;
            C.x = n;
            C.y = c.y;
            C.z = c.z;
        }
    }

    for (const auto& kv : certs) {
        if (!kv.second.found) {
            std::cerr << "missing class " << kv.first << "\n";
            return 3;
        }
    }

    std::uint64_t maxU = 0;
    std::uint64_t maxW = 0;
    std::string maxWKey;

    // Compute the exact correction-gap window.
    for (auto& kv : certs) {
        const std::string& k = kv.first;
        Cert& C = kv.second;
        const QData& d = qdata.at(C.q);

        const cpp_int Rcandidate = d.M * C.y - d.P * C.x;
        if (Rcandidate < 0 || C.Rmax < Rcandidate) {
            std::cerr << "invalid correction in " << k << "\n";
            return 4;
        }

        const cpp_int Wbig = (C.Rmax - Rcandidate) / d.gap;
        const std::uint64_t W = Wbig.convert_to<std::uint64_t>();
        C.U = C.x + W;

        if (W > maxW) {
            maxW = W;
            maxWKey = k;
        }
        maxU = std::max(maxU, C.U);
    }

    if (maxU > DISCOVERY_LIMIT) {
        std::cerr << "discovery limit too small: need " << maxU << "\n";
        return 5;
    }

    // Exact finite-window z-minimum verification.
    for (std::uint64_t n = 1; n <= maxU; ++n) {
        Cross c = first_cross(n, KMAX, a);
        if (!c.ok || c.q < 1 || c.q > QMAX) continue;

        const QData& d = qdata.at(c.q);
        std::vector<int> pref(c.odd_positions.begin(),
                              c.odd_positions.begin() + d.h);
        auto it = certs.find(class_key(c.q, pref));
        if (it == certs.end()) continue;

        Cert& C = it->second;
        if (n <= C.U) {
            ++C.window_hits;
            if (c.z < C.z) {
                std::cerr << "common-minimizer failure in " << it->first
                          << ": n=" << n << " z=" << c.z
                          << " candidate=" << C.x << "," << C.z << "\n";
                return 6;
            }
        }
    }

    std::cout << "PASS classes=" << certs.size()
              << " q<=100 maxU=" << maxU
              << " maxW=" << maxW
              << " at " << maxWKey << "\n";

    for (int target : {29, 41, 82, 94, 100}) {
        for (const auto& kv : certs) {
            const Cert& C = kv.second;
            if (C.q == target) {
                std::cout << kv.first
                          << " x=" << C.x
                          << " y=" << C.y
                          << " z=" << C.z
                          << " U=" << C.U
                          << " W=" << (C.U - C.x)
                          << " hits=" << C.window_hits << "\n";
            }
        }
    }

    return 0;
}

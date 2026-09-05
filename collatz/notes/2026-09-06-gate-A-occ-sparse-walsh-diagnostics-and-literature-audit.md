# Gate A_occ sparse-regime Walsh diagnostics and literature audit

Date: 2026-09-06

## One-line result

The global selector min/max argument necessarily fails after the support barrier, but the **actual aggregate Beatty Lyapunov drift did not fail** in the audited sparse selector layers: all tested sparse blocks for `m=16,18,20,22,23` remained contracting, and root-nested fullmax conditioning also remained contracting for the audited `m=16,18` blocks.  The asymptotic problem is therefore narrowed to controlling sustained local Walsh correlation under recursive/canonical survivor selection, not to global dyadic equidistribution.

## Status

- **SAFE LEMMA:** support-aware Walsh representation and aggregate correlation criterion from the companion note.
- **FINITE DIAGNOSTIC:** exact enumeration of `F_m` for `m=16,18,20,22,23` beyond the forced support barrier.
- **FINITE ROOT DIAGNOSTIC:** exact root-nested fullmax conditioning for `m=16,18` at the audited parent depths.
- **BARRIER:** global `c_min/c_max` mixing cannot persist once `B-2>m`; arbitrary occupied subsets also need not contract.
- **LITERATURE BARRIER / SCOPE:** a much stronger uniform incomplete powers-of-3 exponential-sum theorem would approach the Moore--Schulman conjecture; it should not be hidden inside Gate A.
- **OPEN GATE:** prove asymptotic control of the actual weighted local Walsh correlations under the recursively sufficient/canonical survivor process.

No Collatz proof is claimed.

---

## 1. What the old support barrier does and does not say

For

\[
F_m=\left\{4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
a_i\in\{0,1\}\right\},
\]

there are exactly `2^m` selector atoms.

At binary depth `B`, the reduced dyadic selector table has `2^{B-2}` residue classes.  Hence

\[
B-2>m
\quad\Longrightarrow\quad
c_{\min}(m,B)=0.
\]

Therefore global pointwise min/max transfer cannot be a terminal theorem.

But this says only that **some global dyadic residues are empty**.  It does not imply that the actually occupied children of each short Beatty macro-pair are badly biased toward the high-payoff words.

The Walsh bridge isolates exactly that local question.

---

## 2. Local Walsh quantity being diagnosed

For a Beatty macro-pair `P` of length `L` and `r` rises, define

\[
g_P(u)=\left(\frac32\right)^{|u|-r},
\qquad u\in\{0,1\}^L.
\]

The unrestricted uniform factors are

\[
\sigma_{AB}=\sigma_{BA}=\frac{3125}{3456},
\qquad
\sigma_{BB}=\frac{15625}{20736}.
\]

For the actual selector-conditioned child distribution `p`, the companion Walsh lemma gives

\[
\mathbb E_p[g_P]
=\sigma_P(1+\Phi_P),
\]

with

\[
\Phi_P
=\sum_{\varnothing\ne S\subseteq[L]}
\left(-\frac15\right)^{|S|}\widehat p(S).
\]

Coefficient-invalid descendants can only reduce the actual surviving weighted output, so the selector-only quantity is an upper majorant.

Contraction is guaranteed whenever

\[
\Phi_{AB/BA}<\frac{331}{3125}\approx0.10592,
\]

or

\[
\Phi_{BB}<\frac{5111}{15625}\approx0.327104.
\]

---

## 3. Sparse selector-only exact diagnostics

The source

`collatz/src/gateA_occ_sparse_selector_diagnostic.cpp`

enumerates every one of the `2^m` integers in `F_m`, reconstructs the actual Collatz parity prefix, conditions on coefficient survival at the parent depth, and measures the aggregate weighted short-block payoff.

No assumption `c_min>0` is used.

A block is labelled **SPARSE** when its parent depth already satisfies `B>m+2`, so global pointwise selector positivity is impossible.

### m = 16

First forced sparse parent depth: `19`.

| block | type | parent atoms | selector-only upper ratio | coeff-valid ratio | signed Phi |
|---|---|---:|---:|---:|---:|
| `21 -> 27` | BB | 5,785 | 0.755805325094920 | 0.615260818922179 | +0.003032270154769 |

### m = 18

First forced sparse parent depth: `21`.

| block | type | parent atoms | selector-only upper ratio | coeff-valid ratio | signed Phi |
|---|---|---:|---:|---:|---:|
| `21 -> 27` | BB | 23,304 | 0.756146313259493 | 0.613385986517772 | +0.003484796911926 |
| `24 -> 29` | AB/BA | 17,824 | 0.906887787318273 | 0.789887391674109 | +0.002945341751025 |

### m = 20

First forced sparse parent depth: `23`.

| block | type | parent atoms | selector-only upper ratio | coeff-valid ratio | signed Phi |
|---|---|---:|---:|---:|---:|
| `24 -> 29` | AB/BA | 71,719 | 0.905007569570298 | 0.788911663541172 | +0.000865971339184 |
| `27 -> 32` | AB/BA | 55,001 | 0.907023277693910 | 0.814449367453449 | +0.003095183267249 |

### m = 22

First forced sparse parent depth: `25`.

| block | type | parent atoms | selector-only upper ratio | coeff-valid ratio | signed Phi |
|---|---|---:|---:|---:|---:|
| `27 -> 32` | AB/BA | 220,560 | 0.905657783358963 | 0.812592483294634 | +0.001585055772344 |
| `29 -> 35` | BB | 199,618 | 0.753857802218637 | 0.647553685690230 | +0.000447704755561 |
| `32 -> 37` | AB/BA | 161,645 | 0.903968021857577 | 0.812139612558821 | -0.000283685267268 |

### m = 23

First forced sparse parent depth: `26`.

| block | type | parent atoms | selector-only upper ratio | coeff-valid ratio | signed Phi |
|---|---|---:|---:|---:|---:|
| `27 -> 32` | AB/BA | 440,800 | 0.905052730301600 | 0.812532669515213 | +0.000915915495146 |
| `29 -> 35` | BB | 399,489 | 0.753444802411080 | 0.647888337207050 | -0.000100388941046 |
| `32 -> 37` | AB/BA | 323,438 | 0.904167781231565 | 0.813230981238653 | -0.000062767380388 |

### Finite conclusion

Every audited sparse selector-only upper ratio is `<1`.

The largest positive signed bias observed in these sparse blocks is

\[
\boxed{\Phi_{\max}\approx0.003484796912,}
\]

far below the corresponding sufficient thresholds.

This is a **FINITE DIAGNOSTIC ONLY**.  It does not imply a uniform asymptotic bound in `m` or depth.

---

## 4. Root-nested fullmax sparse diagnostics

Selector conditioning alone is not the terminal candidate language.  A stronger finite diagnostic was therefore run with the previously used root-global/fullmax endpoint filter nested from the root.

Source:

`collatz/src/gateA_occ_sparse_root_diagnostic.cpp`

For every audited parent depth, an atom is retained only if

1. all prior root-nested tests were passed;
2. coefficient survival still holds; and
3. its correction value `R` is endpoint-global maximal for its `(q,R mod 3^q)` key among the audited endpoint words.

This is still only a finite diagnostic; it must not be equated with a complete asymptotic minimal-counterexample theorem.

### m = 16

At depth `21`, 4,758 selector atoms survive the nested root filter.

For sparse block `21 -> 27` (BB):

\[
\boxed{
R_{\rm selector}^{\rm root}
=0.759890859481583<1,
}
\]

\[
R_{\rm coeff-valid}^{\rm root}
=0.619993958017845,
\]

and

\[
\Phi^{\rm root}\approx0.008454199181446.
\]

### m = 18

At depth `21`, 18,915 atoms survive; at depth `24`, 14,508 survive.

Sparse `21 -> 27` (BB):

\[
R_{\rm selector}^{\rm root}
=0.756726886336137,
\qquad
\Phi^{\rm root}\approx0.004255277764232.
\]

Sparse `24 -> 29` (AB/BA):

\[
R_{\rm selector}^{\rm root}
=0.906743254226560,
\qquad
\Phi^{\rm root}\approx0.002785499714237.
\]

Both remain strictly contracting.

Again this is **FINITE ROOT DIAGNOSTIC ONLY**.

---

## 5. What these diagnostics change

The earlier barrier

\[
c_{\min}=0
\]

was a genuine theorem about the failure of global min/max transfer.

The new computations show that, at least in the audited finite layers, this barrier is **not accompanied by a collapse of the actual short-block Beatty drift**.

Thus the following inference is now justified as a research-direction correction:

> The support barrier is primarily a barrier to the old proof technique, not finite evidence that the selector-conditioned Lyapunov drift itself disappears.

The asymptotic Gate A target should therefore be formulated locally on the occupied support.

---

## 6. Cumulative Walsh-drift formulation

Let successive Beatty macro-pairs be indexed by `j`, with type `P_j`, unrestricted factor `sigma_j`, and actual weighted aggregate signed Walsh bias `Phi_j`.

Whenever the selector/canonical conditioning is represented by the corresponding aggregate child distribution,

\[
\boxed{
\frac{W_{j+1}}{W_j}
\le
\sigma_j(1+\Phi_j).
}
\]

Therefore

\[
\boxed{
\frac{W_J}{W_0}
\le
\prod_{j=0}^{J-1}\sigma_j(1+\Phi_j).
}
\]

Taking logarithms,

\[
\boxed{
\log\frac{W_J}{W_0}
\le
\sum_{j<J}
\left[
\log\sigma_j+\log(1+\Phi_j)
\right].
}
\]

Hence it is sufficient to prove

\[
\boxed{
\sum_{j<J}
\left[
\log\sigma_j+\log(1+\Phi_j)
\right]
\longrightarrow-\infty.
}
\]

This is strictly weaker than requiring every block to contract.

Bad blocks with `sigma_j(1+Phi_j)>=1` are allowed, provided their cumulative excess is dominated by the good blocks.

A crude worst-type average criterion is

\[
\limsup_{J\to\infty}
\frac1J\sum_{j<J}\log(1+\Phi_j)
<
\log\frac{3456}{3125},
\]

because `3125/3456` is the larger of the two unrestricted factors.

The exact blockwise criterion is preferable because BB blocks have the stronger factor `15625/20736`.

---

## 7. Why a full global Fourier theorem is unnecessarily strong

The ternary selector Fourier transform modulo `2^r` is the finite Riesz product

\[
|\widehat\mu_{m,r}(t)|
=
\prod_{k=0}^{m-1}
\left|\cos\frac{\pi t3^k}{2^r}\right|.
\]

A hypothetical uniform theorem forcing a fixed cosine-average gap for every nonzero `t mod 2^r` over only `O(r)` consecutive powers of `3` would immediately imply exponential decay of this product by AM--GM.

Indeed, if

\[
\frac1m\sum_{k<m}
\cos\frac{2\pi t3^k}{2^r}
\le1-\delta,
\]

then

\[
|\widehat\mu_{m,r}(t)|^2
=
\prod_{k<m}
\frac{1+\cos(2\pi t3^k/2^r)}2
\le
\left(1-\frac\delta2\right)^m.
\]

But uniform incomplete powers-of-3 exponential-sum cancellation of this strength is closely related to the Moore--Schulman tree-code exponential-sum conjecture, which remains an open research problem in the literature.

Full multiplicative-subgroup estimates of Bourgain type concern a substantially longer/full subgroup average and do not by themselves provide the required `O(r)` incomplete-orbit theorem.

Therefore Gate A should **not** silently assume a global Fourier theorem of Moore--Schulman strength.

The local Walsh formulation avoids that overreach: only `31` or `63` short-block correlations, under the actual survivor weighting, are needed.

---

## 8. Revised Gate A_occ target

The current target can be stated as follows.

### Gate A_occ-WR — weighted recurrent Walsh control

For the actual recursively sufficient / canonical survivor process, prove that the aggregate macro-pair correlations satisfy either

\[
\sum_j
\left[
\log\sigma_j+\log(1+\Phi_j)
\right]
=-\infty,
\]

or a stronger Foster--Lyapunov/finite-state condition implying it outside a bounded surplus strip.

This would establish high-surplus tail control without requiring global dyadic selector equidistribution.

The finite data suggest that `Phi_j` can stay much smaller than the available contraction margin even after the support barrier, but this observation is not yet a theorem.

---

## 9. DSD audit

### SAFE

1. Exact local Walsh expansion.
2. Aggregate weighted-parent correlation formula.
3. Cumulative logarithmic drift implication.
4. Atom-floor conversion once a fixed finite layer's total weighted mass is driven below one atom.

### FINITE ONLY

1. Sparse selector diagnostics for `m=16,18,20,22,23`.
2. Root-nested sparse diagnostics for `m=16,18`.
3. The observed maximum `Phi approximately 0.003485`.

### BARRIERS

1. Global min/max transfer dies once `B-2>m`.
2. Arbitrary occupied subsets do not contract: the all-one child has payoff `9/4`.
3. A uniform global incomplete-orbit Fourier theorem strong enough to trivialize the problem risks importing an independent open exponential-sum conjecture.

### OPEN

1. Prove asymptotic recurrent/cumulative Walsh control after recursive/root/canonical conditioning.
2. Combine that high-surplus recurrence with Gate B's bounded-strip killing mechanism.
3. Complete Gate C's same-integer/minimal-counterexample closure.

---

## 10. Current bottleneck

After this reduction the principal Gate A question is no longer

> Are all dyadic selector fibres approximately uniform?

It is

\[
\boxed{
\text{Can recursive/canonical survivor selection sustain enough positive correlation}
\text{ with the 31/63 high-payoff Walsh modes to cancel Beatty drift forever?}
}
\]

That is the next theorem target.

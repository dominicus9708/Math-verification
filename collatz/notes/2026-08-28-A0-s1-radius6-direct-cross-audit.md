# A0 s=1: first-75 radius-six direct cross-audit

Date: 2026-08-28

Status: **SAFE finite closure / SAFE strengthened necessary condition / C4F OPEN.**

This audit extends the previously certified first-75 Hamming shell from radius five to radius six and independently checks the 72-bit deterministic-extension implementation against a direct 75-bit parity-address enumeration.

## 1. Audit correction before promotion

A first 72-bit implementation temporarily disagreed with the existing radius-one-through-five counts because it counted addresses whose actual orbit had already lost the pure-ballot condition at positions 73--75.

After imposing the required condition that the complete first-75 word itself remains pure-ballot, the 72-bit deterministic-extension method reproduces the existing direct-75-bit bounded counts exactly:

| first-75 Hamming distance | bounded physical words | latest first ballot failure |
|---:|---:|---:|
| 0 | 0 | -- |
| 1 | 1 | 88 |
| 2 | 18 | 110 |
| 3 | 386 | 161 |
| 4 | 6,174 | 222 |
| 5 | 58,212 | 378 |

This discrepancy was therefore an implementation-classification error, not a failure of the 2-adic parity-address identity.

## 2. Exact distance-six shell

The direct 75-bit certificate exhausts every pure-ballot word at exact Hamming distance six from the threshold prefix.

Exact counts are

\[
\boxed{26\,996\,805}
\]

pure-ballot words,

\[
\boxed{1\,687\,133}
\]

addresses in the strict physical shell

\[
2^{71}<X<2^{72},
\]

and, after the already certified necessary upper bound

\[
X\le3\,295\,414\,002\,074\,039\,191\,016,
\]

exactly

\[
\boxed{668\,333}
\]

bounded physical candidates.

Every one of the 668,333 candidates is continued by the actual Collatz map.  All lose the pure-ballot condition by prefix

\[
\boxed{405}.
\]

There is no scan survivor through prefix 1000, and because the latest first failure is 405, the finite closure is already complete by 405.

## 3. Strengthened necessary condition

Combining the previously certified radii zero through five with the new exact radius-six closure gives

\[
\boxed{
d_{75}\ge7.
}
\]

Thus any full A0 s=1 survivor satisfying the current physical-shell and correction-envelope conditions must differ from the exact threshold word in at least seven of its first 75 parity positions.

The total number of bounded physical words audited across radii zero through six is

\[
\boxed{733\,124}.
\]

Every one fails pure ballot.

## 4. Independent implementation routes

Two routes were compared.

**Route A: 72-bit closure.**  Enumerate the first 72 bits, compute the unique physical address modulo \(2^{72}\), then obtain positions 73--75 and all later positions from the deterministic orbit of that address.

**Route B: direct 75-bit address.**  Enumerate the full pure-ballot 75-bit word, compute

\[
A_{75}(w)=-\sum_r3^{-r}2^{a_r}\pmod{2^{75}},
\]

require the resulting ordinary address to lie in the 72-bit physical shell and under the certified \(X\) bound, and then extend its orbit.

The two routes agree on the already known radii and on the exact distance-six bounded count and failure envelope.

## 5. DSD audit

### SAFE

- exact first-75 distance-six pure-ballot count `26,996,805`;
- strict-shell count `1,687,133`;
- bounded physical count `668,333`;
- deterministic extension of all bounded candidates;
- latest first pure-ballot failure `405`;
- combined audited bounded population `733,124`;
- strengthened necessary condition \(d_{75}\ge7\).

### NOT PROMOTED

- no statistical extrapolation from radius six to larger radii;
- no identification of Hamming defect with the ordered-position/Hensel defect coordinates;
- no use of pure ballot as a substitute for `C4F`;
- no conclusion that A0 s=1 as a whole is closed;
- no Collatz proof claim.

### OPEN

The next rigorous gate remains the `C4F`-relevant memory needed for legal state merging on the Christoffel DAG.  The pure-ballot/address summary may be used only for predicates it has been proved to preserve.

## Companion certificates

- `collatz/src/A0_s1_75bit_radius6_block_jump_certificate.cpp`
- `collatz/src/A0_s1_72bit_near_threshold_block_jump_certificate.py`
- `collatz/src/A0_s1_composable_ballot_address_state_certificate.py`

# `A_30` hybrid bootstrap and the growing-resolution transition

Date: 2026-08-12

Status: **finite exact recursive-sufficiency bootstrap through selector depth 30**, together with a methodological transition from fixed-resolution pruning to a growing-resolution survivor hierarchy. The certificate advances the contiguous verified floor by `4*3^30 = 823,564,528,378,596` ordinary integers. This does not prove the full Collatz conjecture.

## 1. Representative family

Define

\[
A_{30}=
\left\{
4\left(3^{44}+\sum_{i=0}^{29}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
\]

Then

\[
\boxed{|A_{30}|=2^{30}=1,073,741,824.}
\]

If every member of `A_30` is recursive, the representative-block bootstrap lemma advances the verified floor to

\[
\boxed{
V_{30}=4(3^{44}+3^{30})+2
=3,939,084,432,298,973,310,122.
}
\]

The interval increment over

\[
V_0=4\cdot3^{44}+2
\]

is

\[
\boxed{
V_{30}-V_0
=4\cdot3^{30}
=823,564,528,378,596.
}
\]

## 2. Fixed-depth class proposition layer

Use binary resolution

\[
B_{\max}=18.
\]

The exact uniform forward-descent cylinder test removes

\[
\boxed{950,949,589}
\]

representatives without deterministic trajectory continuation.

Thus the remaining forward-class fringe is

\[
\boxed{
122,792,235
}
\]

representatives.

An exact OpenMP/128-bit hybrid verifier follows only this fringe and finds:

\[
\boxed{
\max\tau_<=425,
}
\]

with no failure and no overflow.

The same extremal representative already seen at selector depth 28 remains maximal:

\[
\text{mask}=140,506,676,
\]

\[
S=7,662,208,534,542,
\]

\[
N_*=3,939,083,639,383,279,069,695.
\]

Therefore every member of `A_30` is recursive and the `V_30` interval jump is certified.

## 3. Additional cross-place reverse reduction

A separate exact run using the low-six-trit / `3`-adic optimal-backtrace channel at all odd endpoints through depth 18 removes an additional

\[
\boxed{38,793,328}
\]

representatives after the forward class layer.

This leaves only

\[
\boxed{83,998,907}
\]

representatives requiring trajectory continuation, about

\[
\boxed{7.8230\%}
\]

of the full `A_30` family.

The reverse-enhanced run reproduces the same maximum first-descent depth `425` and the same extremal representative. The simpler public bootstrap verifier in the repository uses the forward-only class layer; the reverse enhancement is recorded as an independently executed strengthening of the class architecture.

## 4. Compression scales

At the forward-only public certificate level,

\[
\frac{4\cdot3^{30}}{122,792,235}
\approx6.707\times10^6.
\]

With the reverse-enhanced fringe,

\[
\boxed{
\frac{4\cdot3^{30}}{83,998,907}
\approx9.804\times10^6.
}
\]

Thus at this stage each explicitly continued trajectory accounts for millions of ordinary integers in the final interval inference.

## 5. Why fixed B cannot be the terminal mechanism

The fixed-resolution mixing theorem shows that with `B_max=18` held constant, additional ternary selector digits asymptotically mix across the reduced dyadic group. Therefore the surviving mass approaches a positive residue density rather than zero.

The observed forward-only fringe fractions already stabilize:

\[
\begin{array}{c|c}
d&\text{forward-class surviving fraction}\\\hline
28&0.1143498085\\
29&0.1143577397\\
30&0.1143591804
\end{array}
\]

while the exact fixed-residue limit is

\[
14,990/131,072
=0.1143646240\ldots.
\]

Hence the next structural transition is mandatory:

\[
\boxed{B=B(d)\to\infty.}
\]

## 6. Finite survival function at d=28

As a diagnostic for the needed growing resolution, define

\[
S_{28}(B)
:=
\#\{N\in A_{28}:\tau_<(N)>B\}.
\]

Exact aggregation from the already certified `A_28` scan gives

\[
\begin{array}{c|r|c}
B&S_{28}(B)&S_{28}(B)/2^{28}\\\hline
18&30,695,543&1.1434981\times10^{-1}\\
30&12,773,439&4.7584768\times10^{-2}\\
50&3,562,753&1.3272289\times10^{-2}\\
72&1,058,175&3.9420091\times10^{-3}\\
100&256,937&9.5716491\times10^{-4}\\
150&27,661&1.0304525\times10^{-4}\\
200&3,317&1.2356788\times10^{-5}\\
250&459&1.7099082\times10^{-6}\\
300&60&2.2351742\times10^{-7}\\
350&6&2.2351742\times10^{-8}\\
400&2&7.4505806\times10^{-9}\\
425&0&0
\end{array}
\]

This table is diagnostic finite data, not an asymptotic decay theorem.

Its role is to identify the next proof object: a growing-resolution survivor-cylinder function whose decay can be bounded without re-enumerating all representative starts.

## 7. Next theorem target

Define a nested family of dangerous dyadic/cross-place cylinders

\[
\mathcal S_B
\]

such that every representative surviving through depth `B` lies in `S_B`, and

\[
\mathcal S_{B+1}\subseteq\pi^{-1}(\mathcal S_B).
\]

The desired structural theorem is a quantitative bound on the actual ternary-core lifts contained in these nested sets, for example a contraction estimate at a resolution `B(d)` growing with `d`.

The fixed-resolution mixing barrier proves that `B(d)` cannot remain bounded. The finite `S_28(B)` profile shows that increasing resolution is empirically powerful. The unresolved task is to replace that finite profile by a reusable inequality or dominance theorem.

## 8. Reproducibility

Forward-class hybrid verifier:

`collatz/src/m44_low30_forward_hybrid_bootstrap.cpp`

Earlier exact components used in the architecture:

- `m44_cross_place_cylinder_sieve.py`;
- `m44_low28_hybrid_class_bootstrap.cpp`;
- `m44_low28_recursive_bootstrap.cpp`.

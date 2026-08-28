# A0 s=1: radius-seven defect and Christoffel real-envelope audit

Date: 2026-08-28

Status: **SAFE necessary-condition strengthening.** The dependency order is explicitly acyclic; the stronger `X` bound is derived only after the radius-seven closure under the older bound.

## 1. Dependency order

The legal implication chain is

\[
\boxed{
\text{old correction envelope}
\Rightarrow X\le X_{\rm old}
\Rightarrow \text{radius-7 closure}
\Rightarrow d_{75}\ge8
\Rightarrow \eta\ge\eta_{75}^{\min}
\Rightarrow X\le X_{\rm new}.
}
\]

The stronger `X_new` bound is **not** used to justify the earlier radius-seven closure. Re-filtering with `X_new` is only a later corollary.

This ordering is required by the DSD audit to avoid circular pruning.

## 2. Exact normalized defect forced by `d_75>=8`

For a pure lower-ballot word with the same final odd count as the threshold word, let

\[
a_r\le t_r
\]

be the candidate and threshold positions of the `r`-th odd symbol. Define the normalized correction defect

\[
\eta
:=
\frac{C_{\rm th}-C}{3^{j_0}}
=
\sum_r 3^{-r}\left(2^{t_r}-2^{a_r}\right).
\]

Every summand is nonnegative.

An exact dynamic program over the first 75 symbols, with Hamming distance capped at 8, gives

\[
\boxed{
\eta\ge
\eta_{75}^{\min}
=
\frac{150621601264545747200}
{328256967394537077627}
\approx0.45885271669957073.
}
\]

The unique minimizing pattern retained by the DP has flips at zero-based positions

\[
\boxed{
8,9,27,28,46,47,65,66.
}
\]

Equivalently it performs four one-place left shifts of threshold odd symbols, at ranks

\[
7,19,31,43.
\]

Hence

\[
\eta_{75}^{\min}
=
\frac{2^8}{3^7}
+
\frac{2^{27}}{3^{19}}
+
\frac{2^{46}}{3^{31}}
+
\frac{2^{65}}{3^{43}}.
\]

Future deviations can only increase the full defect, so this is a valid lower bound for every full survivor.

## 3. Earliest-defect consequence

A second exact finite DP asks how late the first disagreement from the threshold can occur while still accumulating at least eight disagreements by depth 75 under the pure-ballot rule.

The answer is

\[
\boxed{f_{\max}=65}
\]

in zero-based coordinates.

Thus every surviving word must have its first threshold displacement no later than position 65. In the normalized defect language this yields

\[
\boxed{v_2(\eta)\le65}
\]

for the first displaced-odd interpretation. This is a finite structural corollary, not yet the main pruning mechanism.

## 4. Real evaluation of the 129-node Christoffel DAG

The lower mechanical base block `L` has

\[
|L|=J_0=10439860591,
\qquad
q(L)=R_0=6586818670.
\]

Its Stern-Brocot/Christoffel construction uses only 129 DAG nodes.

For a block `w`, carry

\[
m(w)=\frac{3^{q(w)}}{2^{|w|}},
\qquad
c(w)=\frac{C(w)}{2^{|w|}}.
\]

Concatenation obeys

\[
\boxed{
m(uv)=m(u)m(v)}
\]

and

\[
\boxed{
c(uv)=m(v)c(u)+c(v).}
\]

The certificate evaluates these recurrences with 256-bit outward fixed-point intervals. Bounds for `ln 2` and `ln 3` come from exact `atanh` series with rigorous positive tails; exponentials use outward-rounded Taylor intervals. No floating-point number participates in an assertion.

The result is

\[
\boxed{
4751385314
<
\frac{C(L)}{2^{J_0}}
<
4751385315.
}
\]

## 5. Full threshold correction without word expansion

The previously certified ten-block decomposition is

\[
W_{\rm th}=U L^9,
\]

with

\[
C(U)=C(L)+3^{R_0}.
\]

Therefore the same interval transfer gives

\[
\boxed{
47513853148
<
\frac{C(W_{\rm th})}{2^{t_0}}
<
47513853149.
}
\]

This materially improves the older safe but very coarse envelope

\[
\frac{C}{2^{t_0}}<j_0=65868186701.
\]

## 6. Apply the forced radius-seven defect

For a surviving word,

\[
C=C(W_{\rm th})-3^{j_0}\eta.
\]

Let

\[
\lambda=\frac{3^{j_0}}{2^{t_0}}.
\]

Using the certified lower interval for `lambda` together with `eta>=eta_75^min` yields the safe simple bound

\[
\boxed{
\frac{C}{2^{t_0}}<47513853147.
}
\]

The exact fixed-point certificate retains more precision internally.

## 7. Stronger physical `X` bound

The bridge relation is

\[
\frac{C}{2^{t_0}}
=(3-\lambda)X-L_-,
\]

with the previously certified debit corridor

\[
L_-\le934928480993.
\]

Using the outward interval upper bound for `lambda` gives a rigorous lower bound on

\[
\delta=3-\lambda>0.
\]

Combining all certified intervals gives

\[
\boxed{
X\le
3234977022306677631165.
}
\]

The previous bound was

\[
X\le3295414002074039191016.
\]

Hence the exact reduction is

\[
\boxed{
60436979767361559851.
}
\]

Relative to the original 72-bit shell above `2^71`, the retained fraction falls from about `0.39566` to about `0.37007`.

## 8. Finite radius recount under the stronger bound

This recount is a **corollary only**. It is not used upstream.

Applying the new `X` bound to the already enumerated radius layers gives:

| `d_75` | bounded under old `X_max` | bounded under new `X_max` |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 2 | 18 | 18 |
| 3 | 386 | 364 |
| 4 | 6,174 | 5,770 |
| 5 | 58,212 | 54,453 |
| 6 | 668,333 | 624,958 |
| 7 | 4,662,684 | 4,361,545 |

Total bounded candidates through radius 7 decrease from

\[
5395808
\]

to

\[
\boxed{5047109}.
\]

All of these layers were already shown to fail the pure-ballot condition under actual Collatz continuation.

## 9. DSD classification

### EXACT / SAFE

- radius-seven finite closure under the old bound;
- `d_75>=8`;
- exact 75-step defect DP;
- `eta>=eta_75^min`;
- 129-node exact Christoffel DAG structure;
- outward fixed-point interval arithmetic;
- threshold normalized-correction interval;
- stronger `X_new` necessary bound.

### COROLLARY ONLY

- recounting the already-closed finite radius layers with `X_new`.

### NOT USED / STILL OPEN

- `C4F` identification;
- interval-filling assumptions for the correction language;
- exact full correction-language membership;
- extrapolation from radius 7 to arbitrary Hamming radius.

## 10. Next structural target

The brute-force distance-eight layer contains more than one billion pure-ballot first-75 words, so radius enumeration is no longer the economical route.

The preferred next step is to use the forced normalized defect and its 2-adic first-defect coordinate together with the mixed-radix / renewal-gap constraints. The goal is to show that a defect large enough to satisfy `d_75>=8` cannot simultaneously satisfy the remaining A0 bridge channels, rather than enumerating the entire distance-eight shell.

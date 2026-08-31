# A0 s=1 Route-B finite-horizon adaptive decoder termination theorem

## Purpose

This note upgrades the existing finite adaptive-decoder regressions to an exact theorem at every **fixed finite word length**.

It does **not** prove a uniform resolution bound independent of word length, and it does **not** prove global Collatz closure.

## Fixed-(h,q) correction language

Let a binary parity word `W` have length `h`, exactly `q` odd positions

\[
0\le a_1<\cdots<a_q<h,
\]

and correction

\[
C(W)=\sum_{r=1}^q 3^{q-r}2^{a_r}.
\]

The exact affine identity is

\[
2^hT^h(x)=3^q x+C(W).
\]

The existing fixed-(h,q) correction-language decoder gives two exact facts:

1. ordinary `C(W)` is injective at fixed `(h,q)`;
2. even `C(W) mod 2^h` is injective at fixed `(h,q)`.

The second fact follows equivalently from the unique parity start address

\[
x(W)\equiv -C(W)(3^q)^{-1}\pmod{2^h}.
\]

Therefore any two distinct fixed-(h,q) words satisfy

\[
C(U)\not\equiv C(V)\pmod{2^h}.
\]

So the dyadic observation depth

\[
\boxed{K_*(h,q)=h}
\]

is always sufficient to separate every fixed-(h,q) correction word.

## Exact ternary diameter bound

Because the odd positions are strictly increasing,

\[
a_r\ge r-1,
\qquad
a_r\le h-q+r-1.
\]

Hence, for `0<q<h`,

\[
C_{\min}(h,q)
=\sum_{r=1}^q3^{q-r}2^{r-1}
=3^q-2^q,
\]

and

\[
C_{\max}(h,q)
=\sum_{r=1}^q3^{q-r}2^{h-q+r-1}
=2^{h-q}(3^q-2^q).
\]

Therefore the diameter of the fixed-(h,q) correction language obeys the exact bound

\[
\boxed{
D_{h,q}
=(2^{h-q}-1)(3^q-2^q).
}
\]

For any two fixed-(h,q) words,

\[
|C(U)-C(V)|\le D_{h,q}.
\]

Define

\[
L_*(h,q)=\min\{L\ge0:3^L>D_{h,q}\}.
\]

If

\[
C(U)\equiv C(V)\pmod{3^{L_*(h,q)}},
\]

then the difference is a multiple of `3^{L_*}` whose absolute value is smaller than `3^{L_*}`. Hence the difference is zero, and fixed-(h,q) injectivity gives `U=V`.

Thus

\[
\boxed{L\ge L_*(h,q)\Longrightarrow\text{ternary residue alone separates the fixed-(h,q) language}.}
\]

The degenerate cases `q=0` and `q=h` contain only one word and are already singleton classes.

## Target-collider monotonicity

Let `T` be any candidate subset of one fixed `(h,q)` class and let `t in T` be a target. Define

\[
\mathcal A_{K,L}(t)
=
\{W\in T\setminus\{t\}: C(W)\equiv C(t)\pmod{2^K3^L}\}.
\]

Then

\[
\mathcal A_{K+1,L}(t)\subseteq\mathcal A_{K,L}(t),
\qquad
\mathcal A_{K,L+1}(t)\subseteq\mathcal A_{K,L}(t).
\]

No refinement step can create a new collider.

Moreover,

\[
K\ge h\quad\Longrightarrow\quad\mathcal A_{K,L}(t)=\varnothing,
\]

and

\[
L\ge L_*(h,q)\quad\Longrightarrow\quad\mathcal A_{K,L}(t)=\varnothing.
\]

## Finite-horizon adaptive termination theorem

Consider any adaptive decoder that starts from a finite resolution `(K_0,L_0)` and, while a non-target collider remains, increases exactly one of `K` or `L` by one.

For every fixed finite `(h,q)` candidate class, this decoder must terminate after finitely many refinements.

Indeed, an unresolved path cannot pass either barrier

\[
K=h
\]

or

\[
L=L_*(h,q).
\]

Therefore there is no infinite refinement path at fixed finite `(h,q)`.

A simple safe refinement-count bound is

\[
\boxed{
N_{\rm refine}
\le (h-K_0)+(L_*(h,q)-L_0)
}
\]

when the initial resolutions lie below both barriers. The bound is intentionally non-sharp; the actual decoder can terminate much earlier.

This theorem does not depend on the greedy axis-selection rule. Greedy refinement is an efficiency policy, not a termination assumption.

## Existing length-18 target as a check

For the threshold target used in the finite target-aware regression,

\[
(h,q)=(18,12).
\]

The generic fixed-(18,12) correction diameter is

\[
D_{18,12}
=(2^6-1)(3^{12}-2^{12})
=33,222,735.
\]

Since

\[
3^{15}=14,348,907 < D_{18,12}<43,046,721=3^{16},
\]

we obtain the target-independent fixed-class bound

\[
L_*(18,12)=16.
\]

The previously audited target+ballot subclass is substantially smaller: its actual target-specific maximum ternary collision valuation is `10`, and the greedy regression isolates the target at `(K,L)=(1,11)`.

Thus the finite regression is consistent with, and much sharper than, the general fixed-horizon theorem.

## What this closes

✅ collider sets are nested under either resolution refinement;

✅ new target candidates cannot appear merely because resolution increases;

✅ every fixed finite `(h,q)` correction class has a universal dyadic separating depth `K=h`;

✅ every fixed finite `(h,q)` correction class has an explicit finite ternary separating depth `L_*(h,q)`;

✅ every one-axis-at-a-time adaptive decoder terminates at fixed finite `(h,q)`, independently of the greedy policy;

✅ finite-horizon adaptive termination no longer requires a separate ambiguity-cardinality descent hypothesis.

## What remains open

❌ `K_*=h` and `L_*(h,q)` grow with the horizon; no length-independent observation-depth theorem has been proved;

❌ this theorem does not by itself compress arbitrary long words into a fixed global finite-state decoder;

❌ recursive long-word closure still requires either a horizon-normalized quotient or a well-founded descent that replaces the growing absolute resolution by a smaller recursive subproblem;

❌ no global Collatz conclusion is claimed.

## DSD audit

The audit distinction is now sharper:

- **finite enumeration evidence**: earlier length-12 and length-18 decoder regressions;
- **exact finite-horizon theorem**: the result above, valid for every fixed finite `(h,q)` without enumeration;
- **global long-language lift**: still open because the required separating depth is not yet uniform in `h`.

The former finite-regression bottleneck has therefore moved: the unresolved question is not whether finite words eventually separate, but whether the scale growth can be quotiented, renewed, or forced to descend recursively.

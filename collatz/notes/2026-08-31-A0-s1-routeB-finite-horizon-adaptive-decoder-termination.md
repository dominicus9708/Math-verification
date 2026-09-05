# A0 s=1 Route-B finite-horizon adaptive decoder termination theorem

## Purpose

This note combines an already-proved fixed-(h,q) dyadic termination theorem with a new exact ternary diameter bound and derives a two-axis adaptive-termination theorem at every **fixed finite word length**.

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

The repository already contains the stronger fixed-(h,q) dyadic theorem:

> If `U != V` have the same `(h,q)`, then
> \[
> v_2(C(U)-C(V))\le h-2.
> \]

Its proof uses the prefix-channel bijection modulo `2^(h-1)`: equality of the first `h-1` parity symbols together with equal total one-count `q` forces the final symbols to agree as well.

Therefore, for every non-singleton fixed-(h,q) class,

\[
\boxed{K_{\rm dy}(h,q)=h-1}
\]

is sufficient to distinguish all words.

This is stronger than the weaker `K=h` consequence of full parity-address injectivity and must be used as the correct dyadic stopping barrier.

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

Therefore the exact correction-language diameter is bounded by

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
L_{\rm ter}(h,q)=\min\{L\ge0:3^L>D_{h,q}\}.
\]

If

\[
C(U)\equiv C(V)\pmod{3^{L_{\rm ter}(h,q)}},
\]

then `C(U)-C(V)` is a multiple of `3^L` whose absolute value is smaller than `3^L`. Hence the difference is zero, and ordinary fixed-(h,q) correction injectivity gives `U=V`.

Thus

\[
\boxed{L\ge L_{\rm ter}(h,q)\Longrightarrow\text{ternary residue alone separates the fixed-(h,q) language}.}
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
\boxed{
\mathcal A_{K+1,L}(t)\subseteq\mathcal A_{K,L}(t),
\qquad
\mathcal A_{K,L+1}(t)\subseteq\mathcal A_{K,L}(t).
}
\]

No refinement step can create a new collider.

Moreover, for a non-singleton fixed-(h,q) class,

\[
K\ge h-1\quad\Longrightarrow\quad\mathcal A_{K,L}(t)=\varnothing,
\]

and

\[
L\ge L_{\rm ter}(h,q)\quad\Longrightarrow\quad\mathcal A_{K,L}(t)=\varnothing.
\]

## Two-axis finite-horizon adaptive termination theorem

Consider any adaptive decoder that starts from finite resolution `(K_0,L_0)` and, while a non-target collider remains, increases exactly one of `K` or `L` by one.

For every fixed finite `(h,q)` candidate class, this decoder must terminate after finitely many refinements, regardless of how the axis is selected.

Indeed, an unresolved path cannot reach either stopping barrier

\[
K=h-1
\]

or

\[
L=L_{\rm ter}(h,q).
\]

Since each refinement raises one coordinate by one, there is no infinite path inside the finite rectangle

\[
K_0\le K<h-1,
\qquad
L_0\le L<L_{\rm ter}(h,q).
\]

A simple deliberately non-sharp bound is

\[
\boxed{
N_{\rm refine}
\le
\max(0,h-1-K_0)+
\max(0,L_{\rm ter}(h,q)-L_0)
}
\]

before one of the two universal stopping barriers must be reached.

Thus the greedy target-aware policy is an efficiency rule, not a termination hypothesis.

## Partition-rank consequence

At any `(K,L)`, equality of correction residues partitions a fixed finite target class. Raising `K` or `L` only refines this partition.

For a finite candidate set `T`, define the unresolved-pair rank

\[
R_{K,L}
=
\sum_{B\in\Pi_{K,L}}\binom{|B|}{2}.
\]

Then

\[
R_{K+1,L}\le R_{K,L},
\qquad
R_{K,L+1}\le R_{K,L}.
\]

Whenever a refinement actually splits a bucket, the inequality is strict. This gives a valid finite partition rank, but the stopping-barrier theorem above is stronger for termination because it also rules out an infinite sequence of resolution increases that temporarily produce no split.

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

we obtain

\[
L_{\rm ter}(18,12)=16.
\]

The existing dyadic theorem gives the generic same-(18,12) barrier

\[
K_{\rm dy}=17.
\]

The previously audited target+ballot subclass is much smaller: its target-specific maximum ternary collision valuation is `10`, and the greedy regression isolates the target at `(K,L)=(1,11)`.

So the observed finite path is consistent with, and much sharper than, the generic fixed-class barriers `(17,16)`.

## What is genuinely added here

✅ existing result reused: fixed-(h,q) dyadic separation satisfies `K<=h-1`;

✅ new exact bound: the fixed-(h,q) correction-language ternary diameter is `(2^(h-q)-1)(3^q-2^q)`;

✅ new combined consequence: either dyadic or ternary resolution has an explicit finite stopping barrier for every fixed `(h,q)`;

✅ new scheduler-independent consequence: any one-axis-at-a-time adaptive refinement path terminates at every fixed finite horizon;

✅ collider sets and observation partitions are monotone under both axes.

## What remains open

❌ both universal barriers depend on the horizon: `K_{dy}=h-1` and `L_{ter}=L_{ter}(h,q)` grow with `(h,q)`;

❌ this does not compress arbitrary long words into one fixed global finite-state decoder;

❌ recursive long-word closure still requires a horizon-normalized quotient, renewal rule, or a well-founded descent that turns a long unresolved class into a strictly smaller recursive subproblem;

❌ target identification remains logically distinct from Route-B language membership;

❌ no global Collatz conclusion is claimed.

## DSD audit

The proof levels are now separated as follows:

- **exact prior theorem**: fixed-(h,q) dyadic termination, `v2(Delta C)<=h-2`;
- **exact new finite-horizon lemma**: ternary correction diameter and `L_{ter}` barrier;
- **exact combined theorem**: arbitrary adaptive axis scheduling terminates for each fixed finite `(h,q)`;
- **finite regression**: length-12 and length-18 efficiency measurements;
- **open globalization**: eliminate or recursively normalize the growth of the required observation scale with `h`.

Therefore the long-word bottleneck is no longer finite-horizon termination. It is **scale normalization/globalization**.

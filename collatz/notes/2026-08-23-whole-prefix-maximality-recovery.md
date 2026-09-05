# Whole-prefix maximality recovers an unconditional deterministic pruning channel

Date: 2026-08-23

Status: **unconditional root-level predecessor theorem + exact depth-28 finite certificates. This replaces, but does not yet asymptotically reproduce, the audited repeated-local-maximality argument. This is not a proof of the Collatz conjecture.**

## 1. Why this survives the local-pullback audit

The audited repeated L7/L14/L19 argument attempted to replace a parity block after an already existing orbit prefix. A local sibling credit introduced after `p` previous odd steps pulls back to the original root with a denominator `3^p`, so a local smaller start is not automatically a smaller integer root predecessor.

The whole-prefix argument has no such denominator.

For a complete length-`H` parity prefix `w`, write

\[
T^H(N)=\frac{3^qN+R_w}{2^H}.
\]

If another complete length-`H` word `u` has the same odd count and

\[
R_u=R_w+3^q d,\qquad d>0,
\]

then the smaller root

\[
\boxed{M=N-d}
\]

satisfies

\[
\frac{3^qM+R_u}{2^H}
=
\frac{3^qN+R_w}{2^H}.
\]

Thus `M` and `N` merge after exactly `H` steps. If `N` were a minimal counterexample and `0<M<N`, this is impossible.

Therefore every sufficiently large minimal counterexample must use, at every chosen root horizon, the maximum-correction representative of its complete class

\[
(q,R\bmod 3^q).
\]

This is a root-level theorem and is unaffected by the local-block pullback defect.

## 2. Prefix inheritance

A useful simplification is that terminal whole-prefix maximality already contains all earlier root-prefix maximality constraints.

Suppose an earlier prefix of length `t` is non-maximal by

\[
R'_t-R_t=3^{q_t}d>0.
\]

Append the same later parity suffix, containing `r` additional odd steps, to both prefixes. Under correction composition the final correction difference is multiplied by `3^r`:

\[
R'_H-R_H=3^r(R'_t-R_t)=3^{q_t+r}d=3^{q_H}d.
\]

Hence the complete length-`H` word would also be non-maximal.

So no repeated local-block product is needed:

\[
\boxed{\text{whole-prefix maximal at }H\Longrightarrow\text{whole-prefix maximal at every earlier prefix}.}
\]

## 3. Exact depth-28 coefficient-survivor theorem

Among the exact length-28 coefficient-surviving words,

\[
\boxed{3,524,586}
\]

words survive the coefficient barrier.

Complete same-`q` correction-class maximality leaves

\[
\boxed{2,882,872}
\]

and removes

\[
\boxed{641,714}.
\]

The per-`q` counts are

\[
\begin{array}{c|r|r|r|r}
q&\text{coefficient}&\text{maximal}&\text{removed}&d_{\max}\\\hline
18&663,535&535,688&127,847&29\\
19&1,236,935&1,003,902&233,033&15\\
20&898,798&736,512&162,286&7\\
21&464,889&385,729&79,160&7\\
22&185,684&156,461&29,223&3\\
23&57,923&49,738&8,185&1\\
24&13,953&12,246&1,707&1\\
25&2,520&2,270&250&1\\
26&322&299&23&1\\
27&26&26&0&0\\
28&1&1&0&0
\end{array}
\]

The global predecessor-credit bound is therefore only

\[
\boxed{d_{\max}=29.}
\]

Consequently this complete depth-28 maximality filter is valid for any hypothetical minimal counterexample `N>29`.

Certificate:

`collatz/src/depth28_whole_prefix_endpoint_maximality_certificate.cpp`.

## 4. Mixed-q whole-prefix siblings add no new depth-28 words

For an alternate word with `q+s` odd steps,

\[
R_u-R_w=3^q d,
\]

same-endpoint equality gives

\[
\boxed{M=\frac{N-d}{3^s}}.
\]

Hence integrality requires the root cylinder

\[
N\equiv d\pmod{3^s}.
\]

For the current m=45 selector core and every possible `1<=s<=28-q`, all such selector-compatible cylinders were enumerated exactly.

There are

\[
\boxed{14,855}
\]

coefficient-surviving binary words carrying at least one compatible mixed-q cylinder, and

\[
\boxed{21,226}
\]

compatible `(word,sibling-cylinder)` pairs.

Every one of these 14,855 words is already among the 641,714 words removed by same-q whole-prefix maximality.

Thus

\[
\boxed{\text{incremental mixed-q depth-28 removal after safe same-q maximality}=0.}
\]

The higher-q branch is therefore structurally redundant at this finite horizon rather than a new independent pruning channel.

## 5. Exact selector same-integer calibration

Condition on the low ternary selector digit `a_0` and either affine block `b`. The exact m=45 selector masses landing in the coefficient-survivor and whole-prefix-maximal dyadic sets are

\[
\begin{array}{c|c|r|r}
a_0&b&\text{coefficient mass}&\text{maximal mass}\\\hline
0&0&461,974,723,696&377,863,976,754\\
1&0&461,974,638,137&377,863,954,371\\
0&1&461,974,296,255&377,863,511,161\\
1&1&461,974,212,398&377,863,642,347
\end{array}
\]

Aggregating all four strata gives actual selector retention

\[
\boxed{0.8179321534882688\ldots}
\]

versus the dyadic word retention

\[
\boxed{\frac{2,882,872}{3,524,586}=0.8179320918825643\ldots}.
\]

Their likelihood-ratio amplification is only

\[
1.0000000753188498\ldots,
\]

so in particular

\[
\boxed{\text{amplification}<1+\frac1{13,000,000}.}
\]

The selector therefore does not meaningfully concentrate on the maximal representatives at depth 28.

The independent mixed-q killed mass is likewise almost exactly uniform: its aggregate coefficient-conditioned selector fraction is

\[
0.002404822417935498\ldots,
\]

while the uniform binary/selector-prefix calculation gives

\[
0.00240482212799521\ldots.
\]

## 6. Complete Hensel-class growth through H=28

Let `S_{H,q}` be the complete set of correction residues modulo `3^q` realized by all length-`H`, `q`-odd parity words.

Appending one bit gives the exact recurrence

\[
\boxed{
S_{H+1,q}
=
S_{H,q}
\cup
\{3r+2^H\pmod{3^q}:r\in S_{H,q-1}\}.
}
\]

The resulting total numbers of complete Hensel classes include

\[
|S_{19}|=130,306,
\qquad
|S_{28}|=42,356,936.
\]

At `H=28`, terminal coefficient survival requires

\[
q\ge18,
\]

and the upper class tail has exactly

\[
\boxed{14,387,029}
\]

classes. Relative to all `2^28` parity words this finite-horizon class bound corresponds to exclusion rate

\[
\boxed{
1-\frac{\log_2(14,387,029)}{28}
\approx0.150776237048.
}
\]

Certificate:

`collatz/src/whole_prefix_hensel_class_growth_certificate.cpp`.

## 7. Important asymptotic caution

The number `0.150776...` is a **finite H=28 rate**, not yet a uniform asymptotic entropy theorem.

The terminal binomial coefficient-survival tail itself has an unusually strong finite-H rate, and the additional reduction from whole-prefix class collisions may or may not retain a positive rate as `H` grows.

For example the complete all-q class exclusion decreases from about

\[
0.105708\quad(H=19)
\]

to

\[
0.095139\quad(H=28).
\]

Therefore the audited repeated-L7 rate `7/50` is **not** restored merely by the finite whole-prefix calculation.

The next proof-level target is now cleaner:

> **Whole-prefix Hensel class entropy theorem.** Determine the asymptotic exponential growth of the terminal coefficient-threshold class tail
> \[
> \sum_{q\ge\lceil H\log_3 2\rceil}|S_{H,q}|,
> \]
> or derive a reusable upper bound that improves the formation-only exponent.

This route is fully root-level and avoids the invalid repeated-local-predecessor step.

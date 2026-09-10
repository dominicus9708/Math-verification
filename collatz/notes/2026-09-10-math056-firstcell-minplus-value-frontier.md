# MATH-056 — first-cell min-plus value frontier and cross-channel Hensel reduction

Date: 2026-09-10
Status: `FINITE EXACT MIN-PLUS FRONTIER / CROSS-CHANNEL REDUCTION REGRESSED / ASYMPTOTIC VALUE LAW OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-056 does not extend the complete one-sided Hensel depth beyond MATH-051/depth 41.
- The min-plus values below use same-integer address + coefficient survival. Hensel is kept as a separate non-redundant filter unless explicitly stated.

## 1. Exact integer min-plus weight

From MATH-053, if an odd shortcut step occurs at position `k` with current odd/even counts `(q,d)` and boundary slack

\[
u=m(q)-d,\qquad m(q)=\lfloor q\log_2(3/2)\rfloor,
\]

then its correction loss relative to the zero-slack mechanical envelope is

\[
p(q,u)=\frac{(1-2^{-u})\Omega_q}{3},
\qquad
\Omega_q=\frac{2^{q+m(q)}}{3^q}.
\]

For a length-72 prefix, multiplying by the common denominator `3^72` gives the exact nonnegative integer edge cost

\[
\boxed{
w_{72}(k,q,u)=(2^u-1)2^k3^{71-q}.
}
\]

Therefore the first-72 penalty can be optimized with exact integer comparisons; no floating-point ordering is required.

## 2. Value function

Let the current first-cell ordinary-start window be

\[
I_{\rm first}=(2^{71},1364\cdot2^{61}).
\]

For `K>=72`, define

\[
\boxed{
V(K)=\min\{P_{72}(N):N\in I_{\rm first},\;N\text{ remains coefficient-valid through depth }K\},
}
\]

where `P_72(N)` is the exact MATH-053 slack penalty accumulated by the first 72 parity steps of that same ordinary integer.

The feasible set for `K+1` is a subset of the feasible set for `K`, hence

\[
\boxed{V(K+1)\ge V(K)}.
\]

This monotonicity is exact but does not imply a positive linear growth rate.

## 3. Exact Dijkstra/min-plus certificate

The certificate

`collatz/src/2026_09_10_firstcell_minplus_value_frontier_certificate.cpp`

generates only coefficient-valid length-72 prefix states. Every odd edge receives the exact integer cost `w_72`; even edges have zero cost. A priority queue orders states by accumulated integer cost.

At depth 72 the prefix is converted to its unique start residue

\[
N\equiv-C3^{-q}\pmod{2^{72}},
\]

then filtered by `I_first`. The same ordinary integer is continued under the shortcut map and must remain coefficient-valid through depth `K`.

Because every edge cost is nonnegative, the first terminal state satisfying all these conditions has globally minimum penalty among the searched exact language.

## 4. Exact finite frontier

Canonical ledger:

`collatz/results/2026-09-10-firstcell-minplus-value-frontier.tsv`.

The exact minima are

\[
\boxed{V(195)\approx0.599240626584020691},
\]

attained by

\[
N=2,444,527,107,741,509,901,307,
\qquad a=1060.
\]

Its exact reduced penalty is

\[
\boxed{
V(195)=
\frac{15933097776587900715008}{26588814358957503287787}.
}
\]

For depth 265,

\[
\boxed{V(265)\approx0.825434691651584558},
\]

attained by

\[
N=3,066,081,888,322,772,163,579,
\qquad a=1329,
\]

with

\[
\boxed{
V(265)=
\frac{371679957014806528}{450283905890997363}.
}
\]

For depth 300,

\[
\boxed{V(300)\approx0.857630048844662025},
\]

attained by

\[
N=2,875,391,792,319,435,791,355,
\qquad a=1247,
\]

with

\[
\boxed{
V(300)=
\frac{7601122052464791519232}{8862938119652501095929}.
}
\]

The three minimizing ordinary starts first violate the coefficient condition at depths 232, 278, and 308 respectively. Thus each is a finite value-function witness, not a first-cell counterexample candidate to the giant crossing depth.

Observed finite ordering:

\[
V(195)<V(265)<V(300).
\]

Only the general nondecreasing property is proved; no interpolation or asymptotic slope is inferred from these three points.

## 5. Relation to MATH-054

MATH-054 proved only the coarser implication that a same-integer first-cell path coefficient-valid through depth 195 must incur at least five positive-slack odd events in its first 72 steps, hence penalty `>5/12`.

MATH-056 replaces that event-count lower bound by the exact objective value

\[
\boxed{V(195)\approx0.599240626584020691>5/12}.
\]

This is a strict computational strengthening inside the same finite coefficient/address scope.

## 6. Cross-channel Hensel reduction

MATH-013 downstream stability implies that if a prefix was exact class-max at depth `k-1`, appending the same parity step to both candidate and competitor preserves their correction order. Consequently a *new* Hensel failure at depth `k` can only come from a competitor whose final parity differs from the candidate's final parity.

In fixed-d gap coordinates this becomes:

- candidate last bit odd: an opposite-channel competitor ending even must place at least one highest-rank even at `G=q`;
- candidate last bit even: an opposite-channel competitor ending odd must place zero even ranks at `G=q`.

The overflow-safe certificate

`collatz/src/2026_09_10_cross_channel_hensel_candidate_certificate.cpp`

uses this restriction with the exact bounded-carry recurrence.

Finite regressions:

1. `N=2614662758027828756219` reproduces the known first Hensel failure at depth 56;
2. the `V(195)` minimizer `N=2444527107741509901307` has no cross-channel Hensel failure through depth 90 in the overflow-safe implementation.

The min-plus values in Section 4 do **not** yet include this Hensel filter.

## 7. Audit correction made during commit preparation

An earlier scratch run had reported the `V(195)` minimizer as cross-channel safe through depth 140. During canonicalization, the pruning upper bound in that scratch implementation was found to use a large-exponent arithmetic path that was not safe for the full claimed range.

That scratch depth-140 statement is therefore **not canonical and must not be cited**. The replacement implementation uses arbitrary-precision arithmetic in the upper-bound check. Its retained audited statement is only the exact depth-90 pass above.

This correction does not affect the MATH-056 min-plus values or the depth-56 regression.

## 8. DSD interpretation

The calculation has moved through the following reductions:

\[
\text{word count}\to\text{fixed-d Hensel state}\to\text{same-integer slack penalty}\to\text{min-plus value}.
\]

For the proof-facing task, histories that reach the same complete future state need not all be retained: only the smallest accumulated penalty matters. This is an objective-preserving DSD quotient.

However the current Dijkstra implementation can itself grow into a new enumeration ladder as `K` increases. Therefore the next target is not to sample more depths but to derive a recurrence/lower-bound theorem for `V(K)` or for the full MATH-055 product-state Bellman value.

A sufficient form would be a proved block inequality such as

\[
V(K+\Delta)\ge V(K)+\delta
\]

for an appropriate exact state-conditioned `delta>0`; a constant unconditional version is only a candidate form, not an established result.

## 9. Prohibited upgrades

- `V(195)<V(265)<V(300)` => positive asymptotic slope: prohibited.
- finite min-plus frontier => first-cell emptiness: prohibited.
- coefficient-valid through `K` => minimal-counterexample trajectory through `K`: prohibited without the stronger same-integer iterate/minimality conditions.
- depth-90 cross-channel pass => arbitrary-depth Hensel maximality: prohibited.
- cross-channel reduction => Hensel filter redundant: prohibited.
- finite objective compression => Collatz proof: prohibited.

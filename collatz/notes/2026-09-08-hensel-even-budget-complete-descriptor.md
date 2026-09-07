# Hensel even-budget complete descriptor — MATH-012

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Scope: the existing arbitrary-competitor root-Hensel **arithmetic-credit inequality** at the frozen floor `B_pub=2^71`
- Result: `CONFIRMED / EXACT COMPLETE DESCRIPTOR / COMPUTATIONAL ACCELERATION`
- New Collatz exclusion: **none**

## 1. Legacy arithmetic-credit predicate

The current root-Hensel credit check is

\[
2^{k-q}\left(1-\left(\frac23\right)^q\right)<2^{71}.
\]

Here `k` is prefix depth and `q` is the number of odd shortcut steps in that prefix.

## 2. Exact DSD complete descriptor

Put

\[
d=k-q.
\]

For a parity prefix, `d` is exactly the number of even shortcut steps.

For every `q>=2`, the legacy predicate is exactly equivalent to

\[
\boxed{d\le71.}
\]

Proof:

If `d<=71`, then

\[
0<1-(2/3)^q<1,
\]

so

\[
2^d(1-(2/3)^q)<2^d\le2^{71}.
\]

Conversely, if `d>=72` and `q>=2`, then

\[
1-(2/3)^q\ge1-(2/3)^2=5/9>1/2,
\]

hence

\[
2^d(1-(2/3)^q)>2^{d-1}\ge2^{71}.
\]

Therefore the large-integer Hensel credit comparison can be replaced, within this predicate, by the single integer descriptor

\[
\boxed{d=k-q.}
\]

This is the direct depth-72+ analogue of the finite complete-descriptor idea used in MATH-011, although it describes **proof-mechanism eligibility**, not coefficient survival itself.

## 3. Combined coefficient/Hensel threshold

Coefficient survival at depth `k` requires

\[
q\ge q_{\min}(k),
\]

where `q_min(k)` is the least integer with `3^q >= 2^k`.

Root-Hensel arithmetic credit requires

\[
q\ge k-71.
\]

Thus satisfying both predicates is exactly

\[
\boxed{
q\ge Q_*(k):=\max\{q_{\min}(k),k-71\}.
}
\]

Near the historical boundary:

| k | q_coeff | q_Hensel | Q_*(k) |
|---:|---:|---:|---:|
| 188 | 119 | 117 | 119 |
| 189 | 120 | 118 | 120 |
| 190 | 120 | 119 | 120 |
| 191 | 121 | 120 | 121 |
| 192 | 122 | 121 | 122 |
| 193 | 122 | 122 | 122 |
| 194 | 123 | 123 | 123 |
| 195 | 124 | 124 | 124 |
| 196 | 124 | 125 | 125 |
| 197 | 125 | 126 | 126 |
| 198 | 125 | 127 | 127 |
| 199 | 126 | 128 | 128 |
| 200 | 127 | 129 | 129 |

This recovers the old uniform boundary but refines its interpretation:

\[
(195,124):\ \text{credit safe},
\]

\[
(196,124):\ \text{coefficient-safe but credit-unsafe},
\]

while

\[
(196,125):\ \text{credit safe}.
\]

So the correct statement is not “all Hensel arithmetic credit ends at depth 196.” Rather, **from depth 196 onward the lowest coefficient-surviving q branches begin to lose this credit, while sufficiently high-q branches can remain arithmetically eligible.**

This does not by itself extend full arbitrary-word Hensel maximality beyond its separately audited assumptions.

## 4. Exact regression

The certificate checks every state

\[
2\le q\le k\le512
\]

against both the original exact integer inequality and the descriptor test `k-q<=71`.

There are `130,816` such `(k,q)` states and the two predicates agree on all of them.

The certificate also asserts the historical/refined boundary states `(195,124)`, `(196,124)`, and `(196,125)` directly.

## 5. Symbolic prefix coverage diagnostic

For the two inequalities alone, one can count parity words whose every prefix obeys coefficient survival, and separately those that also preserve the Hensel credit gate.

The two counts are equal through depth 195 and first separate at 196.

Selected exact counts:

| depth | coefficient-prefix words | also Hensel-credit eligible |
|---:|---:|---:|
| 195 | 184799166355160028491206180611149885957620090494216458 | same |
| 196 | 369598332710320056982412361222299771915240180988432916 | 328482004957934376963542459443028048450892929326063926 |
| 200 | 4917911213247274697935031643998322726370567793471092895 | 2775538436598973010628291296266687519075522801760430412 |

These counts describe **symbolic inequality coverage only**. A word that loses Hensel credit is not thereby excluded as an ordinary Collatz candidate.

The structural reason is simple: persistent Hensel credit requires at most 71 even steps in every prefix, so after the crossover this proof mechanism becomes progressively more restrictive than coefficient survival.

## 6. Computational acceleration

For this subproblem the legacy test uses large exact powers of 2 and 3.

The complete descriptor reduces it to

```text
k - q <= 71
```

for `q>=2`.

A session-local Python benchmark over the `130,816` regression states showed roughly an order-of-magnitude wall-clock reduction. Runtime ratios are environment-dependent diagnostics and are not theorem-facing claims.

More importantly, the predicate state itself collapses to one scalar `d=k-q`. States may therefore be merged by `d` **only when evaluating this arithmetic-credit gate**.

They may not be merged as full Collatz, endpoint, parity, correction, or Hensel states.

## 7. DSD interpretation

- `D`: exact target is root-Hensel arithmetic-credit eligibility, not Collatz survival.
- `R`: exact `(k,q)` resolution under the frozen `2^71` theorem-facing floor.
- `S`: `q>=2`; coefficient-surviving branches may then be compared to the credit threshold.
- `E`: `d>71` excludes use of this credit mechanism only.
- `T`: the original inequality is algebraically reduced to the descriptor gate.
- `C`: exhaustive regression through `k<=512` plus exact proof of the equivalence.
- `N`: `ESTABLISHED_WITHIN_SCOPE`.
- `O`: complete descriptor and calculation acceleration, with no new Collatz exclusion.

## 8. Prohibited upgrades

Do not infer

\[
d>71\Longrightarrow\text{Collatz candidate impossible}.
\]

Do not infer that `(196,125)` automatically inherits every other condition needed for arbitrary-word full-Hensel maximality.

Do not merge full candidate states merely because they share the same `d`.

Do not promote the finite symbolic-prefix coverage counts to density, emptiness, or universal convergence claims.

## Certificate

`collatz/src/2026_09_08_dsd_hensel_even_budget_descriptor.py`

Commit: `6c7ffb083f37989907a690c303b3f99adb43f7b0`

## Next target

Use the descriptor as a cheap gate while examining what **additional non-redundant Hensel/endpoint information** remains after the arithmetic-credit condition is satisfied. The next useful question is whether that remaining eligibility can also be represented by a small exact state, or whether the correction/word structure must be retained in full.

# MATH-058 — paid-macro transition bound

Date: 2026-09-11
Status: `EXACT MACRO-TRANSITION REFINEMENT / CUMULATIVE PENALTY SLOPE STRENGTHENED / FIRST-CELL CLOSURE OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-058 refines the MATH-057 phase/address barrier by using actual same-integer endpoint parity at the boundary where a paid odd event would have to occur.

## 1. Why MATH-057 was still loose

MATH-057 proved that a zero-penalty mechanical continuation from a `u=0` anchor cannot last 79 steps. The static phase/address test still left two necessary intervals at length 78.

However, the ordinary-integer endpoint determines the next parity bit. A candidate cannot choose to leave the mechanical path merely because the slack is positive: a paid odd event is possible only when the actual endpoint is odd while the zero-penalty mechanical continuation requires an even step.

Thus the next refinement must preserve

\[
\boxed{\text{phase} + \text{actual endpoint parity}.}
\]

## 2. Generic paid exit boundary

The exact lift calculation includes every endpoint

\[
y=R+t2^L
\]

below the MATH-057 anchor bound and every rational phase interval compatible with the first-cell ordinary-start window.

A paid exit requires

1. terminal slack `u=1`, so the mechanical next step would be even;
2. actual next endpoint parity odd.

The full lift audit gives:

- a paid exit is still possible at `L=72`;
- no paid exit is possible for `L>=73`.

Therefore the zero-cost prefix immediately preceding any paid cluster has length at most 72.

## 3. Exactly-one-paid cluster condition

Suppose the paid cluster contains exactly one paid odd event.

Let `E` be the odd endpoint just before that paid step.

If the Beatty increment at the paid odd is `epsilon=0`, the post-odd slack remains one and exactly one even step is needed to return to `u=0`. This requires

\[
\boxed{E\equiv1\pmod4}.
\]

If `epsilon=1`, two even steps are required, giving

\[
\boxed{E\equiv5\pmod8}.
\]

These congruence conditions are tested against every allowed dyadic lift in each phase interval.

Result:

- exactly-one-paid clusters exist through `L=71`;
- no exactly-one-paid cluster exists at `L=72`.

## 4. Repeatable one-paid macros

For a proof-facing long trajectory, an internal macro is useful only if, after returning to `u=0`, the same ordinary endpoint can continue coefficient-validly until another paid macro is reached.

The exact new-anchor endpoint and transformed phase interval are therefore propagated once more. The first actual/mechanical mismatch is classified as

- `paid`: actual odd / mechanical even, so another paid macro begins;
- `fail`: actual even / mechanical odd, so coefficient admissibility fails.

The complete lift audit gives

| zero-cost length L | one-paid outcomes | outcomes reaching another paid macro |
|---:|---:|---:|
| 69 | 20 | 1 |
| 70 | 4 | 0 |
| 71 | 4 | 0 |
| 72 | 0 | 0 |

Hence

\[
\boxed{
\text{a repeatable internal one-paid macro has zero-cost length}\le69.
}
\]

The `L=70,71` one-paid outcomes are terminal in the sense that the next same-integer mismatch is coefficient failure rather than another paid transition.

## 5. Global step accounting

Let `P` be the total number of positive-slack odd events in a coefficient-valid prefix of length `K`.

### Internal one-paid block

A repeatable one-paid macro contributes at most

\[
69+3=72
\]

steps for one paid event.

### Internal multi-paid block

For a cluster containing `r>=2` paid odd events,

- the preceding zero-cost part has length at most 72;
- after the opening boundary odd, the paid-cluster residual has length at most `2r+1`.

Thus

\[
72+(2r+1)=73+2r\le72r.
\]

So every internal macro block consumes at most 72 steps per paid event.

### Endpoint overheads

The special initial `q=0` phase is kept separate and bounded conservatively by an additive 9-step overhead relative to `72r`.

A final non-repeatable one-paid cluster can cost at most two extra steps relative to the internal bound, and the terminal zero-penalty tail is at most 78 steps by MATH-057.

Therefore the complete conservative accounting is

\[
\boxed{K\le72P+89.}
\]

This additive constant deliberately overcounts the first/last exceptional pieces so that no phase-specific endpoint case is silently promoted to a repeating macro theorem.

## 6. Strengthened cumulative penalty bound

Every paid odd event has MATH-053 cost strictly greater than `1/12`. Therefore

\[
\boxed{
P\ge\left\lceil\frac{K-89}{72}\right\rceil
}
\]

and

\[
\boxed{
\mathcal P_K>
\frac1{12}
\left\lceil\frac{K-89}{72}\right\rceil.
}
\]

At the final coefficient-valid prefix before the first universal crossing,

\[
K=A_0-1=114,208,327,603,
\]

this gives

\[
\boxed{P\ge1,586,226,772}
\]

and

\[
\boxed{
\mathcal P_{A_0-1}>132,185,564.3333\ldots
}
\]

This supersedes the weaker MATH-057 bound `>117,498,279.4167...`.

## 7. DSD interpretation

The new reduction is not another depth scan. It changes the unit of calculation from single parity steps to **macro transitions between boundary anchors**.

The information retained by one macro is

\[
(\text{phase interval},\text{actual endpoint residue},\text{paid count},\text{next-anchor type}).
\]

Histories that differ internally but have the same future macro state and no smaller accumulated penalty need not both be retained.

This is closer to the final min-plus safety-game representation than the earlier word-count or event-budget calculations.

## 8. What remains open

The slope `1/(72*12)` is still not sufficient by itself to close the first universal cell. The next refinement is to replace the scalar worst-case macro length by the actual weighted macro-transition graph.

In particular, the rare `L=69` one-paid transition should be treated as a vertex/edge state rather than assumed repeatable without cost. If it cannot lie on a low-mean-cost cycle, the asymptotic penalty slope rises again.

Nested Hensel cross-channel state can then be attached only to the surviving low-mean macro graph, avoiding a return to full prefix enumeration.

## Reproducibility

- `collatz/src/2026_09_11_paid_macro_transition_certificate.py`
- `collatz/results/2026-09-11-paid-macro-transition-boundary.tsv`

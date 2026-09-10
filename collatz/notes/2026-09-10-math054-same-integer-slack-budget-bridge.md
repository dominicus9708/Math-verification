# MATH-054 — same-integer slack-budget bridge

Date: 2026-09-10
Status: `FINITE EXACT SAME-INTEGER BRIDGE / POSITIVE SLACK FORCED IN ROOT-SAFE SCOPE / UNIVERSAL ASYMPTOTIC BOUND OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This result is finite and conditional on the current first-cell ordinary-start window and root-safe coefficient obligation through depth 195.

## 1. Why MATH-053 needed a correction

MATH-053 isolated the exact penalty identity

\[
S_*-S(w)=\frac13\sum_n(1-2^{-u_n})\Omega_n.
\]

A tempting next claim would have been

\[
\text{nested Hensel maximality}\Longrightarrow u_n>0\text{ often}.
\]

That implication is not supported. The unique zero-slack mechanical boundary word remains terminally Hensel-undominated through the audited depth-41 frontier, and direct targeted checks reproduce this through the finite test range used here. Therefore Hensel maximality alone is not the correct bridge.

The missing non-redundant channel is the ordinary-integer dyadic start address.

## 2. Zero-slack path is excluded by the same-integer address

The zero-slack path is unique: whenever `u=0`, an even step would violate coefficient admissibility, so the next step must be odd; whenever the Beatty increment creates `u=1`, exactly one even step is required before the next zero-slack odd event.

At depth 72 its parity word determines the unique ordinary residue

\[
\boxed{N_{\rm mech}=4,697,939,311,072,332,635,131}.
\]

Its top-11-bit address is

\[
\boxed{2037}.
\]

The current first-cell ordinary-start window is

\[
2^{71}<N<1364\cdot2^{61},
\]

corresponding to top-address labels `1024..1363`. Therefore the zero-slack path is not a same-integer first-cell candidate.

This already implies at least one positive-slack odd event and hence

\[
S_*-S(w)>1/12,
\]

because `Omega_n>1/2` and `u_n>=1` gives `1-2^{-u_n}>=1/2`.

## 3. Exact slack-budget scan at depth 72

All coefficient-valid length-72 parity prefixes with at most B positive-slack odd events were generated exactly for `B=0..5`. Each parity prefix was converted to its unique start residue modulo `2^72` using

\[
\boxed{N(w)\equiv-C(w)\,3^{-q}\pmod{2^{72}}}.
\]

Only starts inside the first-cell ordinary window were retained. The same ordinary integer was then continued by the actual shortcut Collatz map and required to remain coefficient-valid through the root-safe depth 195.

The exact results are

| slack-event budget in first 72 | first-cell starts | coefficient-valid through 195 |
|---:|---:|---:|
| 0 | 1 | 0 |
| 1 | 5 | 0 |
| 2 | 47 | 0 |
| 3 | 585 | 0 |
| 4 | 4,484 | 0 |
| 5 | 27,959 | 7 |

Therefore every same-integer first-cell path satisfying the root-safe coefficient obligation through depth 195 obeys

\[
\boxed{\#\{n<q_{72}:u_n>0\}\ge5}.
\]

Consequently

\[
\boxed{S_*-S(w)>5/12}
\]

already from the first 72 steps.

This is the first exact positive Hensel/coefficient-compatible slack-penalty lower bound produced by combining the mechanical phase with the ordinary start address.

## 4. Budget-5 survivors

Exactly seven budget-5 first-cell starts remain coefficient-valid through depth 195. Their top-11 labels are

`1027, 1060, 1112, 1133, 1275, 1284, 1289`.

A targeted exact Hensel check through depth 72 removes the `1133` start at depth 56; the other six remain nested-Hensel valid through depth 72.

Thus adding Hensel information improves the finite budget-5 population from seven to six, but does not yet raise the proven universal slack-event lower bound above five.

## 5. What this proves and what it does not

Established in the audited finite scope:

1. the zero-slack mechanical path is incompatible with the current same-integer first-cell start window;
2. no first-cell start with <=4 positive-slack odd events in the first 72 steps remains coefficient-valid through depth 195;
3. hence every root-safe same-integer first-cell candidate has at least five such events and penalty >5/12;
4. one of the seven minimal budget-5 coefficient survivors is already removed by nested Hensel maximality through depth 72.

Not established:

1. a positive asymptotic density of slack events;
2. a penalty lower bound of the scale needed to close the giant first-crossing correction inequality;
3. nested Hensel maximality of the six surviving budget-5 starts through depth 195;
4. first-cell emptiness;
5. later-strip coverage or the Collatz conjecture.

## 6. DSD conclusion

The failed candidate bridge

\[
\text{Hensel}\Rightarrow\text{slack}
\]

must be replaced by the non-redundant composition

\[
\boxed{
\text{same integer address}
+\text{coefficient survival}
+\text{Hensel maximality}
\Longrightarrow
\text{slack penalty}.
}
\]

The address channel is not optional metadata: it is exactly what excludes the zero-penalty mechanical word.

The next proof-facing task is to avoid increasing the slack-event budget by brute force. Build a product transducer whose state combines the normalized Hensel state with the ordinary-start/address state, and attach the MATH-053 penalty as a min-plus weight. The desired object is a lower-bound value function for every same-integer bad path.

## Reproducibility

- `collatz/results/2026-09-10-firstcell-slack-budget-depth195.tsv`
- `collatz/src/2026_09_10_firstcell_slack_budget_depth195_certificate.py`

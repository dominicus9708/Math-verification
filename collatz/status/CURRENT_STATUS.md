# Current status — 2026-09-02

## Current branch

Research branch: `collatz-stage4-window-threshold`

Primary active object: `A0, s=1, Route-B` long-membership closure.

## Retained source family

Every current Route-B survivor lies in the exact 14-root arithmetic forest

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`

after the stated SAFE upstream pruning.

The forest remains a search-family representation, not a membership theorem.

## Closed synchronized seams

The following exact interfaces remain available:

1. right-H affine checkpoint observation
   \[
   z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}};
   \]
2. a **full** coherent pair `Z mod 2^27 × z_H mod 3^28` exposes at most one ordinary checkpoint `Z` in the independent SAFE corridor;
3. one exposed ordinary `Z` contracts every source root to an exact debit-compatible parameter fiber;
4. the checkpoint terminal ternary precision is fully consumed inside the right H block and exports zero ternary digits across the critical cut;
5. modulo `3^L`, only the final `L` ranked one-events affect the target-relative correction residue.

The full CRT singleton seam is conditional: it becomes useful only when an independent stronger predicate supplies a full `z_H mod 3^28` value.

## Terminal-28 target-dominance gate — CLOSED but REDUNDANT for pruning

The nominal 28-gate right-H target-dominance suffix problem admits a stronger exact reduction.

For one gate, local carry admissibility is

\[
G(A)=\begin{cases}
\{0,1\}, & A\text{ even},\\
\{0,2\}, & A\text{ odd}.
\end{cases}
\]

A complete finite residue lemma modulo 6/9 proves that if the next suffix needs slack cap at least `T`, one of the four consecutive values

\[
T,T+1,T+2,T+3
\]

always passes the current mod-3 gate and lands in the next admissible carry class.

Thus for 28 gates

\[
T_{27}=1,\qquad T_t=T_{t+1}+3,
\]

so

\[
T_0=82.
\]

The actual minimum target capacity is

\[
232{,}565{,}502\gg82,
\]

therefore the entire terminal target-dominance suffix exists iff the **first** local class is admissible.

The current rightmost target exponent is even, so

\[
\boxed{z_H\bmod3\in\{0,1\}}.
\]

Using the synchronized affine observation, this is equivalent to

\[
\boxed{Z\bmod3\in\{1,2\}},
\]

i.e. `3` does not divide `Z`.

However, every genuine positive-one-count checkpoint identity

\[
2^hZ=3^qX+C(W),\qquad q\ge1,
\]

already satisfies `3∤Z`, because

\[
C(W)\equiv2^{a_q}\not\equiv0\pmod3.
\]

Therefore the terminal target-dominance ternary gate removes **zero genuine candidates**.

Canonical theorem/audit:

- `../theorems/TERMINAL_28GATE_DOMINANCE_SATURATION.md`;
- `../audits/TERMINAL_DOMINANCE_GATE_REDUNDANCY.md`;
- `../src/A0_s1_routeB_terminal_dominance_gate_redundancy_certificate.py`.

Continuing to refine the dominance-only terminal carry family as a pruning engine is now a rejected search strategy.

## Weak synchronized channel is not checkpoint isolation

Dominance-only acceptance supplies only

\[
Z\bmod3\in\{1,2\}.
\]

Together with a fixed `Z mod 2^27`, this gives two classes modulo

\[
3\cdot2^{27}=402{,}653{,}184.
\]

For fixed `X`, the independent debit-compatible open checkpoint interval has width

\[
37\cdot2^{33}=317{,}827{,}579{,}904
=789(3\cdot2^{27})+2^{27}.
\]

Hence each accepted weak CRT class occurs at least 789 times in such an interval; the two classes contribute at least 1,578 ordinary checkpoint integers before other constraints.

So dominance-only `mod 3` information cannot trigger the full checkpoint-singleton seam.

## Physical Bellman execution evidence

The exact scalar physical score `P` remains valid for its directed rejection predicate.

Finite exact scans of the deepest completed roots to ordinary-X exposure depth `h=72` produced:

| `f` | maximum Bellman states | states at `h=72` | physical-score closed children |
|---:|---:|---:|---:|
| 29 | 1,080,374 | 16 | 0 |
| 32 | 419,510 | 16 | 0 |
| 35 | 167,507 | 14 | 0 |
| 37 | 81,519 | 13 | 0 |

These are **finite execution data only**. They do not prove non-closure later or for other roots.

Execution record:

- `../experiments/2026-09-02-deep-root-Pmin-to72.md`.

The `f=27` attempt did not complete within the execution limit; no partial count is retained.

After `h=72`, the existing `P_min` merge key must not be treated as a universal future-membership state without restoring whatever exact future-control coordinates the next predicate queries.

## Current principal bottleneck

Two standalone pruning ideas are now insufficient:

1. terminal right-H target-dominance ternary filtering is exactly redundant on genuine checkpoints;
2. deep-root directed `P_min` scans produced no whole-family closure through `h=72` in the completed finite runs.

The principal mathematical gate is therefore

\[
\boxed{\text{source-controlled exact full correction/checkpoint membership}.}
\]

For a proposed ordinary pair `(X,Z)`, the required full correction is

\[
C_{req}=2^{t_0}Z-3^{j_0}X.
\]

At fixed `(t_0,j_0)`, the correction map from a parity word to `C(W)` is injective, but existence/inversion in the exact formation language remains open.

The next state must exploit the source prefix/control together with exact correction localization, rather than treating terminal target dominance as an independent sparse filter.

## Still useful secondary tools

- `P_min` physical pruning on large source-controlled families;
- full synchronized CRT singleton when a stronger predicate actually determines `z_H mod 3^28`;
- checkpoint-conditioned source fibers after ordinary `Z` exposure;
- dyadic prefix and ternary suffix correction localization;
- fixed-`(h,q)` correction injectivity;
- exact H/L grammar / block correction laws.

## What remains OPEN

- compact exact inverse/join for source-controlled full correction-language membership;
- actual 14-root source/checkpoint/correction joins;
- ordinary checkpoint/debit/tail/renewal compatibility after membership exposure;
- Route-A;
- all `s>=2` sectors;
- global branch completeness;
- Collatz.

## Forbidden shortcuts

- terminal dominance acceptance -> useful independent pruning;
- terminal dominance acceptance -> full `z_H mod 3^28`;
- dominance-only `mod3` + dyadic residue -> checkpoint singleton;
- adic mismatch -> membership rejection;
- exposed `(X,Z)` -> same orbit without exact pre-bridge language membership;
- small source fiber -> membership;
- finite `P_min` non-closure -> universal no-go theorem;
- continue a merged `P_min` state past `h=72` for arbitrary predicates without an exact future-control theorem;
- marginal density multiplication;
- later refined bound used retroactively.

## Resume instruction

Resume from `../frontier/A0_S1_ROUTEB.md`.

Do **not** restart the terminal 28-gate dominance carry enumeration. The next principal calculation is the source-controlled exact correction/checkpoint membership interface.
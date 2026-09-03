# Canonical live proof stack

This is the shortest current live implication stack. Historical exploratory routes and implementation regressions are omitted.

A line here means only that the stated implication has an exact or explicitly SAFE certificate in its stated domain. Final global lines remain OPEN.

## S0 — Physical A0 domain

Work in the certified `A0, s=1` formation with the fixed long pre-bridge parameters and current physical shell assumptions.

Status: **DOMAIN / imported**.

## S1 — Near-threshold finite closure

Certified finite arithmetic closes radius `0..7` in the first-75 threshold window, giving the SAFE necessary condition

`d_75 >= 8`.

Status: **CERTIFIED ARITHMETIC -> SAFE**.

## S2 — Monotone defect and physical pruning

Target dominance makes the threshold correction maximal. Normalized defect is nonnegative and irreversible under continuation. Together with the directed real envelope this yields the certified physical pruning bound.

Status: **EXACT + CERTIFIED arithmetic -> SAFE pruning**.

## S3 — Exact 14-root source forest

Every remaining Route-B family lies in exactly one retained first-defect root

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`

after the stated upstream SAFE pruning.

Status: **EXACT search-family representation after SAFE inputs**.

## S4 — Exact structural compression

Available exact tools include:

- affine source cylinders and bit refinement;
- fixed-count ballot / target dominance;
- exact H/L grammar;
- fixed-`(h,q)` correction injectivity;
- correction block composition;
- dyadic prefix and ternary suffix localization;
- projective carry/displacement states;
- finite interval quotients.

Status: **EXACT structural lemmas**.

## S5 — Directed physical Bellman score

With

\[
N=3^q\eta,
\qquad
P=m_{W,lo}N+\delta_{lo}3^qX_{lo},
\]

one `P_min` label per exact active source/control + payload class is sufficient for the directed physical rejection predicate.

Status: **EXACT / CLOSED for this predicate**.

Finite deep-root executions through `h=72` on `f=29,32,35,37` produced zero whole-family physical closures. This is execution evidence only and does not alter the theorem.

## S6 — Terminal localization and checkpoint seams

Exact closed interfaces:

- lazy terminal-ternary observation;
- critical-cut shielding;
- terminal precision absorption;
- terminal ranked-one window locality;
- full synchronized `Z mod2^27 × z_H mod3^28` CRT singleton exposure, conditional on a full `z_H` observation;
- exposed ordinary `Z` -> exact checkpoint-conditioned source fibers.

Status: **EXACT / CLOSED in their stated scopes**.

## S7 — Terminal target-dominance saturation

For the current terminal 28-rank right-H window, a finite mod-6/mod-9 lifting lemma yields sufficient slack thresholds

\[
T_{27}=1,
\qquad T_t=T_{t+1}+3,
\]

and therefore

\[
T_0=82.
\]

The actual target capacities exceed `232,565,502`, so the complete target-dominance suffix existence condition reduces to the first local gate:

\[
z_H\bmod3\in\{0,1\}.
\]

Equivalently

\[
Z\bmod3\in\{1,2\}.
\]

Status: **EXACT / CLOSED for target-dominance suffix existence**.

## S8 — Terminal dominance gate redundancy

Every genuine checkpoint with positive one-count satisfies

\[
2^hZ=3^qX+C(W),\qquad q\ge1.
\]

Modulo 3,

\[
C(W)\equiv2^{a_q}\not\equiv0,
\]

so necessarily

\[
3\nmid Z.
\]

This is exactly the terminal target-dominance condition from S7.

Therefore the standalone terminal target-dominance ternary gate removes zero genuine candidates.

Status: **EXACT redundancy theorem / REJECTED as an independent pruning engine**.

## S9 — Residual correction and exact-pair decoding

For a proposed source/checkpoint pair, the required full pre-bridge correction is

\[
\boxed{C_{req}=2^{t_0}Z-3^{j_0}X.}
\]

For an exact realized prefix `A`, with current state `Y`, the correction equation restarts exactly on the remaining suffix `B`:

\[
\boxed{C(B)=2^{|B|}Z-3^{q(B)}Y.}
\]

For a fully specified remaining instance `(Y,Z,n,q)`, define

\[
R=2^nZ-3^qY.
\]

If `q>0`, the next 1-position is forced by

\[
\boxed{a=v_2(R)}
\]

and the forced block `0^a1` may be discharged exactly. Repetition either rejects or reconstructs the unique realizing word.

Thus exact-pair correction inversion is zero-or-one and algorithmically closed.

Status: **EXACT / CLOSED at exact-pair resolution**.

## S10 — Active valuation-cylinder family realization

The unresolved problem is the enormous source/checkpoint family, not the existence of an inverse for one exact pair.

For an affine current-state cylinder

\[
Y=y+A m,
\qquad A\text{ odd},
\]

the next-one valuation branch `a=v2(Y)` is exactly

\[
\boxed{
m\equiv(2^a-y)A^{-1}\pmod{2^{a+1}}.
}
\]

Writing `m=rho_a+2^(a+1)k`, the complete forced block `0^a1` jumps to another affine cylinder

\[
Y'=y'_a+3A k.
\]

The active task is to combine this exact valuation-cylinder jump with:

- remaining length/one-count controls;
- H/L or equivalent pre-bridge future-formation control;
- predicate-relative checkpoint/debit state;
- optional `P_min` only inside exact future-control classes;
- legal merge criteria based on identical future realization sets.

The first implementation obligation is a finite-depth valuation-cylinder transducer regression against the existing bitwise source-channel transducer, followed by application to the deepest retained roots.

Status: **ACTIVE principal family-compression gate**.

## S11 — Checkpoint/debit/tail realization

For every S10-realized or still-possible pre-bridge state, discharge ordinary checkpoint/debit coherence, tail first-passage, and any required renewal/C4F obligation.

Status: **OPEN**.

## S12 — A0 `s=1` Route-B closure

Required conclusion: every family from all 14 roots is exactly rejected or fully discharged through the complete pre/tail/checkpoint formation obligations.

Status: **OPEN**.

## S13 — Global completion

Route-A, all `s>=2` sectors, remaining branches, and global branch completeness must be separately closed before any Collatz conclusion.

Status: **OPEN**.

---

# Forbidden shortcuts

- exact-pair uniqueness -> family-level uniqueness;
- equal valuation/residual -> legal merge when future controls differ;
- terminal target-dominance filtering as an independent pruning engine after its redundancy theorem;
- target-dominance acceptance -> full `z_H mod3^28`;
- dominance-only mod3 + dyadic residue -> checkpoint singleton;
- adic mismatch -> membership rejection outside an explicit equality predicate;
- endpoint/checkpoint exposure -> same orbit/full membership;
- small source fiber -> membership;
- finite `P_min` non-closure -> universal theorem;
- continue a merged physical state beyond its certified future-predicate scope;
- local carry greedy -> global optimum before a cylinder sequence is fixed;
- marginal survival-ratio multiplication without independence;
- later refined bounds used retroactively;
- A0 `s=1` Route-B closure -> Collatz without the remaining modules.

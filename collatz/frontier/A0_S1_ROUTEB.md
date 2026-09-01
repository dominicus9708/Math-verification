# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation. Chronological notes remain evidence/history; new calculation should start from this file.

## Input family

Exact retained first-defect roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary input certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

Each root is an exact source cylinder

`X = r + 2^h m`

with a finite integer parameter interval and exact parity-bit refinement.

## Active two-front architecture

### Forward front

Carry only

`source future control × exact interval payload × P_min`

for the directed physical gate.

The scalar physical score is

`P = mW_lo*N + delta_lo*3^q*X_lo`,

with exact whole-family rejection when

`P > (L_MAX*QFP+cW_hi)*3^q`.

Do not restore `(r,N)` as separate state coordinates unless a later predicate separately queries them.

### Backward right front

A terminal correction/defect predicate modulo `3^L` is completely right-local at the existing critical cut for `L=24,28,47` because the right H block contains `397,573,380` one-events.

Start from the actual required right-block residue and propagate it through the compressed H/projective suffix language.

For a fixed one-event/cylinder transition:

- the predecessor residue is empty or singleton;
- raw carry residues should not be enumerated;
- use displacement/slack projective coordinates;
- for `m>=23`, each specified exponent cylinder is empty or singleton inside the complete legal dominance interval.

### Join

When both fronts have exact export states, join them at an exact block boundary.

No independence assumption and no multiplication of marginal survival ratios is allowed.

## Current closed primitives to use

### Source / interval

- exact affine source-cylinder transducer;
- exact bit refinement `m = m0 + 2k`;
- finite interval payload compression / four-state cylinder theorem;
- reduced source+ballot control where its hypotheses apply.

### Ballot / grammar

- fixed-count ballot future cone;
- target strict-prefix dominance / surplus representation;
- exact dual H/L canonical grammar;
- target-only H/L–Stern-Brocot hierarchy alignment;
- critical-cut product factorization.

### Correction / projective

- fixed `(h,q)` correction injectivity;
- dyadic prefix localization;
- ternary suffix locality and carry recurrence;
- projective block carry law;
- one-step carry bijection;
- general suffix-gate displacement isometry;
- normalized suffix slack partition;
- projective successor carry → exponent/displacement cylinder;
- lazy terminal-ternary observation theorem;
- critical-cut ternary shielding theorem;
- projective-cylinder singleton threshold `m>=23`.

### Membership-relevant defect / physical gate

- monotone normalized defect;
- exact projective-cylinder defect floor;
- fixed-cylinder ordering-aware minimum;
- displaced-rank / phase-weighted lower bounds;
- normalized-defect semiring;
- integer defect numerator `N=3^q eta`;
- inverse physical defect budget;
- exact scalar physical danger score `P` and one-label Bellman reduction.

## Current G1 objective — forward scan

For each of the 14 roots:

1. initialize exact source/control and finite parameter interval;
2. initialize `P_min`;
3. refine by exact source parameter bits;
4. merge histories only under certified exact future-control + payload equivalence;
5. close nodes whose minimum score already exceeds the physical barrier;
6. retain unresolved export families for the future cut join.

Terminal ternary residue is not carried before it becomes observable.

## Current G2 objective — backward right-H filter

The next mathematical task is to close the multi-gate composition problem left open by the local displacement-isometry theorem.

Desired state must represent, without flat carry enumeration:

1. the current projective carry/residue cylinder;
2. the current target capacity/slack ordering cap;
3. exact existence of legal suffix completions;
4. eventually an exact cut-boundary export coordinate.

Useful exact coordinates:

Right-indexed target/candidate positions

`A_t, B_t`,

capacity/slack

`D_t = A_t-(q-t-1)`,

`s_t = B_t-(q-t-1)`,

with

`0 <= s_t <= D_t`,

`s_(t+1) <= s_t`,

and displacement

`delta_t = D_t-s_t`.

At one gate, after required parity is fixed, write

`delta_t = epsilon_t + 2 d_t`.

The carry map is a 3-adic isometry in `d_t`:

`v3(Phi(d)-Phi(e)) = v3(d-e)`.

Hence a prescribed successor carry cylinder corresponds exactly to one arithmetic progression in `d_t`, equivalently one arithmetic progression in `s_t`.

The open issue is how these progression cylinders compose under the monotone slack constraint across multiple gates.

## Immediate theorem target

Seek an exact **backward slack-cylinder quotient**:

- for one specified projective state, intersect its slack residue class with the legal interval;
- when multiple histories reach the same outgoing projective state, determine whether keeping only the largest reachable slack is exact for suffix-existence, because larger slack weakly relaxes all remaining leftward ordering caps;
- separate this feasibility quotient from defect minimization;
- if exact, lift it to block/H grammar transitions.

Do not claim physical-cost dominance from slack dominance alone; right-factor defect cost may trade off against earlier choices unless separately proved.

## Success criteria for the next milestone

A G2 milestone is complete when there is an exact certificate showing either:

- a compact multi-gate backward slack/projective state and its merge theorem; or
- a counterexample proving that the proposed quotient loses a feasible suffix.

Then record state counts on finite exact suffix regressions and proceed to the right-H block recursion.

## Known failure modes to avoid

- local carry greedy before a cylinder sequence is fixed;
- treating singleton exponent cylinder as singleton carry path;
- target-collision mismatch treated as rejection;
- carrying terminal ternary residues through the left root forest while shielded/dormant;
- use of exact completion-defect DP as an uncompressed binary-tree search engine;
- forgetting source transition coordinates after an observation is discharged;
- double counting local defect floors;
- using later refined bounds retroactively.

## Frontier output

When a new G2 theorem is closed, update in the same cycle:

- `../status/CURRENT_STATUS.md`;
- `../status/OPEN_GATES.md`;
- `../CANONICAL_PROOF_STACK.md`;
- this file;
- relevant theorem/certificate/audit indexes.

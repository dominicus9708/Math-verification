# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation.

## Input family

Exact retained roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary source certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`.

Each root is an exact affine source cylinder

\[
X=r+2^h m
\]

with a finite integer parameter interval and exact parity refinement.

## Closed/rejected routes that must not be restarted

### Terminal right-H target-dominance ternary filter

The terminal 28-gate dominance problem is solved exactly.
Its complete existence condition reduces to

\[
z_H\bmod3\in\{0,1\}
\iff
Z\bmod3\in\{1,2\}.
\]

Every genuine positive-one-count checkpoint already satisfies `3∤Z`, so this gate is redundant for pruning.

Canonical objects:

- `../theorems/TERMINAL_28GATE_DOMINANCE_SATURATION.md`;
- `../audits/TERMINAL_DOMINANCE_GATE_REDUNDANCY.md`.

### Dominance-only weak CRT channel

`Z mod2^27` plus the automatic `Z mod3 in {1,2}` condition does not isolate a checkpoint. Each accepted weak CRT class occurs many times in the debit-compatible corridor.

### `P_min` as a sole deep-root strategy

Finite exact scans through ordinary-X exposure depth `h=72` found no physical-score whole-family closures for completed roots `f=29,32,35,37`.

This is execution evidence only, not a theorem. `P_min` remains a secondary predicate.

## Closed synchronized seams retained for later use

1. A full coherent pair `Z mod2^27 × z_H mod3^28` exposes at most one ordinary checkpoint `Z` in the independent SAFE corridor.
2. An exposed ordinary `Z` contracts every source root to an exact debit-compatible parameter fiber.
3. Terminal ternary precision is absorbed inside the current right-H block after its predicate is discharged.
4. Fixed-`(h,q)` correction is injective.
5. Dyadic prefix and ternary suffix correction localization and exact block correction composition are available.
6. Exact prefix discharge restarts the same correction equation on the residual suffix.
7. For an exact `(Y,Z,n,q)` residual instance, valuation decoding gives zero or one realizing parity word.

The full CRT seam remains conditional on a stronger exact state actually supplying a full `z_H mod3^28` observation.

## Exact-pair correction inversion — CLOSED

For a proposed source/checkpoint pair,

\[
C_{req}=2^{t_0}Z-3^{j_0}X.
\]

After an exact prefix is discharged, the suffix problem is again

\[
C(B)=2^{|B|}Z-3^{q(B)}Y.
\]

For

\[
R=2^nZ-3^qY,
\]

the next one-position is forced by

\[
\boxed{a=v_2(R)}.
\]

Before endpoint depth,

\[
v_2(R)=v_2(Y),
\]

so the next odd event can be decoded without checkpoint information.

Canonical objects:

- `../theorems/SOURCE_CONTROLLED_RESIDUAL_CORRECTION_RECURSION.md`;
- `../theorems/RESIDUAL_VALUATION_JUMP_DECODER.md`;
- `../theorems/AFFINE_VALUATION_CYLINDER_JUMP.md`.

## Source-preserving valuation state — CLOSED

At current depth `h`, retain

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\qquad
m_{lo}\le m\le m_{hi}.
\]

With pure-ballot surplus

\[
S=q-Q(h),
\]

we have

\[
q=Q(h)+S,
\qquad
3^q=3^{Q(h)+S}.
\]

Thus stored affine coefficient `A=3^q` is redundant, while the exact source residue `r` is required by later source-sensitive predicates.

The reusable state is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S;\text{future-predicate labels}).}
\]

For a valuation branch `a`,

\[
\rho_a
\equiv
(2^a-y)3^{-q}
\pmod{2^{a+1}},
\]

and writing

\[
m=\rho_a+2^{a+1}k
\]

gives exact child channels

\[
X=r'+2^{h'}k,
\qquad
T^{h'}(X)=y'+3^{q+1}k.
\]

Canonical objects:

- `../theorems/SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`;
- `../src/A0_s1_source_payload_control_factorization_certificate.py`.

## Pure-ballot control factor — CLOSED

The legality and outgoing surplus of `0^a1` depend only on `(h,S,a)`.
Therefore the transition separates into

\[
\boxed{
\text{ballot control template}
\otimes
\text{source arithmetic payload}.
}
\]

At the certified eight-jump frontier:

\[
14\text{ roots}
\to
14{,}224\text{ source cylinders}.
\]

The pure-ballot surviving population is

\[
\boxed{26{,}859{,}837{,}368{,}845{,}079{,}186}.
\]

Those 14,224 payloads occupy only `90` distinct exact `(h,S)` controls.
A four-future-odd-event ballot-control signature has only `13` classes on this frontier.

This permits transition-skeleton reuse but **not** source-payload merging.

Canonical objects:

- `../theorems/VALUATION_JUMP_BALLOT_CONTROL.md`;
- `../theorems/FINITE_HORIZON_BALLOT_CONTROL_SIGNATURE.md`;
- `../src/A0_s1_14root_8jump_ballot_pruning_certificate.py`;
- `../src/A0_s1_finite_horizon_ballot_control_signature_certificate.py`.

## Secondary defect tightening — SAFE / LOW YIELD

Combining the exact accumulated prefix defect with an exact tail DP for the minimum further first-75 defect needed to satisfy the already-certified `d_75>=8` condition gives

\[
26{,}859{,}837{,}368{,}588{,}270{,}254
\]

survivors after eight jumps.

The additional rejection is only

\[
\boxed{256{,}808{,}932},
\]

about `9.56e-12` of the pure-ballot eight-jump population, and it closes no additional cylinder.

Therefore this combination remains a secondary pruning label, not the principal S10 engine.

Canonical object:

- `../src/A0_s1_14root_8jump_tail_defect_tightening_certificate.py`.

## Principal active object — source-sensitive future-language quotient

The remaining S10 problem is no longer exact-pair correction inversion and no longer pure-ballot control.

The next state extension must add the source-sensitive controls that still distinguish future realizability:

1. exact H/L or equivalent pre-bridge formation control;
2. the precise renewal/C4F state still required by Route-B;
3. checkpoint/debit information only when its certified observation resolution becomes active;
4. optional `P_min` or defect labels only inside an already identical future-control class.

A legal merge theorem must answer:

> When do two distinct source payloads have exactly the same future realization set under every still-active predicate?

Equality of `(h,S)`, valuation, residual, population size, or physical score alone is not sufficient.

## Immediate theorem / algorithm target

Construct an exact **source-sensitive valuation-cylinder transducer** by extending

\[
(r,y,m_{lo},m_{hi},h,S)
\]

with the minimal H/L/pre-bridge and renewal/C4F coordinates.

One transition should:

1. use the shared `(h,S)` control template to list ballot-legal `a`;
2. partition each source payload by the exact valuation residue;
3. jump the forced block `0^a1` while preserving `r` and `y`;
4. update H/L and renewal/C4F state exactly;
5. consume/forget a predicate coordinate only after its observation has been discharged;
6. reject children violating an active exact predicate;
7. merge only under a proved source-sensitive future-equivalence theorem.

## DSD audit rules

Allowed:

- exact correction composition and residual recursion;
- exact-pair valuation decoding;
- affine valuation-cylinder partition and forced zero-run jump;
- source-payload / control factorization;
- finite-horizon ballot-control signature reuse;
- exact source residue retention for source-sensitive predicates;
- predicate-relative forgetting after discharge;
- secondary `P_min`/defect pruning inside exact future-control classes.

Forbidden:

- exact-pair uniqueness -> family-level uniqueness;
- equal ballot-control signature -> equal source family;
- equal valuation/residual -> legal merge when future controls differ;
- dropping source residue `r` before all source-sensitive predicates are discharged;
- terminal target-dominance existence -> full correction membership;
- terminal dominance -> full `z_H mod3^28`;
- checkpoint/source exposure -> same orbit automatically;
- finite transducer regression -> universal Route-B closure;
- marginal density multiplication;
- later refined bounds used retroactively.

## Global warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`. Route-A, `s>=2`, remaining formation sectors, and global branch completeness remain separate obligations.

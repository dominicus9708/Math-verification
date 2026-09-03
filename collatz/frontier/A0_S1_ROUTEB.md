# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation.

## Input family

Exact retained first-defect roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary source certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`.

Every active family is represented exactly as

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with a finite integer parameter interval.

## Closed/rejected routes that must not be restarted

### Terminal target-dominance as a pruning engine

The terminal 28-gate target-dominance existence condition reduces to

\[
Z\bmod3\in\{1,2\},
\]

but every genuine positive-one-count checkpoint already satisfies `3∤Z`.

Therefore terminal target dominance is exact but redundant for independent pruning.

### Dominance-only weak CRT

`Z mod2^27` plus only the automatic mod-3 condition does not isolate an ordinary checkpoint in the debit corridor.

### `P_min` alone

The directed physical Bellman score is exact in its stated active class, but finite deep-root execution did not close the tested families. It remains a secondary predicate.

### Direct slack-carry -> one formation-rank-path identification

The normalized suffix carry has the local projective recurrence

\[
c_{t+1}
=
\frac{2c_t+2(2^{D_t}-2^{s_t})}{3},
\]

which is algebraically identical to one formation transition with local ranks `(D_t,s_t)`.

However consecutive local pairs form one ordinary formation rank path only if

\[
s_t=D_{t+1}
\iff
B_t=A_{t+1}+1.
\]

General dominance does not imply this, and finite regression finds failures even for candidate=target. A rank-increase reset is illegal; a descending connector is carry-changing and therefore not a free relabel.

Hence local recurrence equality must **not** be globalized into formation membership without a separate explicit bridge theorem.

Canonical objects:

- `../theorems/SLACK_FORMATION_LOCAL_CONJUGACY_STITCHING_OBSTRUCTION.md`;
- `../src/A0_s1_routeB_slack_formation_local_conjugacy_stitching_certificate.py`;
- `../audits/S10_LOCAL_CONJUGACY_AND_FINITE_TEMPLATE_QUOTIENT_AUDIT.md`.

## Closed structural interfaces retained

1. exact affine source cylinders and source-preserving bit/block refinement;
2. pure-ballot/target-dominance control;
3. fixed-`(h,q)` correction injectivity and valuation decoding;
4. correction composition and exact residual recursion;
5. affine valuation-cylinder `0^a1` jumps;
6. source-payload / ballot-control factorization;
7. certified multibit block transduction;
8. terminal ternary locality and critical-cut precision absorption;
9. synchronized `Z mod2^27 × Z mod3^28` CRT singleton exposure when both coherent observations exist;
10. checkpoint-conditioned source fibers;
11. local CRT/positivity splice giving an actual local accelerated-Collatz orbit segment;
12. finite-horizon source/ballot product-template quotient for transition-DAG reuse.

## Exact-pair inversion — CLOSED

For an exact residual instance

\[
R=2^nZ-3^qY,
\]

the next one-position is forced by

\[
a=v_2(R).
\]

Before endpoint depth,

\[
v_2(R)=v_2(Y),
\]

so repeated exact `0^a1` discharge either rejects or reconstructs the unique possible parity word.

The unresolved difficulty is therefore family-scale execution, not inversion of one exact source/checkpoint pair.

Canonical objects:

- `../theorems/SOURCE_CONTROLLED_RESIDUAL_CORRECTION_RECURSION.md`;
- `../theorems/RESIDUAL_VALUATION_JUMP_DECODER.md`;
- `../theorems/AFFINE_VALUATION_CYLINDER_JUMP.md`.

## Persistent source state — MINIMIZED / CLOSED

Let

\[
S=q-Q(h),
\qquad
Q(h)=\lceil h\log_3 2\rceil.
\]

Then

\[
q=Q(h)+S.
\]

Because the total Route-B target parameters are fixed,

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701,
\]

the remaining counters are also derived:

\[
n_{rem}=t_0-h,
\]

\[
q_{rem}=j_0-Q(h)-S.
\]

Thus the currently justified persistent early/middle S10 core is

\[
\boxed{
(r,y,m_{lo},m_{hi},h,S).
}
\]

Derived rather than stored:

- `q=Q(h)+S`;
- `3^q`;
- `n_rem=t0-h`;
- `q_rem=j0-Q(h)-S`.

Canonical objects:

- `../theorems/SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`;
- `../theorems/FIXED_TARGET_COUNTER_DERIVATION.md`.

## Valuation jump / ballot factor — CLOSED

For a next-one valuation branch `a`,

\[
\rho_a
\equiv
(2^a-y)3^{-q}
\pmod{2^{a+1}},
\]

and

\[
m=\rho_a+2^{a+1}k
\]

produces exact child channels

\[
X=r'+2^{h'}k,
\qquad
T^{h'}(X)=y'+3^{q+1}k.
\]

The legality and outgoing surplus of the forced `0^a1` depend only on `(h,S,a)`, so the computation factors as

\[
\boxed{
\text{shared ballot-control template}
\otimes
\text{distinct source payload}.
}
\]

At the certified eight-jump frontier:

- source cylinders: `14,224`;
- pure-ballot survivors: `26,859,837,368,845,079,186`;
- distinct exact `(h,S)` controls: `90`;
- distinct four-future-jump ballot-control signatures: `13`.

This allows control-code reuse but does **not** prove source-payload merging.

Secondary accumulated-defect + first-75 tail tightening removes only `256,808,932` more integers and closes no additional cylinder, so it is not the principal engine.

## Finite-horizon source/ballot product templates — CLOSED / EXECUTION ONLY

For future raw-bit horizon `d`, define

\[
Q_d^{src}
=
(y\bmod2^d,3^q\bmod2^d)
\]

and

\[
B_d(h,S)
=
(S,\Delta_1,\ldots,\Delta_d),
\qquad
\Delta_i=Q(h+i)-Q(h+i-1).
\]

Then

\[
\boxed{
P_d=(B_d,Q_d^{src})
}
\]

is an exact next-`d`-bit transition template: equal `P_d` gives the same low-parameter-residue -> parity map and the same pure-ballot verdicts through that finite horizon.

At the current 14,224-cylinder frontier:

- `d=4`: `583` templates;
- `d=8`: `8,372` templates;
- `d=12`: `13,923` templates;
- `d=16`: `14,209` templates;
- `d=17`: `14,213` templates;
- `d=18`: `14,224` templates.

Thus short-horizon transition logic is highly reusable, but this particular quotient completely separates the current payloads by 18 future raw bits.

Consequences:

- use `P_d` to share computation/DAG nodes;
- do not merge exact source payloads on `P_d` alone;
- do not infer a horizon-independent finite-state closure from low-`d` reuse;
- a stronger source-sensitive invariant is still required for proof-level contraction.

Canonical objects:

- `../theorems/FINITE_HORIZON_SOURCE_BALLOT_PRODUCT_TEMPLATE_QUOTIENT.md`;
- `../src/A0_s1_routeB_8jump_source_ballot_product_template_quotient_certificate.py`;
- `../audits/S10_LOCAL_CONJUGACY_AND_FINITE_TEMPLATE_QUOTIENT_AUDIT.md`.

## Predicate activation schedule — CLOSED

The remaining state must follow actual observation time rather than carry every later predicate globally.

### H/L / block grammar

A certified block with

\[
(|B|,q(B),C(B))=(b,p,\gamma)
\]

is consumed exactly by the existing multibit source-channel transducer.

Therefore H/L or Christoffel structure is treated as **transient block-computation grammar** unless a separate theorem proves that an unresolved later predicate depends on the grammar-history label itself.

Do not count H/L as an independent probabilistic pruning factor when it represents the same formation language.

### Terminal ternary checkpoint observation

If the pre-checkpoint word is `W=AB` and `B` contains exactly the final `K` one-events, then

\[
\boxed{
Z\equiv2^{-|B|}C(B)\pmod{3^K}.
}
\]

For the current `K=28`, `Z mod3^28` activates only when the remaining pre-checkpoint one-count reaches

\[
\boxed{q_{rem}=28.}
\]

Equivalently,

\[
Q(h)+S=j_0-28=65{,}868{,}186{,}673.
\]

This activation boundary is detected from `(h,S)` alone.

### Post-checkpoint dyadic observation

`Z mod2^27` is determined by the first 27 post-checkpoint parity bits. It is therefore an S11/tail coordinate, not an early S10 coordinate.

### Local same-orbit provenance

Once coherent terminal ternary and post-checkpoint dyadic observations exist, invoke the certified CRT/debit/local-splice interfaces. A permanent pre-bridge same-orbit flag is unnecessary.

### `C4F`

The working label `C4F` is **not** admitted as a state coordinate until its exact Route-B predicate and state requirement are formally identified. An undefined name cannot justify state growth, merging, or rejection.

Canonical objects:

- `../theorems/PREDICATE_ACTIVATION_SCHEDULE.md`;
- `../theorems/FIXED_TARGET_COUNTER_DERIVATION.md`;
- `../audits/S10_PREDICATE_ACTIVATION_AUDIT.md`;
- `../src/A0_s1_checkpoint_late_activation_certificate.py`;
- `../src/A0_s1_fixed_target_counter_derivation_certificate.py`.

## Principal active object — source-sensitive family contraction

The S10 state should **not** now be enlarged with speculative H/L, checkpoint, C4F, or formation-rank coordinates.

The active computation is:

> propagate the minimized exact source state through certified valuation or larger block transitions, share finite-horizon transition logic through exact product templates, reject only by active exact predicates, and seek a stronger source-sensitive invariant that contracts or bounds payload complexity without losing any later predicate.

One transition engine may use either:

1. valuation-cylinder `0^a1` jumps; or
2. a certified larger block `(b,p,\gamma)` supplied by an exact grammar/DAG and consumed by the multibit source transducer.

The current results separate three notions:

- **block compilation** can reduce execution work without reducing exact leaf count;
- **finite source/ballot templates** can share short-horizon transition DAGs without merging payloads;
- **proof-level contraction** still requires a new source-sensitive invariant, whole-payload rejection predicate, or certified global quotient.

## Immediate computation targets

1. use `P_d` only as a shared execution template over short horizons;
2. search existing source-sensitive predicates/invariants for one that is invariant under continuation and can reject or merge whole payload pieces;
3. prefer exact whole-cylinder/fiber rejection over deeper raw valuation expansion;
4. retain `(r,y,m_lo,m_hi,h,S)` exactly whenever source payload remains live;
5. do not pursue direct slack-carry -> formation-rank-path globalization without a new bridge theorem;
6. activate `Z mod3^28` only at `q_rem=28`;
7. move `Z mod2^27`, CRT, debit and local splice to S11;
8. keep `C4F` OPEN until its precise predicate is recovered or defined.

## DSD audit rules

Allowed:

- exact correction composition and residual recursion;
- exact-pair valuation decoding;
- source-preserving valuation or certified multibit block transitions;
- source-payload / control factorization;
- finite-horizon control/template reuse;
- derivation rather than storage of redundant counters;
- predicate-relative activation and forgetting;
- secondary physical/defect pruning inside valid active classes.

Forbidden:

- exact-pair uniqueness -> family-level uniqueness;
- equal control signature -> equal source family;
- equal finite product template -> equal source payload;
- equal valuation/residual -> legal source merge;
- dropping source residue `r` before source-sensitive predicates are discharged;
- local recurrence equality -> one global formation rank path;
- treating H/L representation as independent pruning information without a new predicate;
- inventing a `C4F` state before defining its predicate;
- carrying checkpoint residues before their local observations exist;
- checkpoint exposure -> same orbit without certified splice hypotheses;
- finite regression -> universal Route-B closure;
- marginal density multiplication;
- later refined bounds used retroactively.

## Global warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`. Route-A, `s>=2`, remaining formation sectors, and global branch completeness remain separate obligations before any Collatz conclusion.

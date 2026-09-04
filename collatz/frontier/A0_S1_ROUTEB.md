# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**  
Last synchronized: **2026-09-05**

This is the canonical resume point for the current computation.

## 1. Exact source family

Retained first-defect roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Every active family is represented exactly by

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with a finite integer interval for `m`.

Primary source certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`.

Initial 14-root population:

\[
125{,}072{,}439{,}875{,}999{,}947{,}649.
\]

## 2. Persistent S10 state — MINIMIZED / CLOSED

Let

\[
Q(h)=\min\{q:3^q>2^h\},
\qquad
S=q-Q(h).
\]

Then `q=Q(h)+S`, so the persistent early/middle state is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S)}.
\]

`q`, `3^q`, `n_rem=t_0-h`, and `q_rem=j_0-Q(h)-S` are derived.

Fixed target:

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701.
\]

Do not drop `r` before all source-sensitive predicates are discharged.

## 3. Exact source transition

For the next `0^a1` branch,

\[
\rho_a\equiv(2^a-y)3^{-q}\pmod{2^{a+1}},
\qquad
m=\rho_a+2^{a+1}k,
\]

which produces another exact affine source cylinder.

Exact residual inversion remains

\[
R=2^nZ-3^qY,
\qquad
a=v_2(R).
\]

Canonical dependencies include:

- `SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`;
- `SOURCE_CONTROLLED_RESIDUAL_CORRECTION_RECURSION.md`;
- `RESIDUAL_VALUATION_JUMP_DECODER.md`;
- `AFFINE_VALUATION_CYLINDER_JUMP.md`;
- `VALUATION_MACROBLOCK_COMPILATION.md`.

## 4. Canonical jump-8 population

Pure-ballot jump-8 frontier:

\[
14{,}224\text{ source cylinders},
\]

\[
26{,}859{,}837{,}368{,}845{,}079{,}186
\]

source integers.

First-75 tail-defect tightening leaves

\[
26{,}859{,}837{,}368{,}588{,}270{,}254.
\]

Successive cumulative future-displacement floors, always **replacing rather than adding** the previous floor, give:

| certified floor | exact finite basis | population after cut | incremental removal |
|---|---|---:|---:|
| `eta_future >= 1/4` | `D_46 >= 3` | 26,859,837,368,531,301,450 | 56,968,804 |
| `eta_future >= 1/3` | `D_49 >= 4` | 26,859,837,368,506,133,665 | 25,167,785 |
| `eta_future >= 5/12` | `D_51 >= 5` | 26,859,837,368,480,843,030 | 25,290,635 |
| `eta_future >= 1/2` | exact horizon-51 `D<=5` emptiness | **26,859,837,368,455,538,464** | **25,304,566** |

Thus the current canonical population is

\[
\boxed{26{,}859{,}837{,}368{,}455{,}538{,}464}.
\]

The source-cylinder count is still `14,224`; no whole interval has closed.

Current downstream export:

- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

The canonical `>=1/2` validation workflow passed in GitHub Actions run `33864085911`.

## 5. Bounded future displacement — secondary exact pruning

Certified exact equalities through budget four are

\[
\boxed{H_0=40,\quad H_1=44,\quad H_2=45,\quad H_3=48,\quad H_4=50.}
\]

For budget five, the exact 64-shard horizon-51 decision reports

\[
\boxed{\#\{D_{51}\le5\text{ paths}\}=0}.
\]

Hence

\[
\boxed{H_5\le50},
\qquad
\boxed{D_{51}\ge6},
\qquad
\boxed{\eta_{future}>\frac12}.
\]

`H_5=50` is not claimed without a horizon-50 witness.

Canonical dependencies:

- `../src/A0_s1_8jump_c5_h51_shard_probe.py`;
- `../src/A0_s1_8jump_six_displacement_eta_half_pruning_certificate.py`;
- `../audits/S10_SIX_DISPLACEMENT_HORIZON_PRUNING_AUDIT.md`;
- GitHub Actions run `33756884264`.

The directed `P_min` mechanism is permanently unable to close approximately `82.095%` of the first-75-tightened source population even under the maximal remaining target-correction budget. Further bounded-displacement expansion is therefore secondary unless it reveals a new structural theorem.

## 6. Late terminal observation is event-local, not time-local

Terminal ternary observation activates when

\[
q_{rem}=28,
\qquad
q=j_0-28=65{,}868{,}186{,}673.
\]

The exact threshold one-position formula is

\[
\boxed{t_{r-1}=\lfloor(r-1)\log_2 3\rfloor}.
\]

At the current activation rank the threshold `q`-th one is at

\[
\boxed{104{,}398{,}605{,}865}.
\]

If the canonical activation seam is immediately after the candidate `q`-th one, then under ordering/dominance alone

\[
\boxed{44\le t_0-h_{act}\le38{,}530{,}419{,}237}.
\]

Thus `q_rem=28` means only 28 future **one-events**, not a universal short ordinary-bit suffix. The final exporter must represent 28 valuation gaps/event transitions rather than enumerate raw bit-time.

Dependencies:

- `../theorems/TERMINAL_28_EVENT_LOCALITY_NOT_TIME_LOCALITY.md`;
- `../src/A0_s1_terminal_28_event_locality_not_time_locality_certificate.py`.

Status: **EXACT / CLOSED distinction**.

## 7. Checkpoint observation arithmetic and terminal defect projection — CLOSED

The final 28 one-events determine `Z mod 3^28`; the first 27 post-checkpoint bits determine `Z mod 2^27`.

A synchronized pair exposes at most one ordinary checkpoint `Z` in the certified SAFE corridor.

The terminal/right-H transfer is affine and bijective modulo `3^28`:

\[
z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}}.
\]

For the current terminal 28-gate **target-dominance existence** predicate,

\[
\boxed{\text{completion exists}\iff3\nmid Z}.
\]

The exact final-28 physical defect is not independent of this projective observation.  If the right-H block begins at

\[
p_R=t_0-s=103{,}768{,}467{,}013,
\]

then

\[
\boxed{z_H\equiv-2^{-p_R}F_{28}\pmod{3^{28}}}
\]

with

\[
2^{-p_R}\equiv1{,}051{,}701{,}240{,}047\pmod{3^{28}}.
\]

Hence a validated terminal descriptor `(n,C_B)` gives

\[
F_{28}=C_{T,tail}^{(28)}-2^{t_0-n}C_B
\]

and therefore determines the only compatible `z_H` exactly.

Dependencies:

- `../theorems/TERMINAL_DEFECT_PROJECTIVE_OBSERVATION_REDUNDANCY.md`;
- `../src/A0_s1_routeB_terminal_defect_projective_observation_redundancy_certificate.py`;
- `../audits/S10_TERMINAL_DEFECT_PROJECTIVE_OBSERVATION_REDUNDANCY_AUDIT.md`.

CRT compatibility alone is not source realization.

## 8. Source/checkpoint same-orbit kernel — CLOSED

At a valid late activation channel

\[
X=r+2^hk,
\qquad
T^h(X)=y+3^qk,
\qquad q=j_0-28,
\qquad k\in[k_{lo},k_{hi}],
\]

let a validated terminal suffix descriptor satisfy

\[
|B|=n,
\qquad q(B)=28,
\qquad C_B=C(B).
\]

For one ordinary checkpoint candidate `Z`, define

\[
Y_B(Z)=\frac{2^nZ-C_B}{3^{28}}.
\]

The exact source-provenance test is

\[
Y_B(Z)-y\equiv0\pmod{3^q},
\]

and

\[
k_*:=\frac{Y_B(Z)-y}{3^q}\in[k_{lo},k_{hi}].
\]

When it passes,

\[
\boxed{T^{h+n}(r+2^hk_*)=Z}.
\]

For a fixed activation channel, terminal suffix descriptor and `Z`, the source parameter is unique.

Dependencies:

- `../theorems/SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md`;
- `../src/A0_s1_source_activation_checkpoint_provenance_join_certificate.py`;
- `../audits/S10_SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN_AUDIT.md`.

Regression workflow run `33864578621` passed.

Status: **EXACT / CLOSED join kernel**.

## 9. Source-first terminal endpoint lattice — CLOSED

The fixed terminal descriptor can be applied directly to the activation source parameter before an ordinary checkpoint is supplied from another interface.

For a validated `(n,C_B)`, define the unique source residue

\[
\boxed{
\kappa_B
\equiv
-\left(3^{28}y+C_B\right)(3^{j_0})^{-1}
\pmod{2^n}.
}
\]

Write

\[
k=\kappa_B+2^nt.
\]

Since

\[
h+n=t_0,
\qquad
q+28=j_0,
\]

the complete source/checkpoint endpoints satisfy

\[
\boxed{
(X,Z)=(R_B,Z_B)+t(2^{t_0},3^{j_0}).
}
\]

The certified physical source corridor lies below `2^72`, while `t_0>72`.  Therefore the source spacing `2^{t_0}` is larger than the complete physical source corridor and

\[
\boxed{\text{each fixed activation channel + validated }(n,C_B)\text{ has at most one physical source }X.}
\]

If that source exists, the same unique `t` directly determines its provenanced ordinary checkpoint `Z`.

Thus when the terminal descriptor itself is generated with source provenance, CRT need not manufacture `Z`; the synchronized/right-H/dyadic interfaces become downstream consistency or membership checks on a source-derived checkpoint.

Dependencies:

- `../theorems/SOURCE_TERMINAL_DESCRIPTOR_ENDPOINT_LATTICE.md`;
- `../src/A0_s1_source_terminal_descriptor_endpoint_lattice_certificate.py`.

Status: **EXACT / CLOSED source-first endpoint theorem**.

## 10. State after provenanced checkpoint exposure — MINIMIZED / CLOSED

Once one ordinary `Z` is exposed **with provenance**,

\[
\boxed{z_2=Z\bmod2^{27}}
\]

and the right-H `z_H` value are derived from `Z`; the actual 27-bit post-checkpoint prefix is deterministic from `Z` as well.

Therefore after provenanced `Z` exposure, persistent checkpoint state should prefer

\[
\boxed{Z}
\]

plus only genuinely independent later predicates, rather than retain a Cartesian `(z_2,z_H)` pair.

Before exposure, independently generated directed observations may not be Cartesian-paired.  If `(n,C_B)` is already source-derived, `z_H` is derived from it even before `Z` exposure and must not be independently paired at that stage either.

Dependencies:

- `../theorems/EXPOSED_CHECKPOINT_OBSERVATION_STATE_MINIMIZATION.md`;
- `../src/A0_s1_exposed_checkpoint_observation_state_minimization_certificate.py`.

Combined validation run `33865446235` passed.

## 11. Per-checkpoint source localization — exact but not membership

For one already-exposed ordinary checkpoint `Z`, the independent SAFE debit corridor restricts a current cylinder's source parameter to a window of width

\[
\frac{37\cdot2^{33}}{3\cdot2^h}.
\]

On the current `>=1/2` frontier, summing the deterministic per-cylinder caps gives

\[
\boxed{3{,}256{,}612{,}398}
\]

source parameters per single exposed `Z` at most.

This is at least an

\[
\boxed{8{,}247{,}784{,}533}
\]

fold reduction relative to the current source population.

Further:

- `6,190 / 14,224` cylinders have per-`Z` cap `<=1`;
- `9,537 / 14,224` have per-`Z` cap `<=1000`.

This is localization only. The debit relation does not prove `T^t(X)=Z`.

Dependency:

- `../src/A0_s1_8jump_checkpoint_source_fiber_profile_certificate.py`.

## 12. Principal OPEN gate — source-preserving activation + terminal-descriptor language

The local residue/CRT/same-orbit arithmetic and source-first endpoint arithmetic are no longer the principal gaps.

The current principal object is now

\[
\boxed{\text{source-preserving late-activation and exact terminal-descriptor exporter}.}
\]

It must:

1. carry source provenance from the current 14,224 families to `q=j_0-28` without expanding the raw ~`10^11`-bit middle word;
2. generate/validate the final 28 one-events as an exact valuation-gap or equivalent `(n,C_B)` descriptor language;
3. intersect each descriptor with its exact source-parameter residue `kappa_B mod 2^n`;
4. use the source-first endpoint lattice to expose the at-most-one provenanced `(X,Z)` pair per descriptor;
5. derive `F_28`, `z_H`, `z_2`, and the actual post-checkpoint prefix rather than store them as independent marginals;
6. test the remaining right-H formation/boundary and post-checkpoint predicates on that provenanced state.

On the right-H side, the existing backward exponential carry chart remains one-step injective for precision

\[
m\ge18.
\]

For `m<=17`, several slack representatives of one **prescribed** observation may remain possible.  After the terminal-defect audit this low-precision family is no longer a required independent checkpoint-output family.  It is a local right-H **acceptance/membership problem for the prescribed `z_H` derived from `(n,C_B)`**.

The terminal 28-gate target-dominance existence test itself is already saturated to `3\nmid Z`; reconstructing the whole 28-gate tree merely for that predicate is redundant.

## 13. Rejected shortcuts

Do not restart or use the following as independent proof steps:

1. terminal target-dominance mod-3 filtering as an independent genuine-checkpoint pruning factor;
2. contracting ceiling inside active pure-ballot S10;
3. correction-language or H/L re-expression as an independent pruning factor;
4. adding realized-prefix displacement again to exact current defect;
5. equal `(h,S)`, control signature, block label, correction label, or formation label -> equal source payload;
6. exact-pair uniqueness -> family uniqueness;
7. CRT compatibility -> same orbit;
8. debit-corridor localization -> same orbit;
9. multiplying marginal survival fractions without independence;
10. extrapolating finite `H_c` values;
11. `H_5<=50 -> H_5=50` without a witness;
12. `q_rem=28 -> universal short raw bit shell`;
13. treating exact `F_28` and its derived `z_H` as independent filters;
14. Cartesian pairing of a source-derived `(n,C_B)` with an unrelated right-H `z_H` marginal;
15. exporting the complete `m<=17` carry family merely to manufacture a checkpoint ternary observation;
16. finite Route-B progress -> global Collatz.

## 14. Immediate next calculations

### A. Source-preserving late-activation bridge — principal

1. derive the minimal exact quotient that transports `(r,y,m_lo,m_hi,h,S)` from the current jump-8 frontier to `q=j_0-28`;
2. use valuation/macroblock compilation only where it preserves the source payload exactly;
3. reject any proposed quotient that merges distinct source payloads without a remaining-predicate right-congruence theorem.

### B. Exact 28-event terminal descriptor language — principal after activation

1. use `(n,C_B)` as the preferred exact descriptor interface, or prove an equivalent smaller valuation-gap quotient;
2. compute the unique `kappa_B mod 2^n` source refinement lazily from the descriptor;
3. apply the CLOSED source-first endpoint lattice immediately after a descriptor is validated;
4. derive `F_28` and `z_H` rather than retain them as independent coordinates.

### C. Right-H prescribed-observation membership — local

1. for a source-derived descriptor, query only its prescribed derived `z_H`;
2. use the `m>=18` singleton theorem gate-by-gate where applicable;
3. handle `m<=17` only as the residual formation/boundary acceptance problem;
4. do not rebuild the low-precision carry tree for pure target-dominance existence alone.

### D. Further bounded displacement — secondary

Further `c` expansion remains available but currently gives upper-tail endpoint cuts with zero whole-cylinder closures. Continue only if it yields a structural gain or is computationally cheap relative to the exporter work.

## 15. DSD status

- exact source representation: **CLOSED**;
- persistent S10 state minimization: **CLOSED**;
- `H_4=50`: **EXACT / CLOSED**;
- horizon-51 `c=5` non-reachability: **EXACT / CLOSED finite frontier**;
- `H_5<=50`: **EXACT**;
- `H_5=50`: **OPEN / not claimed**;
- `D_51>=6`: **EXACT / CLOSED**;
- `eta_future>1/2`: **SAFE consequence**;
- `>=1/2` endpoint population: **EXACT finite arithmetic**;
- terminal 28-event locality distinction: **CLOSED**;
- checkpoint CRT/right-H observation arithmetic: **CLOSED**;
- exact terminal defect -> projective `z_H` projection: **CLOSED / state redundancy discharged**;
- source/checkpoint same-orbit join kernel: **CLOSED**;
- source-first terminal endpoint lattice: **CLOSED**;
- post-exposure checkpoint state minimization: **CLOSED**;
- per-`Z` source-fiber cap: **EXACT localization / membership implication REJECTED**;
- source-preserving late-activation bridge: **OPEN / principal**;
- exact terminal descriptor language generation: **OPEN / principal**;
- right-H prescribed-observation formation acceptance: **OPEN / local**;
- `A0,s=1,Route-B` closure: **OPEN**;
- Collatz: **OPEN**.

## Global scope warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`. Route-A, all `s>=2` sectors, remaining branches, and global branch completeness remain separate obligations.
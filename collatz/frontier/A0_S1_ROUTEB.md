# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**  
Last synchronized: **2026-09-03**

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

First-75 tail-defect tightening removes

\[
256{,}808{,}932
\]

and leaves

\[
26{,}859{,}837{,}368{,}588{,}270{,}254.
\]

Successive cumulative future-displacement floors, always **replacing rather than adding** the previous floor, give:

| certified floor | exact finite basis | population after cut | incremental removal |
|---|---|---:|---:|
| `eta_future >= 1/4` | `D_46 >= 3` | 26,859,837,368,531,301,450 | 56,968,804 |
| `eta_future >= 1/3` | `D_49 >= 4` | 26,859,837,368,506,133,665 | 25,167,785 |
| `eta_future >= 5/12` | `D_51 >= 5` | 26,859,837,368,480,843,030 | 25,290,635 |
| `eta_future >= 1/2` | `D_51 >= 6` on the current `>=5/12` frontier | **26,859,837,368,455,538,464** | **25,304,566** |

Thus the current canonical population is

\[
\boxed{26{,}859{,}837{,}368{,}455{,}538{,}464}.
\]

The source-cylinder count is still `14,224`; no whole interval has closed.

Current downstream export:

- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

Downstream S10 calculations must import this export, not an older `1/4`, `1/3`, or `5/12` frontier.

## 5. Bounded future displacement — exact through the c=5 horizon-51 decision

For future one-ranks write

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0,
\]

and let `D_r` count ranks with `d_k>0` among the first `r` future one-events.

Define `H_c` as the maximum horizon reachable by an exact source-preserving pure-ballot path with at most `c` displaced ranks.

Certified exact equalities through budget four are

\[
\boxed{
H_0=40,
\quad H_1=44,
\quad H_2=45,
\quad H_3=48,
\quad H_4=50.
}
\]

For `c=4`, the horizon-49 exact 32-shard scan leaves only two source parents:

- shard 3: live at 49, empty at 50;
- shard 24: live at 49 and 50, empty at 51.

Therefore `H_4=50` exactly.

For budget five, the exact 64-shard horizon-51 decision on all `14,224` current `>=5/12` source parents reports

\[
\boxed{\#\{D_{51}\le5\text{ paths}\}=0}.
\]

Hence

\[
\boxed{H_5\le50},
\qquad
\boxed{D_{51}\ge6}.
\]

`H_5=50` is **not** claimed: equality would require a horizon-50 `D<=5` witness on the relevant pre-cut frontier.

Since every displaced rank contributes

\[
\epsilon_r>\frac1{12},
\]

we obtain

\[
\boxed{\eta_{future}>\frac12},
\]

safely weakened to `>=1/2` for endpoint pruning.

Canonical dependencies:

- `../theorems/BOUNDED_DISPLACEMENT_SOURCE_REACHABILITY.md`;
- `../theorems/FIVE_DISPLACEMENT_HORIZON_PRUNING.md`;
- `../theorems/SIX_DISPLACEMENT_HORIZON_PRUNING.md`;
- `../src/A0_s1_8jump_c5_h51_shard_probe.py`;
- `../src/A0_s1_8jump_six_displacement_eta_half_pruning_certificate.py`;
- `../audits/S10_SIX_DISPLACEMENT_HORIZON_PRUNING_AUDIT.md`;
- GitHub Actions run `33756884264`.

**Do not extrapolate** the finite `H_c` data into a density or asymptotic law.

## 6. Directed `P_min` split

The established global future-reachability cutoff still splits the first-75-tightened source set into approximately:

- `82.095%`: permanently `P_min`-unreachable;
- `17.905%`: future `P_min` activation remains possible.

Future-defect accumulation is therefore only a direct `P_min` pruning mechanism in the upper sector. The lower sector requires a genuinely independent source-sensitive membership obstruction.

The present `1/2` cut is an exact sequential source-tail cut; it does not imply that displacement work alone can close Route-B.

## 7. Checkpoint activation remains late

Terminal ternary observation activates only when

\[
q_{rem}=28,
\]

equivalently

\[
Q(h)+S=65{,}868{,}186{,}673.
\]

`Z mod 2^27` is observed only from the post-checkpoint 27-bit prefix.

A coherent full pair

\[
Z\bmod2^{27},
\qquad
Z\bmod3^{28}
\]

can expose at most one ordinary checkpoint `Z` in the certified corridor, but CRT compatibility alone is not same-orbit provenance.

`C4F` remains undefined/OPEN and is not a state coordinate.

## 8. Rejected shortcuts

Do not restart or use the following as independent proof steps:

1. terminal target-dominance mod-3 filtering — redundant on genuine checkpoints;
2. contracting ceiling inside active pure-ballot S10 — redundant;
3. correction-language or H/L re-expression as an independent pruning factor;
4. adding realized-prefix displacement again to exact current defect;
5. equal `(h,S)`, control signature, block label, or correction label -> equal source payload;
6. exact-pair uniqueness -> family uniqueness;
7. CRT residue compatibility -> same orbit;
8. source interval exposure -> membership;
9. multiplying marginal survival fractions without independence;
10. extrapolating finite `H_c` values;
11. `H_5<=50` -> `H_5=50` without a horizon-50 witness;
12. finite Route-B progress -> global Collatz.

## 9. Principal next calculations

### A. Independent membership obstruction — principal

Continue the lower-sector problem

\[
\boxed{\text{source-controlled exact correction/checkpoint membership}}.
\]

Priority interface:

\[
\boxed{\text{source family}\leftrightarrow(z_2,z_H)\leftrightarrow\text{right-H/checkpoint family}}.
\]

Required stages:

1. source family -> late `z_H=Z mod 3^28` observation;
2. post-checkpoint/right-H family -> `z_2=Z mod2^27`;
3. synchronized CRT pair -> at most one corridor checkpoint candidate;
4. source/debit compatibility;
5. exact same-orbit provenance.

### B. Further bounded displacement — secondary

Further `c` expansion remains available, but the last three floor improvements removed only about 25 million integers each and closed zero whole intervals. Any `c=6` work should therefore be justified by computational cost or by a new structural theorem rather than automatic continuation.

If the exact value `H_5` becomes useful, first search for a horizon-50 `D<=5` witness; otherwise the current upper bound `H_5<=50` is sufficient for the `D_51>=6` cut already obtained.

## 10. DSD status

- exact source representation: **CLOSED**;
- persistent S10 state minimization: **CLOSED**;
- `H_4=50`: **EXACT / CLOSED**;
- horizon-51 `c=5` non-reachability: **EXACT / CLOSED finite frontier**;
- `H_5<=50`: **EXACT**;
- `H_5=50`: **OPEN / not claimed**;
- `D_51>=6`: **EXACT / CLOSED**;
- `eta_future>1/2`: **SAFE consequence**;
- `>=1/2` endpoint population: **EXACT finite arithmetic**;
- whole-source-cylinder closure from this chain: **0**;
- source-controlled full long membership: **OPEN**;
- `A0,s=1,Route-B` closure: **OPEN**;
- Collatz: **OPEN**.

## Global scope warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`. Route-A, all `s>=2` sectors, remaining branches, and global branch completeness remain separate obligations.

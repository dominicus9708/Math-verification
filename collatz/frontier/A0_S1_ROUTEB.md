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
| `eta_future >= 5/12` | `D_51 >= 5` | **26,859,837,368,480,843,030** | **25,290,635** |

Thus the current canonical population is

\[
\boxed{26{,}859{,}837{,}368{,}480{,}843{,}030}.
\]

The source-cylinder count is still `14,224`; no whole interval has closed.

Current downstream export:

- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py::pruned_states`.

Downstream S10 calculations must import this export, not an older `1/4` or `1/3` frontier.

## 5. Bounded future displacement — CLOSED through budget 4

For future one-ranks write

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0,
\]

and let `D_r` count ranks with `d_k>0` among the first `r` future one-events.

Define `H_c` as the maximum horizon reachable by an exact source-preserving pure-ballot path with at most `c` displaced ranks.

Certified values:

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

All other shards are already empty at horizon 49. Therefore

\[
\boxed{H_4=50}
\]

and every horizon-51 survivor satisfies

\[
\boxed{D_{51}\ge5}.
\]

Since every displaced rank contributes

\[
\epsilon_r>\frac1{12},
\]

we obtain

\[
\boxed{\eta_{future}>\frac5{12}},
\]

safely weakened to `>=5/12` for endpoint pruning.

Canonical dependencies:

- `../theorems/BOUNDED_DISPLACEMENT_SOURCE_REACHABILITY.md`;
- `../theorems/FOUR_DISPLACEMENT_HORIZON_PRUNING.md`;
- `../theorems/FIVE_DISPLACEMENT_HORIZON_PRUNING.md`;
- `../src/A0_s1_8jump_c4_h49_shard_certificate.py`;
- `../src/A0_s1_8jump_c4_exception_horizon_certificate.py`;
- `../src/A0_s1_8jump_five_displacement_eta_pruning_certificate.py`;
- `../audits/S10_FIVE_DISPLACEMENT_HORIZON_PRUNING_AUDIT.md`.

**Do not extrapolate** the sequence `40,44,45,48,50` into a density or asymptotic law.

## 6. Directed `P_min` split

The established global future-reachability cutoff still splits the first-75-tightened source set into approximately:

- `82.095%`: permanently `P_min`-unreachable;
- `17.905%`: future `P_min` activation remains possible.

Future-defect accumulation is therefore only a direct `P_min` pruning mechanism in the upper sector.  The lower sector requires a genuinely independent source-sensitive membership obstruction.

The present `5/12` cut is an exact sequential source-tail cut; it does not imply that displacement work alone can close Route-B.

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
11. finite Route-B progress -> global Collatz.

## 9. Principal next calculations

### A. Bounded displacement

The next finite object is

\[
H_5.
\]

Use the current `>=5/12` `pruned_states`.  Preserve exact source payloads and use sparse decision recursion/sharding rather than unrestricted raw-tree expansion.

Before proceeding far beyond `c=5`, compare the added endpoint pruning with execution cost; the last two increments were only about 25 million integers each and closed zero whole interval.

### B. Independent membership obstruction

In parallel, continue the more important lower-sector problem:

\[
\boxed{\text{source-controlled exact correction/checkpoint membership}}.
\]

Priority interfaces:

1. source family -> late `z_H=Z mod 3^28` observation;
2. post-checkpoint -> `z_2=Z mod2^27`;
3. synchronized CRT candidate -> source/debit compatibility;
4. exact same-orbit provenance, not mere residue compatibility.

## 10. DSD status

- exact source representation: **CLOSED**;
- persistent S10 state minimization: **CLOSED**;
- `H_4=50`: **EXACT / CLOSED on current finite frontier**;
- `D_51>=5`: **EXACT / CLOSED**;
- `eta_future>5/12`: **SAFE consequence**;
- `>=5/12` endpoint population: **EXACT finite arithmetic**;
- whole-source-cylinder closure from this step: **0**;
- source-controlled full long membership: **OPEN**;
- `A0,s=1,Route-B` closure: **OPEN**;
- Collatz: **OPEN**.

## Global scope warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`. Route-A, all `s>=2` sectors, remaining branches, and global branch completeness remain separate obligations.

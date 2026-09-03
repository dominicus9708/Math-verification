# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for the current computation.

## 1. Exact input family

Retained first-defect roots:

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

Initial 14-root population:

\[
125{,}072{,}439{,}875{,}999{,}947{,}649.
\]

## 2. Current persistent S10 state — MINIMIZED / CLOSED

Let

\[
S=q-Q(h),
\qquad
Q(h)=\min\{q:3^q>2^h\}.
\]

Then

\[
q=Q(h)+S.
\]

The currently justified persistent state is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S).}
\]

Derived rather than stored:

- `q=Q(h)+S`;
- `3^q`;
- `n_rem=t0-h`;
- `q_rem=j0-Q(h)-S`.

Fixed target parameters:

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701.
\]

Canonical dependencies:

- `../theorems/SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`;
- `../theorems/FIXED_TARGET_COUNTER_DERIVATION.md`.

## 3. Exact-pair inversion and valuation source refinement — CLOSED

For an exact residual pair

\[
R=2^nZ-3^qY,
\]

the next one-position is forced by

\[
a=v_2(R).
\]

Before endpoint depth,

\[
v_2(R)=v_2(Y).
\]

For a source family the next `0^a1` branch selects the exact parameter residue

\[
\rho_a\equiv(2^a-y)3^{-q}\pmod{2^{a+1}},
\]

and writing

\[
m=\rho_a+2^{a+1}k
\]

produces another exact affine source cylinder.

Pure-ballot legality and outgoing surplus depend only on `(h,S,a)`.

Thus computation factors as

\[
\boxed{\text{shared control template}\otimes\text{distinct source payload}.}
\]

Canonical dependencies:

- `../theorems/SOURCE_CONTROLLED_RESIDUAL_CORRECTION_RECURSION.md`;
- `../theorems/RESIDUAL_VALUATION_JUMP_DECODER.md`;
- `../theorems/AFFINE_VALUATION_CYLINDER_JUMP.md`;
- `../theorems/VALUATION_MACROBLOCK_COMPILATION.md`.

## 4. Certified eight-jump frontier — SAFE finite execution

Exact pure-ballot counts:

| jump | cylinders | population |
|---:|---:|---:|
| 0 | 14 | 125,072,439,875,999,947,649 |
| 1 | 32 | 94,018,492,189,951,139,878 |
| 2 | 74 | 78,277,356,063,975,556,852 |
| 3 | 174 | 59,912,679,889,581,873,141 |
| 4 | 374 | 50,489,422,254,631,626,671 |
| 5 | 986 | 44,710,237,164,104,400,785 |
| 6 | 2,192 | 36,555,835,392,716,456,688 |
| 7 | 5,752 | 32,306,978,271,327,268,319 |
| 8 | 14,224 | 26,859,837,368,845,079,186 |

Eight-jump survival:

\[
0.214754244784\ldots
\]

The first-75 defect-tail tightening removes only

\[
256{,}808{,}932
\]

additional integers and closes no whole cylinder.

The exact directed `P_min` recheck also closes zero whole cylinders through jump 8.

These are finite exact execution results, not universal theorems.

## 5. Finite-horizon transition templates — CLOSED / execution reuse only

For raw-bit horizon `d`, the product template

\[
P_d=(B_d,Q_d^{src})
\]

combines ballot-control and low-dyadic source information.

At the current 14,224-cylinder frontier:

- `d=4`: 583 templates;
- `d=8`: 8,372;
- `d=12`: 13,923;
- `d=16`: 14,209;
- `d=17`: 14,213;
- `d=18`: 14,224.

This allows DAG/code reuse only.  Equal finite templates are not a source-payload merge theorem.

## 6. Predicate activation schedule — CLOSED

### Terminal ternary observation

For `W=AB`, with suffix `B` containing the final `K` one-events,

\[
Z\equiv2^{-|B|}C(B)\pmod{3^K}.
\]

For `K=28`, activate only at

\[
q_{rem}=28,
\]

equivalently

\[
Q(h)+S=65{,}868{,}186{,}673.
\]

### Post-checkpoint dyadic observation

`Z mod2^27` is determined by the first 27 post-checkpoint parity bits and belongs to S11/tail processing.

### `C4F`

`C4F` is not admitted as a state coordinate until its exact Route-B predicate is recovered or defined.

Canonical dependencies:

- `../theorems/PREDICATE_ACTIVATION_SCHEDULE.md`;
- `../audits/S10_PREDICATE_ACTIVATION_AUDIT.md`.

## 7. Local maximal-macroblock formation entry — CLOSED as partition / NON-INDEPENDENT

For

\[
Y(m)=y+3^q m,
\]

define

\[
b=v_2(Y),
\quad
O=Y/2^b,
\quad
H=v_2(O+1),
\quad
D=v_2\!\left(3^H\frac{O+1}{2^H}-1\right).
\]

The exact local entry descriptor is

\[
E(m)=(b,H,D).
\]

For each prescribed descriptor there is one exact parameter residue

\[
\boxed{
m\equiv\rho_{b,H,D}\pmod{2^{b+H+D+1}}.
}
\]

Therefore the minimized source state already suffices to partition a live interval exactly by next maximal macroblock type.

However a live interval containing consecutive `m` values cannot carry one common descriptor because the affine coefficient `3^q` is odd, so consecutive endpoints have opposite parity.

Hence:

\[
\boxed{\text{source state sufficient for local partition}}
\]

but

\[
\boxed{\text{one persistent formation label for a wide cylinder is REJECTED}.}
\]

This partition is a dyadic future-parity compilation, not an independent pruning factor.

It also does not repair the known global stitching obstruction between local slack/carry recurrence and the separate bounded-rank formation-subtraction path.

Canonical dependencies:

- `../theorems/SOURCE_TO_MACROBLOCK_FORMATION_ENTRY_PARTITION.md`;
- `../src/A0_s1_source_to_macroblock_formation_entry_partition_certificate.py`;
- `../audits/S10_SOURCE_TO_FORMATION_ENTRY_AUDIT.md`;
- `../theorems/SLACK_FORMATION_LOCAL_CONJUGACY_STITCHING_OBSTRUCTION.md`.

## 8. Realized target-displacement defect — CLOSED / NON-INDEPENDENT

Let the realized prefix have one-positions

\[
a_0<\cdots<a_{q-1}
\]

and target one-positions

\[
t_0<\cdots<t_{q-1},
\qquad a_j\le t_j.
\]

Put

\[
s_j=t_j-a_j.
\]

The exact defect numerator already carried by the `P_min` reconstruction is

\[
\boxed{
N=C_T-C_W
=\sum_{j=0}^{q-1}3^{q-1-j}2^{a_j}(2^{s_j}-1).
}
\]

Therefore all displacement already realized in the prefix is already contained in current `N`.

If `N>0` and `j_*` is the earliest displaced rank, then

\[
\boxed{v_2(N)=a_{j_*}.}
\]

The recursive update

\[
N'=3N+2^{t_q}-2^{a_q}
\]

is exactly the same displacement accounting.

Consequently historical prefix phase/displacement/skew lower bounds cannot be **added** to exact current `N` when they quantify the same realized prefix.  That would double-count the defect.

Canonical dependencies:

- `../theorems/TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`;
- `../src/A0_s1_target_displacement_defect_decomposition_certificate.py`;
- `../audits/S10_TARGET_DISPLACEMENT_DEFECT_AUDIT.md`;
- `../src/A0_s1_14root_8jump_Pmin_recheck_certificate.py`.

## 9. Closed/rejected routes that must not be restarted

1. terminal target-dominance mod-3 gate as independent pruning — **REJECTED / redundant**;
2. dominance-only weak CRT — **insufficient**;
3. `P_min` alone through the certified finite horizon — **zero whole-fiber closures**;
4. contracting ceiling inside active pure-ballot S10 — **redundant**;
5. correction-language recursion as independent pruning — **REJECTED / same valuation information**;
6. H/L or local maximal-macroblock labels as independent pruning — **NON-INDEPENDENT** unless a new predicate uses them;
7. direct local slack/carry -> one global formation-rank path — **REJECTED without explicit bridge**;
8. adding historical realized-prefix displacement bounds to exact current `N` — **REJECTED / double count**;
9. dropping source residue `r` before source-sensitive predicates are discharged — **REJECTED**;
10. equal finite control/template signatures -> source merge — **REJECTED without right-congruence**.

## 10. Principal active object — genuinely future source-sensitive defect

The search has now narrowed to a stricter object.

Current `N` contains the entire already-realized target displacement.  Therefore a stronger physical whole-fiber gate must force a **new** displacement in the unresolved suffix.

The desired chain is

\[
\boxed{
\text{exact source/control cylinder}
\Longrightarrow
\text{forced future }a_j<t_j
\Longrightarrow
N_{future,min}>0
\Longrightarrow
\text{exact transported physical lower bound}.
}
\]

A future contribution must be transported through the correction recurrence with the correct power of 3.  It may not be inserted by mixing normalizations.

The next computational primitive should therefore be a finite-horizon min-plus recursion over exact valuation children:

\[
F_0=0,
\]

\[
F_{r+1}=3F_r+2^{t_{q+r}}-2^{a_{q+r}},
\]

with the minimum taken over all nonempty legal source-preserving descendants of the current cylinder.

If

\[
\boxed{F_r^{min}>0}
\]

for a parent cylinder, then every legal `r`-one continuation accumulates a genuinely new future defect relative to the parent's current `N`.

This is the next object to certify and test on the 14,224 jump-8 cylinders.

## 11. Immediate computation targets

1. implement the exact source-sensitive finite-horizon future-defect min-plus recursion;
2. distinguish `no legal descendant` from `legal descendants with positive forced defect`;
3. transport `F_r^{min}` exactly into descendant `N` via
   \[
   N_{q+r}=3^rN_q+F_r;
   \]
4. test whether any jump-8 source cylinder has `F_r^{min}>0` for a small certified horizon;
5. test whether the transported floor makes every legal descendant of any parent pass the physical rejection barrier;
6. retain the full source payload whenever no right-congruence/rejection theorem applies;
7. activate checkpoint residues only at their certified local observation times.

## 12. DSD audit rules

Allowed:

- exact source-preserving valuation or certified multibit transitions;
- exact correction/residual recursion;
- finite-horizon control/template reuse;
- local formation partition as transient grammar;
- exact current displacement scalar `N`;
- future defect only when it is forced by all legal descendants of the audited source cylinder and transported exactly.

Forbidden:

- exact-pair uniqueness -> family uniqueness;
- equal control/template/formation label -> equal source payload;
- local recurrence equality -> global formation path;
- correction/formation/displacement re-expression -> independent pruning;
- adding a lower bound on already-realized defect to exact current `N`;
- mixing defect normalizations across different odd counts;
- carrying checkpoint observations before they exist;
- finite regression -> universal Route-B closure;
- marginal density multiplication;
- retroactive use of later refined bounds.

## Global warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`.  Route-A, `s>=2`, remaining sectors, and global branch completeness remain separate obligations before any Collatz conclusion.

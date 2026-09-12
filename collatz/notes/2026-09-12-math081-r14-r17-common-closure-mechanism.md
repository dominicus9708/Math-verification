# MATH-081 — common closure mechanism across the closed paid-count layers r=14..17

Date: 2026-09-12

Status: `CROSS-CERTIFICATE SYNTHESIS / NO NEW LAYER CLAIM / COMMON MECHANISM VALIDATED`

## 1. Purpose

MATH-071 explicitly identified `r=14,15,16,17` as the intended comparison set because the four adjacent layers were closed by visibly different computational representations. MATH-072--080 have since extracted a common analytic/address description. This note returns to the four closed layers and asks whether the new description actually matches their closure logic.

No paid-count layer below `r=14` is analyzed here. The Collatz conjecture and first universal Farey cell remain `OPEN`.

## 2. Four representations, one exact lineage rule

The four layer certificates use:

- `r=17`: exact 8-step low-bit block handoff to singleton ordinary integers;
- `r=16`: AP-family continuation + 8-step blocks + constant-memory singleton streaming;
- `r=15`: multiplicity-banded exact AP union;
- `r=14`: adaptive exact AP union with source/parameter sharding and arbitrary-precision arithmetic.

Despite these implementation differences, all four obey the same proof rule:

\[
\boxed{
\text{never discard a symbolic family unless an exact proof-facing condition holds;}
}
\]

and when a family reaches ordinary resolution,

\[
\boxed{
\text{continue the same integer until it reaches }\le2^{71}.
}
\]

Thus representation changes are computational, not mathematical changes of the target set.

## 3. Analytic versus address closure

The MATH-065 branch construction feeding these layers already separates cells into proof-cost-safe, singleton-resolution, and critical sectors.

For the three most recent exact classifications:

\[
\begin{array}{c|r|r|r|r}
 r & \text{total phase/address cells} & \text{cost-safe} & \text{singleton-resolution} & \text{critical}\\
\hline
16&1061&229&557&275\\
15&1061&206&542&313\\
14&1035&175&507&353
\end{array}
\]

As `r` decreases, fewer cells are immediately cost-safe and more enter the critical address/family calculation. This is finite structural evidence only; no monotone law in `r` is asserted.

The two proof mechanisms are:

### A. Analytic/reduced-cost closure

A cost-safe cell already supplies enough penalty/reduced-cost contribution for the current Bellman objective. In MATH-080 language this contributes to lowering

\[
\mathfrak D_{term}
=S_{partial}-\mathcal P-N(\rho-1).
\]

### B. Exact address-resolution closure

When reduced cost alone does not close a cell, the source/target family is retained exactly. Low-bit refinement, AP splitting, union on identical grids, or exact sharding reduces the family without losing ordinary members. Once an ordinary singleton is exposed, deterministic continuation proves that it reaches the frozen floor.

At the terminal ordinary prefix this is exactly

\[
\mathfrak D(X,X_0)<0.
\]

The various AP engines are therefore implementations of the address-resolution branch, not independent dynamical principles.

## 4. r=17

The remaining medium core before MATH-068 consisted of

\[
76,866\text{ AP cylinders}
\]

representing

\[
14,980,075\text{ ordinary occurrences}.
\]

One 8-step residue block reduced every surviving AP to multiplicity at most `4`; a second block reduced every survivor to a singleton. The resulting `1,826,810` unique ordinary states all reached the floor, with a safe total bound of `334` shortcut steps from the original medium-core target.

Common-mechanism interpretation:

\[
\boxed{
\text{exact compatibility residue}
\to
\text{resolution consumption}
\to
\text{singleton}
\to
\mathfrak D<0.
}
\]

## 5. r=16

The complete negative-candidate workload has

\[
2,417,129\text{ cylinders}
\]

representing

\[
213,006,896\text{ ordinary occurrences}.
\]

Large families close under exact AP continuation. Small and medium families pass through exact low-bit blocks and then a constant-memory stream of `11,766,228` singleton occurrences; all close with zero failures. The safe layer-wide additional-depth bound is

\[
\boxed{348}.
\]

Common-mechanism interpretation: the same address-resolution process is implemented with a representation chosen by family size, then terminal descent is the same master-defect sign test.

## 6. r=15

The negative-candidate workload has

\[
2,928,669\text{ AP cylinders}
\]

representing

\[
1,835,780,279\text{ raw ordinary occurrences}.
\]

A global union was computationally inefficient, so the initial representation was partitioned into 33 exact multiplicity bands. Every nonempty band became empty under exact AP-union propagation. The largest certified sweep bound is

\[
\boxed{443}.
\]

Cross-band overlap is harmless because bands are independently proved closed; the partition has no statistical meaning.

Common-mechanism interpretation: the address side is preserved exactly while the representation is changed solely to control state explosion.

## 7. r=14

The negative-candidate workload has

\[
2,599,692\text{ AP cylinders}
\]

representing

\[
10,691,937,078\text{ raw ordinary occurrences}.
\]

The occupied multiplicity support lies in five exact regions. Broad regions are split into exact source shards only when computationally necessary; parameter sharding is a literal set-union identity. All regions close, with the largest audited sweep bound

\[
\boxed{479}.
\]

Common-mechanism interpretation: even when raw multiplicity rises by orders of magnitude, no new proof principle is introduced. Exact address representation is refined until ordinary descent is certified.

## 8. Validation of the resolution potential interpretation

MATH-074 uses

\[
R_{res}=\lceil\log_2M\rceil,
\qquad
H_R=-\lambda R_{res},
\quad \lambda=19/503.
\]

The `r=14..17` certificates independently show the qualitative mechanism behind this potential:

- low-bit refinement consumes unresolved address multiplicity;
- insufficient cost does not imply failure, because exact source resolution can continue;
- singleton is a handoff state, not itself a descent theorem;
- descent is finally checked on the ordinary integer.

Hence `R_res` is a valid abstraction of a real closure resource seen repeatedly in the finite certificates, although the existing finite certificates do not prove that `H_R` alone closes the global Bellman graph.

## 9. Validation of MATH-080 master defect

Every ordinary terminal continuation in `r=14..17` ends only when the same integer reaches

\[
T^j(N)<N
\]

or the frozen verified floor appropriate to the minimal-counterexample argument. For a strict descent prefix,

\[
\mathfrak D(X,X_0)
=\rho[T^j(N)-N]<0.
\]

Thus the terminal condition used in all four closed layers is exactly the negative master-defect condition.

The analytic cost branch and the exact-resolution branch therefore meet at one final target:

\[
\boxed{\mathfrak D<0.}
\]

## 10. Current common architecture

The cross-certificate synthesis now supports the hierarchy

\[
\boxed{
\text{exact affine state}
\to
\text{penalty or address refinement}
\to
\text{ordinary resolution}
\to
\text{negative master defect}.
}
\]

A compact proof-facing state candidate is

\[
\boxed{
(\Omega,\rho,S,R_{res},\mathcal A_{compat},\mathcal A_{dom})
}
\]

with the following reductions already known:

- `rho` is derived from `(k,q)` where those are stored;
- `u` is equivalent to `rho/Omega`;
- `theta`, `H_gap`, root-credit envelopes, and first-cell `delta` are derived quantities;
- `A_compat` cannot yet be removed, but MATH-079 shows its interaction with correction credit is exactly `A_d-C_d`;
- `A_dom` is needed only where Hensel/dominance pruning is invoked.

## 11. Claim boundary

This synthesis establishes no new paid-count closure beyond MATH-071. In particular it does not touch `2<=r<=13`.

It validates that the four adjacent closed layers are consistent with the same analytic/address/master-defect architecture.

Still open:

- construction of a future-complete finite or well-founded Bellman quotient;
- global penalty lower bound at `19/503`;
- the remaining low-paid layers;
- first-cell emptiness;
- the full Collatz conjecture.

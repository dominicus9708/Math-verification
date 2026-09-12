# Collatz common-state checkpoint after MATH-085

Date: 2026-09-12

Status: `WORKING CHECKPOINT / FINITE RESULTS RECORDED / GLOBAL PROBLEM OPEN`

## 1. Global claim boundary

The Collatz conjecture remains open.

The first universal Farey cell remains open.

No finite-depth, finite-paid-count, source-resolution, or Bellman-pruning result is promoted beyond its certified scope.

## 2. Paid-count frontier

The current exact finite paid-count status is

\[
\boxed{r\ge14\text{ CLOSED}},
\]

with

\[
\boxed{2\le r\le13\text{ OPEN / NOT INCLUDED IN THE CURRENT COMMON-FORMULA REAUDIT}}.
\]

The adjacent comparison layers are:

- `r=17`: exact 8-step block -> singleton handoff;
- `r=16`: AP + block + streaming terminal continuation;
- `r=15`: multiplicity-banded AP union;
- `r=14`: adaptive AP union + exact source/parameter sharding.

Their computational representations differ, but their proof-facing closure mechanisms reduce to penalty/reduced-cost safety or exact address resolution followed by ordinary deterministic continuation.

## 3. Depth 1--41 re-audit

Depths 1--41 have been reassembled under the latest DSD analysis/audit rules.

The coefficient-surviving language is one exact prefix-admissibility recursion.

For depths 32--41 the nested Hensel lineage satisfies the exact parent-to-child prefilter relation

\[
P_{k,q}=S_{k-1,q}+S_{k-1,q-1}.
\]

The depth-41 coefficient language size is

\[
\boxed{12,805,670,000}.
\]

No hidden population loss was found in the audited canonical chain.

## 4. Common analytic coordinates

For a parity word/prefix with correction numerator \(C\), odd count \(q\), and depth \(k\), define

\[
S=\frac{C}{3^q},
\qquad
\rho=\frac{2^k}{3^q}.
\]

Then

\[
\boxed{S=1+\Sigma-\rho},
\qquad
\boxed{\rho=2^{-u}\Omega}.
\]

Parity-step updates are

\[
\begin{array}{c|ccc}
& S'&\rho'&\Sigma'\\
\hline
\text{even}&S&2\rho&\Sigma+\rho\\
\text{odd}&S+\rho/3&(2/3)\rho&\Sigma
\end{array}
\]

and the paid penalty atom can be written

\[
\boxed{p=\frac{\Omega-\rho}{3}}.
\]

## 5. Master affine comparison defect

For an affine state

\[
X=(a,S,\rho),
\qquad
y(X)=\frac{a+S}{\rho},
\]

define

\[
\boxed{
\mathfrak D(X_1,X_2)
=\rho_2(a_1+S_1)-\rho_1(a_2+S_2).
}
\]

Then

\[
\boxed{
\mathfrak D(X_1,X_2)=\rho_1\rho_2(y_1-y_2).
}
\]

Hence:

- `D=0` iff the endpoints agree;
- the sign of `D` gives endpoint order;
- against the start reference \((N,0,1)\),

\[
\boxed{
\mathfrak D=S-N(\rho-1)=\rho[T^k(N)-N].
}
\]

Therefore actual descent is exactly

\[
\boxed{\mathfrak D<0}.
\]

## 6. Address/correction separation

For equal-depth states with odd-count difference \(d\), define

\[
A_d=r_L-3^dr_H,
\qquad
C_d=3^dS_H-S_L.
\]

Then

\[
\boxed{
\rho_L(y_L-y_H)=A_d-C_d.
}
\]

Thus endpoint compatibility is

\[
\boxed{A_d=C_d}.
\]

This explains why Hensel/carry information cannot replace exact dyadic compatibility: the correction credit and the address contrast are different channels whose equality must be tested.

## 7. Resolution/Bellman potential

With

\[
\lambda=\frac{19}{503},
\]

MATH-082 uses the coarse source-bit potential

\[
H_{bit}=-\lambda\max(0,73-H).
\]

For a one-paid terminal chain of macro count \(t\), the universal sufficient wedge is

\[
\boxed{503t\ge228(H-73)}
\]

for \(H>73\); \(H\le73\) is automatically safe for that reduced-cost comparison.

The exact current-phase strengthening stores

\[
J=(\Omega^-_{cur},\Omega^+_{cur}),
\qquad
\mathcal P=\alpha\Omega_{cur}
\]

and applies

\[
\boxed{
\alpha\Omega^-_{cur}-\lambda(H-73)\ge0.
}
\]

## 8. One-paid finite symbolic horizon

MATH-084 proves, from the actual source-window width,

\[
\boxed{\text{multi-source}\Rightarrow H\le71}.
\]

Every one-paid macro contributes at least three modulus bits, so

\[
\boxed{\text{multi-source one-paid macro count}\le23}.
\]

Therefore a 24th one-paid macro, if reached, is necessarily singleton-resolved in the current source window.

This removes arbitrary symbolic depth from the one-paid multi-source problem.

## 9. Exact terminal replay through macro depth 6

New singleton handoffs:

\[
\begin{array}{c|r|r|r|r}
\text{depth}&\text{terminal}&\text{universal-safe}&\text{phase-safe total}&\text{ordinary residual}\\
\hline
2&1,137&1,136&1,137&0\\
3&11,511&11,489&11,509&2\\
4&76,585&76,564&76,585&0\\
5&372,841&372,834&372,841&0\\
6&1,358,935&1,358,914&1,358,935&0
\end{array}
\]

The two depth-3 residuals were separately continued as ordinary integers and reached the frozen floor in 1 and 10 shortcut steps.

Depths 4--6 require no ordinary terminal continuation for the Bellman-pruning purpose.

## 10. Current next target

Do **not** resume raw `r=13` or raw macro-depth expansion first.

The next proof-facing target is a depth-independent terminal inequality over the finite horizon

\[
1\le t\le24
\]

that combines:

1. exact dyadic compatibility/address resolution;
2. the current-phase state \((J,\alpha)\);
3. the resolution/Bellman potential;
4. the master comparison defect \(\mathfrak D\).

The desired form should certify terminal low-cost safety without ordinary-address enumeration at every macro depth.

Only if that symbolic route stalls should `r=13` or further finite macro-depth layers be used as new out-of-sample data.

## 11. Canonical recent milestones

- MATH-071: `r=14` finite closure;
- MATH-072/073: common-coordinate bridge and resolution potential;
- MATH-074/075: resolution Bellman reduction and terminal handoff catalogue;
- MATH-076--080: generalized merge credit, orbit-gap bridge, address-credit separation, master defect;
- MATH-081: `r=14..17` common-mechanism synthesis;
- MATH-082: one-paid resolution wedge;
- MATH-083: current-phase replay coordinates;
- MATH-084: finite multi-source one-paid horizon;
- MATH-085: exact current-phase Bellman replay through macro depth 6.

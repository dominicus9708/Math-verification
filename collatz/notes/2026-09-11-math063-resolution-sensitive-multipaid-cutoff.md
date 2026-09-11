# MATH-063 — resolution-sensitive multi-paid cutoff

Date: 2026-09-11
Status: `EXACT RESOLUTION/PHASE-SUM COMBINATION / SYMBOLIC MULTI-PAID RANGE REDUCED TO r<=23 / SINGLETON TRACK OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-063 combines the exact source-resolution theorem from MATH-061 with the exact paid-cluster phase-sum lower bound from MATH-062.

## 1. The missing distinction in MATH-062

MATH-062 treated every multi-paid macro by the uniform length bound

\[
H\le 73+2r,
\]

where `r` is the number of paid odd events in the cluster.  That bound is appropriate before distinguishing how many ordinary source anchors remain inside the exact macro cylinder.

MATH-061 supplies a stronger fact once source multiplicity is included.

An exact composed macro cylinder of total shortcut length `H` has source form

\[
\boxed{Y=A+2^H s.}
\]

Every audited pre-first-cell `u=0` anchor satisfies

\[
Y<2^{73}.
\]

Therefore, if a cylinder still contains at least two ordinary source anchors, then their difference is at least `2^H`, and so necessarily

\[
\boxed{H\le72.}
\]

Equivalently,

\[
\boxed{H\ge73\Longrightarrow\text{source multiplicity}\le1.}
\]

This is an exact arithmetic-resolution statement, not a density estimate.

## 2. Paid-cluster penalty lower bound

For a cluster containing `r` paid odd events, MATH-062 gives

\[
\mathcal P_{\rm cluster}
\ge
\frac16\sum_{j=0}^{r-1}\Omega_j,
\]

where the `Omega_j` are `r` consecutive iterates of the exact phase map

\[
\Omega'=
\begin{cases}
\frac23\Omega,&\Omega>\frac34,\\[1mm]
\frac43\Omega,&\Omega<\frac34.
\end{cases}
\]

For each `r`, the infimum of the consecutive phase sum over `Omega in (1/2,1)` is obtained by an exact finite rational phase partition.

Let

\[
S_r^{\min}
:=
\inf_{\Omega_0\in(1/2,1)}
\sum_{j=0}^{r-1}\Omega_j.
\]

Then every multi-source cylinder satisfies

\[
\boxed{
\mathcal P_e-rac{19}{503}H
\ge
\frac{S_r^{\min}}6
-72\cdot\frac{19}{503}.
}
\]

The old `73+2r` target length is no longer needed on the unresolved symbolic branch.

## 3. Exact transition at r=24

The certificate gives

\[
\frac{S_{23}^{\min}}6
-72\cdot\frac{19}{503}
=
-\frac{8718910501493}{147647688081408}
<0,
\]

so `r=23` is not automatically safe.

At `r=24`, however,

\[
\boxed{
\frac{S_{24}^{\min}}6
-72\cdot\frac{19}{503}
=
\frac{47327533441417}{560599815684096}
>0.
}
\]

The exact phase-sum computation verifies positive margin for every

\[
24\le r\le64.
\]

Together with MATH-062, which already closes all `r>=65` even without source-resolution information, this gives the new split

\[
\boxed{
\begin{array}{ll}
2\le r\le23
&\text{detailed symbolic multi-paid Bellman treatment required},\\[1mm]
24\le r\le64
&\text{multi-source cylinders automatically nonnegative},\\[1mm]
r\ge65
&\text{all cylinders automatically nonnegative by MATH-062}.
\end{array}
}
\]

## 4. What remains in r=24..64

The statement above is deliberately restricted to **multi-source** cylinders.

A negative-adjusted macro with `24<=r<=64` can survive only after its source congruence has already collapsed to at most one ordinary integer.

Thus these counts move from the symbolic Bellman graph into the same-integer singleton track:

\[
\boxed{
24\le r\le64,
\quad
\mathcal P_e-\frac{19}{503}H<0
\Longrightarrow
\#\{\text{ordinary sources}\}\le1.
}
\]

MATH-063 does not claim those singleton starts descend automatically.  They must be checked by exact ordinary-integer continuation, or excluded by another same-integer theorem.

## 5. Why this matters for the mixed graph

Before MATH-063, the detailed multi-paid state space still required

\[
2\le r\le64.
\]

After adding source resolution, the genuinely symbolic part is only

\[
\boxed{2\le r\le23.}
\]

This cuts the paid-count dimension by more than half and, more importantly, separates two qualitatively different proof obligations:

1. **symbolic Bellman graph:** multi-source cylinders with `2<=r<=23` plus unresolved one-paid compositions;
2. **singleton direct track:** exact ordinary starts produced after 73-bit source resolution.

The two tracks must not be merged back together.  A singleton is not a small symbolic family; it is an actual ordinary integer with deterministic future parity.

## 6. DSD audit

### SAFE

- exact source modulus `2^H` for a length-`H` macro cylinder;
- exact anchor ceiling `<2^73`;
- multi-source implication `H<=72`;
- exact phase-sum lower bound from MATH-062;
- exact `r=23` negative / `r=24` positive transition at target slope `19/503`;
- reduction of detailed symbolic multi-paid range to `2..23`.

### OPEN

- exact generation/composition of the `2<=r<=23` symbolic multi-paid cylinders;
- closure of the singleton track for `24<=r<=64`;
- mixed one-paid/multi-paid Bellman potential;
- first-cell emptiness.

### PROHIBITED UPGRADES

- multi-source safety for `r>=24` `=>` every `r>=24` macro closed;
- 73-bit singleton handoff `=>` singleton trajectory descends;
- finite paid-count reduction `=>` finite total proof graph without a future-complete quotient;
- first-cell closure `=>` Collatz proof.

## 7. Next target

MATH-064 should construct exact completed multi-paid cylinders only for

\[
2\le r\le23,
\]

using the MATH-059/MATH-061 arithmetic-progression representation.  Whenever the accumulated source resolution reaches `H>=73`, the branch leaves the symbolic graph and enters the singleton direct track immediately.

This avoids step-history explosion and prevents already-resolved ordinary starts from being carried as symbolic states.

## Reproducibility

`collatz/src/2026_09_11_math063_resolution_sensitive_multipaid_cutoff_certificate.py`

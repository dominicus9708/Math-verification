# MATH-192 — singleton overshoot as one exact modular residue inequality

Date: 2026-09-18

Status: `EXACT SINGLETON REDUCTION / NON-ENUMERATIVE TERMINAL TEST / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-186 proves that every nonpositive multi-paid boundary transfer is already in the singleton regime.

Thus the remaining low-paid obstruction is not a multi-source family. It is an exact compatibility question for at most one ordinary source anchor.

This note eliminates even that ordinary-source lookup: the singleton is determined by one dyadic residue, and the MATH-183 master-defect test becomes one modular residue inequality.

No paid layer or first-cell closure is claimed.

## 2. Current exact cylinder

Let the current same-integer family be

\[
\boxed{
N=A+2^H s,
\qquad
Y=B+3^Q s,
\qquad
0\le s<M.
}
\]

Let

\[
R=\lceil\log_2M\rceil
\]

with `R=0` for `M=1`.

Suppose the next exact zero-cost / macro prefix has length `L` and requires endpoint congruence

\[
\boxed{Y\equiv C\pmod{2^L}.}
\]

Because `3^Q` is odd, it is invertible modulo `2^L`.

Define

\[
\boxed{
G_L:=3^{-Q}\pmod{2^L}
}
\]

and the canonical residue

\[
\boxed{
r_L:=((C-B)G_L)\bmod2^L,
\qquad0\le r_L<2^L.
}
\]

Then compatibility is exactly

\[
\boxed{s\equiv r_L\pmod{2^L}.}
\]

## 3. Overshoot implies zero-or-one source

Assume

\[
\boxed{L>R.}
\]

Since

\[
M\le2^R<2^L,
\]

the parameter interval

\[
0\le s<M
\]

contains at most one integer in any residue class modulo `2^L`.

Because the canonical representative `r_L` already lies in `[0,2^L)`, the compatible source set is exactly

\[
\boxed{
\begin{cases}
\varnothing,&r_L\ge M,\\
\{r_L\},&r_L<M.
\end{cases}
}
\]

Thus singleton overshoot requires no source enumeration.

If it exists, the unique ordinary source anchor is

\[
\boxed{
N_*=A+2^H r_L.
}
\]

## 4. Master-defect terminal test

At the relevant `rho>1` terminal comparison, MATH-183 writes the exact defect as

\[
\boxed{
\mathfrak D(s)
=\Sigma-(A+2^Hs+1)(\rho-1).
}
\]

For the unique compatible singleton,

\[
\boxed{
\mathfrak D_*
=\Sigma-(A+2^Hr_L+1)(\rho-1).
}
\]

Therefore the overshoot branch is closed exactly when either

\[
\boxed{r_L\ge M}
\]

(no compatible ordinary source exists), or

\[
\boxed{
\Sigma<(A+2^Hr_L+1)(\rho-1).
}
\]

No direct Collatz iteration of the singleton is needed for this terminal self-comparison test.

## 5. Dangerous residue threshold

Because `rho>1`, the defect is strictly decreasing in `r_L`.

Define the largest potentially non-descending parameter by

\[
\boxed{
r_{\rm bad}
:=
\max\left(
-1,
\left\lfloor
\frac{\Sigma/(\rho-1)-A-1}{2^H}
\right\rfloor
\right),
}
\]

with the inequality interpreted exactly over rationals rather than floating point in an implementation.

Then a compatible singleton can be dangerous only if

\[
\boxed{
0\le r_L\le\min(M-1,r_{\rm bad}).
}
\]

Equivalently, terminal closure is reduced to the modular-avoidance statement

\[
\boxed{
((C-B)3^{-Q}\bmod2^L)
\notin
[0,\min(M-1,r_{\rm bad})].
}
\]

This is the exact non-enumerative singleton target.

## 6. Relation to the finite-precision address channel

The residue `r_L` depends only on

\[
(C-B)\bmod2^L
\]

and

\[
3^{-Q}\bmod2^L.
\]

Thus the terminal singleton test needs only finite dyadic address precision.

This is structurally consistent with the MATH-090--096 address program: same-integer compatibility is a finite modular state, not a free phase variable and not an ordinary-source scan.

For an overshoot branch, one should carry enough bits to evaluate the required `L` exactly; no larger ordinary-integer representation is logically necessary for the compatibility decision itself.

## 7. DSD interpretation

The low-paid finite workloads can now be decomposed as follows:

1. **multi-source regime:** MATH-186 proves every possible nonpositive transfer must leave it;
2. **overshoot handoff:** exact congruence consumes all remaining source multiplicity;
3. **singleton regime:** MATH-192 replaces the unique ordinary source by one modular residue `r_L`;
4. **terminal risk:** MATH-183 reduces it to whether that residue lies in one initial bad interval.

Therefore the remaining theorem is no longer

> check every singleton integer.

It is

> prove that every legal exact address residue avoids the bad interval, or is incompatible.

That is a finite modular-structure problem suitable for DSD analysis and audit.

## 8. Immediate theorem target

For every legal overshoot transition in the synchronized product state, prove

\[
\boxed{
r_L\ge M}
\]

or

\[
\boxed{
r_L>r_{\rm bad}.}
\]

If this holds uniformly, MATH-186 plus MATH-192 closes all multi-paid boundary transfers without source enumeration.

The paid count `r>=2` enters only through transition legality and the already-positive local surplus; it is no longer a source-enumeration axis.

## 9. Claim boundary

Established:

- exact singleton residue formula;
- zero-or-one compatibility under `L>R`;
- exact unique source formula `N_*=A+2^H r_L`;
- reduction of singleton master-defect closure to one modular residue inequality;
- reduction of possible danger to one initial residue interval.

Not established:

- uniform modular avoidance for all legal overshoot transitions;
- closure of all singleton/aperiodic terminal states;
- any new paid-count layer closure;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

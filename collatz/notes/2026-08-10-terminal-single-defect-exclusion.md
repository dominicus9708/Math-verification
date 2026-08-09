# Terminal single-defect exclusion in the `1000` branch

Date: 2026-08-10

Status: **DERIVED FINITE EXACT EXCLUSION FOR ONE TERMINAL DEFECT**

This note concerns only the isolated first-crossing resonance

\[
(q,\sigma)=(137,528,045,312,217,976,794,617)
\]

and the strongest surviving `m=46` high-four ternary prefix `1000`.  It does not eliminate the branch.  It proves that the last 20 odd-position coordinates cannot contain exactly one mechanical-cap defect.

## 1. Upstream facts used

The branch has:

\[
N_{\rm def}\le 285,942,279,
\]

\[
0\le d:=y-x\le29,785,654<3^{16},
\]

and the endpoint is determined exactly by the last 48 odd positions because `y<3^48`.

Let

\[
\kappa_i=\lfloor i\log_2 3\rfloor,
\qquad z_i=\kappa_i-d_i\ge0.
\]

The defect transition satisfies

\[
z_{i+1}\le z_i+(\kappa_{i+1}-\kappa_i)-1.
\]

Writing

\[
\beta=\log_2(3/2),
\]

the number of available `+1` defect-growth transitions in any run of length `L` is at most `ceil(beta L)`.

## 2. Why modulus `3^20` is the first useful terminal scale

For the `1000` start family, the near-return intervals cover every residue modulo `3^17`.  They first develop gaps modulo `3^18`, but the fully mechanical terminal residue still lies inside the permitted near-return support modulo both `3^18` and `3^19`.

At modulus `3^20` the fully mechanical terminal residue no longer lies in any allowed near-return interval.  Hence at least one of the final 20 odd positions must be a defect.

This is a sharper localization of the earlier last-48 obstruction.

## 3. Case A: the unique terminal defect is not the first of the last 20

If the unique defect occurs at a later terminal coordinate, then the preceding terminal coordinate has `z=0`.  The transition inequality therefore permits a new defect only across a mechanical gap of two, and its amplitude must be exactly

\[
\boxed{z=1.}
\]

There are 11 such admissible positions among the final 19 transitions.  Exact `3^48` endpoint evaluation was performed for all 11.  None lies within

\[
[x,x+29,785,654]
\]

for any `1000` Cantor start.

Thus no non-inherited isolated terminal defect is possible.

## 4. Case B: the unique terminal defect is the first of the last 20

Here the defect may be inherited from a run that began earlier.  Its amplitude can therefore exceed one.

The exact-rational logarithm certificate gives an upper bound for

\[
\beta=\log_2(3/2)
\]

and, together with the global run-aware defect-count bound, certifies

\[
\boxed{z\le167,265,511.}
\]

When only this coordinate is defective, the endpoint change is a multiple of `3^19`, so

\[
y\bmod3^{19}=738,416,854
\]

is fixed.

The near-return condition leaves exactly 13,824 choices among the lower 19 ternary `0/1` digits, with

\[
\boxed{d\ge20,971,503.}
\]

All 13,824 choices have the same high-quotient carry class.  Hence the remaining 21 upper ternary digits collapse to one Cantor-membership test for each amplitude `z`.

The exact C++ scan of every

\[
1\le z\le167,265,511
\]

finds exactly five modular/Cantor hits:

| `z` | exact endpoint `y` | upper-21 Cantor coordinate |
|---:|---:|---:|
| 51,123,563 | 36,788,825,963,355,776,078,158 | 5,172,161,310 |
| 69,623,881 | 36,767,449,656,405,490,789,198 | 574,162,590 |
| 108,790,195 | 36,764,980,509,571,862,422,402 | 43,054,293 |
| 112,458,389 | 36,772,083,750,100,501,999,090 | 1,570,946,409 |
| 157,121,141 | 36,787,219,587,291,159,407,602 | 4,826,633,193 |

No other inherited single-defect amplitude survives the exact start/end congruence.

## 5. Amplitude cost versus remaining correction budget

The affine identity gives the stronger start/end-dependent correction-loss bound

\[
\boxed{
\Delta S
\le U_S-\Lambda_- y-d,
}
\]

because `y=x+d` and

\[
S=\delta x+(1+\delta)d.
\]

For a candidate endpoint `y`, the largest possible right-hand side occurs at the smallest permitted near-return difference, namely

\[
d_{\min}=20,971,503.
\]

On the other hand, to build a terminal amplitude `z` from zero requires a preceding nonzero-defect run.  The exact rational bound

\[
\beta<117/200
\]

implies the safe run-length lower bound

\[
L(z)\ge
\left\lceil\frac{200(z-1)}{117}\right\rceil.
\]

The run-average theorem then gives

\[
\boxed{
\Delta S\ge\frac5{48}L(z).
}
\]

For each of the five exact modular hits, exact rational arithmetic verifies

\[
\boxed{
U_S-\Lambda_-y-d_{\min}
<\frac5{48}L(z).
}
\]

Hence all five are impossible once the amplitude cost and remaining correction budget are imposed simultaneously.

## 6. Result

Both possible one-terminal-defect cases are excluded.  Therefore every paradoxical candidate in the `1000` branch must satisfy

\[
\boxed{
\#\{i\in[q-20,q-1]:z_i>0\}\ge2.
}
\]

This is a finite branch-specific theorem/certificate.  It is not yet numerically large enough to contradict the global defect budget.

## 7. Reproducibility

- `collatz/src/terminal_single_defect_scan.cpp` exhausts the inherited amplitude range with exact integer modular arithmetic and returns exactly five hits.
- `collatz/src/terminal_single_defect_budget_check.py` reconstructs the rational logarithm bounds, certifies `z_max`, the 13,824 lower-19 choices and `d_min`, and rejects all five hits by exact rational budget comparison.

The next target is the analogous two-terminal-defect bridge.  Unlike the one-defect case it is genuinely two-dimensional when the first terminal defect is inherited, so a direct flat `z_1,z_2` scan is not appropriate; the transition/run structure must be used to keep the search finite.
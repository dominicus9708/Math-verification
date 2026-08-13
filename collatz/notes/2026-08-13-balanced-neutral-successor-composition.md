# Balanced neutral successor composition theorem

Date: 2026-08-13

Status: **exact finite-block theorem + certified U6 constant**.  This refines difference-fullness from mere existence of a neutral correction match to existence of one whose actual correction difference is uniformly close to zero.  It yields a bounded-error affine cocycle on Euclidean macroblocks.  It is not a coverage theorem for actual Collatz candidates and is not a proof of Collatz.

## 1. Balanced difference radius

Let `B` be a deterministic mechanical macroblock with time length `L` and mechanical odd count `Q`.  Let `S_B` denote the exact corrections of a chosen neutral orientation family

\[
(\Sigma,M)=(0,0).
\]

Define the balanced correction-difference radius

\[
\boxed{
E_B
:=
\max_{r\in\mathbb Z/3^Q\mathbb Z}
\min_{\substack{R_h,R_l\in S_B\\R_h-R_l\equiv r\;(3^Q)}}
|R_h-R_l|.
}
\]

A finite value implies difference-fullness automatically.

## 2. Controlled neutral successor

For an incoming integer collision quotient `D`, a neutral block successor has the form

\[
D'
=
\frac{2^L D+(R_h-R_l)}{3^Q},
\]

with the correction difference chosen to satisfy

\[
R_h-R_l
\equiv-2^L D
\pmod{3^Q}.
\]

By definition of `E_B`, one can always choose such a pair with

\[
|R_h-R_l|\le E_B.
\]

Hence every integer input has at least one controlled successor satisfying

\[
\boxed{
\left|
D'-\frac{2^L}{3^Q}D
\right|
\le
\frac{E_B}{3^Q}.
}
\]

Thus the exact neutral credit transducer is a bounded-error integer realization of the ideal real multiplication

\[
D\mapsto\frac{2^L}{3^Q}D.
\]

## 3. Exact U6 constant

For

\[
U_6=1010110110101101101,
\qquad(L,Q)=(19,12),
\]

the exact neutral fibre has `11,433` orientations.

The verifier computes, for every residue modulo

\[
3^{12}=531,441,
\]

the smallest absolute correction difference realizing that residue.  The worst residue is

\[
6,154
\]

and the exact radius is

\[
\boxed{
E_6=1,056,728.
}
\]

Therefore every integer `D` admits a neutral U6 successor with

\[
\boxed{
\left|
D'-\frac{2^{19}}{3^{12}}D
\right|
\le
\frac{1,056,728}{531,441}
<1.989.
}
\]

Since

\[
\frac{2^{19}}{3^{12}}<1,
\]

U6 is a slightly contracting real multiplier with a uniformly bounded integer rounding/correction error.

## 4. Concatenation of balanced blocks

Let `A` and `B` have balanced radii `E_A,E_B`.  In the neutral Cartesian subfibre of `AB`, correction differences have the exact form

\[
\Delta R_{AB}
=3^{Q_B}\Delta R_A+2^{L_A}\Delta R_B.
\]

Given an arbitrary target residue modulo `3^(Q_A+Q_B)`:

1. choose `Delta R_B` with `|Delta R_B|<=E_B` to match the low `Q_B` ternary digits;
2. divide the remaining discrepancy by `3^Q_B`;
3. choose `Delta R_A` with `|Delta R_A|<=E_A` to match the remaining `Q_A` digits.

This gives

\[
\boxed{
E_{AB}
\le
3^{Q_B}E_A+2^{L_A}E_B.
}
\]

Writing

\[
e_B:=E_B/3^{Q_B},
\qquad
\rho_B:=2^{L_B}/3^{Q_B},
\]

the normalized error recursion is

\[
\boxed{
e_{AB}\le e_A+\rho_A e_B.}
\]

The corresponding controlled successor satisfies

\[
\boxed{
|D'_{AB}-\rho_A\rho_B D|
\le e_A+\rho_A e_B.
}
\]

Thus Euclidean concatenation produces an exact bounded-error affine cocycle.

## 5. U7 and later blocks

For U7, the exact difference-full certificate gives totality and the full correction width gives the safe, though non-sharp, balanced bound

\[
E_7\le W_7=967,871,451.
\]

Hence

\[
\left|
D'-\frac{2^{27}}{3^{17}}D
\right|
\le
\frac{967,871,451}{129,140,163}
<7.495.
\]

A smaller exact balanced radius for U7 would immediately sharpen every later Euclidean error constant through the composition formula above.  This is now a precise finite additive-combinatorics target rather than a vague mixing problem.

## 6. Relation to the constructive growth calculations

The earlier length-24,727 certificate used the largest available base successor and exhibited a constructive credit `3377`.  The present theorem addresses a different question:

- the greedy certificate asks how large a credit **can** be made;
- the balanced theorem asks how closely a credit can always follow the ideal real multiplier.

Both are exact statements on the same integer transducer.  Together they suggest analyzing the large-scale credit process as a bounded-error cocycle with controllable extremal branches.

## 7. Limitation

Controlled alternate-orientation successors are not the same as coverage of an arbitrary actual R2 orientation.  The missing proof step remains:

> force an actual critical survivor into a correction-collision fibre whose available predecessor credit exceeds the orbit headroom.

The balanced theorem does not provide that coverage.  It supplies the exact transport estimates needed once such a fibre is identified.

## 8. Verification

`collatz/src/u6_neutral_balanced_difference_radius_certificate.cpp` checks the U6 radius using exact integer arithmetic over all `11,433^2` neutral correction pairs and all `3^12` target residues.

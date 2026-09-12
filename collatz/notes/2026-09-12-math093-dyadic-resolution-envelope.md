# MATH-093 — dyadic power-of-two resolution envelope

Date: 2026-09-12

Status: `EXACT SUPERSET LEMMA / EXACT RESOLUTION POTENTIAL ON THE ENVELOPE`

## 1. Envelope construction

For an exact source-parameter family

\[
0\le s<M
\]

define

\[
R=\lceil\log_2M\rceil
\]

and enlarge the family to

\[
\boxed{0\le s<2^R.}
\]

This contains every actual source member.  It may add fictitious members, so any safety result proved for the envelope safely descends to the actual family.

## 2. Multi-edge transition

A dyadic edge of resolution `h` fixes one residue

\[
r\pmod{2^h}.
\]

If

\[
h\le R,
\]

then automatically

\[
0\le r<2^h\le2^R,
\]

so the envelope always contains the selected residue.
Writing

\[
s=r+2^h u
\]

gives exactly

\[
0\le u<2^{R-h}.
\]

Hence the envelope resolution update is

\[
\boxed{R'=R-h.}
\]

No address pruning occurs on an envelope multi-edge.

## 3. Terminal transition

If

\[
h>R,
\]

the envelope contains at most one member of the selected residue class.
Compatibility is exactly

\[
\boxed{r<2^R,}
\]

and the terminal zero-extension overshoot is

\[
\boxed{z=h-R.}
\]

## 4. Exact resolution potential

Let

\[
H_R=-\lambda R,
\qquad
\lambda=\frac{19}{503}.
\]

For a multi-edge `h<=R`,

\[
p-\lambda h+H_R'-H_R
=p-\lambda h-\lambda(R-h)+\lambda R
=\boxed p.
\]

Thus the length charge is cancelled **exactly**, not merely bounded.

For a terminal edge `h>R`, set `R'=0`. Then

\[
p-\lambda h+H_R'-H_R
=\boxed{p-\lambda(h-R)}
=\boxed{p-\lambda z}.
\]

Therefore every earlier multi-edge contributes a nonnegative penalty, and all possible negative reduced cost is localized to the final terminal edge.

## 5. Relation to MATH-089/090

The terminal edge is dangerous only if both

\[
c\Omega_{out}<\lambda z
\]

and the exact address zero-extension condition survives.
MATH-090 writes the latter as a low-resolution residue condition plus

\[
\nu_2(C_R)\ge z.
\]

Thus the envelope gives the clean decomposition

\[
\boxed{
\text{multi path: exact positive penalty}
\quad\longrightarrow\quad
\text{one terminal phase/address wedge}.
}
\]

## 6. Finite horizon without macro depth

Every one-paid macro has `h>=3`, so every envelope multi-edge reduces `R` by at least 3.
The first-cell source-window bound gives a finite initial `R` ceiling.  Hence the envelope graph is acyclic in `R` and has a finite path length automatically.

This suggests replacing the remaining macro-depth frontier by a resolution-indexed danger recursion rather than continuing depth 7, 8, ..., 16 separately.

Reproducibility:

`collatz/src/2026_09_12_math093_dyadic_resolution_envelope_certificate.py`

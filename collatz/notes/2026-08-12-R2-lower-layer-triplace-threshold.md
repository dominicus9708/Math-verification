# R2 lower-layer tri-place defect and threshold theorem

Date: 2026-08-12

Status: **exact local theorem for economical R2 renewal segments**. It explains why the finite residue-window mechanism that is useful on the first-crossing/supercritical side cannot by itself eliminate the coefficient-survival side.

## 1. Economical lower layer

Let an R2 renewal segment contain `H` odd events and `A` accelerated steps. If it avoids a floor doubling, the preceding R2 excursion theorem gives

\[
\boxed{A=\lfloor H\gamma\rfloor,\qquad \gamma:=\log_2 3.}
\]

Hence the odd-to-odd aggregate coefficient is

\[
\boxed{a:=\frac{3^H}{2^A}>1.}
\]

Fix a finite parity/block word `w` with these aggregate counts. Write its odd-event correction as

\[
c(w)=\sum_{i=0}^{H-1}\frac{2^{A_i(w)}}{3^{i+1}}.
\]

Then the aggregate affine map is

\[
\boxed{F_w(x)=a(x+c(w))=ax+b_w,\qquad b_w:=a c(w)>0.}
\]

## 2. Lower Beatty reference and displacement defect

For the critical lower Beatty reference put

\[
A_i^*:=\lfloor i\gamma\rfloor,
\]

and

\[
\boxed{c_*:=\sum_{i=0}^{H-1}\frac{2^{A_i^*}}{3^{i+1}}.}
\]

An economical R2 excursion has the same terminal count `A=floor(H gamma)` and satisfies

\[
A_i(w)=A_i^*-s_i,
\qquad
s_i\ge0,
\qquad
s_0=s_H=0.
\]

Define the normalized lower-layer defect

\[
\boxed{\xi(w):=c_*-c(w)
=\sum_{i=0}^{H-1}
\frac{2^{A_i^*}}{3^{i+1}}
(1-2^{-s_i})\ge0.}
\]

It vanishes exactly for the lower Beatty reference word.

## 3. Real action: negative rational shadow

Because `a>1`, the unique affine fixed point is negative:

\[
\boxed{C_w:=\frac{b_w}{1-a}
=-\frac{a c(w)}{a-1}<0.}
\]

For the reference word,

\[
C_*=-\frac{a c_*}{a-1}.
\]

Since `c(w)=c_*-xi`,

\[
\boxed{C_w=C_*+\frac{a\xi}{a-1}.}
\]

Thus positive displacement defect moves the real shadow upward toward zero. This is the opposite Archimedean orientation from the first-crossing/supercritical case, whose positive rational shadow is lowered by defect.

## 4. Exact 2-adic formation shift

The reference and actual economical words have the same total accelerated length `A`, the same odd count `H`, and the same endpoint-odd convention. Their exact starting residues therefore live modulo the same modulus `2^{A+1}`.

Subtracting the Bernstein/formation correction formulas gives

\[
\boxed{
\rho_w\equiv \rho_*+\xi
\pmod{2^{A+1}},
}
\]

where every odd denominator is interpreted through its inverse modulo `2^{A+1}`.

Thus the same lower-layer defect is the exact 2-adic formation-address shift.

## 5. Exact gap-residue shift

Let

\[
\boxed{Z_-:=3^H-2^A>0.}
\]

If an integer start `N` realizing the word has odd endpoint

\[
N'=N+g,
\]

then

\[
2^A(N+g)=3^H N+R_w,
\]

where

\[
R_w:=3^H c(w).
\]

Hence

\[
2^A g=Z_-N+R_w
\]

and therefore

\[
\boxed{
g\equiv R_w(2^A)^{-1}\pmod{Z_-}.}
\]

Since

\[
2^A\equiv3^H\pmod{Z_-},
\]

subtracting the reference and actual residues gives

\[
\boxed{
g_w\equiv g_*-\xi\pmod{Z_-}.}
\]

Thus formation and gap addresses again move in opposite directions under the same defect coordinate.

## 6. Local renewal-compatible threshold

The Archimedean geometry is fundamentally different from the supercritical side.

Let an interior maximal-block boundary `r` have prefix affine map

\[
F_r(x)=a_r x+b_r
\]

and define the corresponding rational shadow state

\[
C_r:=F_r(C_w).
\]

For a genuine renewal segment, every interior block start `X_r` exceeds the endpoint `N'`. The proper suffix from `X_r` to `N'` has positive affine correction and decreases a positive state, so its coefficient must be less than one. Since the suffix coefficient is `a/a_r`,

\[
\boxed{a_r>a}
\]

at every interior block boundary.

For an integer start `N` in the exact formation class, write

\[
N'=C_w+a(N-C_w),
\]

and

\[
X_r=C_r+a_r(N-C_w).
\]

The finite renewal-compatible inequality `X_r>N'` is equivalent to

\[
(a_r-a)(N-C_w)>C_w-C_r.
\]

Hence

\[
\boxed{
N>
C_w+
\frac{C_w-C_r}{a_r-a}.
}
\]

Define

\[
\boxed{
L(w):=
\max_{r\,\mathrm{interior}}
\left[
C_w+
\frac{C_w-C_r}{a_r-a}
\right].
}
\]

Then, for a fixed word satisfying the required suffix-coefficient inequalities, its positive finite renewal-compatible starts are exactly the points of its dyadic formation class above the threshold:

\[
\boxed{
\left(\rho_w+2^{A+1}\mathbb Z\right)
\cap\mathbb N
\cap(L(w),\infty).
}
\]

The global condition that the endpoint is a true suffix minimum of the infinite continuation remains separate.

## 7. Structural asymmetry with R1

For a first-crossing/supercritical word the full affine coefficient is `<1`, the rational shadow is positive, and finite renewal-compatible starts lie in a bounded interval below the shadow. This makes a residue-window separation theorem possible.

For an economical R2 word the full affine coefficient is `>1`, the rational shadow is negative, and the finite compatible starts lie in an **unbounded half-line** above a threshold.

Therefore:

\[
\boxed{
\text{no one-word residue--window separation can eliminate R2 locally.}
}
\]

Any R2 exclusion theorem must use infinite concatenation, a transported renewal attribute, or the fixed-natural-number condition across arbitrarily long prefixes.

## 8. Current role

This theorem gives a finite lower-layer counterpart of the first-crossing tri-place defect:

- real shadow: defect moves a negative shadow toward zero;
- 2-adic formation: `+xi`;
- gap residue: `-xi`.

The sign change on the real side explains why R2 is the harder terminal branch. Local arithmetic thinning remains available, but local candidate sets are unbounded.

The next viable targets are therefore global:

1. an infinite Beatty-defect naturalness theorem for one fixed positive integer;
2. a renewal-excursion concatenation obstruction;
3. or a transported discrete quantity that cannot repeatedly reset while the harmonic displacement area grows like `q log q`.
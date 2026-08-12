# Strengthened renewal address and exact formation-gap lattice unification

Date: 2026-08-12

Status: **exact renewal-address theorem**. For genuine renewal floors, the condition that both endpoints are `3 mod 4` strengthens the finite formation modulus from endpoint-oddness scale `2^(A+1)` to `2^(A+2)`. At this stronger scale the dyadic start address and the `4Z` renewal-gap progression become one and the same affine lattice. In the polynomial-start regime of primitive upper-CF first crossings, the gap is therefore determined exactly by the least strengthened renewal address. This does not prove Collatz.

## 1. Setup

Let a finite parity word have

\[
A=\text{total parity length},
\qquad
H=\text{odd count},
\]

and affine iterate

\[
\boxed{
T^A(N)=\frac{3^H N+R}{2^A}.
}
\]

Put

\[
\boxed{Z:=2^A-3^H.}
\]

For a genuine renewal segment write

\[
N'=N+g,
\qquad g>0.
\]

Then exactly

\[
\boxed{
2^A g=R-ZN.
}
\]

## 2. Renewal floors are `3 mod 4`

For any renewal floor `N>1`, the first odd-only valuation must be `v_0=1`. Indeed, `v_0>=2` would give

\[
\frac{3N+1}{4}<N,
\]

contradicting the suffix-minimum property.

Thus

\[
v_2(3N+1)=1,
\]

which is equivalent to

\[
\boxed{N\equiv3\pmod4.}
\]

The next renewal floor satisfies the same property, so

\[
\boxed{N'\equiv3\pmod4.}
\]

Therefore

\[
\boxed{g=N'-N\equiv0\pmod4.}
\]

## 3. Strong endpoint formation congruence

Ordinary completed-word formation with endpoint oddness gives a residue modulo `2^(A+1)`.

A renewal endpoint is stronger: it is not merely odd but `3 mod 4`. Since

\[
3^H N+R=2^A N',
\]

and

\[
N'\equiv3\pmod4,
\]

we obtain

\[
\boxed{
3^H N+R
\equiv
3\cdot2^A
\pmod{2^{A+2}}.
}
\]

Because `3^H` is odd and hence invertible modulo `2^(A+2)`, the word determines one unique start residue class modulo

\[
\boxed{2^{A+2}.}
\]

Define its least positive representative by

\[
\boxed{
\widehat\rho_w
\in\{1,2,\ldots,2^{A+2}\}.
}
\]

This is one bit stronger than the completed endpoint-odd formation class modulo `2^(A+1)` and two bits stronger than the bare length-`A` parity cylinder.

## 4. Equivalent gap-divisibility form

From

\[
2^A g=R-ZN,
\]

the renewal condition `g=0 mod 4` is exactly

\[
\boxed{
R-ZN\equiv0\pmod{2^{A+2}}.
}
\]

Since `Z` is odd, this also determines one unique residue class for `N mod 2^(A+2)`.

Thus the strengthened endpoint congruence and the gap-divisibility congruence are the same renewal address written in two forms.

## 5. Exact affine start-gap lattice

Let

\[
M:=2^{A+2}.
\]

Every integer realization of the strengthened renewal congruence is

\[
\boxed{
N=\widehat\rho_w+kM,
\qquad k\in\mathbb Z.
}
\]

Define the canonical strengthened gap

\[
\boxed{
\widehat g_w
:=
\frac{R-Z\widehat\rho_w}{2^A}.
}
\]

By construction,

\[
\boxed{\widehat g_w\in4\mathbb Z.}
\]

Substituting `N=widehat rho_w+kM` into the exact gap formula gives

\[
\begin{aligned}
g
&=
\frac{R-Z(\widehat\rho_w+k2^{A+2})}{2^A}\\
&=
\widehat g_w-4kZ.
\end{aligned}
\]

Hence

\[
\boxed{
(N,g)
=
(\widehat\rho_w,\widehat g_w)
+k(2^{A+2},-4Z).
}
\]

This is the exact renewal realization lattice.

The earlier statement

\[
g\equiv g_w\pmod{4Z}
\]

is therefore not an independent modular filter: it is the gap projection of this one dyadic start-address lattice.

## 6. Polynomial-start regime removes the lattice ambiguity

For primitive upper-CF first-crossing words, the established linear-form estimate plus the first-crossing correction ceiling gives an effective polynomial upper bound

\[
N\le\operatorname{poly}(H).
\]

But

\[
2^{A+2}\asymp3^H
\]

grows exponentially in `H`. Therefore for every sufficiently large upper convergent,

\[
\boxed{N<2^{A+2}.}
\]

A surviving ordinary integer must then use the least strengthened renewal address itself:

\[
\boxed{N=\widehat\rho_w.}
\]

Consequently its renewal gap is no longer merely a residue class:

\[
\boxed{g=\widehat g_w.}
\]

The full gap condition becomes the exact finite inequality

\[
\boxed{
0<\widehat g_w<\frac H3,
\qquad
\widehat g_w\in4\mathbb Z.
}
\]

There is no remaining `+/- 4Z` choice in the large primitive-CF polynomial-start regime.

## 7. Christoffel defect at the stronger address scale

Let `R_chr` be the Christoffel correction numerator and

\[
R_s=R_{chr}-\mathcal E
\]

for a displaced word. Let their strengthened renewal addresses be

\[
\widehat\rho_{chr},
\qquad
\widehat\rho_s.
\]

Subtracting the strong endpoint congruences gives

\[
3^H(\widehat\rho_s-\widehat\rho_{chr})
\equiv
\mathcal E
\pmod{2^{A+2}}.
\]

Therefore

\[
\boxed{
\widehat\rho_s-\widehat\rho_{chr}
\equiv
\eta
\pmod{2^{A+2}},
\qquad
\eta:=\frac{\mathcal E}{3^H}.
}
\]

Using the exact skew-displacement collapse theorem,

\[
\eta=\frac13\mathfrak D_H,
\]

so

\[
\boxed{
\widehat\rho_s
\equiv
\widehat\rho_{chr}
+
\frac13\mathfrak D_H
\pmod{2^{A+2}}.
}
\]

Thus the weighted sparse defect shifts the strengthened renewal address directly, one bit deeper than the earlier endpoint-odd formation address.

## 8. Exact gap is the dual projection of the same address

For a word in the polynomial-start regime,

\[
N=\widehat\rho_w.
\]

Then

\[
\boxed{
\widehat g_w
=
\frac{R-Z\widehat\rho_w}{2^A}.
}
\]

Equivalently, with the positive rational shadow

\[
C_w:=\frac RZ,
\]

\[
\boxed{
\widehat g_w
=
\frac Z{2^A}
(C_w-\widehat\rho_w).
}
\]

Therefore

\[
\boxed{
\widehat g_w>0
\iff
\widehat\rho_w<C_w.
}
\]

The ordinary-start admissibility and the positive renewal gap are the same Archimedean comparison after the strengthened dyadic address has been fixed.

## 9. Collapse from tri-place to a strengthened two-place problem

Previously the primitive upper-CF residual branch was described by three coupled requirements:

1. real Christoffel-shadow budget;
2. 2-adic formation address;
3. modular `4Z` gap residue.

For sufficiently large primitive upper-CF first crossings, Sections 5--8 show that items 2 and 3 are not independent. The strengthened residue

\[
\boxed{\widehat\rho_w\pmod{2^{A+2}}}
\]

determines the exact ordinary start and hence the exact gap.

Thus the residual problem may be rewritten as a **two-place compatibility problem**:

### Dyadic renewal address

\[
\boxed{
N=\widehat\rho_w
=
[\widehat\rho_{chr}+\mathfrak D_H/3]_{2^{A+2}}.
}
\]

### Archimedean shadow window

\[
\boxed{
0<
\frac Z{2^A}(C_w-N)
<\frac H3.
}
\]

The middle quantity is automatically a multiple of `4` for the strengthened renewal address.

## 10. Refined sparse residual target

Combining this theorem with the exact skew-displacement collapse, any sufficiently large surviving primitive upper-CF first crossing must satisfy simultaneously:

\[
\boxed{r_*=o(H)}
\]

if it evades a positive-density defect loss,

\[
\boxed{
N=
[\widehat\rho_{chr}+\mathfrak D_H/3]_{2^{A+2}}
<\operatorname{poly}(H),
}
\]

and

\[
\boxed{
0<
\frac{R_s-ZN}{2^A}
<\frac H3.
}
\]

The earlier modular target set has therefore been absorbed into one exact strengthened dyadic representative.

The next hard theorem is correspondingly sharper:

> Exclude sparse nonzero displacement staircases whose weighted defect moves the strengthened Christoffel renewal address into a polynomial-size representative while simultaneously leaving that representative below the displaced rational shadow.

This is a smaller arithmetic target than the previous three-filter formulation.

# Asymptotic transition-width lower bound for gate Hensel repair

Date: 2026-08-15

Status: **analytic lower-bound theorem for the enlarged gate transition family + explanation of the observed ~37% thresholds**.  It shows that a fixed bounded predecessor-credit target cannot be repaired by rearranging only a subcritical fraction of the front/pair transition region.  It applies to the enlarged sections of the companion transition-band theorem; it is not yet a full-gate-fibre theorem and does not prove Collatz.

## 1. Balanced residual without a power table

For a remaining pair cube of dimension `n`, the normalized integer-credit target is

\[
T_\delta=-2^{2n+1}\delta=-2\,4^n\delta.
\]

After multiplying by `4^(-(n-1))`, the initial balanced-Hensel residual is simply

\[
\boxed{U_0\equiv-8\delta.}
\]

This is independent of the gate scale and of `n`.

As long as the least signed representative does not wrap modulo the remaining power of three, write

\[
U_j=-a_j,
\qquad a_j>0.
\]

The balanced digit `e_j in {-1,0,1}` is chosen by

\[
e_j\equiv U_j\pmod3,
\]

and the renormalized recurrence is

\[
U_{j+1}=\frac{4(U_j-e_j)}3.
\]

Thus

\[
\boxed{
a_{j+1}=\frac43(a_j+e_j),
\qquad e_j\in\{-1,0,1\}.}
\]

## 2. Exact Archimedean envelope

Because `|e_j|<=1`,

\[
\frac43(a_j-1)
\le a_{j+1}\le
\frac43(a_j+1).
\]

The fixed points of the two affine comparison recurrences give

\[
\boxed{
4+(a_0-4)\left(\frac43\right)^j
\le a_j
\le
-4+(a_0+4)\left(\frac43\right)^j.
}
\]

Since `a_0=8 delta`, this is

\[
\boxed{
4+(8\delta-4)\left(\frac43\right)^j
\le a_j
\le
-4+(8\delta+4)\left(\frac43\right)^j.
}
\]

For every `delta>=1`, in particular,

\[
\boxed{a_j>4(4/3)^j.}
\]

For a fixed finite credit range, the upper envelope also shows that along the critical gate hierarchy the signed residual remains exponentially smaller than the remaining modulus `3^(F+h)` throughout the subcritical transition widths used below, so the no-wrap representation is valid for all sufficiently large gates.  The current `delta<=397` first- and second-return gates are independently checked by the exact finite certificates.

## 3. Transition-band geometry

Use the enlarged family

\[
1^{F-h}B(01/10)^{J-h}0,
\qquad |B|=3h,\quad |B|_1=2h.
\]

Put

\[
n=J-h.
\]

After the remaining `n` pair coordinates solve the low Hensel target, the required boundary correction difference has magnitude

\[
\boxed{|T_h(\delta)|=2^{3h-2}a_{J-h}.}
\]

The exact maximum difference between any two length-`3h`, weight-`2h` boundary words is

\[
\boxed{
M_h=(2^h-1)(3^{2h}-4^h)<18^h.
}
\]

Using the lower residual envelope,

\[
|T_h(\delta)|
>
2^{3h-2}\cdot4\left(\frac43\right)^{J-h}
=
6^h\left(\frac43\right)^J.
\]

Therefore if

\[
\left(\frac43\right)^J>3^h,
\]

then

\[
|T_h(\delta)|>18^h>M_h,
\]

so no boundary repair exists.

Equivalently,

\[
\boxed{
h<J\log_3\frac43
\quad\Longrightarrow\quad
\text{no repair in the enlarged transition family}.}
\]

This bound is uniform over every positive credit `delta` for which the signed no-wrap condition holds; in particular it applies to the entire certified recurrent range `1<=delta<=397` at the present gate scales.

## 4. Critical-gate asymptotics

For the gate-wide neutral cube,

\[
J=L-q-1,
\qquad
F=q-J.
\]

At critical Euclidean scale

\[
\frac Lq\to\log_2 3.
\]

Hence

\[
\frac Jq\to\log_2\frac32,
\qquad
\frac Fq\to2-\log_2 3.
\]

Using

\[
\log_2\frac32=rac{\ln(3/2)}{\ln2},
\qquad
2-\log_2 3=rac{\ln(4/3)}{\ln2},
\]

we get

\[
\frac JF
\to
\frac{\ln(3/2)}{\ln(4/3)}.
\]

Therefore the transition-width theorem gives the asymptotic lower ratio

\[
\boxed{
\frac{h_{\min}}F
\ge
\log_3\frac32-o(1)
=0.3690702464\ldots-o(1).
}
\]

Thus a bounded-credit repair cannot be localized to an `o(F)` perturbation of the front/pair boundary.  It must reorganize a positive fraction of the syndrome-front scale.

## 5. Agreement with the exact finite thresholds

The exact companion certificate, which uses the full signed residue rather than only the analytic lower envelope, finds the first transition width at which the **magnitude test alone** ceases to prove impossibility:

\[
\boxed{\begin{array}{c|c}
\text{gate/fibre}&h_{\rm first\ possible\ by\ magnitude}\\\hline
G_{81}\text{ neutral}&150\\
G_{81}\text{ one-slack}&150\\
G_{82}\text{ neutral}&151\\
G_{82}\text{ one-slack}&152\\
G_{13}\text{ neutral}&1936\\
G_{13}\text{ one-slack}&1937\\
G_{14}\text{ neutral}&2085\\
G_{14}\text{ one-slack}&2085
\end{array}}
\]

These values track the analytic critical fraction extremely closely.  For example

\[
1936/5245=0.369113\ldots,
\qquad
2085/5648=0.369157\ldots.
\]

The exact thresholds are stronger finite facts; the theorem above explains their stable scale.

## 6. Proof-program consequence

The missing kernel freedom in the full gate fibre is not a narrow local correction near the systematic Hensel cube.  Any bounded-credit repair in this enlarged family must penetrate a positive fraction of the complementary syndrome sector.

This changes the next target from a small local enumeration to a renormalized one:

\[
\boxed{
\text{full-fibre repair must transport information across a width }
\asymp F\log_3(3/2).
}
\]

The natural next question is whether the Euclidean survival state permits such a macroscopic transition reorganization while also preserving the fixed ordinary dyadic zero-lift target and the early first-defect channel.

# Fixed-resolution cross-place mixing barrier

Date: 2026-08-12

Status: **exact finite-group asymptotic limitation theorem** for any cross-place sieve whose dyadic resolution is held fixed while additional ternary `0/1` selector digits are released. It explains the observed stabilization of the `B_max=18` class-pruning rate and proves that a fixed dyadic modulus cannot drive the surviving representative fraction to zero unless its survivor residue set is already empty. This is a proof-strategy limitation theorem, not a Collatz result.

## 1. Reduced dyadic coordinate

Every recursively sufficient Cantor-core start has the form

\[
N=4Y+3.
\]

Fix a dyadic resolution

\[
N\pmod{2^L},
\qquad L\ge3.
\]

Since `N=3 mod4`, this is equivalent to the reduced coordinate

\[
\boxed{Y\pmod{M},\qquad M=2^{L-2}.}
\]

For a fixed low ternary selector prefix through index `Q-1`, the remaining high selectors contribute

\[
\boxed{
S_{Q,d}
=\sum_{i=Q}^{d-1}a_i3^i
\pmod M,
\qquad a_i\in\{0,1\}.}
\]

Put the uniform measure on the `2^(d-Q)` selector assignments and let `mu_{Q,d}` be the induced probability distribution on `Z/MZ`.

## 2. Fourier factorization

For a character

\[
\chi_t(x)=e^{2\pi i tx/M},
\qquad t\in\mathbb Z/M\mathbb Z,
\]

the normalized Fourier coefficient is

\[
\boxed{
\widehat\mu_{Q,d}(t)
=
\prod_{i=Q}^{d-1}
\frac{1+e^{2\pi i t3^i/M}}2.
}
\]

For `t=0`, the coefficient is one.

If `t!=0 mod M`, multiplication by the odd unit `3^i` cannot send `t` to zero modulo `M`. Hence every factor has modulus strictly less than one:

\[
\left|
\frac{1+e^{2\pi i t3^i/M}}2
\right|
=
\left|
\cos\left(\frac{\pi t3^i}{M}\right)
\right|
<1.
\]

Because the group is finite and `3^i mod M` is periodic, for each nonzero `t` there is a constant

\[
0\le\rho_t<1
\]

such that

\[
\boxed{
|\widehat\mu_{Q,d}(t)|
\le
\rho_t^{d-Q}.}
\]

Therefore all nontrivial Fourier coefficients tend to zero exponentially, and Fourier inversion gives

\[
\boxed{
\mu_{Q,d}
\longrightarrow
\text{uniform measure on }\mathbb Z/M\mathbb Z
}
\]

as `d-Q -> infinity` with `L,Q` fixed.

## 3. Consequence for any fixed class sieve

Let a fixed-resolution proposition sieve retain, for one low ternary prefix `u`, a residue subset

\[
R_u\subseteq\mathbb Z/M\mathbb Z.
\]

Then

\[
\boxed{
\Pr(S_{Q,d}\in R_u)
\longrightarrow
\frac{|R_u|}{M}.}
\]

Averaging over the finite `2^Q` low ternary prefixes gives the corresponding global fixed-resolution survival limit

\[
\boxed{
\lim_{d\to\infty}
\text{surviving representative fraction}
=
\frac1{2^Q M}
\sum_u |R_u|.
}
\]

Hence a fixed-resolution sieve can make the limiting fraction zero **only if every survivor set `R_u` is already empty**.

If even one class survives, increasing only the number of high ternary selector digits cannot eventually eliminate all representatives through that fixed modulus.

## 4. Exact `B_max=18` forward example

For the current forward class sieve,

\[
L=19,
\qquad
M=2^{17}=131,072.
\]

Exact enumeration of the dyadic parity cylinders shows that precisely

\[
\boxed{14,990}
\]

reachable residues `N=3 mod4` survive every uniform forward-descent proposition through depth 18.

Therefore the fixed-resolution limiting survival density is

\[
\boxed{
\frac{14,990}{131,072}
=0.1143646240234375.
}
\]

The exact finite representative calculations approach this value:

\[
\begin{array}{c|c}
d&\text{surviving fraction after fixed }B\le18\\\hline
28&0.11434980854392052\\
29&0.11435773968696594\\
30&0.11435918044298887
\end{array}
\]

This convergence is not used to prove the theorem; it is a numerical cross-check of the finite-group mixing statement.

## 5. Cross-place extension

The same argument applies when a finite low-ternary / `3`-adic address is appended to the class state.

Fix `Q` and `L`. For each of the finitely many low ternary addresses `u`, the high selector digits still enter the dyadic coordinate only through the translated random sum `S_{Q,d}`. Any finite forward/reverse proposition filter therefore leaves some finite residue subset `R_u`.

As long as at least one such subset is nonempty, the fixed `(Q,L)` sieve has a positive asymptotic surviving fraction.

Thus neither a fixed dyadic depth nor a fixed cross-place address resolution can be a terminal route merely by releasing more ternary selectors.

## 6. Required scaling law for the proof program

A terminal structural argument must therefore use at least one resolution that grows with the representative depth:

\[
\boxed{
L=L(d)\to\infty
\quad\text{or}\quad
Q=Q(d)\to\infty,
}
\]

or an equivalent cross-depth consistency condition carrying unbounded information.

Operationally, the current program should replace

\[
\text{fixed }B_{\max}=18
\]

by a nested survivor-cylinder hierarchy

\[
\boxed{
\mathcal S_{B+1}\subseteq
\pi^{-1}(\mathcal S_B),
\qquad B\to\infty,
}
\]

and study whether actual ternary-core lifts can remain in that hierarchy.

## 7. Relation to earlier fixed-low-bit saturation

The earlier zero-slack projection-saturation theorem showed from the parity-language side that fixed low binary information reappears at arbitrarily deep coefficient-surviving targets.

The present theorem is the complementary ternary-static-aggregation statement: for a fixed binary modulus, adding sufficiently many ternary `0/1` selectors mixes their subset sums across the available residue group.

Together they show from both directions why a terminal proof must preserve **growing-resolution compatibility**, not merely sharpen one fixed finite sieve.

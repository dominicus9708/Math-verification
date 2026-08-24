# Exact valuation-shell Fourier energy for the coefficient-survivor language

Date: 2026-08-24

Status: **exact identity.** This note converts an entire 2-adic Fourier valuation shell of the coefficient-survivor residue set into a polynomial-time boundary/tail-count expression. It is not yet a selector-intersection theorem and not a proof of Collatz.

## 1. Setup

Let `P_H` be the set of canonical residues modulo `2^H` of all length-`H` parity words satisfying coefficient survival at every prefix,

\[
3^{q_j}\ge 2^j.
\]

Write

\[
b_j:=q_{\min}(j)=\min\{q:3^q\ge2^j\}.
\]

Fix an effective dyadic depth `K<=H` and put `s=H-K`. For each residue `r mod 2^K`, define the projected completion multiplicity

\[
g_{H,K}(r):=\#\{x\in P_H:x\equiv r\pmod{2^K}\}.
\]

Because the first `K` parity symbols determine the canonical residue modulo `2^K`, each surviving length-`K` prefix contributes exactly the number of admissible tails from its current odd count.

## 2. Tail completion counts

Let

\[
F_{H,K}(q)
\]

be the number of coefficient-admissible binary tails of length `H-K` beginning immediately after depth `K` from odd count `q`.

Let

\[
C_{K-1}(q)
\]

be the number of coefficient-surviving prefixes of length `K-1` with odd count `q`.

For a fixed parent prefix at depth `K-1`, its two dyadic children have projected multiplicities

\[
G_0(q)=\mathbf 1_{q\ge b_K}F_{H,K}(q),
\]

\[
G_1(q)=\mathbf 1_{q+1\ge b_K}F_{H,K}(q+1).
\]

Define the sibling imbalance

\[
\boxed{
D_{H,K}(q):=G_0(q)-G_1(q).
}
\]

## 3. Odd-shell Parseval identity

For a function `g` on `Z/2^K Z`, pair the two top-bit siblings `r` and `r+2^(K-1)`. The odd-frequency characters change sign between these two lifts. Standard Parseval on `Z/2^(K-1) Z` gives

\[
\boxed{
\sum_{u\;\mathrm{odd}\;(\mathrm{mod}\;2^K)}
|\widehat g(u)|^2
=
2^{K-1}
\sum_{r\bmod2^{K-1}}
|g(r)-g(r+2^{K-1})|^2.
}
\]

Apply this to `g=g_{H,K}`. Parent prefixes with the same odd count `q` have the same tail multiplicities, and there are exactly `C_{K-1}(q)` such parents. Therefore

\[
\boxed{
\sum_{u\;\mathrm{odd}\;(\mathrm{mod}\;2^K)}
|\widehat g_{H,K}(u)|^2
=
2^{K-1}
\sum_q
C_{K-1}(q)\,D_{H,K}(q)^2.
}
\]

Finally, frequencies in the original modulus `2^H` with exact valuation `v_2(t)=H-K` are precisely `t=2^{H-K}u` with odd `u mod 2^K`, and

\[
\widehat{1_{P_H}}(2^{H-K}u)=\widehat g_{H,K}(u).
\]

Hence the complete valuation-shell energy is

\[
\boxed{
E_{H,K}
:=
\sum_{\substack{t\bmod2^H\\v_2(t)=H-K}}
|\widehat{1_{P_H}}(t)|^2
=
2^{K-1}
\sum_q C_{K-1}(q)D_{H,K}(q)^2.
}
\]

No individual Fourier frequency is evaluated.

## 4. Boundary support

Let `a=b_K` and `b=b_H`. For sufficiently large `q>=b`, every remaining tail choice is admissible, so

\[
F_{H,K}(q)=2^{H-K}.
\]

Thus `D_{H,K}(q)=0` for `q>=b`. For `q<a-1`, both children are forbidden at depth `K`. Consequently only

\[
\boxed{a-1\le q\le b-1}
\]

can contribute.

This is the L2 version of the previously derived valuation boundary-projection theorem: the whole Fourier shell is controlled by a strip of at most

\[
(b-a+1)\le H-K+1
\]

odd-count layers.

## 5. Terminal shell recovers plateau/rise factorization

When `K=H`, the tail length is zero.

- If `b_H=b_{H-1}`, every parent has either two children or none, so `D=0` and the odd shell energy is exactly zero.
- If `b_H=b_{H-1}+1`, only the parent layer `q=b_H-1` has one child. Therefore

\[
\boxed{
E_{H,H}=2^{H-1}B_H,
}
\]

where

\[
B_H=C_{H-1}(b_H-1)
\]

is the Beatty boundary-parent count.

Thus the earlier exact odd-frequency annihilation at plateau depths and boundary factorization at rise depths are the terminal case of the shell-energy theorem.

## 6. Role

The pointwise Fourier problem can now be split into two levels:

1. exact shell energy of the coefficient-survivor language, computable in polynomial time from integer ballot/tail counts;
2. selector energy or pointwise concentration inside the same shell.

A future same-address estimate can combine these shell energies by Cauchy-Schwarz separately for each 2-adic valuation instead of requiring a uniform pointwise bound over all frequencies.

Certificate:

`collatz/src/survivor_fourier_shell_energy_certificate.py`.

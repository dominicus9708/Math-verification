# First global resonance: 72-bit exclusion of the mechanical equality branch

Date: 2026-08-26

Status: exact finite binary-domain theorem. It uses the previously certified first-cell start ceiling and the first-crossing mechanical-envelope theorem. No ternary selector and no repeated local pullback is used. This eliminates the unique maximum-correction equality word at the first resonance, but not all nonmechanical words.

## 1. First-cell start size makes the address finite

At the first global resonance

\[
(A_0,q_0)
=(114,208,327,604,\ 72,057,431,991),
\]

the mechanical first-crossing ceiling gives

\[
N<\frac43\,2^{71}<2^{72}.
\]

Therefore the first 72 parity symbols already determine the ordinary positive integer start exactly: a length-72 parity word corresponds to one canonical residue in \([0,2^{72})\), and no further dyadic lift is available below \(2^{72}\).

## 2. Exact first 72 symbols of the maximum-correction word

The first-crossing mechanical word is defined by

\[
k_i=\lceil i\log_3 2\rceil,
\qquad
m_i=k_i-k_{i-1}.
\]

Exact integer comparisons

\[
3^{k_i-1}<2^i<3^{k_i}
\]
for \(1\le i\le72\) certify the prefix

```text
110110110101101101011011011010110110101101101101011011010110110110101101
```

with 46 odd symbols.

This is not a floating-point identification; the companion certificate checks every Beatty ceiling by exact integer powers.

## 3. Canonical 72-bit formation residue

For a length-72 parity prefix, let

\[
T^{72}(r)=\frac{3^q r+R}{2^{72}}.
\]

The canonical start residue is

\[
r\equiv-R(3^q)^{-1}\pmod{2^{72}}.
\]

For the exact mechanical prefix above,

\[
\boxed{
\rho_{72}^{\rm mech}
=4,697,939,311,072,332,635,131.
}
\]

It lies just below \(2^{72}\), but crucially

\[
3\rho_{72}^{\rm mech}>4\cdot2^{71},
\]
so

\[
\boxed{
\rho_{72}^{\rm mech}>rac43\,2^{71}.
}
\]

## 4. Exclusion theorem

Any ordinary start \(N<2^{72}\) realizing these 72 parity symbols must equal the canonical residue itself:

\[
N=\rho_{72}^{\rm mech}.
\]

But the first-resonance no-descent ceiling requires

\[
N<\frac43\,2^{71}.
\]

Contradiction.

Therefore

\[
\boxed{
\text{the unique maximum-correction mechanical/Christoffel first-crossing word cannot realize the first global resonance.}
}
\]

This is a complete exclusion of the equality branch at \((A_0,q_0)\).

## 5. Consequence for the residual first cell

Every remaining first-resonance candidate must be strictly nonmechanical and, because sharing the first 72 symbols would give the same forbidden formation residue, it must already differ from the mechanical word within the first 72 parity positions.

Hence the residual branch has simultaneously:

1. the fixed exponent pair \((A_0,q_0)\);
2. start band
   \[
   2^{71}<N<\frac43\,2^{71}<2^{72};
   \]
3. near-return gap
   \[
   g\in4\mathbb Z_{>0},\qquad g<2^{33};
   \]
4. strict positive mechanical correction defect;
5. a defect visible already inside the first 72 parity symbols.

This is substantially stronger than the previous generic near-Christoffel formulation.

## 6. Audit correction concerning square prefixes

The first resonance is an intermediate/semiconvergent of \(\log_3 2\), not a full convergent. Therefore the older supercritical-convergent square-prefix theorem cannot be attached automatically to this cell. The direct 72-bit formation argument above avoids that invalid extension entirely.

## 7. Next target

The remaining first-cell problem is now a **nonmechanical defect-to-gap congruence problem**:

> prove that every first-crossing ballot word of \((A_0,q_0)\) that deviates from the mechanical word within the first 72 positions has either a formation residue outside the 72-bit start band or a gap residue outside
> \[
> 4\mathbb Z_{>0}\cap(0,2^{33}).
> \]

The existing balanced-carry / two-ended defect coordinates should be re-audited against this exact target.

Certificate:

`collatz/src/global_first_resonance_mechanical_prefix72_exclusion.py`.

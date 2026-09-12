# MATH-095 — phase-resolution Bellman value remains insufficient without carry/address

Date: 2026-09-13

Status: `EXACT NEGATIVE ABSTRACTION RESULT / CARRY-ADDRESS CHANNEL REQUIRED / ONE-PAID FRONTIER STILL OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- Detailed one-paid Bellman frontier `7<=t<=16` remains open.

## 1. Question

MATH-094 showed that the Boolean phase danger kernel saturates after exact dyadic address and previously paid penalty are discarded. MATH-095 restores the complete positive multi-edge penalty while still forgetting address compatibility.

For resolution envelope `R` and current phase `Omega`, define

\[
V_R(\Omega)=\min_e
\begin{cases}
 c_e\rho_e\Omega-\lambda(h_e-R),&h_e>R,\\
 c_e\rho_e\Omega+V_{R-h_e}(\rho_e\Omega),&h_e\le R,
\end{cases}
\]

with

\[
\lambda=\frac{19}{503}.
\]

This recursion is exact for the address-forgotten MATH-093 dyadic envelope.

## 2. Exact finite result

The canonical 126 phase-edge components from MATH-086 and the 857 actual multi-source first-macro phase states are evaluated with exact `Fraction` arithmetic.

For every one of those 857 initial states, including the exact first-macro penalty, the lower-envelope Bellman value satisfies

\[
\boxed{-\frac52<J_{\rm env}<-2.}
\]

Thus all 857 states retain a negative path in the address-forgotten envelope.

## 3. Interpretation

This is a negative result about state compression, not evidence of an actual bad Collatz path.

The abstraction keeps:

- dyadic resolution `R`;
- exact phase transport;
- complete accumulated positive penalty through the Bellman value.

It removes:

- exact dyadic address compatibility;
- the MATH-090 carry/Hensel-lift constraint.

Because the abstraction enlarges the actual language, a negative envelope path may be fictitious. MATH-088 already supplies an explicit example of this phenomenon at macro depth 17, where millions of phase-danger edges have zero address-compatible realizations.

Therefore

\[
\boxed{(R,\Omega,\text{penalty})\text{ is not a sufficient proof-facing state}.}
\]

Any successful remaining quotient must retain an exact compatibility channel equivalent to the normalized 2-adic address/carry information of MATH-090--092.

## 4. State-minimality consequence

The current evidence rules out both reductions

\[
(R,\Omega)
\]

and

\[
(R,\Omega,\text{accumulated penalty})
\]

as sufficient states for closing the remaining one-paid Bellman language.

The next candidate state must contain at least

\[
\boxed{(R,\Omega,\mathcal C_{2})}
\]

where `C_2` is an exact finite 2-adic carry/address descriptor.

MATH-090 gives terminal compatibility in the form

\[
r_R<M,\qquad \nu_2(C_R)\ge h-R,
\]

while MATH-092 gives an exact normalized address transducer. These are the two natural constructions to use in the next quotient.

## 5. Claim boundary

MATH-095 does **not** show:

- existence of an actual negative Bellman path;
- failure of the `19/503` target;
- failure of the resolution potential;
- failure of the first-cell program.

It shows only that forgetting the carry/address channel creates fictitious negative paths even after exact phase and penalty information are restored.

## Reproducibility

`collatz/src/2026_09_12_math095_phase_resolution_bellman_value_certificate.py`

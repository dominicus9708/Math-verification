# MATH-072 — exact common-coordinate bridge between depth-Hensel and paid-count descriptions

Date: 2026-09-12

Status: `EXACT ALGEBRAIC BRIDGE / COMMON-STATE EXTRACTION STARTED`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note does not close `2<=r<=13`.
- The purpose is to identify the quantity seen in common by MATH-051 depth-41 finite-state analysis and MATH-060--071 paid-count/phase/AP analysis.

## 1. Definitions

For a parity word of depth `k`, let

\[
q=\#\{\text{odd positions}\},\qquad d=k-q.
\]

Let `C(w)` be the usual correction and define

\[
\boxed{S(w)=\frac{C(w)}{3^q}}.
\]

MATH-051 defines, from the even positions

\[
E=(e_0<\cdots<e_{d-1}),
\]

the fixed-d signature

\[
\boxed{
\Sigma_d(E)=\sum_{j=0}^{d-1}3^j\left(\frac23\right)^{e_j}.
}
\]

Introduce the inverse coefficient ratio

\[
\boxed{
\rho(k,q):=\frac{2^k}{3^q}.
}
\]

For the paid-count description, let

\[
m(q)=\lfloor q\log_2(3/2)\rfloor,
\]

\[
u=m(q)-d,
\]

and

\[
\boxed{
\Omega_q=\frac{2^{q+m(q)}}{3^q}.
}
\]

## 2. First bridge: depth signature and normalized correction

MATH-051 proves

\[
\frac{C(E)}{3^{k-d}}
=1+\Sigma_d(E)-3^d\left(\frac23\right)^k.
\]

Since `q=k-d`,

\[
3^d\left(\frac23\right)^k
=\frac{2^k}{3^{k-d}}
=\frac{2^k}{3^q}
=\rho.
\]

Therefore

\[
\boxed{
S=1+\Sigma_d-\rho.
}
\]

Equivalently,

\[
\boxed{
S+\rho=1+\Sigma_d.
}
\]

Thus the depth-41 fixed-d signature and the normalized correction are not merely analogous variables. They are the same exact coordinate up to the coefficient-ratio term `rho`.

## 3. Second bridge: slack/phase and coefficient ratio

Because

\[
d=m(q)-u,
\]

we have

\[
k=q+d=q+m(q)-u.
\]

Hence

\[
\rho
=\frac{2^{q+m(q)-u}}{3^q}
=2^{-u}\frac{2^{q+m(q)}}{3^q}.
\]

Therefore

\[
\boxed{
\rho=2^{-u}\Omega_q.
}
\]

Combining with the first bridge gives the common-coordinate identity

\[
\boxed{
S
=1+\Sigma_d-2^{-u}\Omega_q.
}
\]

This single equation contains the depth signature, the paid slack, the phase coordinate, and the normalized correction.

## 4. Exact parity-step recurrence

The common coordinate has a particularly simple one-step recurrence.

### Even extension

Appending an even shortcut bit leaves `C` and `q` unchanged while increasing `k` by one. Therefore

\[
\boxed{S'=S},
\]

\[
\boxed{\rho'=2\rho}.
\]

Using `Sigma=S+rho-1`,

\[
\boxed{\Sigma'=\Sigma+\rho}.
\]

### Odd extension

Appending an odd shortcut bit at position `k` gives

\[
C'=3C+2^k,
\qquad
q'=q+1.
\]

Thus

\[
S'
=\frac{3C+2^k}{3^{q+1}}
=S+\frac{\rho}{3},
\]

so

\[
\boxed{S'=S+\rho/3}.
\]

Also

\[
\boxed{\rho'=\frac23\rho}.
\]

Consequently

\[
\boxed{\Sigma'=\Sigma}.
\]

The complete exact transition table is therefore

| shortcut bit | `S'` | `rho'` | `Sigma'` |
|---|---|---|---|
| even | `S` | `2 rho` | `Sigma + rho` |
| odd | `S + rho/3` | `(2/3) rho` | `Sigma` |

This explains why the MATH-051 signature is naturally indexed by even-position gaps: odd steps leave `Sigma` invariant, while every even step adds the current `rho`.

## 5. Penalty atom is an increment deficit

For a paid event the existing penalty atom is

\[
p
=\frac13(1-2^{-u})\Omega_q.
\]

Using

\[
\rho=2^{-u}\Omega_q,
\]

we obtain

\[
\boxed{
p=\frac{\Omega_q-\rho}{3}.
}
\]

But an actual odd extension increases the normalized correction by

\[
\Delta S=\rho/3.
\]

Therefore

\[
\boxed{
p=\frac{\Omega_q}{3}-\Delta S.}
\]

This gives an exact interpretation of the paid penalty:

> the penalty is the difference between the phase-boundary reference increment `Omega/3` and the actual normalized-correction increment `rho/3` paid by that odd step.

Thus the penalty calculation and the depth-Hensel `S/Sigma` calculation are measuring the same correction budget from two descriptions.

## 6. Hensel-class consequence

At fixed `(k,d)` we also have fixed `q` and fixed `rho`.
Hence for two words `E,F` in the same fixed-d layer,

\[
\boxed{
S(F)-S(E)=\Sigma_d(F)-\Sigma_d(E).
}
\]

MATH-051 showed that the exact Hensel-class collision/translation condition is integrality of the Sigma difference.
Therefore it is equivalently an integrality condition on the normalized-correction difference:

\[
\boxed{
\Delta\Sigma\in\mathbb Z
\iff
\Delta S\in\mathbb Z
\quad\text{at fixed }(k,d).
}
\]

So the bounded-carry recurrence in the depth-41 solver is an exact finite-state mechanism for testing integer translation differences in the same `S` that appears in the paid-count calculation.

## 7. Redundant and irreducible coordinates

The bridge permits a DSD reduction.

Define

\[
x:=\frac{\rho}{\Omega_q}.
\]

Then

\[
\boxed{x=2^{-u}}.
\]

Thus `u` and the normalized ratio `rho/Omega` contain the same information.
The penalty becomes

\[
\boxed{p=\frac{\Omega_q}{3}(1-x)}.
\]

A minimal analytic state candidate is therefore

\[
\boxed{(S,\rho,\Omega_q)}
\]

or equivalently

\[
\boxed{(\Sigma_d,\rho,\Omega_q)}.
\]

However this is not yet sufficient to replace the exact dyadic source address.
MATH-068--071 show that resolution/multiplicity can close a branch even when the analytic penalty alone does not.
Therefore the current future-relevant state candidate must retain a fourth, address-side coordinate, for example

\[
\boxed{
(S,\rho,\Omega_q,\mathcal A_k)
}
\]

where `A_k` denotes the exact dyadic source class / remaining address family.

## 8. Relation to r=14--17

The adjacent closed paid-count layers use different computational descriptions:

- `r=17`: low-bit block -> singleton handoff;
- `r=16`: AP + block + streaming;
- `r=15`: multiplicity-banded AP union;
- `r=14`: adaptive AP union + source/parameter sharding.

All of these retain the same ordinary-integer address lineage while changing only the representation of that lineage.

MATH-072 indicates that their analytic side should be compared through

\[
\boxed{
S=1+\Sigma-\rho,
\qquad
\rho=2^{-u}\Omega,
\qquad
p=(\Omega-\rho)/3.
}
\]

The next extraction target is therefore not another arbitrary fitted expression. It is to determine whether the address-side resolution can be coupled to the analytic deficit `Omega-rho` by one exact or monotone potential.

## 9. Candidate next potential question

A useful next question is whether there exists an exact future-valid function `H(A_k)` or a small extension of it such that

\[
\boxed{
\Delta\mathcal P
-\lambda\,\Delta L
+\Delta H
\ge0,
}
\]

with

\[
\lambda=19/503,
\]

where the analytic part of `Delta P` is expressed through

\[
\Omega-\rho.
\]

MATH-072 does **not** prove such an `H` exists.
It reduces the search space by showing which formerly separate variables are algebraically the same coordinate.

## 10. Regression audit

The companion exact-rational script checks every parity word through depth 16:

\[
\sum_{k=0}^{16}2^k=\boxed{131,071}
\]

words.

It verifies:

- `S = 1 + Sigma - rho`;
- `rho = 2^{-u} Omega`;
- both parity-step recurrences.

This regression supports implementation correctness; the universal identities above are algebraic and do not depend on the finite depth-16 check.

## 11. Claim boundary

MATH-072 proves only the coordinate identities above.
It does not prove:

- that `(S,rho,Omega)` alone is a closed finite state;
- that multiplicity is a Lyapunov function;
- that a Bellman potential exists;
- closure of `2<=r<=13`;
- first-cell emptiness;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math072_common_coordinate_bridge_certificate.py`

# MATH-074 — 3-adic carry envelope and dyadic-address duality

Date: 2026-09-12

Status: `EXACT COMPARISON-STATE REDUCTION / DEPTH-41 CENTRAL REGRESSION PASSED`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- Paid-count layers `r>=14` are already closed by MATH-071 and earlier certificates.
- This note does not close `2<=r<=13`.
- The purpose is to determine whether the MATH-051 bounded-carry state is genuinely new information or a finite-state representation of the common normalized-correction coordinate isolated in MATH-072.

## 1. Starting point

MATH-072 gives, at fixed `(k,d)` and therefore fixed `q=k-d` and fixed

\[
\rho=\frac{2^k}{3^q},
\]

that

\[
\boxed{\Delta S=\Delta\Sigma_d}.
\]

MATH-051 groups the fixed-d signature by cumulative odd-gap level `G`. If

\[
\Delta a_r
\]

denotes competitor block weight minus candidate block weight at gap level `r`, then

\[
\Delta\Sigma_d
=\sum_{r\ge0}\Delta a_r\left(\frac23\right)^r.
\]

The bounded-carry solver processes the gap levels from high to low with

\[
\boxed{
h_{r-1}=\frac{2(h_r+\Delta a_r)}3,
}
\]

requiring divisibility by 3 at every step.

## 2. Carry is scaled partial Delta-S

Suppose levels strictly above `r` have already been processed. Starting from zero carry at the highest gap, induction on the recurrence gives

\[
\boxed{
h_r
=\sum_{j>r}\Delta a_j\left(\frac23\right)^{j-r}.
}
\]

Multiplying by `(2/3)^r` yields

\[
\boxed{
\left(\frac23\right)^r h_r
=\sum_{j>r}\Delta a_j\left(\frac23\right)^j
=\Delta\Sigma_{>r}.
}
\]

Because `Delta S = Delta Sigma` at fixed `(k,d)`, this is equivalently

\[
\boxed{
\Delta S_{>r}=\left(\frac23\right)^r h_r.
}
\]

At the terminal level,

\[
\Delta a_0+h_0=\Delta\Sigma=\Delta S.
\]

Therefore the MATH-051 carry is not an independent absolute coordinate. It is an exact integer-state encoding of the already identified normalized-correction difference.

## 3. 3-adic carry / dyadic translation duality

Take two primitive competitor states at the same remaining level `r`, with the same remaining competitor-rank count `n_B`, and carries `h_1,h_2` satisfying

\[
 h_2-h_1=c3^r,
\qquad c>0.
\]

Then their already accumulated partial correction difference is

\[
\Delta S_{>r}^{(2)}-\Delta S_{>r}^{(1)}
=\left(\frac23\right)^r c3^r
=\boxed{c2^r}.
\]

Thus

\[
\boxed{
h_1\equiv h_2\pmod{3^r}
\iff
\Delta S_{>r}^{(1)}\equiv\Delta S_{>r}^{(2)}\pmod{2^r}
}
\]

within the matched fixed-layer comparison.

This is the direct bridge between the MATH-051 3-adic carry divisibility and the dyadic source/address resolution used in MATH-061--073.

## 4. Exact envelope lemma

Let the lower `r` gap-level choices be identical for the two primitive competitors above.

Because `h_2-h_1` is divisible by `3^r`, the first carry divisibility test is identical for both states. After one accepted transition,

\[
h_{r-1}^{(2)}-h_{r-1}^{(1)}
=2c3^{r-1}.
\]

After `j` matched lower-level transitions,

\[
\boxed{
h_{r-j}^{(2)}-h_{r-j}^{(1)}
=2^j c3^{r-j}.
}
\]

Hence every subsequent divisibility condition is identical. At the terminal level,

\[
\boxed{
h_0^{(2)}-h_0^{(1)}=2^r c>0.}
\]

The remaining competitor-rank count also evolves identically under the matched block choices because the two states start with the same `n_B`.

Therefore every future domination witness available to the smaller carry is also available to the larger carry, with strictly larger terminal translation credit.

So the smaller state may be discarded exactly.

## 5. Canonical 3-adic carry envelope

For a primitive competitor set `S` at remaining level `r`, define

\[
\boxed{
\mathcal E_r(n_B,\eta)
=
\max\{h:(n_B,h)\in S,\ h\equiv\eta\pmod{3^r}\}.
}
\]

Only nonempty classes are stored.

Replacing `S` by this envelope preserves the existential question

> does any competitor completion yield positive exact Hensel translation credit?

exactly.

The reduction is comparison-state canonicalization. It is not a statistical approximation and does not discard a unique future witness.

## 6. Relation to the source address

MATH-051 already established that exact Hensel translation at fixed `(k,d)` is integrality of `Delta Sigma`, hence by MATH-072 integrality of `Delta S`.

The present identity sharpens this at intermediate resolution:

\[
 h_2-h_1\in3^r\mathbb Z
\quad\Longleftrightarrow\quad
\Delta S_{>r}^{(2)}-\Delta S_{>r}^{(1)}\in2^r\mathbb Z.
\]

Since the normalized Hensel root/address is determined from `-S` in the dyadic modulus, an integer shift by a multiple of `2^r` leaves the lower `r` address bits unchanged.

Thus the 3-adic residue of the carry is the comparison-side representation of the same finite dyadic resolution that appears directly as source congruence in the paid-count certificates.

This is the first exact address bridge between the two formerly separate methods.

## 7. Depth-41 central regression

The companion solver is the MATH-051 fixed-d finite-state solver with the envelope canonicalization inserted after every primitive competitor transition.

The difficult depth-41 central layers reproduce the canonical dominated counts exactly:

| d | q | original `D_{41,d}` | envelope `D_{41,d}` |
|---:|---:|---:|---:|
| 12 | 29 | 361,499,293 | 361,499,293 |
| 13 | 28 | 586,723,760 | 586,723,760 |
| 14 | 27 | 703,863,494 | 703,863,494 |
| 15 | 26 | 355,002,462 | 355,002,462 |

The outer candidate subset-state peaks also remain exactly the canonical MATH-051 values:

\[
3227,\quad9835,\quad28455,\quad44095.
\]

But the maximum number of primitive competitor entries retained inside one subset state decreases:

| d | original max primitive entries | 3-adic envelope max |
|---:|---:|---:|
| 12 | 33 | 23 |
| 13 | 46 | 33 |
| 14 | 100 | 44 |
| 15 | 147 | 68 |

Cumulative primitive transition entries removed by the envelope during these runs were respectively

\[
1412,\quad7557,\quad37185,\quad109081.
\]

The exact dominated counts are the proof-facing regression target; the size reductions are implementation evidence only.

## 8. DSD interpretation

MATH-072 proposed a future state with an unresolved address-side coordinate `A`.

MATH-074 shows that, for fixed-depth Hensel comparison, the bounded carry is not an additional independent physical/analytic coordinate. Instead:

\[
\boxed{
\text{carry}
\longleftrightarrow
\text{scaled partial }\Delta S
\longleftrightarrow
\text{finite dyadic address resolution}.
}
\]

However one must retain the distinction between:

1. an **absolute path state**, such as `(S,rho,Omega,R)` in the Bellman calculation; and
2. a **comparison state**, such as `(n_A, n_B, h)` or its envelope, used to decide whether another path dominates the current path in the Hensel language.

The envelope is therefore an exact dominance filter, not by itself a scalar Bellman potential.

## 9. Consequence for the common-state search

The previous tentative coordinate

\[
(S,\rho,\Omega,\mathcal A)
\]

can now be refined conceptually.

The address-side information has two exact manifestations:

- absolute dyadic source-resolution height `R` from MATH-073;
- relative 3-adic carry envelope `E_r` from MATH-074.

They are linked by

\[
\boxed{
3^r\text{-carry congruence}
\leftrightarrow
2^r\text{-normalized-correction/address translation}.
}
\]

The next target is to determine whether the Bellman path state can use the absolute pair

\[
\boxed{(S,\rho,\Omega,R)}
\]

while the carry envelope is used only as an exact quotient/dominance operator on competing histories, rather than being promoted to another independent coordinate.

## 10. Claim boundary

Established:

- carry equals scaled partial `Delta S` at fixed `(k,d)`;
- equal carry residue modulo `3^r` corresponds to an integer `2^r` translation in the partial normalized correction;
- within equal `(n_B, h mod 3^r)`, only maximal `h` is future-relevant for existential Hensel domination;
- the canonical depth-41 central dominated counts survive this reduction exactly.

Not established:

- a depth-independent bound on envelope size;
- that `(S,rho,Omega,R)` is already a finite future-complete Bellman quotient;
- that the carry envelope is a Lyapunov function;
- the global `19/503` penalty bound;
- first-cell emptiness;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math074_3adic_carry_envelope.cpp`

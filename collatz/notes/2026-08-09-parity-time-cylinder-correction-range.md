# Exact correction range on parity-time cylinders

Date: 2026-08-09

Status: **DERIVED LEMMA + INDEPENDENT SMALL EXHAUSTIVE CHECK + FINITE CORE AUDIT**

This note distinguishes two objects that had been denoted informally by a common `B-core` language:

1. the first `B` **odd-position coordinates** of an odd-position vector;
2. the first `B` **time/parity bits** of the Collatz trace.

They are not the same object. A bound `x<2^B` is reconstructed by the second object, so finite-core candidate counting must use parity-time cylinders when that argument is invoked.

## 1. Fixed first-crossing layer

Fix total odd count `q` and

\[
\sigma=\lceil q\log_2 3\rceil,
\quad M=2^\sigma,
\quad P=3^q,
\quad D=M-P>0.
\]

For an admissible first-crossing word let the odd positions be

\[
d_0<\cdots<d_{q-1},
\]

with the standard first-crossing caps

\[
d_i\le\kappa_i:=\lfloor i\log_2 3\rfloor.
\]

Fix a parity-time prefix of length `B`, and let

\[
r=q_B
\]

be its number of odd steps. Then the prefix fixes all correction terms whose odd positions are `<B`. The unfixed odd indices are `i=r,...,q-1`.

## 2. Coordinatewise tail extrema

Every remaining odd position satisfies

\[
d_i\ge B+(i-r)
\]

by strict increase. The first-crossing cap gives

\[
d_i\le\kappa_i.
\]

For an extendable surviving parity prefix, both simultaneous extremal vectors are feasible:

\[
d_i^{\min}=B+(i-r),
\qquad
d_i^{\max}=\kappa_i.
\]

Since

\[
R=\sum_{i=0}^{q-1}3^{q-1-i}2^{d_i}
\]

is coordinatewise increasing, these give the exact minimum and maximum tail corrections within the fixed parity cylinder.

The minimum tail correction has the closed form

\[
\begin{aligned}
R_{\min}^{\rm tail}(B,r)
&=\sum_{i=r}^{q-1}3^{q-1-i}2^{B+i-r}\\
&=\boxed{2^B\left(3^{q-r}-2^{q-r}\right)}.
\end{aligned}
\]

The maximum is

\[
\boxed{
R_{\max}^{\rm tail}(r)
=\sum_{i=r}^{q-1}3^{q-1-i}2^{\kappa_i}.
}
\]

Therefore the exact correction variation in any extendable length-`B` parity cylinder with current odd count `r` is

\[
\boxed{
\Delta R_{B,r}
=
\sum_{i=r}^{q-1}3^{q-1-i}2^{\lfloor i\log_2 3\rfloor}
-
2^B\left(3^{q-r}-2^{q-r}\right).
}
\]

The value depends on `(B,r,q)` but not on the detailed pattern of the fixed parity prefix.

## 3. Parity-cylinder co-order lemma

Two completions of the same length-`B` parity prefix have identical canonical start modulo `2^B`, hence

\[
2^B\mid\Delta x.
\]

The same conclusion follows from the correction congruence because all unfixed correction terms are divisible by `2^B` and `P=3^q` is odd.

Thus distinct starts in the cylinder satisfy

\[
|\Delta x|\ge2^B.
\]

For the descent margin `z=x-y`,

\[
M\Delta z=D\Delta x-\Delta R.
\]

Because

\[
|\Delta R|\le\Delta R_{B,r},
\]

the exact sufficient condition

\[
\boxed{
D2^B>\Delta R_{B,r}
}
\]

implies

\[
\boxed{
\operatorname{sgn}(\Delta z)=\operatorname{sgn}(\Delta x)
}
\]

for every pair of completions in that parity-time cylinder.

This is a state-adaptive sharpening of the coarse condition

\[
D2^B>q3^{q-1}.
\]

## 4. Uniform parity-time buffer

Define

\[
\boxed{
B_{\rm time}(q)
=
\min\left\{B:\ D2^B>\Delta R_{B,r}\text{ for every extendable }r\right\}.
}
\]

Because `Delta R_{B,r}<q3^(q-1)`, the previous coarse logarithmic buffer remains a valid upper bound; this refinement cannot worsen the asymptotic core length.

Exact integer calculations give selected values:

| q | sigma | coarse B | exact parity-time B |
|---:|---:|---:|---:|
| 10 | 16 | 5 | 4 |
| 17 | 27 | 8 | 7 |
| 29 | 46 | 9 | 8 |
| 41 | 65 | 11 | 10 |
| 82 | 130 | 11 | 10 |
| 94 | 149 | 12 | 12 |
| 100 | 159 | 7 | 6 |
| 253 | 401 | 15 | 15 |
| 306 | 485 | 17 | 17 |
| 8,951 | 14,187 | 23 | 23 |
| 13,606 | 21,565 | 25 | 25 |
| 15,601 | 24,727 | 29 | 28 |
| 47,468 | 75,235 | 31 | 30 |
| 79,335 | 125,743 | 33 | 33 |

For `10<=q<=100`, the exact time-buffer is one bit shorter in 64 of the 91 layers and equal in the other 27 layers.

## 5. Candidate-count correction

The count of first `B` odd-position coordinate prefixes is not the number of length-`B` parity-time cylinders.

For a time buffer `B`, the relevant finite-core count is the number of coefficient-surviving parity words of length `B` that can extend to the fixed first-crossing layer.

Selected comparisons:

| q | time B | surviving parity-time cylinders |
|---:|---:|---:|
| 29 | 8 | 19 |
| 41 | 10 | 64 |
| 253 | 15 | 1,295 |
| 306 | 17 | 4,228 |
| 8,951 | 23 | 168,807 |
| 15,601 | 28 | 3,524,586 |
| 47,468 | 30 | 12,771,274 |
| 79,335 | 33 | 82,694,966 |

For example, an earlier diagnostic table lists 38,036,848,410 prefixes at `q=15,601`, `B=29`; that number belongs to an odd-position-coordinate prefix object. The actual parity-time survivor count at `B=29` is 6,385,637, and the exact range lemma reduces the uniform time buffer to `B=28`, where the count is 3,524,586.

Likewise, the earlier odd-position diagnostic at `q=79,335`, `B=33` is about `1.857e12`, whereas the length-33 parity-time survivor core contains 82,694,966 words.

The two counts answer different questions and should not be compared as if they were the same state space.

## 6. Independent checks

Python exhaustive enumeration checked the exact range formula for every first-crossing word for `2<=q<=8` and multiple prefix depths `B`; no mismatch occurred.

An independent Wolfram exhaustive check grouped the same small first-crossing words by their first `B` parity bits and verified

\[
\max R-\min R=\Delta R_{B,r}
\]

in every tested group; no mismatch occurred.

The larger selected buffer values above were computed by exact integer arithmetic. They are finite diagnostics, not asymptotic evidence.

## 7. Relation to the proof program

The correct finite-core distinction is now:

- **odd-position core**: useful for coordinatewise correction/defect analysis;
- **parity-time core**: useful for reconstructing an ordinary start below `2^B` and for finite-horizon min-plus/Bellman work.

The global first-crossing route should use the second object whenever a magnitude bound `x<2^B` is converted into a finite set of candidate starts.

This refinement does not solve the remaining global problem: one still needs a uniform exclusion showing that none of the growing logarithmic parity-time cores can realize arbitrarily large first-crossing counterexamples.
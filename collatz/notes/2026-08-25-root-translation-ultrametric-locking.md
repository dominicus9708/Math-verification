# Root-globalized neutral-excursion translation and ultrametric locking

Date: 2026-08-25

Status: **exact algebraic theorem + finite exhaustive regression certificate.**  This theorem identifies a genuine same-integer invariant across any concatenation of neutral relative-height excursions.  It does not exclude an open-positive tail that eventually never returns to relative height zero, and it is not a proof of the Collatz conjecture.

## 1. Setup

For a binary time-expanded parity word `w` of length `L` with `q` odd symbols, use

\[
T^L(n)=\frac{3^q n+R(w)}{2^L},
\]

where

\[
R(w)=\sum_{t=0}^{q-1}3^{q-1-t}2^{i_t}
\]

and `i_t` are the odd positions.

Fix a mechanical reference word `m` of the same length.  Assume

\[
h_k:=q_w(k)-q_m(k)\ge0
\]

at every prefix and

\[
h_L=0.
\]

Thus `w` and `m` have the same total odd count.

Partition the set where `w` differs from `m` into maximal positive excursions of `h`: excursion `j` begins at `a_j`, first differs at

\[
p_j=a_j,
\]

and returns to zero at `b_j`.  Put

\[
Q_j=q_w(b_j)=q_m(b_j).
\]

Let \(\Delta R_j\) be the correction difference of the two words restricted to `[a_j,b_j)`, but retaining the **absolute dyadic positions** `2^i`.

## 2. Exact correction decomposition

Because the actual and reference odd counts agree at every neutral return, the contribution of excursion `j` to the full correction difference receives exactly the suffix factor

\[
3^{q-Q_j}.
\]

Hence

\[
\boxed{
R(w)-R(m)=\sum_j3^{q-Q_j}\Delta R_j.
}
\]

The canonical starting residue for a length-`L`, weight-`q` word is

\[
n(w)\equiv-3^{-q}R(w)\pmod{2^L}.
\]

Therefore the same-integer/root-coordinate translation is

\[
\boxed{
D:=n(w)-n(m)
\equiv\sum_jD_j\pmod{2^L},
}
\]

with

\[
\boxed{
D_j:=-3^{-Q_j}\Delta R_j\pmod{2^L}.
}
\]

This formula is independent of every common suffix following a completed neutral excursion.

## 3. Exact dyadic valuation of one excursion

At the first changed position `p_j`, the two parity symbols differ.  The term of `Delta R_j` generated there is

\[
\pm 3^r2^{p_j}
\]

for some integer `r>=0`, whereas every later changed position contributes a multiple of

\[
2^{p_j+1}.
\]

Since `3^r` is odd,

\[
\boxed{
v_2(\Delta R_j)=p_j.
}
\]

Multiplication by the odd unit \(3^{-Q_j}\) does not change the dyadic valuation, so

\[
\boxed{
v_2(D_j)=p_j.
}
\]

The first-defect positions of successive neutral excursions satisfy

\[
p_1<p_2<\cdots<p_r.
\]

## 4. Ultrametric locking theorem

For a sum of 2-adic integers with pairwise strictly increasing valuations, the valuation of the sum is the smallest valuation.  Thus

\[
\boxed{
v_2(D)=p_1.
}
\]

More strongly, let

\[
D^{(j)}:=\sum_{i=1}^{j}D_i.
\]

Every later term \(D_i\), `i>=j+1`, is divisible by \(2^{p_{j+1}}\).  Hence

\[
\boxed{
D\equiv D^{(j)}\pmod{2^{p_{j+1}}}.
}
\]

Consequently a later neutral renewal can never repair or alter any lower dyadic bit already fixed before its own first defect.

This is the root-globalized form of the no-retroactive-repair principle.

## 5. Relation to the depth-28 audit

The exact depth-28 enumeration

`collatz/src/depth28_root_globalized_excursion_translation_certificate.py`

found all `118,265` nontrivial positive finite-return excursions against the current repeated H19 phase and verified:

- zero nontrivial root-globalized Hensel coincidences;
- `118,265` distinct canonical translations;
- \(v_2(D_j)=p_j\) in every case.

The present theorem explains these valuation observations algebraically and shows that the locking persists under an arbitrary concatenation of neutral excursions.

## 6. Independent finite regression

`collatz/src/root_translation_ultrametric_locking_certificate.py`

exhaustively checks every relative-nonnegative neutral word against the repeated H19 reference through length 14.  For every word it verifies:

1. the correction decomposition;
2. the root-coordinate translation sum;
3. \(v_2(D_j)=p_j\);
4. \(v_2(D)=p_1\);
5. the successive residue-lock congruences.

The theorem itself is algebraic; the finite enumeration is an implementation regression, not the proof.

## 7. What this removes from the remaining state

For a branch containing infinitely many finite neutral returns, the global first-defect channel cannot be forgotten after renewal normalization.  It is a permanent same-integer label.

A quotient state need not retain the full old parity prefix merely to remember its earliest dyadic mismatch.  It may instead retain, for suitable finite resolution,

\[
\boxed{
(p,\ D/2^p\bmod2^d,\ \text{renewal/height state}).
}
\]

For the current resonance, only the already surviving first-defect channels need be considered:

- current `m=44`: `p in {2,5,8,10,13,16}`;
- current `m=45`: `p in {2,5,8,10}`.

Later neutral excursions may refine higher bits of this translation label but cannot change the locked lower part.

## 8. Remaining fork

The theorem closes only the neutral-return side of the bookkeeping problem.  A hypothetical hard orbit may instead enter an **open-positive relative-height tail** that never returns to zero against the chosen mechanical reference.

Existing harmonic/state-escape results strongly constrain such a tail, but they do not currently exclude it.  Therefore the current global fork is

\[
\boxed{
\text{infinitely many neutral returns with ultrametric locking}
\quad\lor\quad
\text{eventually open-positive height}.
}
\]

The next closure calculation should treat these two branches separately rather than collapse them into one scalar renewal state.

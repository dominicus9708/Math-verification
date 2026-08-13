# Unit-residue predecessor-credit coverage and the U7 slack spectrum

Date: 2026-08-13

Status: **exact general counting lemma + exact finite U7 spectrum for slack 1 through 16**.  The theorem converts survival-state multiplicity into a lower bound for the fraction of orientations with a positive integer predecessor credit.  It is not an elimination theorem for every orientation and is not a proof of Collatz.

## 1. Fixed survival fibre

Fix a mechanical macroblock of length `L` with mechanical odd count `Q`.  For an integer incoming slack `h>=1`, consider the exact relative-state fibre

\[
\boxed{
\mathcal F_h
:=
\{w:(\Sigma(w),M(w))=(-h,-h)\}.
}
\]

Every orientation in this fibre has the same actual odd count

\[
\boxed{q=Q-h.}
\]

Starting the block with global Beatty slack at least `h`, every member is coefficient-surviving throughout the block and exits with `h` fewer units of slack.

For fixed `L,q`, the correction map `w -> R(w)` is injective.

## 2. Positive predecessor credit inside one residue class

Partition the fibre by

\[
R(w)\bmod3^q.
\]

In one occupied residue class, order the exact corrections

\[
R_1<R_2<\cdots<R_m.
\]

For every nonmaximal member,

\[
R_m-R_j=3^q\Delta_j
\]

with an integer \(\Delta_j>0\).  The higher-correction orientation starting from `x-Delta_j` reaches the same block endpoint as the lower-correction orientation starting from `x`.

Hence **exactly one orientation per occupied correction residue class can fail to have a positive same-fibre predecessor credit**: the maximum-correction representative.

## 3. Corrections occupy only 3-adic units

For `q>=1`, write the correction in ordered-one form

\[
R
=\sum_{j=1}^{q}2^{d_j}3^{q-j}.
\]

Modulo three, every term except the last vanishes, leaving

\[
R\equiv2^{d_q}\not\equiv0\pmod3.
\]

Therefore every correction is a unit modulo \(3^q\).  The number of possible occupied residue classes is at most

\[
\boxed{
\varphi(3^q)=2\cdot3^{q-1}.
}
\]

## 4. General coverage bound

Let

\[
F_h:=|\mathcal F_h|.
\]

Since at most one orientation per occupied unit residue can be credit-free,

\[
\boxed{
N_{\rm no\text{-}credit}
\le2\cdot3^{q-1}
}
\]

for `q>=1`.  Consequently

\[
\boxed{
\frac{N_{\rm positive\ credit}}{F_h}
\ge
1-\frac{2\cdot3^{q-1}}{F_h}.
}
\]

This uses only the survival-fibre multiplicity and does not require the correction residues to be enumerated.

## 5. General maximum-credit lower bound

The `F_h` orientations occupy at most

\[
2\cdot3^{q-1}
\]

residue classes.  Hence some class contains at least

\[
\left\lceil\frac{F_h}{2\cdot3^{q-1}}\right\rceil
\]

orientations.

Distinct corrections in one class differ by nonzero multiples of `3^q`; therefore the correction span in that class is at least

\[
\left(
\left\lceil\frac{F_h}{2\cdot3^{q-1}}\right\rceil-1
\right)3^q.
\]

Thus the available integer predecessor credit satisfies the purely multiplicity-based lower bound

\[
\boxed{
\Delta_{\max}
\ge
\left\lceil\frac{F_h}{2\cdot3^{q-1}}\right\rceil-1.
}
\]

Again, no correction enumeration is needed once `F_h` is known.

## 6. Exact U7 slack spectrum

For

\[
U_7=011011011010110110101101101,
\qquad(L,Q)=(27,17),
\]

the exact verifier gives:

\[
\boxed{
\begin{array}{c|r|r|r|r}
h&q&F_h&\text{occupied classes}&\Delta_{\max}\\\hline
1&16&4,717,204&2,994,059&19\\
2&15&8,592,795&3,388,771&59\\
3&14&12,032,438&2,260,388&167\\
4&13&13,716,208&1,001,830&481\\
5&12&13,050,437&353,924&1,377\\
6&11&10,490,228&118,098&4,011\\
7&10&7,156,370&39,366&11,027\\
8&9&4,142,481&13,122&29,025\\
9&8&2,026,638&4,374&78,886\\
10&7&831,657&1,458&203,915\\
11&6&282,891&486&546,214\\
12&5&78,386&162&1,376,523\\
13&4&17,248&54&3,080,998\\
14&3&2,900&18&7,145,845\\
15&2&350&6&13,048,945\\
16&1&27&2&22,369,621
\end{array}
}
\]

For every `h>=6`, the occupied-class count is exactly

\[
\boxed{2\cdot3^{q-1}},
\]

so every 3-adic unit residue modulo \(3^q\) occurs.

## 7. Exact positive-credit coverage

The corresponding exact positive-credit fractions begin

\[
36.53\%,\ 60.56\%,\ 81.21\%,\ 92.70\%,\ 97.29\%,\ 98.87\%,\ldots
\]

and remain above `99%` for much of the middle/high-slack range.  For example:

\[
\boxed{
h=12:\quad
78,224/78,386
\approx99.7933\%.
}
\]

The coverage drops again very near the degenerate endpoint `q=0` because the entire fibre itself becomes tiny; no monotonic infinite-scale conclusion is inferred from the finite table.

## 8. Headroom-scale observation

At an odd-event discrepancy corresponding to time-expanded slack `h`, the multiplicative orbit-state scale relative to the critical line is naturally of order

\[
2^{h/\log_3 2}=3^h.
\]

The exact U7 maximum-credit sequence

\[
19,59,167,481,1377,4011,11027,\ldots
\]

also grows on a roughly `3^h` finite scale.  This is a diagnostic observation, not an asymptotic theorem.  Its significance is that predecessor credits are not confined to polynomial growth in `h`; at finite Euclidean scale they live on the same exponential base as the natural orbit headroom.

## 9. Proof-program consequence

The coverage problem is now split into two parts:

1. **state multiplicity:** compute/lower-bound `F_h` by the Euclidean `(Sigma,M,multiplicity)` recursion;
2. **residue maximality:** the only potentially credit-free orientations are at most one maximum-correction representative per 3-adic unit residue.

Thus a future large-scale theorem need not classify every correction.  It is enough to show that the state-multiplicity growth forces the set of residue-maximal representatives to be incompatible with the critical R2 canonical-address constraints.

This turns the remaining coverage issue into a much smaller extremal-section problem rather than a full parity-language problem.

## 10. Verification

`collatz/src/u7_slack_credit_spectrum_certificate.cpp` recomputes the exact fibre counts, occupied residue counts, positive-credit counts, maximum credits, and the full-unit-residue property for `h=1,...,16` using integer arithmetic only.

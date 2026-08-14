# R1 hard-phase start alignment in the length-19 Euclidean quotient

Date: 2026-08-14

Status: **exact mechanical phase identification + finite neutral-Hensel audit in the current large-start regime**.  This explains why the low dyadic start address lies inside the locally most resistant length-19 phase sector.  It is a negative/structural result, not a Collatz proof.

## 1. Time-expanded Christoffel reference from odd-only valuations

Let

\[
\gamma:=\log_2 3.
\]

The odd-only mechanical valuation word is

\[
r_j^{\rm mech}
=
\lfloor(j+1)\gamma\rfloor-\lfloor j\gamma\rfloor
\in\{1,2\}.
\]

Convert it to the accelerated time-expanded parity word by writing one odd symbol followed by `r_j^mech-1` even symbols for each odd event.

The first nineteen time bits are exactly

\[
\boxed{
H_{19}=1101101101011011010.
}
\]

They contain twelve odd symbols.

The first four length-19 blocks are all identical:

\[
\boxed{
H_{19}H_{19}H_{19}H_{19}.
}
\]

Thus the first phase change occurs only after time bit

\[
\boxed{76.}
\]

## 2. Current ordinary-start address closes before the phase change

Every remaining member of the current `m=44` core obeys

\[
N<2^{73}.
\]

Hence a realized parity prefix of length 73 already fixes its canonical residue to the ordinary integer itself:

\[
\boxed{r_{73}=N.}
\]

Since

\[
73<76,
\]

the entire low dyadic address of the start is fixed before the mechanical length-19 phase changes even once.

Therefore the low-address problem is contained in four repetitions of the single factor `H_19` (with only the first sixteen bits of the fourth factor needed at resolution 73).

## 3. Neutral-fibre Hensel audit of `H_19`

Consider actual 19-bit orientations `v` relative to the mechanical factor `H_19` with

\[
(\Sigma,M)=(0,0).
\]

Equivalently, the relative odd-count path never drops below zero and returns to zero at the end.  There are exactly

\[
\boxed{2,652}
\]

such neutral orientations.

Apply the exact same-length/same-odd-count Hensel sibling-max integerization sieve in the current large-start regime.  Since `L=19`, the simple large-start condition needed to ignore additive threshold ambiguity is many orders of magnitude below the current `m=44` floor.

The exact result is

\[
\boxed{
2,652\text{ neutral orientations},
\qquad
0\text{ removed by the local neutral Hensel sieve}.
}
\]

Thus `H_19` is a locally Hensel-resistant neutral phase.

## 4. Length-19 phase corridor

Following the mechanical predecessor/rotation phase in successive 19-bit blocks gives long dwell runs.  Starting at the R1 reference phase, the successive phase factors with zero neutral-Hensel elimination occupy block indices

\[
\boxed{0,1,\ldots,33.}
\]

The first phase with a nonzero local neutral-Hensel removal fraction begins at block index

\[
\boxed{34.}
\]

Hence the locally resistant corridor extends through

\[
\boxed{34\cdot19=646}
\]

time bits before the first locally eliminative phase appears.

For orientation, the exact phase runs from the start are:

- the starting hard factor for 4 blocks;
- the next hard phase for 4 blocks;
- then hard-phase dwell lengths `5,4,5,4,3,5`;
- only after these 34 blocks does the neutral sibling-max sieve first remove any local orientations.

No multiplication of local removal percentages is asserted; local predecessor credits at an intermediate orbit state need not fall below the global minimal start.

## 5. Structural interpretation

The current R1 low-address obstruction is aligned with the worst local phase of the 19-bit Euclidean quotient:

\[
\boxed{
\text{ordinary address closes at bit }73
<
\text{first phase change at bit }76
<
\text{first locally eliminative phase at bit }646.
}
\]

This explains why shallow Hensel/predecessor filters can remove a large fraction of generic coefficient-surviving cylinders yet leave the isolated R1 branch structurally difficult.

The hard branch is not sampling phase space generically at its low dyadic boundary.  It begins in the phase sector where the neutral correction-collision mechanism is weakest.

## 6. Proof-program consequence

The next target should not be to iterate the same local neutral Hensel sieve more deeply inside this corridor.  The low address is already fixed before that mechanism becomes effective.

A successful argument must instead use at least one genuinely cross-scale condition:

1. the eventually-zero high dyadic lift of the same ordinary start;
2. the return to later Euclidean phases through the 81/82 and 13/14 gate hierarchy;
3. the global renewal-gap/headroom condition;
4. the ternary recursively-sufficient address.

The hard-phase alignment therefore acts as a precise stopping criterion for purely local-prefix elimination strategies.

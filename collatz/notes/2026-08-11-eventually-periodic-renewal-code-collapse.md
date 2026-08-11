# Eventually periodic renewal-code collapse

Date: 2026-08-11

Status: **exact consequence of the 2-adic parity conjugacy**. It removes eventually periodic renewal-code tails from the genuinely aperiodic hard core.

## 1. Parity conjugacy input

For the accelerated Collatz map `T` on `Z_2`, the parity-vector map is a bijective conjugacy with the 2-adic shift. Equivalently, an infinite parity word determines a unique 2-adic starting state.

If an infinite parity tail is periodic with period word `w` of accelerated length `A`, then shifting the parity sequence by `A` positions leaves it unchanged.

Injectivity of the parity conjugacy therefore gives

\[
\boxed{T^A(x)=x}
\]

for the 2-adic state `x` at the beginning of the periodic tail.

Thus an eventually periodic parity vector yields an eventually periodic `T`-orbit.

## 2. Renewal-code consequence

Each maximal renewal word is finite. If, after some renewal index, the sequence of renewal words repeats periodically,

\[
W_1,W_2,\ldots,W_s,
W_1,W_2,\ldots,W_s,\ldots,
\]

then their concatenated accelerated parity sequence is eventually periodic.

Therefore the positive-integer state at the beginning of that renewal-code period satisfies an exact iterate return and lies on an actual positive integer cycle.

Hence

\[
\boxed{
\text{eventually periodic renewal code}
\Longrightarrow
\text{periodic branch}.
}
\]

It cannot represent a genuinely aperiodic divergent renewal-floor counterexample.

## 3. Consequence for economical continued-fraction layers

The residual economical renewal language is organized by nearest critical layers and continued-fraction resonance classes.

A hypothetical aperiodic counterexample cannot simply reuse one fixed renewal word, or any fixed finite pattern of renewal words, forever. Such reuse would make the parity tail eventually periodic and collapse the trajectory into the periodic terminal branch.

Therefore the aperiodic hard core must keep generating genuinely new renewal-code information indefinitely.

This does not imply that the aggregate pairs `(H,D)` themselves must all be distinct; different exact words can share the same counts. The exclusion applies to eventual repetition of the exact finite renewal-word pattern.

## 4. Role

This theorem removes a natural synthetic countermodel in which one economical near-critical transition is repeated indefinitely.

The remaining aperiodic renewal chain must be both:

1. arithmetically economical enough to evade the established floor/depth costs; and
2. symbolically non-eventually-periodic at the exact renewal-word level.

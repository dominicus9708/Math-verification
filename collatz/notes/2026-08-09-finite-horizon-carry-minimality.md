# Minimality of the finite-horizon carry state

Date: 2026-08-09

Status: **DERIVED LEMMA FROM THE CLASSICAL PARITY-VECTOR BIJECTION**

This note asks whether the exact finite-horizon endpoint residue

\[
\eta=y\bmod2^m
\]

can be replaced by a strictly coarser deterministic state while preserving the canonical lift/carry behavior of **every** requested future parity suffix of length `m`.

For fixed current odd count `q`, the answer is no in general.

## 1. Carry-response map

Fix a depth `k`, odd count `q`, and remaining horizon `m`.
For each endpoint residue

\[
\eta\in\mathbb Z/2^m\mathbb Z,
\]

define its carry-response map

\[
\mathcal C_{q,\eta}:\{0,1\}^m\to\{0,1\}^m,
\]

which sends a requested future parity suffix

\[
b=(b_0,\ldots,b_{m-1})
\]

to the unique canonical lift-bit suffix

\[
c=(c_0,\ldots,c_{m-1})
\]

obtained from

\[
c_j=b_j\oplus(y_j\bmod2)
\]

with the appropriate canonical endpoint update.

## 2. Separation lemma

### Lemma

For fixed `q`, if

\[
\eta_1\not\equiv\eta_2\pmod{2^m},
\]

then

\[
\boxed{
\mathcal C_{q,\eta_1}
e\mathcal C_{q,\eta_2}.
}
\]

### Proof

Let

\[
b^*(\eta_1)
\]

be the actual length-`m` parity vector of an integer representative of `eta_1` under the accelerated Collatz map.

If this suffix is requested from the state with endpoint residue `eta_1`, no canonical lift is required at any of the `m` steps, because the requested parity always equals the actual parity.  Therefore

\[
\boxed{
\mathcal C_{q,\eta_1}(b^*(\eta_1))=0^m.
}
\]

Suppose the second endpoint residue also gave zero lift bits on the same requested suffix:

\[
\mathcal C_{q,\eta_2}(b^*(\eta_1))=0^m.
\]

Then `eta_2` itself would have exactly the same first `m` parity bits as `eta_1`.
But the classical parity-vector theorem states that length-`m` parity vectors are in bijection with residues modulo `2^m` for the accelerated map.  Hence

\[
\eta_2\equiv\eta_1\pmod{2^m},
\]

contradicting the assumption.

Therefore the carry-response maps are distinct.

## 3. Consequence

Among states with a fixed odd count `q`, the residue

\[
\boxed{\eta=y\bmod2^m}
\]

is a **minimal exact deterministic carry signature** in the following sense:

> no quotient that identifies two distinct realized `eta` classes can preserve the lift-bit response for every length-`m` future parity suffix.

This does not rule out objective-specific pruning.  A state may still be removed because another state has a smaller min-plus cost and provably dominates it on all coefficient-admissible continuations.
What it rules out is a further lossless compression based only on declaring distinct endpoint residues behaviorally equivalent.

## 4. Interpretation for the E/O matrix program

The exact target-specific hierarchy is therefore

\[
\boxed{
(k,q)
\longrightarrow
\eta=y\bmod2^{K-k}
\longrightarrow
D_k(q,\eta)=\min r.
}
\]

The two-dimensional E/O plane is the coarse base.
The low endpoint bits are an essential finite carry fiber.
The min-plus value is the optimization channel.

The earlier counterexamples to slack-only and endpoint-only dominance and the present minimality lemma together show that the arithmetic complexity cannot be removed merely by changing coordinates.
Any substantial further reduction must exploit **dominance, inequalities, arithmetic restrictions, interval certificates, or additional structure of the realized survivor subset**, rather than a pure deterministic state equivalence.

## 5. Literature positioning

The parity-vector bijection used in the proof is classical.  Terras' stopping-time framework encodes finite parity vectors by dyadic residue classes, and the Bernstein--Lagarias 2-adic conjugacy induces a permutation modulo `2^m` between residues and parity codes.

Accordingly, the novelty claimed here is only the consequence for the current finite-horizon canonical-lift quotient: `eta` is not merely sufficient but separates all deterministic carry-response classes at fixed `q`.

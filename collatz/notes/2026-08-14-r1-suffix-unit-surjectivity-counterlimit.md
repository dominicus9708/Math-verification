# R1 suffix-address unit surjectivity under the record constraint

Date: 2026-08-14

Status: **exact local realizability theorem / proof-strategy limitation**. It shows that the first-crossing record inequality by itself does not make the final odd-event suffix address sparse modulo powers of three. This does not construct a global Collatz counterexample; it identifies information that is insufficient for the R1 closure.

Use the current R1 first-crossing pair

\[
(A,H)
=(217,976,794,617,
137,528,045,312),
\]

and put

\[
\beta:=\log_2 3<2.
\]

For a backward suffix of `j` odd events, let

\[
S_j=v_{H-j}+\cdots+v_{H-1}
\]

be its accumulated binary exponent.

The first-crossing record condition before the endpoint is equivalent to

\[
\boxed{
S_j\ge
m_j:=A-\lfloor(H-j)\beta\rfloor.
}
\]

## 1. A coarse universal record envelope

Since

\[
A=\lceil H\beta\rceil<H\beta+1
\]

and

\[
\lfloor(H-j)\beta\rfloor>(H-j)\beta-1,
\]

we have

\[
m_j<j\beta+2<2j+2.
\]

Because `m_j` is an integer,

\[
\boxed{m_j\le2j+1\le3j}
\]

for every `j>=1`.

Thus any backward valuation suffix with

\[
\boxed{S_j\ge3j\quad\text{for all }j}
\]

automatically satisfies the R1 record lower envelope.

## 2. Reverse one-step unit construction

Fix any unit residue

\[
y\in(\mathbb Z/3^Q\mathbb Z)^\times.
\]

A reverse odd step has the form

\[
\boxed{x=\frac{2^v y-1}{3}.}
\]

For integrality one needs

\[
2^v y\equiv1\pmod3.
\]

Since `2 mod 3` has order two, this determines the parity of `v`.

Among the three exponents of that parity in

\[
\{1,2,3,4,5,6\},
\]

there is exactly one exponent class modulo six satisfying the stronger congruence

\[
2^v y\equiv1\pmod9.
\]

That one choice would make

\[
x\equiv0\pmod3.
\]

The other two choices produce a predecessor which remains a unit modulo three.

Choose the larger of those two good exponents. Then

\[
\boxed{3\le v\le6}
\]

and the predecessor is again a 3-adic unit.

## 3. Iteration through an arbitrary finite suffix depth

Repeat the construction at the new predecessor residue.

At every step:

- the division by three is integral;
- the predecessor remains a unit modulo three;
- the chosen valuation lies in `[3,6]`.

After `j` reverse odd steps,

\[
\boxed{3j\le S_j\le6j.}
\]

By Section 1,

\[
S_j\ge3j\ge m_j,
\]

so the whole suffix satisfies the current R1 record condition.

Therefore, for every `Q` and every unit endpoint residue

\[
y\pmod{3^Q},
\]

there exists a `Q`-odd valuation suffix satisfying the local R1 record inequalities and realizing that endpoint residue.

In particular, at the gap-localization depth used in the companion theorem,

\[
\boxed{
Q=22,
}
\]

the locally record-admissible endpoint-residue family is the full unit group

\[
\boxed{
(\mathbb Z/3^{22}\mathbb Z)^\times.
}
\]

## 4. Meaning for the gap-22 Cantor halving theorem

The companion gap theorem proved that **for one fixed final-22 suffix address** at most half of the low-22 ternary Cantor selectors can satisfy the small renewal-gap condition.

The present theorem shows that this fibrewise factor-two loss cannot be promoted to a global factor-two loss merely by counting record-admissible suffix residues: the record condition alone allows every unit residue.

Thus the following attempted inference is invalid:

\[
\text{R1 record}
\Rightarrow
\text{few final suffix residues}
\Rightarrow
\text{global Cantor halving}.
\]

The middle implication is false.

## 5. What additional channel is required

To make the gap-22 fibre contraction global, the suffix family must be restricted by information not contained in the coefficient record alone. Candidate sources already present in the proof architecture are

1. the phase-adaptive positive-backtrace/minimality filter;
2. the Christoffel defect budget and skew-height transition state;
3. the strengthened dyadic ordinary-start address;
4. a larger mixed-place state retaining both the suffix residue and the local defect cost.

This is a useful negative theorem: it prevents spending further effort on pure record-based suffix enumeration and identifies exactly which independent channel must be preserved in the next state compression.

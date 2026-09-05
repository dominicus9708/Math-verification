# Valuation-tuple macroblock compilation

Status: **EXACT / CLOSED as a transition-equivalence theorem**

## Purpose

The active source-family engine already supports exact one-odd-event valuation jumps

\[
0^{a_1}1,
\quad
0^{a_2}1,
\quad\ldots
\]

and a separate exact multibit source-channel transducer can consume any supplied fixed parity block.

This theorem identifies the exact equivalence between these two interfaces. It permits a finite future valuation-control tree to be compiled into fixed macroblocks without changing the represented source family.

It is a computation/representation theorem. It does not reduce the number of distinct source payloads by itself.

## 1. Valuation tuple and parity macroblock

Fix a tuple of nonnegative zero-run lengths

\[
\mathbf a=(a_1,\ldots,a_d),
\qquad a_i\ge0.
\]

Define its parity macroblock

\[
\boxed{
B(\mathbf a)
=0^{a_1}1\,0^{a_2}1\cdots0^{a_d}1.
}
\]

Then

\[
|B|=b=d+\sum_{i=1}^d a_i,
\qquad
q(B)=d.
\]

Let

\[
\gamma(\mathbf a):=C(B(\mathbf a)).
\]

This correction may be computed either directly from the one positions or recursively by block composition.

## 2. Exact source channel before the block

Suppose the current exact source/current-state channel is

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m.
\]

For the fixed block `B` of length `b`, one has

\[
2^bT^b(Y)=3^dY+\gamma,
\qquad Y=T^h(X).
\]

Substituting `Y=y+3^q m`,

\[
2^bT^b(Y)
=3^d y+\gamma+3^{q+d}m.
\]

Because `3^{q+d}` is odd, there is exactly one residue

\[
\boxed{
m\equiv m_0\pmod{2^b}}
\]

for which the supplied parity block is realized, namely

\[
\boxed{
m_0
\equiv
-\left(3^d y+\gamma\right)
\left(3^{q+d}\right)^{-1}
\pmod{2^b}.
}
\]

Write

\[
m=m_0+2^b k.
\]

Then the child source/current-state channel is

\[
\boxed{
X=r'+2^{h+b}k,
}
\]

with

\[
r'=r+2^h m_0,
\]

and

\[
\boxed{
T^{h+b}(X)=y'+3^{q+d}k,
}
\]

where

\[
y'
=
\frac{3^d y+\gamma+3^{q+d}m_0}{2^b}.
\]

This is exactly the existing multibit source-channel transition.

## 3. Equivalence with sequential valuation jumps

Assume the valuation-jump engine successively chooses

\[
a_1,a_2,\ldots,a_d.
\]

By definition, these choices force exactly the parity block

\[
B(\mathbf a).
\]

Each one-jump transition refines the current parameter by the unique residue required for the next block `0^{a_i}1`. Successive refinements therefore impose exactly the unique residue modulo

\[
2^{a_1+1}\cdots2^{a_d+1}=2^b
\]

that realizes the concatenated parity word.

The multibit equation above also has exactly one such residue modulo `2^b`. Hence the two residues are identical.

After the residue is fixed, both constructions describe the same ordinary integers `X` and apply the same deterministic accelerated Collatz map for `b` steps. Therefore their child source residue, child current-state offset, one-count, and parameter fiber are identical.

Thus

\[
\boxed{
\text{sequential valuation jumps along }\mathbf a
\equiv
\text{one multibit transition by }B(\mathbf a).
}
\]

The equivalence is exact, not asymptotic.

## 4. Interval consequence

If the parent parameter is restricted to an exact integer interval

\[
m_{lo}\le m\le m_{hi},
\]

then the macroblock child parameter interval is

\[
\boxed{
\left\lceil\frac{m_{lo}-m_0}{2^b}\right\rceil
\le k\le
\left\lfloor\frac{m_{hi}-m_0}{2^b}\right\rfloor.
}
\]

This is exactly the interval obtained after composing the `d` sequential valuation-jump interval refinements.

## 5. Ballot-control consequence

For a fixed absolute entrance depth and incoming surplus, legality of the compiled block is exactly the legality of its expanded parity word. Therefore a finite future valuation-control signature may precompute its legal valuation tuples and emit the corresponding macroblocks.

The source payload is still evaluated independently for each emitted block through the unique congruence above.

In particular, the previously observed four-future-jump ballot-control signatures may be compiled into exact four-one-event macroblock templates.

## 6. DSD interpretation

This theorem separates two levels:

- **control compilation:** many bitwise transition instructions can be replaced by one certified macroblock instruction;
- **source equivalence:** remains separate and is not implied by sharing the same control or macroblock template.

Therefore macroblock compilation can reduce transition overhead and expose block-level predicates without silently merging different source addresses.

## Scope restrictions

This theorem does **not** prove:

- that two different valuation tuples have the same source realization set;
- that different source cylinders sharing one control signature may be merged;
- that a finite set of macroblocks covers all future Route-B behavior uniformly at arbitrary horizon;
- any Christoffel equality assumption;
- checkpoint or tail closure;
- Collatz.

## Certificate

- `../src/A0_s1_valuation_macroblock_compilation_certificate.py`

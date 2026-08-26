# First resonance: 21-run Stern-Brocot macro grammar

Date: 2026-08-26

Status: **exact structural compression** of the repaired first-resonance mechanical gap word.  It changes the representation of the Bellman input word; it is not by itself a Collatz proof.

## 1. From 72 billion letters to a Farey grammar

The first-resonance mechanical gap-2 indicator is the anchored lower Christoffel word of slope

\[
\frac{P}{Q}
=
\frac{42150895613}{72057431991}.
\]

The previous exact certificate represented this word by 138 distinct Farey/Christoffel DAG nodes.

The same construction can be viewed as a Stern-Brocot search between the boundary fractions

\[
\frac01,\qquad\frac11.
\]

At each step the mediant word is the ordered concatenation

\[
W_M=W_LW_R.
\]

If the target lies to the right, update

\[
L\leftarrow M,
\qquad
W_L\leftarrow W_LW_R.
\]

If the target lies to the left, update

\[
R\leftarrow M,
\qquad
W_R\leftarrow W_LW_R.
\]

The target is reached after 135 individual mediant moves.

## 2. Group equal directions

Repeated moves in the same direction have closed forms.

For `a` consecutive right moves,

\[
\boxed{W_L\leftarrow W_LW_R^a.}
\]

For `a` consecutive left moves,

\[
\boxed{W_R\leftarrow W_L^aW_R.}
\]

The entire 135-move path groups into exactly 21 runs:

```text
R^1 L^2 R^2 L^3 R^1 L^5 R^2 L^23 R^2 L^2 R^1 L^1
R^55 L^1 R^4 L^3 R^1 L^1 R^15 L^1 R^9
```

The largest exponent is only

\[
\boxed{55}.
\]

After these 21 macro updates, the final target word is

\[
\boxed{W=W_LW_R}
\]

with exactly

\[
|W|=Q=72057431991,
\qquad
\#1(W)=P=42150895613.
\]

## 3. Euclidean checksum

The Euclidean partial quotients for `Q/P` are

\[
(1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,10).
\]

There are 22 partial quotients and their sum is 137.  The final Stern-Brocot endpoint adjustment turns this into the 135 explicit moves and 21 direction-runs above.

This is an independent arithmetic checksum of the macro grammar.

## 4. Bellman consequence

Let `\star` denote exact two-boundary min-plus block composition.  The previous 138-node representation gave a finite recursive operator DAG.  The macro grammar strengthens the implementation form:

- an `R^a` macro requires the operator of `W_R` raised to the `a`-fold min-plus power and composed with `W_L`;
- an `L^a` macro does the symmetric update;
- only 21 macro updates are needed;
- each power has exponent at most 55.

Thus the first-resonance mechanical input has now been compressed through the hierarchy

\[
\boxed{
72057431991\text{ gap letters}
\to
138\text{ distinct Farey nodes}
\to
21\text{ Stern-Brocot macro runs}.}
\]

The remaining difficulty is not word length.  It is the interface state carried by each block operator: Hensel alignment, displacement debt, and correction cost.

## 5. DSD interpretation

This is a direct DSD-style reduction of description complexity without loss of arithmetic content:

\[
\text{individual orbit events}
\to
\text{repeated structural blocks}
\to
\text{macro transition grammar}.
\]

The reduction is exact.  No probabilistic independence, asymptotic replacement, or word rotation is used.

Companion certificate:

`collatz/src/first_resonance_stern_brocot_macro_grammar_certificate.py`.

# Common-`OO` alternate-preimage sieve inside the ternary core

Date: 2026-08-12

Status: **exact finite 3-adic alternate-preimage sieve for the already verified-floor minimal-counterexample search**. It strictly strengthens the direct reverse-ancestor sieve and removes `8608/2^18 = 3.28369140625%` of the depth-18 ternary `0/1` cylinders. The additive constant is audited explicitly; the elimination is rigorous above the existing verified floor. This does not prove Collatz.

## 1. Universal `OO` prefix of the ternary core

Write an Ansari-core integer as

\[
\boxed{n=4S+3.}
\]

For every integer `S>=0`, the first two accelerated Collatz parity symbols are odd:

\[
T(n)=6S+5,
\]

and

\[
\boxed{T^2(n)=9S+8.}
\]

Thus every member of the ternary `0/1` core shares the exact forward prefix

\[
\boxed{OO.}
\]

In base three, the descendant

\[
y:=9S+8
\]

has the two fixed least-significant trits `22`, while its higher trits are precisely the trits of `S`.

This makes `y` a particularly natural endpoint for an aligned 3-adic reverse search.

## 2. Alternate preimages of the common descendant

Let a reverse word ending at `y` contain `q` inverse-odd steps and `E` additional inverse-even doublings. Its total forward length is

\[
k=q+E.
\]

The corresponding ancestor has leading multiplicative factor

\[
\frac{2^k}{3^q}
\]

relative to `y`.

But

\[
y=T^2(n)
=\frac{9n+5}{4}.
\]

Therefore the multiplicative factor relative to the original `n` is

\[
\boxed{
\lambda
=\frac{2^{k-2}}{3^{q-2}}.
}
\]

A strict multiplicative contraction relative to `n` occurs exactly when

\[
\boxed{
2^{k-2}<3^{q-2}.
}
\]

Since `k=q+E`, this is equivalent to

\[
\boxed{
2^{(q-2)+E}<3^{q-2}.
}
\]

Thus the same integer contraction budget used in the direct reverse sieve reappears, shifted by the two universal odd steps.

## 3. Additive-constant audit

The forward `OO` map is

\[
y=\frac{9n+5}{4}.
\]

If an alternate reverse word has correction numerator `R_w`, then

\[
m
=\frac{2^k y-R_w}{3^q}
=\lambda n+C,
\]

where

\[
\boxed{
C
=\frac{5\,2^{k-2}-R_w}{3^q}.
}
\]

Because `R_w>0`,

\[
C<\frac{5\,2^{k-2}}{3^q}.
\]

Write

\[
q'=q-2,
\qquad
k'=k-2,
\]

so that `2^{k'}<3^{q'}`. Then

\[
1-\lambda
=
\frac{3^{q'}-2^{k'}}{3^{q'}}.
\]

Since the numerator is a positive integer,

\[
3^{q'}-2^{k'}\ge1.
\]

Hence a sufficient threshold for `m<n` is

\[
\begin{aligned}
n
&>\frac{C}{1-\lambda}\\
&<
\frac{5\,2^{k'}}{9\left(3^{q'}-2^{k'}\right)}\\
&<\boxed{\frac59\,3^{q'}.}
\end{aligned}
\]

In the depth-18 computation below, `q'<=18`, so every threshold is smaller than

\[
\boxed{
\frac59\,3^{18}
=215,233,605.
}
\]

Therefore every such endpoint cylinder above the already published/recursively extended verification floor is rigorously recursive: its alternate ancestor is a positive integer strictly smaller than the endpoint.

This threshold audit is important. The coefficient inequality alone should not be presented as a global all-positive-integers statement without controlling `C`.

## 4. Exact finite 3-adic DP

A ternary core prefix of depth `d` fixes

\[
S\pmod{3^d}.
\]

The common descendant

\[
y=9S+8
\]

is therefore fixed modulo

\[
3^{d+2}.
\]

Starting from this residue, apply the reverse-cycle transition

\[
\boxed{
y\mapsto\frac{2^{e+1}y-1}{3}}
\]

whenever the numerator is divisible by three.

As in the direct reverse sieve:

- `y=0 mod3` has no inverse-odd continuation;
- `y=2 mod3` permits even `e`;
- `y=1 mod3` permits odd `e`;
- after each inverse-odd division, the required 3-adic precision decreases by one digit;
- for a fixed remaining residue, only the least accumulated `E` needs to be retained.

At reverse odd-depth `q`, a candidate is accepted as a contracted alternate ancestor precisely when

\[
2^{(q-2)+E}<3^{q-2}.
\]

All operations can therefore be performed with exact integers.

## 5. Minimal forbidden ternary cylinders through depth 18

Intersect the exact alternate-preimage DP with the ternary `0/1` prefixes of `S`.

The new prefix-minimal forbidden cylinders occur at the following depths:

\[
\boxed{
\begin{array}{c|r}
d&\text{new minimal forbidden cylinders}\\\hline
7&2\\
9&2\\
11&5\\
12&24\\
14&42\\
16&104\\
18&224
\end{array}
}
\]

There are no new prefix-minimal cylinders at the intervening depths through `18`.

Consequently the exact fraction of depth-18 ternary `0/1` cylinders removed is

\[
\boxed{
\frac{8608}{262144}
=0.0328369140625.
}
\]

Thus this sieve eliminates

\[
\boxed{3.28369140625\%}
\]

of the depth-18 Ansari core from the current minimal-counterexample search.

## 6. Relation to the direct reverse-ancestor sieve

The earlier direct sieve searched for a smaller ancestor that maps to `n` itself.

Every such ancestor also maps, after the universal `OO` suffix, to

\[
T^2(n)=9S+8.
\]

Therefore the direct reverse sieve must be contained in the common-`OO` alternate-preimage sieve.

The exact depth-18 calculation confirms this containment:

\[
\boxed{
3665\text{ direct-forbidden cylinders}
\subset
8608\text{ common-OO-forbidden cylinders}.}
\]

Hence the `3.2837%` figure supersedes the earlier `1.3981%` direct-sieve figure for the present verified-floor minimal-counterexample core.

## 7. Example of a new cylinder

At depth seven, the common-`OO` sieve removes two ternary prefixes rather than the one removed by the direct sieve.

In low-to-high `(a_0,...,a_6)` notation they are

\[
\boxed{(0,0,0,1,0,0,0)}
\]

and

\[
\boxed{(1,1,0,0,0,1,0).}
\]

The second is the previously found direct ancestor cylinder; the first is genuinely new and exists only because a smaller integer may merge with the orbit at the common descendant rather than at the original start itself.

This is the essential strengthening:

\[
\boxed{
\text{smaller ancestor of a descendant}
\quad\text{is strictly more flexible than}\quad
\text{smaller ancestor of the start}.}
\]

## 8. Recursively sufficient interpretation

Let `R_18^{OO}` be the union of the certified common-`OO` alternate-preimage cylinders above the small explicit threshold from Section 3.

Every member of this union above the threshold is recursive. Every member below the threshold is already inside the established verified interval and therefore converges, hence is recursive as well (except the trivial `n=1`, which is irrelevant to the present core and may be added to the retained set explicitly).

Accordingly one can form a recursively sufficient complement and intersect it with Ansari's `F`.

For the present proof program, the operational statement is simpler:

> a hypothetical minimal counterexample above the current verified floor must avoid all `8608` forbidden depth-18 extensions.

This restriction applies before any R1/R2 split.

## 9. Strategic role for the m=44 bootstrap block

The `m=44` block contains 44 free ternary `0/1` choices. A depth-18 cylinder restriction therefore eliminates entire families of

\[
2^{44-18}
\]

block members at once.

The current `3.2837%` elimination is not remotely sufficient by itself to close the block, but it proves that the ternary Cantor intersection can be refined by an aligned 3-adic finite automaton without enumerating `2^44` integers.

The next target is the entropy/rate of this alternate-preimage subshift under increasing reverse depth and, more strongly, the effect of allowing alternate preimages of longer common/conditioned forward descendants.

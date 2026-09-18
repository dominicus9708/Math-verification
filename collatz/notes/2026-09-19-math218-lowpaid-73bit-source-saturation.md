# MATH-218 — 73-bit source saturation for the remaining r=2..10 singleton corridor

Date: 2026-09-19

Status: EXACT SYMBOLIC-SOURCE SATURATION / NO AP ENUMERATION / r=10 OPEN

## 1. Purpose

MATH-217 shows that after at most one Bellman-dangerous multi-source handoff, the remaining low-paid hard core is permanently singleton.

At a singleton boundary, an emitted paid count r can be Bellman-dangerous only when MATH-202's overshoot threshold is met:

\[
L\ge z_{\min}(r).
\]

The following paid first-return cluster has local shortcut length

\[
h_r
=
r+1+m(r)+\mathbf 1_{\{\varpi\le\tau_r\}},
\qquad
m(r)=\lfloor r\log_2(3/2)\rfloor.
\]

Therefore every dangerous full boundary macro has length

\[
H=L+h_r
\]

at least

\[
\boxed{
W(r):=
z_{\min}(r)+r+1+m(r).
}
\]

This note uses the ordinary first-cell boundary-anchor ceiling to turn that accumulated parity length into exact source recovery.

## 2. Minimum dangerous full-macro lengths

For the unresolved paid counts \(2\le r\le10\):

| r | \(z_{\min}(r)\) | \(m(r)\) | \(h_{\min}(r)\) | \(W(r)\) |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 4 | 5 |
| 3 | 2 | 1 | 5 | 7 |
| 4 | 3 | 2 | 7 | 10 |
| 5 | 6 | 2 | 8 | 14 |
| 6 | 7 | 3 | 10 | 17 |
| 7 | 8 | 4 | 12 | 20 |
| 8 | 10 | 4 | 13 | 23 |
| 9 | 11 | 5 | 15 | 26 |
| 10 | 13 | 5 | 16 | 29 |

Thus a dangerous r=10 macro contributes at least

\[
\boxed{29}
\]

actual shortcut parity bits.

## 3. Parity-vector source residue

For any shortcut parity prefix of total length \(K\), odd count \(Q\), and correction \(C_K\),

\[
T^K(Y)
=
\frac{3^QY+C_K}{2^K}.
\]

The prefix determines the unique source residue

\[
\boxed{
A_K
\equiv
-C_K3^{-Q}
\pmod{2^K},
\qquad
0\le A_K<2^K.
}
\]

An ordinary integer realizes that parity prefix iff

\[
Y\equiv A_K\pmod{2^K}.
\]

## 4. First-cell boundary-anchor ceiling

MATH-057 proves that every coefficient-surviving \(u=0\) boundary anchor in the current first-cell scope satisfies

\[
\boxed{0<Y<2^{73}}.
\]

Therefore once

\[
K\ge73,
\]

the congruence

\[
Y\equiv A_K\pmod{2^K}
\]

has at most one positive solution below \(2^{73}\).

In fact:

\[
\boxed{
0<Y<2^{73},\ K\ge73
\Longrightarrow
Y=A_K
}
\]

whenever the parity prefix is realizable.

So after 73 accumulated parity bits there is no unresolved ordinary-source parameter at all.

## 5. Weighted macro saturation

For a dangerous singleton macro sequence with emitted tags

\[
r_1,\ldots,r_n\in\{2,\ldots,10\},
\]

the accumulated shortcut length satisfies

\[
K_n
\ge
\sum_{i=1}^{n}W(r_i).
\]

Hence exact source recovery is guaranteed as soon as

\[
\boxed{
\sum_i W(r_i)\ge73.
}
\]

This is the weighted saturation criterion.

No source APs, source integers, or depth intervals are enumerated.

## 6. Uniform macro-count bounds

The worst unresolved tag is \(r=2\), with

\[
W(2)=5.
\]

Therefore any dangerous low-paid singleton chain saturates its ordinary source after at most

\[
\boxed{
\left\lceil\frac{73}{5}\right\rceil=15
}
\]

macros.

Tag-specific bounds are:

| repeated tag | maximum macros needed to reach source saturation |
|---:|---:|
| r=2 | 15 |
| r=3 | 11 |
| r=4 | 8 |
| r=5 | 6 |
| r=6 | 5 |
| r=7 | 4 |
| r=8 | 4 |
| r=9 | 3 |
| r=10 | 3 |

In particular,

\[
\boxed{
3\text{ dangerous }r=10\text{ macros}
\Longrightarrow
K\ge87>73
}
\]

and the boundary source is exactly the canonical residue of that symbolic parity history.

The three r=10 macros need not be adjacent in shortcut time; intervening dangerous macros only increase the accumulated parity length.

## 7. Exact hard-window gate after saturation

The published verified floor is at least

\[
B_{\rm pub}=2^{71},
\]

and MATH-057 supplies the sharper boundary-anchor upper bound

\[
Y
<
2\left(1364\cdot2^{61}+\frac{q_0}{3}\right)
<2^{73}.
\]

Once \(K\ge73\), the hard symbolic state therefore survives only if its exact canonical residue satisfies

\[
\boxed{
B_{\rm pub}<A_K<Y_{\max}.
}
\]

If \(A_K\le B_{\rm pub}\), the represented boundary anchor is already in the verified region.

If \(A_K\ge Y_{\max}\), no current first-cell boundary anchor realizes the symbolic history.

Thus source recovery is immediately followed by one exact integer interval test.

A stronger external verified floor may be substituted without changing the theorem.

## 8. Consequence for r=10

The r=10 closure problem no longer contains an indefinitely unresolved integer source.

After singletonization:

1. one dangerous r=10 macro consumes at least 29 parity bits;
2. a second consumes at least another 29;
3. a third forces total depth at least 87 and therefore identifies the source integer exactly.

So every hypothetical long r=10 hard lineage reaches an exact-source terminal gate after at most three r=10 danger tags.

What remains is to show that every reachable 73-bit-saturated symbolic state either

- lies outside the hard anchor interval;
- is Hensel/Pareto dominated under the synchronized origin;
- or has a certified descent to the verified floor.

## 9. Relation to the project goal

This replaces the old architecture

\[
\text{278,725 cylinders}\to\text{128 shards}\to\text{billions of AP members}
\]

by

\[
\boxed{
\text{one common recurrence}
\to
\text{emitted }r
\to
\text{weighted bit budget}
\to
\text{exact source recovery at 73 bits}.
}
\]

The depth coordinate is accumulated algebraically; it is not scanned as an outer loop.

## 10. Claim boundary

Established:

- exact minimum dangerous full-macro bit contribution \(W(r)\);
- exact 73-bit source-saturation theorem;
- at most 15 dangerous low-paid macros before exact source recovery;
- at most 3 dangerous r=10 macros before exact source recovery;
- exact post-saturation hard-window gate.

Not established:

- emptiness of all saturated symbolic states;
- closure of r=10;
- closure of lower paid tags;
- first-cell emptiness;
- the Collatz conjecture.

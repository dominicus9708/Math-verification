# Bounded-record terminal Haar contraction

Date: 2026-08-22

Status: **exact local Fourier contraction for every non-singleton record macro, with an effective uniform constant under any fixed record-length bound.** This is not yet the repeated selector/Hensel splice and not a proof of the Collatz conjecture.

Let

\[
d_1\cdots d_L
\]

be the mechanical Beatty word of a record first-passage macro. As in the singleton classification note, the final mechanical bit is necessarily

\[
d_L=0.
\]

A non-singleton record macro is characterized by the fact that the prefix

\[
d_1\cdots d_{L-1}
\]

contains at least one occurrence of \(10\).

## 1. The rightmost descent forces one of two terminal mechanical tails

Choose the rightmost \(10\) in the prefix. After its zero there is no later \(10\).

The mechanical word contains no \(00\), so after that zero the next bit, if any, is one.

It also contains no \(111\), so there can be at most two consecutive ones before the final zero \(d_L=0\).

Moreover \(d_{L-1}=1\), again because \(00\) is forbidden.

Therefore every non-singleton record macro ends in exactly one of

\[
\boxed{1010}
\]

or

\[
\boxed{10110}.
\]

No other terminal mechanical pattern is possible.

## 2. Only deficits zero and one can reach the record exit

Use the deficit coordinate

\[
y=D-q\ge0
\]

immediately before the terminal tail.

For the tail \(1010\), the mechanical tail has length four and contains two ones. To finish with record surplus \(+1\), an incoming deficit \(y\) requires

\[
2+y+1=3+y
\]

actual odd bits among four positions. Hence \(y\le1\).

For \(10110\), the mechanical tail has length five and contains three ones, so the required number is

\[
3+y+1=4+y
\]

among five positions, again forcing \(y\le1\).

Thus all prefix mass at deficits \(y\ge2\) is irrelevant to the record exit.

Let

\[
A=f(0),
\qquad
B=f(1)
\]

be the numbers of valid prefixes arriving at the beginning of the terminal tail with deficits zero and one.

## 3. Exact terminal completions

A direct four- or five-step calculation gives:

### Mechanical tail 1010

From \(y=0\), the two and only two valid record-exit parity suffixes are

\[
0111,
\qquad
1011.
\]

From \(y=1\), the unique valid suffix is

\[
1111.
\]

### Mechanical tail 10110

From \(y=0\), the two and only two valid suffixes are

\[
01111,
\qquad
10111.
\]

From \(y=1\), the unique valid suffix is

\[
11111.
\]

Consequently every non-singleton record language has exact size

\[
\boxed{
|\mathcal R|=2A+B.
}
\]

The positivity \(A\ge1\) follows from the mechanical boundary prefix itself.

## 4. Exact Haar cancellation at the first terminal-tail bit

The two \(y=0\) suffixes have a common prefix before the first terminal-tail bit and differ in that critical parity bit.

By the triangular parity-residue correspondence, their canonical dyadic residues differ by exactly one half-period at the corresponding Fourier shell. Therefore their character values are opposite.

For every one of the \(A\) prefixes at deficit zero, the two suffix contributions cancel exactly.

The \(B\) deficit-one prefixes have only one completion each, so their total Fourier contribution has absolute value at most \(B\).

Thus at the dyadic shell whose critical bit is the first bit of the terminal \(1010\) or \(10110\) tail,

\[
\boxed{
|\widehat\mu(t)|
\le
\frac{B}{2A+B}
<1.
}
\]

This is an exact local contraction for every non-singleton record macro. It needs no asymptotic mixing theorem.

## 5. Fixed record-length bound gives a uniform constant

Assume now that all record lengths in a tail satisfy

\[
L\le M
\]

for some fixed \(M\).

For each \(L\le M\), the irrational Beatty/Sturmian mechanical word has only finitely many length-\(L\) factors (in fact \(L+1\)). Therefore there are only finitely many non-singleton terminal configurations and finitely many ratios

\[
\frac{B}{2A+B}.
\]

Define

\[
\boxed{
\kappa_M
:=
\max_{\substack{L\le M\\\text{non-singleton factors}}}
\frac{B}{2A+B}.
}
\]

Since every factor in the maximum has \(A\ge1\), each ratio is strictly below one, and the maximum is finite. Hence

\[
\boxed{
\kappa_M<1.
}
\]

Thus every non-singleton record macro in a bounded-record tail supplies a fresh fine dyadic shell with a phase-uniform contraction by at least the orbit-independent factor \(\kappa_M\) once \(M\) is fixed.

The constant is effective: enumerate the \(L+1\) Sturmian factors at each \(L\le M\), propagate the two endpoint prefix counts \(A,B\), and take the finite maximum.

## 6. Exact finite calibration

The companion certificate enumerates all mechanical factor types through \(M=50\) and gives:

\[
\begin{array}{c|c}
M&\kappa_M\\\hline
5&1/3\\
10&0.5333333333\ldots\\
20&0.6181204053\ldots\\
30&0.6440790838\ldots\\
50&0.6605711777\ldots
\end{array}
\]

For \(M=50\), the worst checked factor occurs at \(L=49\), with

\[
A=84\,141\,805\,077,
\qquad
B=327\,501\,070\,154,
\]

so

\[
\frac{B}{2A+B}
\approx0.6605711776946074.
\]

These numerical values are finite calibrations only. The all-\(M\) theorem needed here is simply the exact finite-set statement \(\kappa_M<1\) for every fixed \(M\).

## 7. Revised bounded-record bridge

Combining with the singleton theorem:

1. an infinite bounded-record tail contains infinitely many non-singleton macros;
2. every such macro carries a fresh terminal Haar shell with contraction at most \(\kappa_M<1\);
3. singleton stretches between them are all-odd stretches after at most one initial bit and have length \(O_N(r)\) at record height \(r\).

Therefore the bounded-record obstruction has been reduced to one remaining global statement:

> **Repeated fresh-shell selector/Hensel theorem.** Show that the ternary selector / ordinary-integer Hensel state cannot remain concentrated along an infinite sequence of fresh dyadic shells on which the record side has contraction at most \(\kappa_M<1\), even when those shells are separated by long all-odd singleton stretches.

This is now substantially narrower than an arbitrary bounded-macro cross-base problem.

Companion certificate:

`collatz/src/bounded_record_terminal_haar_certificate.py`.

# Two-coordinate affine duality for Collatz prefix classes

Date: 2026-08-11

Status: **exact normalized prefix dynamics + dual formation/survival interpretation**. This note further compresses the four-attribute state. It does not prove the remaining universal boundary-crossing theorem.

## 1. Normalized coefficient and correction

For a realizable accelerated Collatz prefix of length \(k\), write

\[
T^k(n)=\frac{3^q n+R}{2^k}.
\]

Define

\[
\boxed{
a:=\frac{3^q}{2^k}}
\]

and

\[
\boxed{
c:=\frac{R}{3^q}.}
\]

Then the entire affine prefix map becomes

\[
\boxed{
T^k(n)=a(n+c).
}
\]

Because the numerator of \(a\) is a power of 3 and its denominator is a power of 2, the fraction is already reduced and

\[
\boxed{\operatorname{den}(a)=2^k.}
\]

Thus the depth \(k\) is encoded in \(a\) and need not be stored separately in an exact rational implementation.

---

## 2. Exact branch dynamics

Extend the parity prefix by \(p\in\{0,1\}\).

### Even extension

\[
T^{k+1}(n)=\frac12T^k(n),
\]

so

\[
\boxed{
a'=\frac a2,}
\qquad
\boxed{c'=c.}
\]

### Odd extension

\[
T^{k+1}(n)=\frac{3T^k(n)+1}{2}.
\]

Therefore

\[
\begin{aligned}
T^{k+1}(n)
&=\frac{3a(n+c)+1}{2}\\
&=\frac{3a}{2}
\left(n+c+\frac1{3a}\right),
\end{aligned}
\]

and hence

\[
\boxed{
a'=\frac{3a}{2},}
\qquad
\boxed{
c'=c+\frac1{3a}.}
\]

Thus the exact prefix dynamics on \((a,c)\) is the fixed two-branch system

\[
\boxed{
(a,c)\mapsto
\begin{cases}
(a/2,c),&p=0,\\
(3a/2,c+1/(3a)),&p=1.
\end{cases}
}
\]

It is independent of the numerical magnitude of the starting integer.

---

## 3. Formation as a 2-adic projection of c

Prefix formation requires

\[
3^qn+R\equiv0\pmod{2^k}.
\]

Divide by the odd unit \(3^q\) modulo \(2^k\):

\[
\boxed{
n+c\equiv0\pmod{2^k}.}
\]

Hence the prefix residue is

\[
\boxed{
n\equiv-c\pmod{2^k}.}
\]

The denominator of \(c\) divides a power of 3 and is therefore odd, so \(c\) is a well-defined 2-adic integer for this congruence.

Thus \(-c\) is the 2-adic formation coordinate. As the prefix depth grows, its residues modulo \(2^k\) specify the nested starting-integer classes.

---

## 4. Survival as an Archimedean projection of the same c

The no-descent condition at the current prefix endpoint is

\[
a(n+c)\ge n.
\]

If \(a>1\), then \(c\ge0\) implies this automatically for every positive \(n\).

If \(a<1\), then

\[
\boxed{
n\le\frac{ac}{1-a}.}
\]

Define the current contracting fixed-point ceiling

\[
\boxed{
C(a,c):=\frac{ac}{1-a}
}
\]

for \(a<1\).

Therefore the same correction coordinate has two simultaneous meanings:

\[
\boxed{
-c\pmod{2^k}
\quad\text{determines formation},
}
\]

while

\[
\boxed{
\frac{ac}{1-a}
\quad\text{determines the real survival ceiling when }a<1.
}
\]

This is the central 2-adic/Archimedean duality of the property-filter state.

---

## 5. Monotonicity of c

Since

\[
c'=c
\]

on an even extension and

\[
c'=c+\frac1{3a}>c
\]

on an odd extension,

\[
\boxed{c_k\text{ is nondecreasing in the ordinary real order}.}
\]

At the same time, \(-c_k\) gives progressively finer 2-adic residues of the starting class. Thus the same sequence is monotone in its real correction magnitude while converging in the 2-adic formation sense along a fixed infinite parity path.

The explicit partial-sum form is

\[
\boxed{
c_k
=\sum_{\substack{0\le j<k\\p_j=1}}
\frac{2^j}{3^{Q_{j+1}}}.}
\]

---

## 6. Cumulative survival state

A current contracting ceiling is not sufficient because an earlier prefix may have imposed a smaller ceiling. Therefore carry

\[
\boxed{
\Theta_k
=
\min_{\substack{1\le j\le k\\a_j<1}}
\frac{a_jc_j}{1-a_j},
}
\]

with \(\Theta_k=+\infty\) if no contracting prefix has occurred.

The exact Markov-style state can therefore be written as

\[
\boxed{(a,c,\Theta),}
\]

with depth recovered from the denominator of \(a\).

After either branch, compute \((a',c')\); if \(a'<1\), set

\[
\boxed{
\Theta'=\min\left(\Theta,\frac{a'c'}{1-a'}\right),
}
\]

otherwise \(\Theta'=\Theta\).

The formation floor is computed from the residue

\[
-c'\pmod{\operatorname{den}(a')}.
\]

The entire parity class is removed when its least admissible positive representative exceeds \(\Theta'\).

---

## 7. Remaining theorem target

The exact arithmetic dynamics has therefore been compressed to a fixed two-coordinate affine system plus one monotone history ceiling.

The unresolved universal task is:

> prove that no infinite branch whose 2-adic formation residues stabilize to a finite integer \(n>1\) can keep the Archimedean cumulative ceiling \(\Theta_k\) at or above \(n\) forever.

Equivalently, find a fixed property quotient or Lyapunov/progress certificate on \((a,c,\Theta)\) that forces formation-floor / survival-ceiling crossing without enumerating parity prefixes.

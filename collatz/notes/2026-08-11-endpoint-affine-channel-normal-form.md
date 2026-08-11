# Endpoint-affine channel normal form

Date: 2026-08-11

Status: **exact reduced state theorem**. This is a lossless reparameterization of the previously established interval-channel dynamics.

## 1. Reduced exact state

For a depth-\(k\) exact residue channel, the previous state was written

\[
(k,r,y,q,[L,U]),
\]

where \(y=T^k(r)\) is the canonical endpoint and \(q\) is the odd-step count in the prefix.

Define

\[
\boxed{d:=y-r}
\]

and

\[
\boxed{u:=3^q.}
\]

Then the full depth-\(k\) affine cylinder identity is

\[
\boxed{
T^k(r+2^k m)
=
r+d+u m.
}
\]

Hence the exact channel may be represented losslessly as

\[
\boxed{
s=(k,r,d,u,[L,U]).
}
\]

Here

- \(k\) is depth;
- \(0\le r<2^k\) is the canonical residue;
- \(d\) is endpoint displacement of the canonical representative;
- \(u\) is the exact odd-branch multiplier \(3^q\);
- \([L,U]\) is the exact unresolved integer interval in the lift coordinate.

The represented starting integers are

\[
\boxed{
\llbracket s\rrbracket
=
\{r+2^k m:m\in[L,U]\cap\mathbb Z\}.
}
\]

---

## 2. Current-step no-descent inequality

For any represented lift \(m\),

\[
T^k(r+2^k m)-(r+2^k m)
=d+(u-2^k)m.
\]

Thus the current endpoint constraint is simply

\[
\boxed{
d+(u-2^k)m\ge0.}
\]

The stored interval \([L,U]\) already incorporates all earlier prefix constraints as well.

---

## 3. Exact binary child refinement

Choose the next lift bit

\[
c\in\{0,1\}
\]

and write

\[
m=c+2m'.
\]

The inherited interval becomes

\[
\boxed{
L_{\rm inh}'
=
\max\!\left(0,\left\lceil\frac{L-c}{2}\right\rceil\right)
}
\]

and, if \(U<\infty\),

\[
\boxed{
U_{\rm inh}'
=
\left\lfloor\frac{U-c}{2}\right\rfloor;
}
\]

if \(U=+\infty\), then \(U_{\rm inh}'=+\infty\).

The child residue is

\[
\boxed{r'=r+c2^k.}
\]

The lifted canonical endpoint before the new Collatz step is

\[
\widetilde y
=r+d+cu.
\]

Since \(u=3^q\) is odd, its parity is

\[
\boxed{
p
=(r+d+c)\bmod2.
}
\]

Thus no separate storage of \(q\) is needed to determine the new parity.

The new multiplier is

\[
\boxed{u'=3^p u.}
\]

The new endpoint is

\[
y'
=
\frac{3^p(r+d+cu)+p}{2},
\]

so the new endpoint displacement is

\[
\boxed{
d'
=
\frac{3^p(r+d+cu)+p}{2}
-r-c2^k.
}
\]

Therefore the child endpoint identity is

\[
\boxed{
T^{k+1}(r'+2^{k+1}m')
=
r'+d'+u'm'.
}
\]

---

## 4. New no-descent half-line

The new endpoint constraint is

\[
\boxed{
d'+(u'-2^{k+1})m'\ge0.}
\]

Intersecting this half-line with the inherited interval gives the exact child unresolved interval \([L',U']\). If the intersection is empty, the child is removed.

Thus the state family

\[
\boxed{(k,r,d,u,[L,U])}
\]

is exactly closed under the survivor refinement.

---

## 5. Why the reduction matters

The old coordinates \((y,q)\) contained more information than the next survivor transition requires.

The reduced state separates two roles:

### Range geometry

\[
(k,r,[L,U])
\]

determines the represented starting-number set and its generating mass.

### Endpoint dynamics

\[
(d,u)
\]

determines the affine endpoint displacement and multiplier relevant to the next no-descent filter.

The next abstraction task is therefore to find a coarser attribute map of these five ingredients that still suffices to bound surviving child mass and a Lyapunov potential. Any further attribute should be justified only by its necessity for a universal contraction inequality.

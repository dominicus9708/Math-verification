# Exact macroblock formation classes and nested residue representation

Date: 2026-08-11

Status: **exact formation theorem for maximal odd/even macroblocks**. This note aggregates singleton-spine arithmetic into residue classes indexed by macroblock attributes. It does not prove that dangerous infinite macroblock paths are impossible.

## 1. Maximal macroblock type

Let \(x\) be an odd positive integer and define

\[
\boxed{h:=v_2(x+1)\ge1.}
\]

Write uniquely

\[
\boxed{x+1=2^h u,\qquad u\text{ odd}.}
\]

The accelerated odd branch satisfies

\[
T_1(y)+1=\frac32(y+1),
\]

so after \(h\) consecutive odd accelerated steps,

\[
\boxed{y=3^h u-1.}
\]

This value is even. Define

\[
\boxed{d:=v_2(3^hu-1)\ge1.}
\]

After the following \(d\) even accelerated steps, the next odd state is

\[
\boxed{x'=\frac{3^hu-1}{2^d}.}
\]

The maximal accelerated parity block is therefore

\[
\boxed{1^h0^d.}
\]

We call \((h,d)\) its macroblock type.

---

## 2. Formation congruence for one macroblock

Exactness of the debit valuation \(d\) is equivalent to

\[
3^hu-1\equiv2^d\pmod{2^{d+1}},
\]

or

\[
\boxed{
3^hu\equiv1+2^d\pmod{2^{d+1}}.
}
\]

Because \(3^h\) is invertible modulo \(2^{d+1}\), there is a unique residue

\[
\boxed{
u_{h,d}
\equiv3^{-h}(1+2^d)
\pmod{2^{d+1}}.
}
\]

The residue \(u_{h,d}\) is odd. Therefore all and only the odd starts realizing macroblock type \((h,d)\) satisfy

\[
\boxed{
x
\equiv
x_{h,d}:=2^hu_{h,d}-1
\pmod{2^{h+d+1}}.
}
\]

Hence the formation set of one macroblock type is exactly one arithmetic progression.

---

## 3. Affine map to the next odd state

Write

\[
u=u_{h,d}+2^{d+1}m,
\qquad m\in\mathbb Z.
\]

Then the corresponding start is

\[
\boxed{
x=x_{h,d}+2^{h+d+1}m.
}
\]

The next odd state is

\[
\begin{aligned}
x'
&=\frac{3^h(u_{h,d}+2^{d+1}m)-1}{2^d}\\
&=\frac{3^hu_{h,d}-1}{2^d}+2\,3^h m.
\end{aligned}
\]

Thus

\[
\boxed{
x'=y_{h,d}+2\,3^h m,
}
\]

where

\[
\boxed{y_{h,d}:=\frac{3^hu_{h,d}-1}{2^d}}
\]

is odd.

---

## 4. Transition to a prescribed next macroblock type

Let the desired next type be \((h',d')\). From the one-block formation theorem, it requires

\[
\boxed{
x'\equiv x_{h',d'}
\pmod{2^{h'+d'+1}}.
}
\]

Substitute

\[
x'=y_{h,d}+2\,3^hm.
\]

Since both odd residues have even difference, division by 2 gives

\[
\boxed{
3^hm
\equiv
\frac{x_{h',d'}-y_{h,d}}{2}
\pmod{2^{h'+d'}}.
}
\]

Again \(3^h\) is invertible modulo the power of 2, so there is a unique solution

\[
\boxed{
m\equiv m_0
\pmod{2^{h'+d'}}.
}
\]

Therefore the subset of starts realizing two consecutive macroblock types \((h,d)\) and \((h',d')\) is again exactly one residue class, now modulo

\[
\boxed{
2^{1+h+d+h'+d'}.
}
\]

---

## 5. Finite macroblock-word theorem

By induction, any finite macroblock word

\[
\mathcal W_m
=((h_1,d_1),\ldots,(h_m,d_m))
\]

that is arithmetically realizable determines exactly one residue class

\[
\boxed{
x\equiv r_m\pmod{2^{K_m}},}
\]

where

\[
\boxed{
K_m
=1+\sum_{i=1}^{m}(h_i+d_i).
}
\]

The residue classes are nested as the word is extended.

Thus a finite macroblock history represents infinitely many starting integers without enumerating them, and an infinite macroblock path determines a unique 2-adic residue limit.

---

## 6. Generating function of a macroblock formation class

For the positive starts in one residue class

\[
x=r_m+2^{K_m}q
\]

above its least positive representative, the ordinary generating function is geometric:

\[
\boxed{
G_{\mathcal W_m}(z)
=
\frac{z^{r_m}}{1-z^{2^{K_m}}},
\qquad 0<z<1,
}
\]

up to the obvious shift if the canonical residue \(r_m=0\) or if a lower positivity bound is imposed.

Hence an entire finite macroblock word is an exact static aggregate with a closed generating function.

---

## 7. Infinite-path interpretation

An infinite macroblock sequence produces nested residue classes modulo powers of two whose exponents \(K_m\to\infty\). Therefore it determines one 2-adic integer.

For that infinite path to represent a finite positive natural number, the canonical residues must eventually stabilize to that finite integer; equivalently, the associated binary lift must have finite support.

This identifies the next universal theorem target:

> Show that any infinite macroblock path satisfying the no-first-descent / resource-survival filters forces the nested canonical residue frontier to escape to infinity (equivalently, forces infinitely many nonzero lift bits), rather than stabilizing at a finite positive integer.

The previously derived headroom, multiplier, resonance, and CRT conditions are candidate filters on the macroblock type sequence for proving this statement.

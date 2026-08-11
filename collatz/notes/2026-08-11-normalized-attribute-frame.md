# Normalized fixed-dimensional attribute frame

Date: 2026-08-11

Status: **exact normalized coordinate system for the centered survivor channels**. This note identifies a fixed-dimensional attribute domain independent of the numerical size of the starting integer. It does not provide the missing global contraction theorem.

## 1. Exact centered state

Start from

\[
s=(k,\rho,h,u,N),
\]

with

\[
\llbracket s\rrbracket=\{\rho+2^k t:0\le t\le N\}
\]

and

\[
T^k(\rho+2^k t)=\rho+h+ut.
\]

Define normalized attributes

\[
\boxed{
\varepsilon:=\frac1\rho,
\qquad
s:=\frac{2^k}{\rho},
\qquad
a:=\frac{u}{2^k},
\qquad
g:=\frac h\rho,
}
\]

and the endpoint-parity bit

\[
\boxed{e:=(\rho+h)\bmod2.}
\]

The exact normalized attribute state is therefore

\[
\boxed{\Xi=(\varepsilon,s,a,g,N,e).}
\]

The semantic roles are:

- \(\varepsilon\): reciprocal frontier scale;
- \(s\): dyadic refinement scale relative to the frontier;
- \(a\): multiplier balance \(3^q/2^k\);
- \(g\): relative headroom of the least represented integer;
- \(N\): centered channel width;
- \(e\): one-bit arithmetic phase selecting the next parity branch.

This has fixed dimension at every depth.

---

## 2. Child parity and multiplier

Split

\[
t=c+2t',\qquad c\in\{0,1\}.
\]

Because \(u\) is odd, the depth-k endpoint parity on the child is

\[
\boxed{p=(e+c)\bmod2.}
\]

The normalized multiplier updates exactly as

\[
\boxed{a'_{\rm pre}=\frac{3^p}{2}a.}
\]

Thus the multiplier coordinate has a scale-free update conditioned only on the parity bit.

---

## 3. Dimensionless child no-descent inequality

The unshifted child lower start is

\[
\rho_c=\rho+c2^k=\rho(1+cs).
\]

Its next endpoint is

\[
z_c'
=
\frac{3^p(\rho+h+cu)+p}{2}.
\]

Divide the new headroom intercept by \(\rho\) and define

\[
\boxed{
\alpha_c
:=
\frac{z_c'-\rho_c}{\rho}
=
\frac{3^p(1+g+cas)+p\varepsilon}{2}
-(1+cs).
}
\]

Since

\[
u'=3^p u
\]

and

\[
\frac{u'-2^{k+1}}{\rho}
=2s\left(\frac{3^p}{2}a-1\right),
\]

the exact child no-descent condition is

\[
\boxed{
\alpha_c
+2s(a'_{\rm pre}-1)t'
\ge0.
}
\]

Thus, apart from the integer nature of \(t'\) and the width bound, the new survivor half-line is determined entirely by the fixed-dimensional normalized attributes.

---

## 4. Re-centering update

Let the exact surviving child interval be

\[
J\le t'\le K.
\]

Define the frontier scale factor

\[
\boxed{R:=1+cs+2sJ.}
\]

Since

\[
\rho'=\rho R,
\]

the normalized frontier and dyadic scales update as

\[
\boxed{
\varepsilon'=\frac{\varepsilon}{R},
\qquad
s'=\frac{2s}{R}.
}
\]

The re-centered relative headroom is

\[
\boxed{
 g'
=
\frac{
\alpha_c+2s(a'_{\rm pre}-1)J
}{R}.
}
\]

The multiplier coordinate is

\[
\boxed{a'=a'_{\rm pre},}
\]

and the width is

\[
\boxed{N'=K-J.}
\]

The next endpoint parity is the exact bit

\[
\boxed{e'=(\rho'+h')\bmod2.}
\]

and can be retained as a discrete attribute.

---

## 5. Where absolute integer size remains

The only explicit absolute-size correction in the normalized child inequality is

\[
\boxed{p\varepsilon=p/\rho,}
\]

which comes from the \(+1\) in the odd Collatz branch.

Therefore all large-integer dependence is compressed into the single monotone frontier coordinate \(\varepsilon=1/\rho\).

Whenever the frontier strictly increases,

\[
\rho'>\rho,
\]

we have

\[
\boxed{\varepsilon'<\varepsilon.}
\]

Thus \(\varepsilon\) is a natural progress coordinate, while \((s,a,g,N,e)\) describe the scale-free local state.

---

## 6. Frontier-preserving singleton spine

On a stabilized frontier, the unique preserving transition has

\[
c=0,
\qquad J=0,
\qquad R=1.
\]

Hence

\[
\boxed{\varepsilon'=\varepsilon,}
\qquad
\boxed{s'=2s,}
\]

\[
\boxed{a'=\frac{3^e}{2}a,}
\]

and

\[
\boxed{
g'
=
\frac{3^e(1+g)+e\varepsilon}{2}-1.}
\]

Explicitly,

\[
e=0:\quad g'=\frac{g-1}{2},
\]

\[
e=1:\quad g'=\frac{1+3g+\varepsilon}{2}.
\]

For a singleton unresolved spine, \(g\ge0\) must hold at every step.

Thus the terminal fixed-frontier obstruction is a low-dimensional arithmetic dynamical system parameterized only by \(\varepsilon=1/n\), rather than by an unstructured list of starting integers.

---

## 7. Attribute-proof target

The universal proof task can now be stated on a fixed domain:

> Construct a positive potential, finite partition, or well-founded progress function on the normalized attribute state \(\Xi=(\varepsilon,s,a,g,N,e)\) such that every exact survivor transition either decreases unresolved generating mass or makes strict progress in a well-founded/frontier coordinate.

The attribute frame is acceptable only if the relevant inequality is proved uniformly over its full domain. Finite numerical samples may test candidate potentials but cannot supply the universal quantifier.

For the terminal singleton sector \(N=0\), future refinement should use arithmetic alignment information only if the coarse coordinates \((\varepsilon,a,g,e)\) are insufficient to obtain a universal potential. The earlier valuation/macroblock/CRT variables are candidates for precisely that refinement.

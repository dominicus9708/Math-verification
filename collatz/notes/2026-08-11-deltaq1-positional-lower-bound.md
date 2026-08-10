# Delta-Q=1 positional lower bound and first dangerous odd-count layer

Date: 2026-08-11

Status: **derived inequality + exact finite threshold identification**.

This note continues

`collatz/notes/2026-08-11-deltaq1-carry-wrap-dominance.md`.

## 1. Exact positional expression

For a Delta-Q=1 pair, write the H odd positions as

\[
0=a_0<a_1<\cdots<a_q
\]

and the L odd positions as

\[
0=b_0<b_1<\cdots<b_{q-1}.
\]

The correction gap is

\[
G
=1+
\sum_{i=0}^{q-1}
\frac{2^{a_{i+1}}-2^{b_i}}{3^{i+1}}.
\]

Individual coefficient survival implies

\[
a_i\le\kappa(i),\qquad b_i\le\kappa(i),
\]

where

\[
\kappa(i)=\lfloor i\log_2 3\rfloor.
\]

Strict increase and \(a_0=b_0=0\) also imply

\[
a_i\ge i,\qquad b_i\ge i.
\]

Therefore

\[
2^{a_{i+1}}\ge2^{i+1}
\]

and

\[
2^{b_i}\le2^{\kappa(i)}.
\]

Substitution gives the exact position-only lower bound

\[
\boxed{
G>L_q
:=
1+
\sum_{i=0}^{q-1}
\frac{2^{i+1}-2^{\kappa(i)}}{3^{i+1}}.
}
\]

The inequality is strict because for positive \(i\),

\[
2^{\kappa(i)}<3^i.
\]

A simpler coarse form is

\[
\boxed{
G>
3-\frac q3-2\left(\frac23\right)^q.
}
\]

The exact \(L_q\) is appreciably stronger.

---

## 2. Congruence and dominance

Coefficient survival through depth at least two gives

\[
r_H\equiv r_L\equiv3\pmod4,
\]

hence

\[
\boxed{G\equiv2\pmod4.}
\]

The actual Pareto order channel is

\[
J=r_L-r_H=2r_H+G.
\]

Because \(r_H\ge3\), a dominance failure

\[
J\le0
\]

requires at least

\[
\boxed{G\le-6.}
\]

Thus any range in which the positional bound gives

\[
G>-6
\]

is automatically safe for Delta-Q=1 start dominance, independently of the 3-adic carry or 2-adic wrap details.

---

## 3. Exact threshold

The exact rational values near the transition are:

\[
L_{33}
=
-\frac{28054076412945158}{5559060566555523}
\approx-5.0465498760,
\]

\[
L_{34}
=
-\frac{29555270562112262}{5559060566555523}
\approx-5.3165944512,
\]

\[
L_{35}
=
-\frac{30556066661556998}{5559060566555523}
\approx-5.4966241680,
\]

\[
\boxed{
L_{36}
=
-\frac{861042528161526178}{150094635296999121}
\approx-5.7366642482>-6,
}
\]

whereas

\[
\boxed{
L_{37}
=
-\frac{303026959457942326}{50031545098999707}
\approx-6.0567179938<-6.
}
\]

Therefore:

> For every Delta-Q=1 coefficient-surviving true first merge with lower odd-count
> \[
> q\le36,
> \]
> one has
> \[
> \boxed{r_H<r_L.}
> \]

No endpoint enumeration or carry-spectrum computation is needed for this finite statement.

The first odd-count layer at which the position-only bound permits a potentially dangerous value is exactly

\[
\boxed{q=37.}
\]

At that layer the first newly permitted dangerous congruence class is

\[
\boxed{G=-6,\qquad c_0=-7.}
\]

Whether an admissible integer carry chain with \(c_0=-7\) actually reaches a true first merge remains open in the present calculation.

---

## 4. Reduction to a small-start obstruction

From

\[
J=2r_H+G
\]

and \(G>L_q\), any dominance failure would imply

\[
2r_H+L_q<0,
\]

hence

\[
\boxed{
r_H<-\frac{L_q}{2}.
}
\]

Using only the coarse bound gives

\[
r_H
<
\frac q6-\frac32+\left(\frac23\right)^q.
\]

Thus a Delta-Q=1 dominance counterexample is forced into a starting-residue window that grows only linearly in \(q\), with coefficient at most approximately \(1/6\) under the coarse bound and more tightly under the exact \(L_q\).

Since a true merge at depth \(k\) has \(q+1\le k\), the coarse consequence is

\[
\boxed{r_H<\frac{k}{6}}
\]

for any sufficiently nontrivial dominance counterexample.

This connects the endpoint-dominance problem to the minimal coefficient-survivor function \(\mu(k)\): a dominance counterexample would force an unusually small coefficient survivor relative to its depth.

---

## 5. Current proof target

The corrected hierarchy is now:

\[
\text{position bounds}
\to
\text{finite negative-G spectrum}
\to
\text{3-adic carry existence}
\to
\text{2-adic wrap/contact}
\to
\text{start dominance }J.
\]

The first unresolved dangerous layer is

\[
\boxed{q=37,\ c_0=-7,\ G=-6.}
\]

The immediate computational target is to decide whether this root supports any admissible carry chain and, if so, whether any such chain satisfies the true-contact wrap condition \(m=0\).

The asymptotic target is weaker than the discarded correction-order conjecture: it is sufficient to show that the most negative admissible \(G\) grows too slowly in magnitude to overcome \(2r_H\).

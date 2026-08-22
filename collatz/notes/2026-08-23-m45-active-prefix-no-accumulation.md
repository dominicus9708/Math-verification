# m=45 active-prefix nested conditioning does not accumulate

Date: 2026-08-23

Status: **exact finite active-prefix theorem. This closes accumulation inside the already exposed 28-bit selector window, not the renewal tail and not the Collatz conjecture.**

## 1. Certified selector histogram

The existing exact NTT mass-transport certificate proves that, for the 44 free selector digits in the current m=45 decomposition, every residue modulo \(2^{26}\) has multiplicity

\[
260110\le c(r)\le264167.
\]

The fixed affine terms \(3^{45}+b3^{44}\) only translate this histogram and therefore do not change its dynamic range.

## 2. Arbitrary nested conditioning lemma

Let \(\nu\) be uniform measure on the active residue coordinate and let \(\mu\) be selector measure with point weights proportional to \(c(r)\).

For any two nonempty events \(A\subseteq E\) measurable in this same residue space,

\[
\frac{\mu(A\mid E)}{\nu(A\mid E)}
=
\frac{\frac1{|A|}\sum_{r\in A}c(r)}
{\frac1{|E|}\sum_{r\in E}c(r)}.
\]

Each average lies between the certified minimum and maximum. Hence

\[
\boxed{
\frac{\mu(A\mid E)}{\nu(A\mid E)}
\le
\frac{264167}{260110}
<\frac{65}{64}.
}
\]

This statement is hard-set independent: the shapes of \(A\) and \(E\) do not matter.

## 3. No multiplicative accumulation inside the active prefix

For a nested chain

\[
E_0\supseteq E_1\supseteq\cdots\supseteq E_s,
\]

the product of stepwise same-integer amplification factors telescopes to the final selector/uniform density ratio. Therefore the total amplification over any number of nested filters in this active coordinate is still bounded by the same dynamic range,

\[
\boxed{
\Xi^{\circ}_{\rm active}<\frac{65}{64}.
}
\]

It does not grow as \((65/64)^s\).

The exact power comparison

\[
65^{40}<2\,64^{40}
\]

implies

\[
\boxed{
\log_2\Xi^{\circ}_{\rm active}<\frac1{40}\text{ bit}.
}
\]

Certificate:

`collatz/src/m45_active_prefix_nested_conditioning_certificate.py`.

## 4. Relation to the new Stage-4 threshold

The current L7 exclusion theorem permits a repeated normalized 28-step conditional amplification strictly below 15. The complete m=45 selector-active prefix uses less than \(65/64\) total amplification even after arbitrary nested conditioning inside the exposed residue coordinate.

Thus the active prefix is no longer a candidate source of a positive linear repair rate.

## 5. What remains

The theorem applies only to events measurable in the already exposed free-selector residue coordinate modulo \(2^{26}\), equivalently through binary depth 28 after the common \(N=4Y+3\) prefix is removed.

Conditions depending on higher binary digits can distinguish integers that are identical in this active coordinate. Consequently the unresolved Stage-4 mechanism has moved entirely to the renewal tail:

1. transport from one normalized renewal boundary to the next;
2. open positive-height excursions crossing the finite depth-28 boundary;
3. possible new mixed-place/Hensel syndrome information beyond the active residue coordinate.

The next target is therefore sharper than before:

> **Tail-only conditional transversality theorem.** After quotienting the selector-active prefix by the bound \(\Xi^{\circ}_{\rm active}<65/64\), prove that each normalized renewal-tail window has conditional amplification below 15, or otherwise show a sublinear total tail repair budget.

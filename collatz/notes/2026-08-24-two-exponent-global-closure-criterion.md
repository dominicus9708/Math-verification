# Two-exponent global closure criterion

Date: 2026-08-24

Status: **sufficient asymptotic budget theorem.**  This combines the two remaining exponential channels—nearest root credit and same-address selector concentration—into one inequality.  It does not prove the required exponent bounds and is not a proof of Collatz.

## 1. Unconditional formation exclusion rate

Let

\[
\alpha:=\log_3 2,
\qquad
\delta_{\rm form}:=1-H_2(\alpha).
\]

Numerically,

\[
\boxed{\delta_{\rm form}\approx0.05004447281166946.}
\]

The coefficient-surviving binary language has size

\[
2^{(1-\delta_{\rm form})H+o(H)}.
\]

## 2. Same-address amplification exponent

Let \(\Xi_H\) denote the multiplicative excess of the recursively sufficient ternary selector mass on the relevant coefficient-surviving / terminal language relative to the baseline dyadic mass at depth H.

Define

\[
\boxed{
\beta:=\limsup_{H\to\infty}
\frac{\log_2\Xi_H}{H}.
}
\]

Then the effective exclusion rate after allowing for same-address repair is

\[
\delta_{\rm eff}=\delta_{\rm form}-\beta.
\]

A useful closure criterion requires \(\beta<\delta_{\rm form}\).

## 3. Nearest-root-credit exponent

For a non-maximal coefficient-surviving complete prefix, let \(G_H\) be the largest, over the relevant words, of the least positive whole-prefix sibling credit

\[
R'-R=3^q d,
\qquad d>0.
\]

Define

\[
\boxed{
\gamma:=\limsup_{H\to\infty}
\frac{\log_2G_H}{H}.
}
\]

For a recursively sufficient depth-m root,

\[
N\ge4\cdot3^m+3
=2^{m\log_2 3+O(1)}.
\]

At a binary horizon

\[
H=cm,
\]

nearest-credit root validity is asymptotically guaranteed whenever

\[
\gamma c<\log_2 3.
\]

## 4. Selector-extinction horizon

The depth-m selector family has \(2^m\) members.  If the same-address amplification exponent is \(\beta\), then at H=cm the effective entropy budget is

\[
m-(\delta_{\rm form}-\beta)cm+o(m).
\]

To force a negative exponent one needs

\[
\boxed{
c(\delta_{\rm form}-\beta)>1.}
\]

Thus a usable c must satisfy

\[
\frac1{\delta_{\rm form}-\beta}<c<\frac{\log_2 3}{\gamma}.
\]

Such a c exists exactly when

\[
\boxed{
\gamma<(\delta_{\rm form}-\beta)\log_2 3.
}
\]

This is the two-exponent global closure criterion.

## 5. Important special cases

### Subexponential same-address repair

If

\[
\beta=0,
\]

then it suffices to prove

\[
\boxed{
\gamma<\delta_{\rm form}\log_2 3
\approx0.07931861277485554.
}
\]

So the nearest-credit theorem need not prove \(G_H=2^{o(H)}\); any exponential rate strictly below about 0.07932 bit per binary step is enough, provided selector repair has zero exponential rate.

### Subexponential nearest credit

If

\[
\gamma=0,
\]

then it suffices to prove

\[
\boxed{
\beta<\delta_{\rm form}\approx0.05004447281166946.
}
\]

Thus same-address near-independence is also stronger than necessary.

### Trade-off

More generally, a positive but small nearest-credit exponent can be paid for by a stronger selector transversality exponent and conversely.  For example,

\[
\gamma=0.02
\]

would require only

\[
\beta<0.03742587774024031\ldots.
\]

## 6. Strategic consequence

The remaining globalization program no longer needs two separately maximal theorems such as

- \(G_H=2^{o(H)}\), and
- \(\Xi_H=2^{o(H)}\).

Those are sufficient but unnecessarily strong.

The actual target is the open region

\[
\boxed{
\gamma+(\log_2 3)\beta
<
(\log_2 3)\delta_{\rm form}.
}
\]

The finite data currently available—small \(G_H\) through H=32 and extremely small first-window selector bias at m=45—are encouraging diagnostics, but they do not establish either asymptotic exponent.

Certificate:

`collatz/src/two_exponent_global_closure_budget_certificate.py`.

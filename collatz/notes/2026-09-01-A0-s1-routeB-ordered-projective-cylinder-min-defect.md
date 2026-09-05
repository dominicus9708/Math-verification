# A0 s=1 Route-B — ordered projective-cylinder minimum defect

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Purpose

The one-step projective-cylinder theorem converts a fixed successor carry into
one arithmetic residue class for a ranked-one position.

A long suffix or block can impose such cylinders at several ranks.  Those
local constraints are **not independent**, because ranked one positions must
remain strictly ordered.

This note closes the exact multi-rank accumulation problem once the cylinders
are known.

Source:

`collatz/src/A0_s1_routeB_ordered_projective_cylinder_min_defect_certificate.py`

---

## 2. Ordered cylinder family

Let the target ranked-one positions be

\[
a_1<a_2<\cdots<a_q.
\]

For each candidate rank impose

\[
\mathcal B_r
=
[\ell_r,u_r]
\cap
(\beta_r+\lambda_r\mathbf Z)
\cap
(-\infty,a_r].
\]

The candidate positions must also satisfy

\[
b_1<b_2<\cdots<b_q.
\]

Projective ternary cylinders have

\[
\lambda_r=2\cdot3^{m_r-1},
\]

but the theorem needs only that each \(\mathcal B_r\) is an arithmetic
progression intersected with an interval.

---

## 3. Right-to-left greedy maximum

Define recursively

\[
g_q=\max\mathcal B_q.
\]

Then for

\[
r=q-1,q-2,\ldots,1,
\]

set

\[
\boxed{
g_r=\max\{b\in\mathcal B_r:b<g_{r+1}\}.}
\]

If one of these sets is empty, the entire ordered cylinder family is empty.

Otherwise

\[
\boxed{g=(g_1,\ldots,g_q)}
\]

is feasible.

---

## 4. Componentwise maximality theorem

For every feasible

\[
b=(b_1,\ldots,b_q),
\]

one has

\[
\boxed{b_r\le g_r\qquad\forall r.}
\]

The proof is a backward induction.

At the final rank, \(g_q\) is by definition the largest legal member, so

\[
b_q\le g_q.
\]

Assume

\[
b_{r+1}\le g_{r+1}.
\]

Because \(b_r<b_{r+1}\),

\[
b_r<g_{r+1}
\]

or at worst lies under an even tighter cap.  Since \(g_r\) is the largest
member of \(\mathcal B_r\) below \(g_{r+1}\),

\[
b_r\le g_r.
\]

Thus the greedy vector is not merely lexicographically maximal.  It is the
**componentwise greatest feasible vector**.

---

## 5. Exact minimum normalized defect

The rank-\(r\) normalized defect atom is

\[
d_r(b_r)
=
\frac{2^{a_r}-2^{b_r}}{3^r}.
\]

For fixed \(a_r,r\), this is strictly decreasing in \(b_r\).

Since every feasible vector satisfies

\[
b_r\le g_r,
\]

one obtains

\[
\boxed{
d_r(b_r)\ge d_r(g_r).}
\]

Summing gives

\[
\boxed{
\eta(b)
\ge
\eta(g)
=
\sum_{r=1}^q
\frac{2^{a_r}-2^{g_r}}{3^r}.
}
\]

Because \(g\) itself is feasible, the bound is attained.

Therefore

\[
\boxed{
\eta_{\min}
=
\sum_{r=1}^q
\frac{2^{a_r}-2^{g_r}}{3^r}.
}
\]

This is an exact family minimum, not a sum of unrelated local lower bounds.

---

## 6. Ordering amplification

The theorem captures an effect that the previous `1/12 per displaced rank`
summary cannot see.

Suppose a late projective cylinder forces

\[
g_{r+1}\ll a_{r+1}.
\]

Then the strict-order cap

\[
b_r<g_{r+1}
\]

may force

\[
g_r<a_r
\]

**even if rank \(r\)'s own arithmetic cylinder still contains the target
position \(a_r\)**.

Thus one directly forced displacement can propagate leftward into additional
forced defects.

This propagation is exact and should be counted once through the greedy vector,
not by independently adding local gap claims.

---

## 7. Relation to slack partitions

In the normalized suffix notation, write

\[
B_t=a_{q-t}-\delta_t
\]

or equivalently the slack

\[
s_t=B_t-(q-t-1).
\]

The strict order of the \(B_t\) is equivalent to the previously derived
nonincreasing slack condition.

The right-to-left greedy theorem therefore has an equivalent slack statement:
for fixed arithmetic cylinders, the defect-minimizing slack path is the
componentwise largest admissible slack path beneath the target capacity
staircase.

This connects the projective carry cylinder directly to the partition/Ferrers
representation without expanding all partitions.

---

## 8. Regression

The finite certificate exhausts:

- every target one-position set through `h <= 7`;
- up to three ranked ones;
- projective-style periods `2` and `6`;
- every residue class for those periods.

Results:

- ordered-cylinder families checked: `39,648`;
- empty families correctly detected: `34,185`;
- every nonempty family had the greedy vector inside the direct feasible set;
- every direct feasible vector was componentwise bounded by the greedy vector;
- every nonempty family's direct minimum \(\eta\) equaled the greedy formula.

These checks are regression only; the proof is the componentwise maximality
argument above.

---

## 9. DSD audit

### EXACT / CLOSED

- multiple arithmetic/projective cylinders plus rank ordering have an exact
  feasibility test by right-to-left greedy selection;
- if feasible, the greedy vector is componentwise greatest;
- the greedy vector gives the exact minimum of the full normalized defect;
- ordering-induced secondary displacements are included automatically;
- no independence assumption and no double counting are used.

### REGRESSION ONLY

- the `39,648` finite family checks audit indexing and arithmetic-cylinder
  conventions.

### NOT INFERRED

- the actual 14-root source families are not yet known to force a specific
  full sequence of successor-carry cylinders;
- projective-cylinder periods need not remain fixed along a long adaptive
  decoder;
- no root family is closed merely by this theorem;
- the Collatz conjecture remains open.

---

## 10. Updated bottleneck

Two exact defect accumulators are now available.

### Grammar-side

\[
\text{fixed-resolution H/L residue state}
\to
\text{exact min-plus defect}.
\]

### Dominance/projective-side

\[
\text{ordered arithmetic cylinders}
\to
\text{exact minimum }\eta.
\]

The next unresolved interface is therefore narrower:

\[
\boxed{
\text{14-root source/end-point state}
\longrightarrow
\text{forced successor-carry cylinder sequence}.
}
\]

Once such a sequence is available, the ordered greedy theorem converts it
immediately to \(\underline\eta\), which can then be compared with the exact
physical threshold \(\eta_{close}(X_{lo})\).

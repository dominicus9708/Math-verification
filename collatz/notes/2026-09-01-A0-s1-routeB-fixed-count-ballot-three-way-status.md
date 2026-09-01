# A0 s=1 Route-B — fixed-count ballot cone and exact F/P/U status

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Why fixed count matters

The current target-aware decoder does not consider arbitrary future binary suffixes once the final \((h,q)\) class is fixed.  At an intermediate prefix, both the remaining length and the remaining one-count are known budgets.

This strengthens the earlier unrestricted ballot future cone.

Let the current prefix \(W\) have length \(h\), and define

\[
b(W)=\min_{0\le u\le h}
\left(q_W(u)-\lfloor\alpha u\rfloor\right),
\]

\[
e(W)=q(W)-\lfloor\alpha h\rfloor,
\qquad 0<\alpha<1.
\]

Let every admissible completion have

\[
|V|=\ell,
\qquad
q(V)=s.
\]

Set

\[
z=\ell-s,
\]

the exact number of zeros that remain to be placed.

## 2. Extremal prefix-one profiles

For a prefix of the suffix of relative length \(u\), let \(j_V(u)\) denote the number of ones seen so far.

Among all length-\(\ell\), one-count-\(s\) words,

\[
\boxed{
j_V(u)\ge\max(0,u-z)}
\]

for every \(u\), because at most \(\ell-u\) ones can still be postponed beyond the prefix.

Equality simultaneously for all \(u\) is achieved by

\[
\boxed{V_{\min}=0^z1^s.}
\]

Similarly,

\[
\boxed{
j_V(u)\le\min(u,s)}
\]

for every \(u\), with simultaneous equality for

\[
\boxed{V_{\max}=1^s0^z.}
\]

Thus these two monotone arrangements are pointwise extremal for every suffix prefix, not merely at the endpoint.

## 3. Exact worst-case ballot minimum

Define

\[
\Delta_\alpha(h,t)
=
\lfloor\alpha(h+t)\rfloor-\lfloor\alpha h\rfloor.
\]

For \(0\le u\le z\), the zero-first extremal suffix contributes no new ones, so its deviation decreases as far as

\[
e(W)-\Delta_\alpha(h,z).
\]

After position \(z\), every new symbol is 1.  Since \(\alpha<1\), each further step changes

\[
j(u)-\Delta_\alpha(h,u)
\]

by either 0 or 1, never negatively.  Therefore the lowest new deviation occurs at the zero/one boundary \(u=z\).

Hence

\[
\boxed{
\min_{\substack{|V|=\ell\\q(V)=s}} b(WV)
=
\min\left(
b(W),
e(W)-\Delta_\alpha(h,\ell-s)
\right).
}
\]

The exact worst completion is

\[
\boxed{0^{\ell-s}1^s.}
\]

## 4. Exact best-case ballot minimum

For the one-first extremal word \(1^s0^z\), the deviation cannot decrease during its first \(s\) symbols.  After all required ones have appeared, only zeros remain, so the new minimum can be smallest at the final endpoint.

Every fixed-count completion has the same final endpoint discrepancy

\[
e(W)+s-\Delta_\alpha(h,\ell).
\]

Therefore

\[
\boxed{
\max_{\substack{|V|=\ell\\q(V)=s}} b(WV)
=
\min\left(
b(W),
e(W)+s-\Delta_\alpha(h,\ell)
\right).
}
\]

The exact best completion is

\[
\boxed{1^s0^{\ell-s}.}
\]

## 5. Exact three-way status for a threshold gate

Consider

\[
b(WV)\ge\beta.
\]

Define

\[
B_{\min}
=
\min\left(
b(W),
e(W)-\Delta_\alpha(h,\ell-s)
\right),
\]

\[
B_{\max}
=
\min\left(
b(W),
e(W)+s-\Delta_\alpha(h,\ell)
\right).
\]

Then the entire fixed-count continuation family has the exact status

### F — impossible

\[
\boxed{B_{\max}<\beta}
\]

if and only if **no** fixed-count completion can satisfy the gate.

### P — universal

\[
\boxed{B_{\min}\ge\beta}
\]

if and only if **every** fixed-count completion satisfies the gate.

### U — genuinely unresolved

Otherwise

\[
\boxed{B_{\min}<\beta\le B_{\max},}
\]

so at least one completion fails and at least one completion passes.

This gives an exact F/P/U predicate-status transition using only

\[
\boxed{(h,e,b,\ell,s)}
\]

for the ballot-minimum coordinate.

No suffix enumeration is required.

## 6. Stronger active-frontier consequence

The previous unrestricted all-suffix criterion used a worst suffix \(0^\ell\).  In a fixed-\((h,q)\) family that suffix is usually inadmissible because the remaining \(s\) ones must still be placed.

The fixed-count theorem replaces the dangerous zero run of length \(\ell\) by only

\[
\boxed{\ell-s}
\]

zeros.

Therefore many states that remained unresolved under the unrestricted cone can become exact \(P\) states once the global one-count budget is enforced.

Conversely, the exact best envelope detects \(F\) states that cannot possibly recover even under the most favorable one-first completion.

This is exactly the kind of predicate-relative family pruning required by the active-frontier architecture.

## 7. Relation to target ballot metadata

The finite target-aware decoder currently filters candidates by exact ballot metadata, including the ballot minimum and a critical-prefix field.

The theorem here closes the **minimum-threshold coordinate** under fixed length/count budgets.  It does not yet prove equality of the literal critical-prefix metadata.

Accordingly:

- minimum failure can already be rejected family-wide;
- minimum safety can already be discharged family-wide when the exact \(P\) condition holds;
- critical-prefix compatibility remains active when the candidate definition still queries it.

The next useful target is therefore the critical-prefix sector rather than the minimum itself.

## 8. DSD audit

### Exact / closed

- zero-first and one-first suffixes are pointwise extremal among fixed-count suffixes;
- the exact minimum and maximum achievable future ballot minima have closed forms;
- a ballot-minimum threshold has an exact F/P/U classification under fixed remaining length and one-count;
- the classification uses family budgets and needs no leaf enumeration.

### Regression only

`collatz/src/A0_s1_routeB_fixed_count_ballot_future_cone_certificate.py`
contains exhaustive small fixed-count regressions as an implementation guard.  The script has been committed but has not been executed in the current connector environment.

### Not inferred

- literal critical-prefix equality is not determined by \((h,e,b,\ell,s)\);
- full target ballot-summary equality is therefore not yet closed;
- universal long-language membership and the Collatz conjecture remain open.

## 9. Updated bottleneck

At fixed \((h,q)\), the correction-collision sector is two-front localized and the ballot-minimum sector has an exact family-level three-way status.

The remaining target-aware middle bottleneck has now narrowed primarily to

\[
\boxed{
\text{critical-prefix / critical-phase compatibility under a fixed-count budget.}
}
\]

The existing compositional state \((e,r,b,g)\) already propagates the critical **phase** exactly.  The next audit should determine when the literal critical index is actually necessary, and whether the target case permits replacing it by phase plus a finite tie-status coordinate.

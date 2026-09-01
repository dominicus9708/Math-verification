# A0 s=1 Route-B — ballot future cone for family closure

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Scope

The source-cylinder boundary coordinates can now be discharged on whole source intervals.  The next question is whether the interior ballot sector also has predicate-relative early termination regions.

The existing Route-B state stores a ballot minimum together with a critical prefix/phase.  The result below closes only the **minimum-coordinate threshold gate**.  It does not discard critical information when later conditions still query it.

## 2. Ballot quantities

Fix any real slope

\[
0<\alpha<1.
\]

For a binary word \(W\), let \(q_W(u)\) be the number of ones in its prefix of length \(u\), and define

\[
d_W(u)=q_W(u)-\lfloor \alpha u\rfloor.
\]

Let

\[
\boxed{b(W)=\min_{0\le u\le |W|}d_W(u)}
\]

and the endpoint discrepancy

\[
\boxed{e(W)=q(W)-\lfloor\alpha |W|\rfloor.}
\]

Let \(V\) be an arbitrary future suffix with

\[
|V|\le\ell.
\]

## 3. Universal finite-horizon future cone

For a suffix prefix of relative length \(u\), with \(j(u)\ge0\) ones,

\[
d_{WV}(|W|+u)
=
q(W)+j(u)-\lfloor\alpha(|W|+u)\rfloor.
\]

Using

\[
\lfloor a+b\rfloor
\le
\lfloor a\rfloor+\lfloor b\rfloor+1,
\]

we obtain

\[
d_{WV}(|W|+u)
\ge
e(W)-\lfloor\alpha u\rfloor-1
\ge
e(W)-\lfloor\alpha\ell\rfloor-1.
\]

All prefixes lying wholly inside \(W\) retain minimum \(b(W)\).  Hence

\[
\boxed{
b(WV)
\ge
\min\left(
b(W),
e(W)-\lfloor\alpha\ell\rfloor-1
\right).
}
\]

Conversely the old minimum remains present, and the full endpoint of \(W\) is also a prefix of \(WV\), so

\[
\boxed{
b(WV)\le\min(b(W),e(W)).}
\]

Therefore every suffix of length at most \(\ell\) lies in the exact safe enclosure

\[
\boxed{
\min\left(b,e-\lfloor\alpha\ell\rfloor-1\right)
\le b(WV)\le
\min(b,e).
}
\]

The lower bound is a universal guarantee; it need not be the exact attainable minimum for a restricted admissible suffix family.

## 4. Threshold-gate closure

Consider any gate

\[
\boxed{b(W)\ge\beta.}
\]

### A — irreversible rejection

If

\[
b(W)<\beta,
\]

then every extension still contains the already bad prefix.  Therefore

\[
\boxed{
b(WV)<\beta\quad\text{for every }V.}
\]

This is an exact absorbing rejection condition.

### B — guaranteed finite-horizon acceptance

If

\[
b(W)\ge\beta
\]

and

\[
e(W)-\lfloor\alpha\ell\rfloor-1\ge\beta,
\]

then

\[
\boxed{
b(WV)\ge\beta}
\]

for every suffix \(|V|\le\ell\).

Thus the minimum-coordinate gate can be discharged for the entire remaining horizon without enumerating suffixes.

## 5. Restricted-family sharpening

Suppose an admissible suffix family \(\mathcal V\) has a stronger certified lower bound

\[
b(V)\ge\underline b
\]

for every \(V\in\mathcal V\).

Using the exact compositional ballot state, the suffix contribution is bounded below by

\[
e(W)+\underline b-1,
\]

so

\[
\boxed{
b(WV)
\ge
\min\bigl(b(W),e(W)+\underline b-1\bigr).}
\]

Hence any independently proved structural restriction on future admissible blocks immediately strengthens the family-acceptance cone.

This is the intended point of contact with the existing correction-language, lazy-frontier, and Christoffel/run restrictions.  Such restrictions must be proved before they are used; they are not assumed globally here.

## 6. Interaction with source-cylinder boundary closure

At a source-family node there are now at least two exact predicate-relative early-termination mechanisms:

1. boundary cylinder gate:
   \[
   h\ge K,\ q\ge L
   \]
   freezes start/end boundary residues on the entire interval;
2. ballot-minimum future cone:
   an already failed minimum is permanently rejected, while a sufficiently high pair \((b,e)\) guarantees the minimum gate through the remaining horizon.

This suggests the following non-singleton family recursion:

\[
\boxed{
\text{A: reject by frozen boundary or absorbing ballot failure}
}
\]

\[
\boxed{
\text{B: discharge frozen boundary and/or guaranteed ballot coordinate}
}
\]

\[
\boxed{
\text{C: refine only coordinates still queried by the predicate.}
}
\]

The earlier interval rank proves that repeated C-refinement is well founded in the finite SAFE-pruned forest.

## 7. DSD audit

### Exact / closed

- ballot minimum can never recover from an already violated threshold;
- the displayed finite-horizon lower enclosure follows from the floor inequality and nonnegative suffix one-count;
- the sufficient acceptance cone is valid for every binary suffix of the stated maximum length;
- restricted admissible-family lower bounds can only improve the cone.

### Regression only

`collatz/src/A0_s1_routeB_ballot_future_cone_certificate.py`
contains finite rational-slope checks as an implementation guard.  The proof does not depend on those checks.

### Not inferred

- the repository does not currently define universal Route-B membership solely by a condition `base_min >= beta`;
- therefore this theorem is a reusable coordinate-level closure theorem, not by itself a universal Route-B recognizer;
- critical-prefix/critical-phase conditions remain separate whenever queried;
- Collatz remains open.

## 8. Updated bottleneck

The next strongest target is now to identify the actual unresolved interior predicate as a conjunction of monotone/frozen coordinates and to derive a **predicate-status automaton** whose states forget a coordinate immediately after that coordinate has been discharged.

If successful, state growth will be governed by the active frontier of unresolved gates rather than by the full future source precision.

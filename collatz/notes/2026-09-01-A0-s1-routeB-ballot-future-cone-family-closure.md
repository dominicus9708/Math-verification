# A0 s=1 Route-B — exact ballot future cone for family closure

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

For a binary word \(W\) of length \(h\), let \(q_W(u)\) be the number of ones in its prefix of length \(u\), and define

\[
d_W(u)=q_W(u)-\lfloor \alpha u\rfloor.
\]

Let

\[
\boxed{b(W)=\min_{0\le u\le h}d_W(u)}
\]

and the endpoint discrepancy

\[
\boxed{e(W)=q(W)-\lfloor\alpha h\rfloor.}
\]

Let \(V\) be an arbitrary future suffix with

\[
|V|\le\ell.
\]

Define the exact floor increase over the remaining horizon

\[
\boxed{
\Delta_\alpha(h,\ell)
=\lfloor\alpha(h+\ell)\rfloor-\lfloor\alpha h\rfloor.
}
\]

## 3. Exact universal finite-horizon future cone

For a suffix prefix of relative length \(u\), with \(j(u)\ge0\) ones,

\[
\begin{aligned}
d_{WV}(h+u)
&=q(W)+j(u)-\lfloor\alpha(h+u)\rfloor\\
&=e(W)+j(u)-\bigl(\lfloor\alpha(h+u)\rfloor-\lfloor\alpha h\rfloor\bigr).
\end{aligned}
\]

Because \(0\le u\le\ell\), monotonicity of the floor function gives

\[
\lfloor\alpha(h+u)\rfloor-\lfloor\alpha h\rfloor
\le
\Delta_\alpha(h,\ell),
\]

and therefore

\[
d_{WV}(h+u)
\ge
e(W)-\Delta_\alpha(h,\ell).
\]

All old prefixes remain present, so

\[
\boxed{
b(WV)
\ge
\min\bigl(b(W),e(W)-\Delta_\alpha(h,\ell)\bigr).
}
\]

This bound is not merely sufficient.  Take the full-length all-zero suffix

\[
V=0^\ell.
\]

Its endpoint has no additional ones, hence

\[
d_{W0^\ell}(h+\ell)
=e(W)-\Delta_\alpha(h,\ell).
\]

Together with the inherited old minimum \(b(W)\), this yields

\[
\boxed{
b(W0^\ell)
=
\min\bigl(b(W),e(W)-\Delta_\alpha(h,\ell)\bigr).
}
\]

Therefore the exact worst-case envelope over **all** binary suffixes of length at most \(\ell\) is

\[
\boxed{
\min_{|V|\le\ell} b(WV)
=
\min\bigl(b(W),e(W)-\Delta_\alpha(h,\ell)\bigr).
}
\]

This improves the earlier generic carry estimate: there is no extra \(-1\) once the absolute prefix length \(h\) is retained.

## 4. Exact threshold-gate closure

Consider any ballot-minimum gate

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

### B — all-suffix finite-horizon acceptance

Because the worst-case suffix is known exactly, **every** binary suffix \(|V|\le\ell\) satisfies the gate if and only if

\[
\boxed{
b(W)\ge\beta}
\]

and

\[
\boxed{
e(W)-\Delta_\alpha(h,\ell)\ge\beta.}
\]

Thus

\[
\boxed{
\forall |V|\le\ell:\ b(WV)\ge\beta
\iff
\min\bigl(b(W),e(W)-\Delta_\alpha(h,\ell)\bigr)\ge\beta.
}
\]

This is an exact finite-horizon acceptance criterion for the minimum coordinate, not merely a sufficient condition.

## 5. Restricted-family sharpening

If future admissibility rules exclude the all-zero suffix or otherwise impose positive-one constraints, the unrestricted worst case above may be too pessimistic.

Suppose an admissible suffix family \(\mathcal V\) has an independently proved lower bound on its internal ballot deviations.  The exact compositional ballot state can then replace the unrestricted zero-suffix envelope by a stronger family-specific envelope.

This is the intended point of contact with correction-language restrictions, lazy-boundary localization, and any subsequently proved Christoffel/run-family coverage.  Such structural restrictions must be proved before they are used; they are not assumed globally here.

## 6. Interaction with source-cylinder boundary closure

At a source-family node there are now two exact predicate-relative early-termination mechanisms:

1. boundary cylinder gate: once \(h\ge K\) and \(q\ge L\), the requested dyadic start and ternary endpoint residues are constant over the entire source interval;
2. ballot-minimum gate: failure is absorbing, and finite-horizon all-suffix acceptance has the exact criterion
   \[
   \min\bigl(b,e-\Delta_\alpha(h,\ell)\bigr)\ge\beta.
   \]

This gives the family recursion

\[
\boxed{
\text{A: reject by frozen boundary mismatch or absorbing ballot failure}
}
\]

\[
\boxed{
\text{B: discharge frozen boundary and/or exact finite-horizon ballot minimum}
}
\]

\[
\boxed{
\text{C: refine only coordinates still queried by the predicate.}
}
\]

The previously proved interval rank makes repeated C-refinement well founded inside the finite SAFE-pruned 14-root forest.

## 7. DSD audit

### Exact / closed

- ballot minimum can never recover from an already violated threshold;
- the exact worst-case future minimum over all suffixes of length at most \(\ell\) is
  \[
  \min\bigl(b,e-\Delta_\alpha(h,\ell)\bigr);
  \]
- the all-zero suffix of full remaining length attains that worst case;
- therefore all-suffix finite-horizon acceptance of a threshold gate is characterized by an iff condition, not just a sufficient bound.

### Regression only

`collatz/src/A0_s1_routeB_ballot_future_cone_certificate.py`
contains finite rational-slope checks as an implementation guard.  The algebraic proof above is independent of those checks.  The script has been written to the repository but has not been executed in the current connector environment.

### Not inferred

- the repository does not define universal Route-B membership solely by `base_min >= beta`;
- this is therefore a coordinate-level closure theorem, not a universal Route-B recognizer;
- critical-prefix/critical-phase conditions remain separate whenever queried;
- universal correction-language membership and the Collatz conjecture remain open.

## 8. Updated bottleneck

For unrestricted future binary suffixes, the ballot-minimum coordinate is now completely characterized at finite horizon.

The next unresolved question is narrower:

\[
\boxed{
\text{Which remaining Route-B interior predicates still query correction residues or critical-prefix data after the boundary and minimum coordinates are discharged?}
}
\]

The next useful construction is a predicate-status automaton that forgets each coordinate immediately after an exact A/B decision, so state growth follows only the active unresolved frontier.

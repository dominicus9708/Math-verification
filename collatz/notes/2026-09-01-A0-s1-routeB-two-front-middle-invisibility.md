# A0 s=1 Route-B — two-front correction middle invisibility

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Correct boundary coordinates

For an ordinary binary parity word \(W\) of length \(h\), one-count \(q\), and correction \(C(W)\),

\[
2^hT^h(x)=3^q x+C(W).
\]

The boundary coordinates used by the existing lazy-frontier decoder are the normalized projections

\[
\boxed{
S_K(W)
=-C(W)\,3^{-q}\pmod{2^K}
}
\]

and

\[
\boxed{
E_L(W)
=C(W)\,2^{-h}\pmod{3^L}.
}
\]

The first is the canonical start residue modulo \(2^K\).  The second is the normalized endpoint correction modulo \(3^L\).

This normalization matters: the raw correction \(C\bmod2^K\) does not itself remain unchanged under an arbitrary suffix because of the factor \(3^{q(V)}\).

## 2. Composition identity

For two words \(A,B\),

\[
\boxed{
C(AB)=3^{q(B)}C(A)+2^{|A|}C(B).
}
\]

Also

\[
|AB|=|A|+|B|,
\qquad
q(AB)=q(A)+q(B).
\]

## 3. Left localization

Let \(W=UZ\).  If

\[
|U|\ge K,
\]

then

\[
\begin{aligned}
S_K(UZ)
&=-\bigl(3^{q(Z)}C(U)+2^{|U|}C(Z)\bigr)
  3^{-(q(U)+q(Z))}\pmod{2^K}\\
&=-C(U)3^{-q(U)}
  -2^{|U|}C(Z)3^{-(q(U)+q(Z))}\pmod{2^K}.
\end{aligned}
\]

The second term vanishes because \(2^K\mid2^{|U|}\).  Hence

\[
\boxed{
|U|\ge K
\Longrightarrow
S_K(UZ)=S_K(U).
}
\]

Therefore the dyadic start boundary is completely determined by a sufficiently long left frontier.

## 4. Right localization

Let \(W=ZV\).  If

\[
q(V)\ge L,
\]

then

\[
\begin{aligned}
E_L(ZV)
&=\bigl(3^{q(V)}C(Z)+2^{|Z|}C(V)\bigr)
2^{-(|Z|+|V|)}\pmod{3^L}.
\end{aligned}
\]

The first term vanishes because \(3^L\mid3^{q(V)}\).  The second reduces to

\[
C(V)2^{-|V|}.
\]

Thus

\[
\boxed{
q(V)\ge L
\Longrightarrow
E_L(ZV)=E_L(V).
}
\]

The ternary endpoint boundary is therefore completely determined by a sufficiently one-rich right frontier.

## 5. Two-front middle-invisibility theorem

Now decompose

\[
\boxed{W=UMV.}
\]

If

\[
|U|\ge K
\qquad\text{and}\qquad
q(V)\ge L,
\]

then applying the two localization identities gives

\[
\boxed{
S_K(UMV)=S_K(U),
}
\]

\[
\boxed{
E_L(UMV)=E_L(V).
}
\]

Therefore

\[
\boxed{
\bigl(S_K(UMV),E_L(UMV)\bigr)
=
\bigl(S_K(U),E_L(V)\bigr),
}
\]

independently of the length, one-count, correction, or literal contents of the middle block \(M\).

This is an exact **middle-invisibility theorem for the two correction boundary predicates**.

## 6. Predicate-level consequence

Fix target boundary values \((s_*,e_*)\).  Once the left and right frontier capacities are reached,

\[
S_K(U)=s_*,
\qquad
E_L(V)=e_*
\]

implies that every middle block \(M\) satisfies the same two boundary comparisons.

If either comparison mismatches, every middle block fails those boundary conditions.

Hence for these coordinates alone the entire middle language

\[
\{M\}
\]

collapses to one PASS/FAIL decision.

The number of possible middle parity words does not enter the boundary-state complexity.

## 7. Relation to the active predicate frontier

This theorem supplies exact P/F transitions for the correction boundary coordinates:

- after the left frontier reaches \(K\) symbols, the start coordinate is no longer active;
- after the right frontier accumulates \(L\) ones, the normalized endpoint coordinate is no longer active;
- the unresolved middle is queried only by still-active interior predicates such as correction-language compatibility beyond these necessary projections, ballot/critical conditions, or other Route-B gates.

Thus a two-sided decoder should not carry the already frozen boundary observations through the middle recursion.

## 8. Existing target-specific frontier scale

The existing lazy-frontier certificate gives, for the current Route-B target hierarchy, examples where very large words expose requested boundary coordinates on small frontier nodes.  In particular the stored target audit reports a dyadic \(K=27\) frontier at a node of length 27 and a ternary \(L=28\) frontier at a node of length 84 with 53 ones.

These values are target/hierarchy-specific finite facts already encoded in the repository.  They are not used to prove the general theorem above.

## 9. DSD audit

### Exact / closed

- the normalized start and endpoint projections obey opposite localization laws;
- a sufficiently capable left/right pair makes the entire middle invisible to both boundary coordinates;
- PASS or FAIL of those two coordinates can therefore be certified without enumerating middle words;
- the result follows directly from the affine correction composition identity.

### Regression only

`collatz/src/A0_s1_routeB_two_front_middle_invisibility_certificate.py`
contains exhaustive small-word checks as an implementation guard.  The script is committed but has not been executed in the current connector environment.

### Not inferred

- matching \((S_K,E_L)\) is still only necessary boundary compatibility;
- the theorem does not prove that an arbitrary middle belongs to the target correction language;
- it does not discharge critical-prefix or other ballot conditions;
- it does not justify global use of the Christoffel hierarchy for all survivors;
- universal Route-B membership and the Collatz conjecture remain open.

## 10. Updated bottleneck

After the two frontiers have frozen, neither boundary coordinate sees the middle at all.  The remaining problem is therefore concentrated in the middle-language predicate:

\[
\boxed{
\text{classify or quotient the unresolved middle using only the still-active interior gates.}
}
\]

The next target should be a middle-state theorem that intersects

1. the exact ballot future cone,
2. correction-language/right-congruence state,
3. source-interval family payload,

while keeping the frozen two-front boundary coordinates out of the state entirely.

# A0 s=1 Route-B — fixed-(h,q) correction collision is a two-front predicate

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Context

The target-aware adaptive decoder compares words inside a class with the same exact length \(h\) and one-count \(q\), then tests correction collision at resolution \((K,L)\):

\[
C(W)\equiv C(W_*)\pmod{2^K3^L}.
\]

The two-front localization theorem uses normalized boundary coordinates.  In a fixed-\((h,q)\) class these normalized comparisons are exactly equivalent to the raw correction congruence, so the full correction-collision predicate itself localizes to the two boundaries.

## 2. Boundary coordinates

For a word \(W\), define

\[
S_K(W)
=-C(W)3^{-q(W)}\pmod{2^K},
\]

\[
E_L(W)
=C(W)2^{-|W|}\pmod{3^L}.
\]

Let \(W,W_*\) satisfy

\[
|W|=|W_*|=h,
\qquad
q(W)=q(W_*)=q.
\]

Because \(3^q\) is invertible modulo \(2^K\),

\[
\boxed{
C(W)\equiv C(W_*)\pmod{2^K}
\iff
S_K(W)=S_K(W_*).
}
\]

Because \(2^h\) is invertible modulo \(3^L\),

\[
\boxed{
C(W)\equiv C(W_*)\pmod{3^L}
\iff
E_L(W)=E_L(W_*).
}
\]

Since \(2^K\) and \(3^L\) are coprime, CRT gives

\[
\boxed{
C(W)\equiv C(W_*)\pmod{2^K3^L}
\iff
\begin{cases}
S_K(W)=S_K(W_*),\\
E_L(W)=E_L(W_*).
\end{cases}
}
\]

Thus within fixed \((h,q)\), the adaptive correction collision test is exactly a pair of boundary comparisons.

## 3. Two-front localization

Write

\[
W=UMV,
\qquad
W_*=U_*M_*V_*.
\]

Assume

\[
|U|,|U_*|\ge K
\]

and

\[
q(V),q(V_*)\ge L.
\]

The two-front theorem gives

\[
S_K(W)=S_K(U),
\qquad
S_K(W_*)=S_K(U_*),
\]

and

\[
E_L(W)=E_L(V),
\qquad
E_L(W_*)=E_L(V_*).
\]

Therefore

\[
\boxed{
C(W)\equiv C(W_*)\pmod{2^K3^L}
}
\]

if and only if

\[
\boxed{
S_K(U)=S_K(U_*)
\quad\text{and}\quad
E_L(V)=E_L(V_*).
}
\]

The middle words \(M,M_*\) do not occur in this criterion.

Hence:

\[
\boxed{
\text{fixed-(h,q) correction collision is a two-front predicate.}
}
\]

## 4. Consequence for the adaptive target decoder

The existing finite target decoder first fixes the same \((h,q)\) and ballot/counter metadata as the target, then resolves remaining correction collisions by increasing \(K\) or \(L\).

For its correction sector, the present theorem means that a candidate family does **not** need to propagate the full correction state through an unresolved middle merely to answer the final congruence question.

At any requested \((K,L)\):

1. expose a left frontier with at least \(K\) symbols;
2. expose a right frontier with at least \(L\) ones;
3. compare their normalized coordinates with the corresponding target frontiers;
4. ignore the middle for the correction-collision predicate.

The adaptive choice of increasing \(K\) or \(L\) can therefore be interpreted as requesting more information from one of two boundary fronts, not as increasing observation precision everywhere in the word.

## 5. What remains in the middle

Once the correction collision has been reduced to its two fronts, the unresolved middle is still constrained by other parts of the candidate definition, including

- total fixed \(h\) and \(q\);
- the target ballot summary / critical-prefix condition used by the current finite decoder;
- any stronger long-language membership condition not implied by the boundary congruences.

Thus the correction sector is no longer the reason to enumerate middle corrections.

For the current target-aware architecture the central symbolic-compression problem shifts toward

\[
\boxed{
\text{fixed-count ballot/critical middle language.}
}
\]

This is a narrower target than universal correction-language decoding.

## 6. Relation to correction injectivity

At sufficiently high resolution the fixed-\((h,q)\) correction map is injective.  The existing dyadic theorem already gives a universal separating barrier \(K\le h-1\), and the ternary diameter gives an alternative finite barrier.

The present theorem does not improve those worst-case resolution bounds.  Instead it changes **where that resolution must be observed**: the correction comparison can be serviced by the two fronts while the middle remains symbolic.

This distinction is important for family-level complexity.

## 7. DSD audit

### Exact / closed

- within one fixed \((h,q)\) class, raw correction congruence modulo \(2^K3^L\) is equivalent to equality of normalized start/end boundary projections;
- those projections localize to opposite word fronts;
- therefore the middle is exactly invisible to the correction-collision predicate once the front capacities are met;
- the theorem is algebraic and independent of finite target size.

### Regression only

`collatz/src/A0_s1_routeB_fixed_hq_correction_collision_frontier_certificate.py`
contains exhaustive small-word comparisons as an implementation guard.  It has been committed but not executed in the current connector environment.

### Not inferred

- equal boundary projections do not imply arbitrary long-language membership outside the fixed candidate predicate being tested;
- ballot/critical metadata is not determined by the two correction fronts;
- no universal Christoffel coverage is assumed;
- the Collatz conjecture remains open.

## 8. Updated bottleneck

The correction-collision part of the fixed-\((h,q)\) target decoder no longer requires middle enumeration.

The next central question is therefore

\[
\boxed{
\text{Can the fixed-}(h,q)\text{ ballot/critical candidate language be represented by a small compositional quotient?}
}
\]

The exact ballot state \((e,r,b,g)\) already supplies a right-congruence for minimum/critical-phase evolution.  The next step is to combine it with a remaining-one-count budget and determine whether the middle candidate language admits absorbing rejection, guaranteed completion, or state merging without storing the literal critical-prefix index.

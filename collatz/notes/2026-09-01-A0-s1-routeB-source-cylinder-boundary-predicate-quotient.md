# A0 s=1 Route-B — source-cylinder boundary predicate quotient

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Motivation

The previous audit showed that the generic future source transducer cannot merge distinct

\[
Y=y\bmod 2^d
\]

states while preserving every future input/output parity word.  Therefore the next useful quotient must be relative to the actual Route-B predicate rather than to the complete source dynamics.

The first exact predicate-relative quotient is available for the two boundary coordinates.

## 2. Exact source channel

Let a parity prefix define the affine cylinder

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\qquad m\in I\subset\mathbb Z.
\]

Fix dyadic start resolution \(K\) and ternary endpoint resolution \(L\).

If

\[
h\ge K,
\]

then

\[
X-r=2^h m
\]

is divisible by \(2^K\), hence

\[
\boxed{X\equiv r\pmod{2^K}}
\]

for every \(m\in I\).

If

\[
q\ge L,
\]

then

\[
T^h(X)-y=3^q m
\]

is divisible by \(3^L\), hence

\[
\boxed{T^h(X)\equiv y\pmod{3^L}}
\]

for every \(m\in I\).

Therefore when \(h\ge K\) and \(q\ge L\), the two-sided boundary predicate

\[
G_{K,L}^{a,b}(X)
=
[\,X\equiv a\pmod{2^K}\,]
\land
[\,T^h(X)\equiv b\pmod{3^L}\,]
\]

is constant on the entire source cylinder.

Equivalently,

\[
\boxed{
G_{K,L}^{a,b}\bigl(r+2^h m\bigr)
=
[\,r\equiv a\pmod{2^K}\,]
\land
[\,y\equiv b\pmod{3^L}\,]
}
\]

for all \(m\in I\).

## 3. Family-level A/B closure

This gives an exact family action without parameter splitting.

### A — boundary mismatch

If either

\[
r\not\equiv a\pmod{2^K}
\]

or

\[
y\not\equiv b\pmod{3^L},
\]

then every member of \(I\) fails the requested boundary predicate.

Thus

\[
\boxed{I\text{ is pruned as one family.}}
\]

### B — boundary match

If both congruences hold, every member of \(I\) satisfies both requested boundary coordinates.

Thus those coordinates are discharged for the whole interval and later refinement is needed only for still-unresolved interior / ballot / correction-language conditions.

This does **not** mean all members are Route-B admissible.

## 4. Relation to lazy boundary frontiers

The existing lazy-boundary theorem localizes the dyadic start coordinate along the left decomposition axis and the ternary endpoint coordinate along the right decomposition axis.

The present theorem is the source-cylinder counterpart:

- once a source prefix has accumulated \(h\ge K\), its entire parameter interval has one dyadic start residue;
- once it has accumulated \(q\ge L\), its entire parameter interval has one ternary endpoint residue.

Hence boundary observations need not force descent to singleton source parameters.

## 5. Predicate-relative quotient

For the boundary predicate alone, the relevant channel observation is

\[
\boxed{
B_{K,L}(P)
=
\left(
 r\bmod2^K,
 y\bmod3^L
\right)
}
\]

provided \(h\ge K\) and \(q\ge L\).

Distinct channels with different full projective source state may therefore be equivalent for this boundary predicate.

This does not contradict the previous generic-source no-go theorem: that theorem required preservation of **all future input/output parity behavior**, whereas \(B_{K,L}\) preserves only the chosen Route-B boundary decision.

## 6. Consequence for the family-cover program

The family-cover recursion should therefore be ordered by unresolved predicate coordinates, not by raw source precision.

A useful state split is now

\[
\boxed{
\text{boundary status}
\times
\text{interior correction/ballot state}
\times
\text{interval payload}.
}
\]

Once a boundary axis is discharged, its source precision need not continue to grow merely to preserve that already-decided gate.

This is the first exact mechanism that can beat the generic \(Y\)-state lower bound: it discards information only after proving that the Route-B predicate no longer queries it.

## 7. DSD audit

### Exact / closed

- \(h\ge K\Rightarrow X\bmod2^K\) is constant on the full source cylinder;
- \(q\ge L\Rightarrow T^h(X)\bmod3^L\) is constant on the full source cylinder;
- two-sided boundary PASS/FAIL is therefore a family-level decision;
- mismatch gives exact A-pruning without singleton expansion;
- match discharges only the boundary coordinates, not universal membership.

### Regression only

`collatz/src/A0_s1_routeB_source_cylinder_boundary_predicate_certificate.py`
checks small exact channels and several integer parameters.  The algebra above is the proof; the script is only an implementation guard.

### Still open

1. interior correction-language membership;
2. ballot / C4F closure for all surviving source families;
3. a predicate-relative quotient that also collapses those interior conditions;
4. universal Route-B membership;
5. the Collatz conjecture.

## 8. Updated bottleneck

The next question is no longer whether the boundary coordinates require full source expansion.  They do not.

The central remaining problem is

\[
\boxed{
\text{Can the interior correction+ballot predicate also be discharged on whole source families?}
}
\]

The natural next attempt is to define monotone acceptance/rejection regions in the compositional ballot state and combine them with adaptive correction separation, so that an interval can terminate before its source parameter becomes singleton.

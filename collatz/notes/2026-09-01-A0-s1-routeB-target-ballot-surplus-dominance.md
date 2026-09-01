# A0 s=1 Route-B — target ballot class as a surplus-dominance DAG

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Target metadata collapses to strict prefix dominance

The current target-aware finite decoder uses the exact threshold target

\[
TH_i=REQ(i+1)-REQ(i),
\]

with

\[
REQ(u)=\lfloor\alpha u\rfloor+1
\qquad(u>0),
\]

and target metadata

\[
(h,q,m,a)=(h,q_{TH},0,\varnothing).
\]

The ballot implementation initializes `base_min=0`, `critical=None` and scans only nonempty prefixes.  Therefore

\[
(base\_min,critical)=(0,\varnothing)
\]

holds if and only if no nonempty prefix ever reaches or crosses the zero deviation level:

\[
q_W(u)-\lfloor\alpha u\rfloor>0
\qquad(1\le u\le h).
\]

Since the deviation is integral, this is equivalent to

\[
q_W(u)\ge\lfloor\alpha u\rfloor+1=REQ(u).
\]

But the threshold target itself satisfies

\[
q_{TH}(u)=REQ(u).
\]

Hence the target ballot class is exactly

\[
\boxed{
q_W(u)\ge q_{TH}(u)
\quad\text{for every prefix }u,
}
\]

with the same final one-count

\[
q_W(h)=q_{TH}(h).
\]

Thus the literal `critical` field disappears entirely for this target class: `critical=None` is simply the strict prefix-dominance condition.

## 2. One-position formulation

Let the target one positions be

\[
0\le a_1<a_2<\cdots<a_q<h
\]

and a candidate's one positions be

\[
0\le b_1<b_2<\cdots<b_q<h.
\]

Prefix dominance is equivalent to

\[
\boxed{b_r\le a_r\qquad(1\le r\le q).}
\]

Proof: if the candidate's \(r\)-th one occurs no later than the target's \(r\)-th one, every target prefix containing \(r\) ones also contains at least \(r\) candidate ones.  Conversely, a violation \(b_r>a_r\) gives a prefix immediately after \(a_r\) in which the target has \(r\) ones but the candidate has at most \(r-1\).

So the candidate language is an order ideal of left-shifted one positions.

## 3. Surplus counter

Define

\[
\boxed{
\sigma(u)=q_W(u)-q_{TH}(u).
}
\]

Then

\[
\sigma(0)=0,
\]

and the bitwise transition is

\[
\boxed{
\sigma(u+1)=\sigma(u)+W_u-TH_u.
}
\]

The exact candidate condition is

\[
\boxed{
\sigma(u)\ge0\quad(0\le u\le h),
\qquad
\sigma(h)=0.
}
\]

Thus the entire same-\((h,q,0,\varnothing)\) target ballot language is recognized by a one-counter layered automaton.

At layer \(u\), \(\sigma\) is an integer between 0 and at most \(u\), so there are at most \(u+1\) raw surplus states.  Hence the total number of layered states is bounded by

\[
\boxed{
\sum_{u=0}^h(u+1)
=\frac{(h+1)(h+2)}2
=O(h^2).
}
\]

The actual reachable set is usually smaller after the final-count return condition is imposed.

This replaces the naive \(2^h\) ballot-candidate enumeration by a quadratic-size exact DAG.

## 4. Finite target regression

For the existing length-18 target,

\[
h=18,
\qquad q=12.
\]

The surplus DP gives

\[
\boxed{2652}
\]

return-to-zero candidate paths.

This exactly matches the previously exhaustively measured number of words with metadata

\[
(18,12,0,\varnothing).
\]

The count can therefore be recovered without enumerating all \(2^{18}\) words.

This finite equality is a regression confirmation of the general algebraic language equivalence.

## 5. Correction monotonicity inside the dominance language

Using one positions,

\[
C(W)=\sum_{r=1}^q3^{q-r}2^{b_r},
\]

while

\[
C(TH)=\sum_{r=1}^q3^{q-r}2^{a_r}.
\]

Since

\[
b_r\le a_r
\]

for every candidate,

\[
\boxed{C(W)\le C(TH).}
\]

Equality holds only when

\[
b_r=a_r
\quad\forall r,
\]

that is, only for the target itself.

Therefore

\[
\boxed{
TH\text{ is the unique maximum-correction word in its ballot-dominance class.}
}
\]

This is stronger structural information than mere fixed-\((h,q)\) injectivity, although it is specialized to this dominance class.

## 6. Exact dyadic valuation from the first left shift

Let \(W\ne TH\), and let

\[
r_0=\min\{r:b_r<a_r\}
\]

be the first one that has been shifted left relative to the target.

Then

\[
\Delta=C(TH)-C(W)
=\sum_{r:r\ge r_0}3^{q-r}
\left(2^{a_r}-2^{b_r}\right),
\]

where unchanged later terms may vanish.

For the first shifted term,

\[
2^{a_{r_0}}-2^{b_{r_0}}
=
2^{b_{r_0}}
\left(2^{a_{r_0}-b_{r_0}}-1\right),
\]

and the parenthesized factor is odd.  Hence this term has exact 2-adic valuation

\[
b_{r_0}.
\]

Every later moved one has

\[
b_r>b_{r_0},
\]

so every later nonzero term is divisible by at least

\[
2^{b_{r_0}+1}.
\]

The lowest dyadic term is therefore unique and cannot cancel.  Thus

\[
\boxed{
v_2\bigl(C(TH)-C(W)\bigr)=b_{r_0}.
}
\]

Equivalently, the first dyadic separating resolution is

\[
\boxed{K_*=b_{r_0}+1.}
\]

This is also consistent with the existing prefix-channel bijection: within a fixed one-count class, the dyadic collision depth is the first parity disagreement position.  The positional proof above makes that fact explicit for the target-dominance language.

## 7. Dyadic collision becomes prefix equality

For a non-target dominance candidate,

\[
C(W)\equiv C(TH)\pmod{2^K}
\]

if and only if

\[
K\le b_{r_0}.
\]

But \(b_{r_0}\) is exactly the first bit position where the candidate can differ from the target in this dominance orientation.  Therefore

\[
\boxed{
C(W)\equiv C(TH)\pmod{2^K}
\iff
W_{[0,K)}=TH_{[0,K)}.
}
\]

So the dyadic correction collision gate for this fixed-\(q\) target language is simply a literal target-prefix equality gate.

This gives a particularly cheap left-front implementation of the adaptive decoder.

## 8. Family-level consequence

At fixed \((h,q)\), the target-aware candidate architecture now separates into:

1. ballot/critical candidate language: an \(O(h^2)\) surplus DAG;
2. dyadic correction collision: target prefix equality through depth \(K\);
3. ternary correction collision: a right-front normalized endpoint comparison;
4. interval/source payload: handled by the previously proved projective family quotient and well-founded interval descent.

The literal critical-prefix index is no longer part of the target candidate state.

This substantially narrows the earlier family-level bottleneck.

## 9. DSD audit

### Exact / closed

- `(base_min,critical)=(0,None)` is equivalent to strict threshold-prefix dominance for the current target definition;
- same-final-count candidates are exactly nonnegative surplus walks returning to zero;
- the ballot candidate language has an exact quadratic-size layered DAG;
- the target is the unique correction maximum in that dominance language;
- the first left-shift position gives the exact dyadic valuation of the correction difference.

### Finite regression

`collatz/src/A0_s1_routeB_target_ballot_surplus_automaton_certificate.py`
contains an exact threshold construction and verifies that the length-18 surplus DP returns 2,652 candidates, matching the existing exhaustive audit.  The general surplus proof does not depend on length 18.

The script has been committed but has not been executed through the GitHub connector in the current session.  A separate local arithmetic check during this analysis reproduced the 2,652 DP count.

### Not inferred

- the ternary target-collision sector is not eliminated by surplus alone;
- a polynomial bound for the combined surplus + arbitrary ternary-resolution state is not yet proved;
- universal Route-B membership is not proved;
- the Collatz conjecture remains open.

## 10. Updated bottleneck

The previously suspected literal-critical-index obstruction disappears for the actual target metadata.

The remaining combinatorial core is now much more specific:

\[
\boxed{
\text{nonnegative surplus paths returning to zero, filtered by a right-front ternary collision.}
}
\]

The next strongest step is to derive a right-to-left ternary state directly on the surplus DAG and determine whether its target-collision classes admit a compact recurrence, rather than enumerating all surplus paths.

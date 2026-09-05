# A0 s=1 Route-B — source min-plus defect quotient

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Purpose

The fixed-resolution H/L min-plus recurrence is exact but still has a billion-
scale length axis.

The current 14-root search already has a different exact representation:

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m.
\]

This note places the monotone normalized defect directly on that source
refinement DAG.

For the restricted predicate set

1. exact source transition;
2. strict threshold/pure-ballot prefix dominance;
3. accumulated normalized defect;

histories can be merged by an exact Bellman/min-plus rule.

Source:

`collatz/src/A0_s1_routeB_source_minplus_defect_quotient_certificate.py`

---

## 2. Reduced source state

Suppose \(D\) parameter bits remain to be exposed.

At a layer with remaining precision \(d\), use

\[
\boxed{
S_d=(Y,q)
=
(y\bmod2^d,q).
}
\]

The coefficient

\[
3^q\bmod2^d
\]

is reconstructed from \(q\).

For the next parameter bit

\[
\epsilon\in\{0,1\},
\]

the emitted Collatz parity is

\[
\boxed{
\beta=(Y+\epsilon)\bmod2.
}
\]

The next projective endpoint residue is then determined exactly by the usual
affine source transition.

Thus, at fixed layer and remaining precision, two histories with the same
\((Y,q)\) have the same future parity response to every common future parameter
suffix.

---

## 3. Exact defect increment

Let the target ranked-one positions be

\[
a_1<a_2<\cdots.
\]

If the next emitted `1` is the candidate's rank \(r\) one at absolute position
\(h\), the normalized defect increment is

\[
\boxed{
\kappa(h,r)
=
\frac{2^{a_r}-2^h}{3^r}.
}
\]

The strict threshold-prefix gate guarantees

\[
h\le a_r,
\]

so

\[
\kappa(h,r)\ge0.
\]

An emitted `0` contributes zero at that step.

The increment is determined by

- the layer \(h\);
- the new one-count \(r\);
- the emitted bit.

No older history is queried.

---

## 4. Bellman dominance lemma

Suppose two legal histories reach the same \(S_d=(Y,q)\) with accumulated
defects

\[
E_1\le E_2.
\]

Attach the same remaining parameter suffix to both histories.

Exact source-control equality gives the same future parity bits.  Since the
current \(q\) is also the same, every future ranked-one index is the same, and
therefore every future defect increment is identical.

If the common future increment is \(F\ge0\), the two final defects are

\[
E_1+F
\le
E_2+F.
\]

Hence the larger accumulated value can never produce a lower-defect survivor.

Therefore one may retain only

\[
\boxed{
E_{\min}(Y,q)
=
\min\{\eta_{prefix}:\text{history reaches }(Y,q)\}.
}
\]

This is an exact min-plus quotient for the stated predicate set.

---

## 5. State-count improvement for the defect-only predicate frontier

Let \(i\) future parameter bits have been consumed from one fixed parent.

The raw number of parameter prefixes is

\[
2^i.
\]

At that layer,

\[
Y\bmod2^{D-i}
\]

has at most

\[
2^{D-i}
\]

values.

The one-count can differ from the parent's one-count by only

\[
0,1,\ldots,i,
\]

so it has at most

\[
i+1
\]

values.

Thus

\[
\boxed{
n_i
\le
\min\left(
2^i,
2^{D-i}(i+1)
\right).
}
\]

The min-plus defect value is a label and does not multiply the number of
states.

Using

\[
\min(x,y)\le\sqrt{xy},
\]

one gets

\[
n_i
\le
2^{D/2}\sqrt{i+1}.
\]

Therefore

\[
\boxed{
N_{DAG}
\le
2^{D/2}(D+1)^{3/2}.
}
\]

This is a defect-pruning-specific bound.  It is smaller than the more general
source+ballot+critical+correction state bound because those inactive coordinates
have deliberately been removed from this predicate frontier.

---

## 6. Finite 14-root-shape regression

The certificate starts from the current first-defect prefix shapes

\[
f=2,5,8
\]

and exposes ten additional source-parameter bits.

The exact starting defect values are

\[
\eta_{f=2}=\frac4{27},
\]

\[
\eta_{f=5}=\frac{32}{243},
\]

\[
\eta_{f=8}=\frac{256}{2187}.
\]

For all three roots, the merged Bellman map agreed exactly with direct
enumeration of all

\[
2^{10}=1024
\]

future parameter residues.

Actual state-merging events occurred in the regression.

A useful negative observation is that the minimum defect after these ten
unconstrained source bits remains equal to the root's initial prefix defect.
Thus short source refinement **by itself** does not force an additional defect
for these examples.

That result reinforces the need to combine the source DAG with endpoint,
correction/projective, or other membership constraints rather than expecting
ordinary source determinism alone to create the required root-scale defect.

---

## 7. Relation to physical pruning

At any family node, current accumulated defect is irreversible.

Therefore if a safe lower bound for every represented history satisfies

\[
\underline\eta
\ge
\eta_{close}(X_{lo}),
\]

the node closes physically.

However an important exactness issue remains when several source histories are
merged:

- smaller \(\eta\) is harder to reject;
- smaller ordinary \(X_{lo}\) is also harder to reject.

The history with minimum \(\eta\) need not be the history with minimum
\(X_{lo}\).

Thus exact adaptive physical pruning of a merged state may require a joint
frontier, or a conservative separated bound such as

\[
\min\eta
\quad\text{and}\quad
\min X_{lo}.
\]

Using the two separate minima is SAFE but may lose pruning strength.
It must not be called an exact joint quotient without an additional theorem.

---

## 8. Predicate-relative scope

The state \((Y,q)\) is intentionally small because only three predicates are
active here.

If the decoder also queries

- correction residues;
- checkpoint endpoint residues;
- literal critical metadata;
- renewal/C4F state;

then those exact coordinates must be restored to the state key before merging
histories.

This is the DSD active-predicate principle applied to the defect search.

---

## 9. DSD audit

### EXACT / CLOSED

- `(Y mod 2^d,q)` is exact future control for the restricted source/ballot
  defect predicate set;
- accumulated normalized defect is a Bellman scalar label;
- for one exact control state, every history except the minimum-defect history
  is dominated for low-defect existence;
- the label does not enlarge state count;
- the defect-only finite-horizon DAG satisfies the displayed
  square-root-exponential bound.

### FINITE REGRESSION

- first-defect shapes `2,5,8`, ten future parameter bits, direct enumeration
  against merged DP.

### REJECTED / NOT INFERRED

- source refinement alone is not assumed to force new defect;
- `(Y,q)` is not a complete state for correction/endpoint/C4F predicates;
- separate minima of `eta` and `X_lo` are not called an exact joint frontier;
- no 14-root family is closed by this note;
- Collatz remains open.

---

## 10. Updated bottleneck

The source and grammar directions now both support exact min-plus defect labels.

The next important problem is the **joint physical frontier**:

\[
\boxed{
\text{same exact future-control state}
\longmapsto
\text{compact frontier of }(X_{lo},\eta).
}
\]

A bounded or strongly compressible frontier would permit source refinement to
lower \(\eta_{close}(X_{lo})\) without giving up the exact Bellman merging just
proved.

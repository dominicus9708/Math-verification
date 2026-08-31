# A0 s=1 Route-B — projective interval-family quotient

Date: 2026-08-31  
Branch: `collatz-stage4-window-threshold`

## 1. Goal

The source-channel quotient already showed that, for a finite future depth `d`, the affine control state

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m
\]

needs only

\[
Q_d(P)=\left(y\bmod 2^d,\;3^q\bmod 2^d\right)
\]

to determine every common block transition of length at most `d`.

The remaining payload was an exact finite integer interval

\[
I=[L,U]\cap\mathbb Z.
\]

This note proves that the interval payload itself has an exact finite-horizon projective quotient, and combines it with `Q_d` into a finite-horizon family right-congruence.

---

## 2. Interval projective state

Let

\[
N=|I|=U-L+1.
\]

For `d >= 0`, define

\[
\boxed{
\Pi_d(I)=\left(N,\;L\bmod 2^d\right).
}
\]

For `d=0`, the second coordinate is taken to be the unique trivial residue.

The claim is that `Pi_d` contains exactly the endpoint information needed for every dyadic residue pullback through future depth `d`.

---

## 3. Exact residue pullback

Fix `1 <= ell <= d` and a residue

\[
0\le a<2^\ell.
\]

Restrict the parent parameter to

\[
m\equiv a\pmod{2^\ell},
\qquad
m=a+2^\ell n.
\]

Then the exact child interval in the new parameter `n` is

\[
\Phi_{a,\ell}(I)
=
\left[
\left\lceil\frac{L-a}{2^\ell}\right\rceil,
\left\lfloor\frac{U-a}{2^\ell}\right\rfloor
\right]\cap\mathbb Z.
\]

It is empty exactly when the lower endpoint exceeds the upper endpoint.

---

## 4. Projective interval theorem

### Theorem

If

\[
\Pi_d(I)=\Pi_d(I'),
\]

then for every `ell <= d` and every residue `a mod 2^ell`:

1. `Phi_{a,ell}(I)` is empty iff `Phi_{a,ell}(I')` is empty;
2. when nonempty, the two children have the same cardinality;
3. when nonempty,

\[
\boxed{
\Pi_{d-\ell}(\Phi_{a,\ell}(I))
=
\Pi_{d-\ell}(\Phi_{a,\ell}(I')).
}
\]

### Proof

Equality of `Pi_d` gives the same cardinality `N` and

\[
L'\equiv L\pmod{2^d}.
\]

Therefore for some integer `k`,

\[
L'=L+k2^d.
\]

Because the intervals have the same cardinality,

\[
U'=U+k2^d.
\]

Now

\[
\left\lceil\frac{L'-a}{2^\ell}\right\rceil
=
\left\lceil\frac{L-a}{2^\ell}\right\rceil
+k2^{d-\ell},
\]

and similarly

\[
\left\lfloor\frac{U'-a}{2^\ell}\right\rfloor
=
\left\lfloor\frac{U-a}{2^\ell}\right\rfloor
+k2^{d-\ell}.
\]

Thus the two child intervals are exact translates by `k 2^(d-ell)`.  Emptiness and cardinality are identical, and their lower endpoints agree modulo `2^(d-ell)`.  This proves the theorem.

---

## 5. Balanced child cardinalities

Let

\[
M=2^\ell.
\]

The `M` residue classes partition the consecutive interval `I` exactly.  Therefore

\[
\sum_{a=0}^{M-1}|\Phi_{a,\ell}(I)|=N.
\]

Moreover each child size is one of

\[
\boxed{
\left\lfloor\frac NM\right\rfloor,
\qquad
\left\lceil\frac NM\right\rceil.
}
\]

The number of nonempty residue children is exactly

\[
\boxed{
\min(M,N).
}
\]

Hence every nonempty child satisfies

\[
|I_a|\le\left\lceil\frac{N}{2^\ell}\right\rceil.
\]

For `N >= 2` and `ell >= 1`,

\[
\boxed{|I_a|<N.}
\]

This is the block-length version of the earlier one-bit interval descent theorem.

---

## 6. Combined channel + interval family quotient

For a source channel `P` and finite interval payload `I`, define

\[
\boxed{
\mathcal F_d(P,I)
=
\left(Q_d(P),\Pi_d(I)\right).
}
\]

Let `B` be the same binary parity block of length `ell <= d` applied to two family representatives with equal `F_d` state.

The source-channel projective theorem gives:

- the same selected parameter residue `m_B mod 2^ell`;
- equal child channel states in `Q_{d-ell}`.

The interval projective theorem then gives:

- the same child emptiness verdict;
- the same child cardinality;
- equal child payload states in `Pi_{d-ell}`.

Therefore, whenever the common child is nonempty,

\[
\boxed{
\mathcal F_d(P,I)=\mathcal F_d(P',I')
\Longrightarrow
\mathcal F_{d-\ell}(P\cdot B,I_B)
=
\mathcal F_{d-\ell}(P'\cdot B,I'_B).
}
\]

This is an exact finite-horizon **family right-congruence** for a common block transition.

Important scope condition: this theorem compares the same block `B`.  Identifying two different blocks requires an additional block-state/right-congruence certificate such as the separately proved correction/ballot quotient.  The present theorem does not silently identify different parity words.

---

## 7. Well-founded finite-horizon rank

Use the lexicographic rank

\[
\boxed{
\mathcal R(I,d)=(|I|,d)\in\mathbb N^2.
}
\]

For a nonempty block child of length `ell >= 1`:

- if `|I| >= 2`, the first coordinate decreases strictly;
- if `|I| = 1`, the child remains a singleton but the remaining precision changes from `d` to `d-ell < d`.

Hence every nonempty finite-horizon block refinement satisfies

\[
\boxed{
\mathcal R(I_B,d-\ell)<_{lex}\mathcal R(I,d).
}
\]

So finite-horizon family recursion is well-founded even if the implementation does not install a special singleton stopping rule.

This does **not** imply a horizon-independent global termination theorem: `d` is fixed at the start of this statement.

---

## 8. Exact symbolic residue-family cover

For a fixed parent channel and block length `ell`, the previously certified map

\[
B\longmapsto m_B\pmod{2^\ell}
\]

is a permutation of all `2^ell` residues.

Let a block/certificate classifier assign each block a state label `sigma`, and define

\[
R_\sigma
=
\{m_B\bmod2^\ell:\;\tau(B)=\sigma\}.
\]

Then the parent parameters assigned to state class `sigma` are exactly

\[
I_\sigma
=
I\cap
\bigcup_{a\in R_\sigma}
\{m:m\equiv a\pmod{2^\ell}\}.
\]

Their exact count is

\[
\boxed{
N_\sigma(I)
=
\sum_{a\in R_\sigma}
\max\left(
0,
\left\lfloor\frac{U-a}{2^\ell}\right\rfloor
-
\left\lceil\frac{L-a}{2^\ell}\right\rceil
+1
\right).
}
\]

If the state classes partition all blocks/residues, then

\[
\boxed{
\sum_\sigma N_\sigma(I)=N.
}
\]

If only an admissible subset of state classes is retained, the same formula gives the exact surviving source count.

### Family-cover induction lemma

Suppose the residue sets `R_sigma` form an exact cover of every currently admissible block cylinder, and every nonempty child family belonging to each retained class has either:

- **A:** a direct closure certificate, or
- **B:** an exact equivalence to an already certified family state,

while any unresolved class is sent through **C:** exact source refinement.

Then the parent family is certified once all nonempty pieces are certified.  No source integer is lost or counted twice because block-to-parameter residues are a permutation and the pullbacks are disjoint.

The lexicographic rank above makes repeated C-refinement well-founded for every fixed finite horizon.

The lemma is exact, but it deliberately does not assert that the sets `R_sigma` themselves already possess a compact global representation.

---

## 9. Finite regression audit

`collatz/src/A0_s1_routeB_projective_interval_family_quotient_certificate.py` checks:

- lower endpoints `L=-12,...,12`;
- interval cardinalities `N=1,...,16`;
- precision `d=1,...,8`;
- every `ell=1,...,d`;
- every residue modulo `2^ell`;
- four deliberately distinct equivalent representatives shifted by `k 2^d`, `k in {-3,-1,1,4}`.

This gives:

- 401,600 residue child-size checks;
- 1,606,400 projective-equivalence comparisons;
- 14,400 complete residue-partition checks;
- 14,400 grouped-cover count checks;
- 82,350 nonempty-child rank checks.

These finite checks audit the implementation.  The theorems above are algebraic and do not depend on the checked range.

---

## 10. DSD audit

### Exact / closed

- `Pi_d=(N,L mod 2^d)` is a sufficient finite-horizon interval payload state;
- equal `Pi_d` states preserve every residue-child emptiness, cardinality and remaining projective state;
- `F_d=(Q_d,Pi_d)` is an exact common-block finite-horizon family right-congruence;
- all length-`ell` residue children form an exact balanced partition;
- `R=(N,d)` strictly decreases lexicographically along every nonempty finite-horizon refinement;
- grouped residue-family counts are exact when the residue sets are known;
- A/B/C family-cover induction is logically valid once the child certificate classes form an exact cover.

### Finite regression only

- the numerical audit domain through `d=8` checks the implementation but is not used to promote a finite computation to a global theorem.

### Still open

1. a compact recursive representation of the admissible residue sets `R_sigma` at arbitrarily large scale;
2. enough A/B state reuse to close large source families without exposing exponentially many residue classes;
3. a horizon-independent/global Route-B correction-language membership decoder;
4. the later global Collatz obligations.

---

## 11. Updated bottleneck

The interval payload is no longer an obstruction to finite-horizon state reuse.  Both control and payload now admit compatible projective quotients:

\[
Q_d\xrightarrow{|B|=\ell}Q_{d-\ell},
\qquad
\Pi_d\xrightarrow{|B|=\ell}\Pi_{d-\ell}.
\]

Therefore the next irreducible problem is not the affine channel and not the finite interval arithmetic.  It is the structure of the admissible residue sets themselves:

\[
\boxed{
\text{Can }R_\sigma\subseteq\mathbb Z/2^\ell\mathbb Z
\text{ be generated, quotiented, and certified recursively without enumerating }2^\ell\text{ residues?}
}
\]

That is the next target for Route-B family-level closure.

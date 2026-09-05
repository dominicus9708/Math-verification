# Finite checkpoint-predicate source-cylinder transport

Status: **EXACT / CLOSED as a finite source-family transport theorem.**

This theorem does **not** define the global checkpoint-surplus sectors, does not provide a global source bound, and does not prove Collatz.  It closes a narrower structural question: once an exact finite source family and an exact finite checkpoint predicate are supplied, the predicate can be transported to and from ordinary sources by exact dyadic source cylinders.

## 1. Starting source family

Let

\[
X(m)=x+A m,
\qquad m\in I\cap\mathbb Z,
\]

where `A` is odd and `I=[m_{lo},m_{hi}]` is a finite integer interval.  Assume all represented source values are positive.

At any current affine state

\[
Y(m)=y+B m,
\]

with `B` odd, the next accelerated Collatz odd event is preceded by

\[
a=v_2(Y(m))\ge0
\]

zero steps.  By `AFFINE_VALUATION_CYLINDER_JUMP.md`, fixing `a` selects exactly one parameter residue class modulo

\[
2^{a+1}.
\]

The corresponding child is again an exact affine source family.

## 2. Iterated valuation word

Fix a finite valuation-gap word

\[
\mathbf a=(a_0,a_1,\ldots,a_{q-1}),
\qquad a_i\ge0.
\]

Define the consumed raw length

\[
H(\mathbf a)=\sum_{i=0}^{q-1}(a_i+1).
\]

Repeated application of the exact valuation-cylinder jump gives either an empty family or a unique nested source-parameter cylinder

\[
\boxed{
m=\rho_{\mathbf a}+2^{H(\mathbf a)}k}
\]

with an exact transformed integer interval

\[
k\in I_{\mathbf a}.
\]

Hence the ordinary source values in this child are exactly

\[
\boxed{
X=R_{\mathbf a}+A2^{H(\mathbf a)}k,
\qquad k\in I_{\mathbf a},
}
\]

where

\[
R_{\mathbf a}=x+A\rho_{\mathbf a}.
\]

After the `q` odd events, the represented orbit state has the exact affine form

\[
\boxed{
T^{H(\mathbf a)}(X)
=Y_{\mathbf a}+3^qA k.
}
\]

Thus every fixed finite valuation word has an exact ordinary-source cylinder and exact orbit endpoint family.

## 3. Exactness and reflection

The construction is bidirectional.

### Forward

Every source in the cylinder for `\mathbf a` realizes exactly the valuation sequence

\[
a_0,a_1,\ldots,a_{q-1}
\]

because each recursion stage imposed the exact valuation congruence

\[
v_2(Y)=a_i.
\]

### Reflection

Conversely, if a source from the parent family realizes the valuation word `\mathbf a`, then at each stage its parameter belongs to the unique valuation residue cylinder selected by that `a_i`.  Hence it belongs to the unique nested cylinder above.

Therefore

\[
\boxed{
X\text{ realizes }\mathbf a
\iff
X\in\Phi_{\mathbf a}(I_{\mathbf a}),
}
\]

where

\[
\Phi_{\mathbf a}(k)=R_{\mathbf a}+A2^{H(\mathbf a)}k.
\]

Distinct valuation words are source-disjoint: at the first differing valuation index they occupy disjoint exact valuation residue classes.

## 4. Finite raw-horizon predicates

A checkpoint predicate need not end exactly on an odd event.  Suppose a finite horizon ends with `\ell>=0` unresolved zero steps after the last realized odd event.

The condition that no additional odd event occurs in those `\ell` steps is

\[
v_2(Y)\ge\ell,
\]

or equivalently

\[
Y\equiv0\pmod{2^\ell}.
\]

Because the affine coefficient is odd, this again selects exactly one parameter residue modulo `2^\ell`.  Thus a finite parity/checkpoint prefix that terminates inside a zero run is also an exact dyadic source cylinder.

Consequently every predicate depending only on a finite raw prefix, or equivalently on finitely many ordered odd-event positions plus a finite terminal no-event condition, admits exact source transport.

## 5. Finite checkpoint predicate theorem

Let `P` be an exact predicate whose truth is determined by finite checkpoint data up to a fixed raw horizon `L`.

Let

\[
\mathcal W_P
\]

be the finite set of valuation/parity-prefix descriptors of length at most `L` that satisfy `P`, including the terminal truncated-zero descriptor where needed.

For every nonempty descriptor `w in W_P`, construct its exact source chart

\[
\Phi_w:I_w\to\mathbb N
\]

by the preceding recursion.

Define

\[
\boxed{
\mathcal D_P
=
\bigsqcup_{w\in\mathcal W_P}\Phi_w(I_w).
}
\]

Then

\[
\boxed{
X\in\mathcal D_P
\iff
X\text{ belongs to the parent source family and satisfies }P.
}
\]

The union is source-disjoint after empty cylinders are removed.

This supplies both the forward transport and reflection required for an exact finite checkpoint-defined source branch **inside the stated parent source family**.

## 6. Application schema to checkpoint surplus

Let

\[
A_s(\sigma)
\]

be an exactly defined checkpoint-surplus predicate for a fixed `s_cp=s`, and suppose `A_s` is determined by finite checkpoint data in the above sense.

Then for every exact finite parent source family `F`, the theorem constructs

\[
\mathcal D_s(F)
=
\{X\in F:A_s(\sigma_X)\},
\]

as a disjoint union of exact ordinary-source cylinders, and

\[
\boxed{
X\in\mathcal D_s(F)
\iff
A_s(\sigma_X)\land R(X,\sigma_X).
}
\]

Here `R` is not an additional statistical assumption: it is the source/orbit provenance supplied by the exact cylinder construction itself.

For `s_cp=1`, the directly recorded checkpoint condition

\[
\tau_{j_0}\le t_0<\tau_{j_0+1}
\]

is a finite checkpoint predicate, so this theorem gives an exact source-cylinder transport mechanism for any exact finite parent family on which that condition is evaluated.

For `s_cp>=2`, the same conclusion is available **once the exact finite predicate defining that sector is supplied**.  This theorem does not invent or infer that missing predicate.

## 7. Relation to the existing late-activation join

`SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md` proves a later local statement: once an exact activation channel, validated terminal suffix, and checkpoint `Z` are supplied, a congruence-plus-interval test proves that they belong to the same ordinary orbit.

The present theorem acts earlier:

\[
\text{finite checkpoint predicate}
\longleftrightarrow
\text{exact source cylinders}.
\]

The activation/checkpoint join acts later:

\[
\text{source activation cylinder}
+\text{terminal descriptor}
+Z
\longleftrightarrow
\text{same-orbit splice}.
\]

These are complementary provenance interfaces and must not be double-counted as independent pruning predicates.

## 8. What this closes and what remains open

### CLOSED

- exact source transport for a fixed finite valuation word;
- exact reflection from the source cylinder back to that word;
- exact transport for a finite raw/checkpoint-prefix predicate;
- disjoint source-cylinder union inside a supplied exact finite parent source family;
- same-source provenance of the transported finite checkpoint state.

### OPEN

- exact global definition/provenance of every live `s_cp>=2` sector;
- proof that the chosen parent source families cover every global counterexample candidate to which the surplus split is intended to apply;
- computationally compressed enumeration of the astronomically large cylinder union at the A0 horizon;
- branch-specific source upper bounds suitable for external finite-range closure;
- Route-A predicate;
- global branch cover and global Collatz.

## 9. DSD classification

The source cylinder is L0 provenance.  The finite checkpoint predicate is an L1/L2 observation on that source orbit.  The theorem proves exact forward preservation and reflection between them.

No quotient or compressed checkpoint coordinate may replace the cylinder construction unless every later source-sensitive predicate is proved to factor through that quotient.

In particular, a difference in surplus-tax, Hensel budget, terminal defect, or projective observation does not create an additional independent source branch after the exact checkpoint predicate has already selected the source cylinder.

## Dependencies

- `AFFINE_VALUATION_CYLINDER_JUMP.md`
- `SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md` (downstream complementary interface; not needed for the core finite-prefix proof)
- `CHECKPOINT_SURPLUS_SOURCE_REALIZATION_TRANSPORT_OBLIGATION.md`

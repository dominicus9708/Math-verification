# A0 s=1 Route-B — boundary predicate-relative quotient

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Purpose

The generic source-channel audit proved that the full future parity semantics cannot merge distinct values of

\[
Y\bmod 2^d.
\]

That no-go applies only when **all future source/parity outputs** must be preserved.

A Route-B proof is allowed to use a coarser equivalence after the preserved predicate is explicitly specified.

This note gives the first exact such quotient for the already defined dyadic/ternary boundary-equality subsystem. It does not use the undefined `C4F` label.

## 2. Boundary observations

For a binary word \(W\) of length \(h\), one-count \(q\), and correction \(C(W)\), define

\[
D_K(W)
=
-C(W)(3^q)^{-1}\pmod{2^K},
\qquad 1\le K\le h,
\]

and

\[
E_L(W)
=
C(W)(2^h)^{-1}\pmod{3^L},
\qquad 1\le L\le q.
\]

These are exactly the start-side dyadic and end-side ternary boundary coordinates used by the Route-B localization machinery.

## 3. Projective nesting theorem

If \(K_1\le K_2\), reduction of the same defining integer congruence gives

\[
\boxed{
D_{K_2}(W)\bmod2^{K_1}=D_{K_1}(W).
}
\]

Likewise, if \(L_1\le L_2\),

\[
\boxed{
E_{L_2}(W)\bmod3^{L_1}=E_{L_1}(W).
}
\]

No structural assumption about Christoffel words is needed for these two identities.

## 4. Nested gate-collapse theorem

Let \(\mathcal K\) and \(\mathcal L\) be finite nonempty requested resolution sets and put

\[
K_*=\max\mathcal K,
\qquad
L_*=\max\mathcal L.
\]

Suppose the target values are compatible reductions of maximal target residues:

\[
d_K=d_{K_*}\bmod2^K,
\qquad
K\in\mathcal K,
\]

\[
e_L=e_{L_*}\bmod3^L,
\qquad
L\in\mathcal L.
\]

Then

\[
\boxed{
\bigwedge_{K\in\mathcal K}[D_K(W)=d_K]
\iff
[D_{K_*}(W)=d_{K_*}],
}
\]

and

\[
\boxed{
\bigwedge_{L\in\mathcal L}[E_L(W)=e_L]
\iff
[E_{L_*}(W)=e_{L_*}].
}
\]

The reverse implications are the only nontrivial directions and follow immediately from projective nesting.

Hence the whole compatible boundary conjunction factors through

\[
\boxed{
\Omega_{K_*,L_*}(W)
=
\bigl(D_{K_*}(W),E_{L_*}(W)\bigr).
}
\]

Equality of \(\Omega\) is therefore an exact **predicate-relative equivalence** for this boundary subsystem.

## 5. Interaction with lazy frontier localization

The existing lazy-boundary theorem says a requested \(D_K\) coordinate may be pushed down the legal left boundary until the next child lacks \(K\) bits of capacity, and \(E_L\) may analogously be pushed down the right boundary.

Therefore, once the nested gate family has been collapsed to \((K_*,L_*)\), only two maximal-resolution frontier observations are required:

\[
D_{K_*}(F_{\rm left}),
\qquad
E_{L_*}(F_{\rm right}).
\]

For the already certified target Christoffel DAG examples, the existing audit localizes

\[
D_{27}
\]

to a length-27 frontier node and

\[
E_{28}
\]

to a length-84 frontier node, even though the base block length is \(J_0=10,439,860,591\).

This target-specific localization is exact but must not be assigned automatically to arbitrary candidate words.

## 6. Why this escapes the generic Y no-go

The generic source-state theorem proves that distinct

\[
Y\bmod2^d
\]

cannot be merged while preserving every length-\(d\) future parity output.

The present quotient asks for less. It preserves only the explicit Boolean boundary predicate.

Thus two states may differ in full source/parity semantics yet satisfy

\[
\Omega_{K_*,L_*}(W)=\Omega_{K_*,L_*}(W').
\]

For the boundary gate, merging them is legal.

There is no contradiction: the equivalence relation changed together with its explicitly stated semantic obligation.

## 7. DSD audit

### Exact / closed

- dyadic boundary observations are projectively nested;
- ternary boundary observations are projectively nested;
- a compatible conjunction of same-block boundary equality gates collapses to the maximal resolution on each axis;
- \(\Omega_{K_*,L_*}\) is an exact predicate-relative quotient for that explicitly defined gate subsystem;
- lazy frontier localization may then be applied only to those two maximal observations.

### Regression

`collatz/src/A0_s1_routeB_boundary_predicate_quotient_certificate.py` exhaustively checks the nesting and conjunction identities through binary word length 7. The algebra above is the proof; the finite test is an implementation guard.

### Not claimed

- this quotient does not preserve correction-language membership;
- it does not preserve pure-ballot or formation predicates unless those coordinates are separately added with their own preservation theorem;
- it does not define or preserve `C4F`;
- it is not yet a renewable long-orbit state;
- it does not prove Route-B closure or the Collatz conjecture.

## 8. Updated G4-S handoff

The next safe step is to form a product of **only explicitly certified predicate coordinates** and ask which coordinates genuinely need long-range renewal.

The boundary-equality component is now reduced to two maximal projective observations rather than an arbitrary stack of nested resolutions.

The remaining long-range complexity must therefore come from interior correction/ballot/formation semantics or from generating the deterministic candidate block itself, not from repeated nested boundary equality gates.

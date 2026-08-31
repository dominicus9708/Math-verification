# A0 s=1 Route-B — family-cover ballot compositional state

Date: 2026-08-31  
Branch: `collatz-stage4-window-threshold`

## 1. Scope

This note closes one missing algebraic component of the Route-B family-cover program.

The existing target-aware ballot diagnostic records, for a binary word `W`,

- `base_min`, and
- a `critical` prefix selected among minimizers by largest fractional phase.

A naive concatenation of these summaries is not valid because

\[
\left\lfloor \frac{R(h+u)}J\right\rfloor
\]

contains a rational-floor carry across the concatenation boundary.

The result below shows that the existing summary nevertheless *is* exactly compositional once this carry is included explicitly.

This is an exact algebraic result.  The finite regression in

`collatz/src/A0_s1_routeB_ballot_compositional_state_certificate.py`

is only a guard against implementation errors.

It does **not** prove universal Route-B membership.

---

## 2. Definitions

Fix a reduced rational slope

\[
\alpha=\frac RJ,
\qquad 0<R<J.
\]

For a binary word \(W\) of length \(h\), let \(q_W(u)\) be the number of ones in its prefix of length \(u\), with \(q_W(0)=0\).

Define

\[
d_W(u)=q_W(u)-\left\lfloor\frac{Ru}{J}\right\rfloor,
\]

and the phase

\[
r(u)=Ru\pmod J,
\qquad 0\le r(u)<J.
\]

The ballot minimum is

\[
b(W)=\min_{0\le u\le h}d_W(u)\le 0.
\]

Let \(c(W)\) be a minimizing prefix for which \(r(c(W))\) is maximal.  If the maximal phase is tied, retain the earlier prefix, matching the existing implementation.

Write

\[
g(W)=r(c(W)).
\]

Also define the endpoint discrepancy and endpoint phase

\[
e(W)=q(W)-\left\lfloor\frac{Rh}{J}\right\rfloor,
\qquad
r(W)=Rh\pmod J.
\]

For phases \(a,b\in\{0,\dots,J-1\}\), define the carry

\[
\kappa(a,b)=
\begin{cases}
1,&a+b\ge J,\\
0,&a+b<J.
\end{cases}
\]

---

## 3. Phase-shift lemma

Suppose a word \(W\) is appended after an already existing prefix whose phase is \(p\).

For a prefix of \(W\) of relative length \(u\), the boundary identity is

\[
\left\lfloor\frac{R(H+u)}J\right\rfloor
=
\left\lfloor\frac{RH}J\right\rfloor
+
\left\lfloor\frac{Ru}J\right\rfloor
+
\kappa(p,r(u)),
\]

where \(p=RH\pmod J\).

Therefore the relative ballot deviation inside \(W\) becomes

\[
d_W^{(p)}(u)=d_W(u)-\kappa(p,r(u)).
\]

### Lemma

\[
\boxed{
\min_u d_W^{(p)}(u)
=
 b(W)-\kappa(p,g(W)).
}
\]

Moreover, after the phase shift, the phase-maximal minimizer is still represented by the original critical prefix \(c(W)\), now viewed at the shifted absolute position.

### Proof

Every term can decrease by at most one, so no shifted value can be below \(b(W)-1\).

If

\[
p+g(W)\ge J,
\]

then the critical base minimizer carries and attains \(b(W)-1\).  Hence the shifted minimum is exactly \(b(W)-1\).  Any shifted minimizer at that level must have had unshifted value \(b(W)\) and must carry.  Among these, shifted phase is monotone in the original phase after subtracting \(J\), so the original critical minimizer remains phase-maximal.

If

\[
p+g(W)<J,
\]

then no base minimizer carries because \(g(W)\) is the largest phase among all base minimizers.  Hence the critical prefix still attains \(b(W)\).  A prefix with unshifted value \(b(W)+1\) can tie \(b(W)\) only by carrying; its shifted phase is then strictly below \(p\), whereas every non-carrying base minimizer has shifted phase at least \(p\).  Thus the phase-maximal shifted minimizer again comes from the base-minimizer set, and the critical one remains selected.

This proves the claim.

---

## 4. Exact composition of the existing ballot summary

Let \(U,V\) be words.

Write

\[
(h_U,q_U,b_U,c_U),
\qquad
(h_V,q_V,b_V,c_V)
\]

for their full ballot states.

Set

\[
e_U=q_U-\left\lfloor\frac{Rh_U}{J}\right\rfloor,
\qquad
r_U=Rh_U\pmod J,
\qquad
g_V=Rc_V\pmod J.
\]

The minimum contributed by prefixes that enter the \(V\) block is

\[
\boxed{
s=e_U+b_V-\kappa(r_U,g_V).
}
\]

The corresponding phase-maximal suffix candidate is

\[
c_s=h_U+c_V.
\]

Therefore

\[
\boxed{
b(UV)=\min(b_U,s).}
\]

The critical prefix is selected exactly as follows:

- if \(b_U<s\), use \(c_U\);
- if \(s<b_U\), use \(c_s\);
- if \(s=b_U\), compare \(Rc_U\pmod J\) and \(Rc_s\pmod J\), using the larger phase; on an exact phase tie retain \(c_U\), which is earlier.

Hence

\[
\boxed{(h,q,b,c)}
\]

is an exact compositional state for the existing ballot summary once the rational-floor carry is included.

Associativity follows because this operation reproduces the state of literal word concatenation.

---

## 5. Compressed ballot-evolution state

For future ballot-minimum propagation, the literal critical index is stronger than necessary.

Define

\[
\boxed{
B(W)=(e,r,b,g)
}
\]

with

\[
e=e(W),\quad r=r(W),\quad b=b(W),\quad g=g(W).
\]

For \(A=B(U)=(e_U,r_U,b_U,g_U)\) and \(B=B(V)=(e_V,r_V,b_V,g_V)\), define

\[
e_{UV}=e_U+e_V-\kappa(r_U,r_V),
\]

\[
r_{UV}=(r_U+r_V)\bmod J,
\]

\[
s=e_U+b_V-\kappa(r_U,g_V),
\]

\[
g_s=(r_U+g_V)\bmod J.
\]

Then

\[
(b_{UV},g_{UV})=
\begin{cases}
(b_U,g_U),&b_U<s,\\
(s,g_s),&s<b_U,\\
(b_U,\max(g_U,g_s)),&b_U=s.
\end{cases}
\]

Thus

\[
\boxed{B(UV)=B(U)\star B(V)}
\]

exactly.

Consequently equality of compressed ballot states is a right congruence for future ballot evolution:

\[
B(U)=B(U')
\quad\Longrightarrow\quad
B(UV)=B(U'V)
\]

for every common suffix \(V\).

### Scope warning

The compressed state stores only the **critical phase** \(g\), not the literal critical-prefix index \(c\).

Therefore it is sufficient for future ballot-minimum/phase evolution, but it may not replace \(c\) in a target diagnostic whose predicate explicitly compares the numerical critical-prefix position.

---

## 6. Combined correction + ballot right-congruence

The correction state obeys

\[
C(UV)=3^{q_V}C(U)+2^{h_U}C(V).
\]

At fixed resolutions \((K,L)\), define the full combined observable state

\[
\boxed{
\Sigma^*_{K,L}(W)
=
\bigl(
 h,q,
 C(W)\bmod2^K,
 C(W)\bmod3^L,
 b,c
\bigr).
}
\]

The correction composition law together with the ballot composition law proves

\[
\boxed{
\Sigma^*_{K,L}(U)=\Sigma^*_{K,L}(U')
\Longrightarrow
\Sigma^*_{K,L}(UV)=\Sigma^*_{K,L}(U'V)
}
\]

for every common suffix \(V\).

So this is an exact fixed-resolution right-congruence for the combined correction/ballot observables.

A coarser version can replace \((h,q,b,c)\)'s ballot role by \((e,r,b,g)\) when the literal critical index is not part of the closure predicate.

---

## 7. Family-cover consequence

For a fixed parent channel and block length \(\ell\), the already certified block-to-parameter theorem gives a bijection

\[
\rho_\ell:\{0,1\}^{\ell}\to\mathbb Z/2^{\ell}\mathbb Z.
\]

Thus the parameter interval is partitioned exactly into block cylinders

\[
I_B=\{m\in I:m\equiv\rho_\ell(B)\pmod{2^\ell}\}.
\]

Group blocks by their combined state \(\Sigma^*_{K,L}\).

For every state class \(s\), define

\[
I_s=
\bigsqcup_{\Sigma^*_{K,L}(B)=s} I_B.
\]

Because the block cylinders are disjoint, the state families remain disjoint unions of exact source residues.

If an A/B closure certificate depends only on \(\Sigma^*_{K,L}\) and is stable under the required continuations, one certificate for state \(s\) certifies every source cylinder in \(I_s\).

This is the exact **family-cover reuse lemma** for state-measurable closure predicates.

---

## 8. Fixed-resolution class-count bound

At a fixed block length \(h=\ell\):

- \(q\) has at most \(\ell+1\) values;
- \(b\in[-\ell,0]\), so at most \(\ell+1\) values;
- \(c\in\{0,\dots,\ell\}\), so at most \(\ell+1\) values;
- the dyadic correction residue has at most \(2^K\) values;
- the ternary correction residue has at most \(3^L\) values.

Therefore the number of combined observable classes satisfies the coarse bound

\[
\boxed{
N_\Sigma(\ell;K,L)
\le
(\ell+1)^3 2^K3^L.
}
\]

For fixed \((K,L)\), this is polynomial in \(\ell\), whereas the raw block family has \(2^\ell\) members.

This establishes a genuine family-compression mechanism at fixed observable resolution.

It does **not** show that the resolutions required for universal Route-B membership remain fixed as \(\ell\to\infty\).

---

## 9. DSD audit

### Exact / closed

1. rational-floor phase-shift lemma;
2. exact composition of `(h,q,base_min,critical)`;
3. exact compressed ballot-evolution monoid `(e,r,b,g)`;
4. exact combined correction/ballot right-congruence at fixed \((K,L)\);
5. exact family-cover reuse for closure predicates measurable in that state;
6. polynomial upper bound on the number of fixed-resolution observable classes.

### Finite computation only

The companion Python certificate exhaustively compares the formulas with direct scans for total word length at most 8 for the actual Route-B slope and five small reduced rational slopes.  These checks validate the implementation; they are not the mathematical proof.

### Still open

The quotient above does not yet prove that two unresolved children with the same observable state have identical **exact affine source-channel** futures.  The existing channel recursion carries exact values such as \(r\) and \(y\), and unresolved C-refinement may distinguish states that the observable quotient merges.

Therefore the next exact question is:

\[
\boxed{
\text{Can the affine channel transition itself be quotiented by a finite or recursively controlled state?}
}
\]

Until that is proved, the new quotient may be used safely for A/B closure predicates that are state-measurable, but not as a blanket merger of unresolved C branches.

Universal correction-language membership and the Collatz conjecture remain open.

---

## 10. Status update

Previous bottleneck:

> ballot information had no certified compositional law suitable for family-state reuse.

Current status:

> that compositionality gap is CLOSED exactly.

New bottleneck:

> extend the family quotient through the exact affine source-channel recursion, or prove enough A/B closures that unresolved C branches never require such a merger.

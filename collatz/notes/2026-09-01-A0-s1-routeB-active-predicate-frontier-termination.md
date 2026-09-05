# A0 s=1 Route-B — active predicate frontier and combined A/B/C termination

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Purpose

The generic source transition state and the Route-B decision state must not be conflated.

The previous source-state lower bound shows that distinct

\[
Y=y\bmod 2^d
\]

cannot in general be merged while preserving every future source-input/parity-output behavior.  Nevertheless, a Route-B predicate coordinate may become permanently decided before the source transition itself is finished.

Therefore split every family node into

\[
\boxed{
\text{transition control}\times\text{active predicate frontier}\times\text{interval payload}.
}
\]

The transition control retains whatever source information is still needed to generate future parity symbols.  The predicate frontier retains only decision coordinates that are still queried.

This distinction is essential: forgetting a decided predicate coordinate is exact; forgetting transition control merely because a predicate coordinate was decided is not generally exact.

## 2. Three-valued predicate status

For each finite-horizon predicate coordinate \(P_j\), use status

\[
\sigma_j\in\{U,P,F\},
\]

where

- \(U\): unresolved;
- \(P\): certified PASS for every continuation still represented by the node;
- \(F\): certified FAIL for every continuation still represented by the node.

The semantics require stability:

\[
P\to P,
\qquad
F\to F
\]

under every later refinement contained in the already certified continuation family.

Thus a coordinate may move only

\[
U\to U,
\qquad
U\to P,
\qquad
U\to F.
\]

It never returns from \(P\) or \(F\) to \(U\).

If the global finite-horizon decision is a conjunction of its active coordinates, then any \(F\) closes the node by rejection.  A \(P\) coordinate can be deleted from the active predicate state because its truth value can no longer affect descendants.

## 3. Coordinates already certified in Route-B

The present repository has exact stability mechanisms for the following coordinates.

### 3.1 Dyadic source boundary

For

\[
X=r+2^h m,
\]

once \(h\ge K\),

\[
X\equiv r\pmod{2^K}
\]

for every parameter \(m\) in the source interval.

Therefore the requested dyadic boundary comparison becomes \(P\) or \(F\) on the entire source family and may then be removed from the predicate frontier.

### 3.2 Ternary endpoint boundary

For

\[
T^h(X)=y+3^q m,
\]

once \(q\ge L\),

\[
T^h(X)\equiv y\pmod{3^L}
\]

for every parameter \(m\).

The requested ternary endpoint comparison likewise becomes stable \(P\) or \(F\).

### 3.3 Ballot-minimum threshold coordinate

Let

\[
b(W)=\min_{0\le u\le h}
\left(q_W(u)-\lfloor\alpha u\rfloor\right),
\]

\[
e(W)=q(W)-\lfloor\alpha h\rfloor,
\]

and let \(\ell\) be the remaining horizon.  Define

\[
\Delta_\alpha(h,\ell)
=
\lfloor\alpha(h+\ell)\rfloor-\lfloor\alpha h\rfloor.
\]

For a gate

\[
b\ge\beta,
\]

exact finite-horizon status is available:

\[
\boxed{b<\beta\Longrightarrow F,}
\]

and

\[
\boxed{
\min\bigl(b,e-\Delta_\alpha(h,\ell)\bigr)\ge\beta
\Longrightarrow P.
}
\]

The latter is in fact equivalent to every binary suffix of length at most \(\ell\) satisfying the minimum gate.

When neither condition holds, the coordinate remains \(U\).

### 3.4 Correction and critical-prefix coordinates

No new absorbing status is assumed here merely from the existence of a correction residue or critical-prefix state.  These coordinates remain \(U\) until an exact existing or future theorem certifies \(P\) or \(F\).

This prevents the active-frontier abstraction from silently promoting a diagnostic state to a membership theorem.

## 4. Exact coordinate-forgetting lemma

Let a family node represent a continuation set \(\mathcal C\).  Suppose predicate coordinate \(P_j\) has status \(P\), meaning

\[
P_j(c)=\mathrm{true}
\qquad
\text{for every }c\in\mathcal C.
\]

Every descendant continuation set \(\mathcal C'\) satisfies

\[
\mathcal C'\subseteq\mathcal C.
\]

Therefore

\[
P_j(c)=\mathrm{true}
\qquad
\text{for every }c\in\mathcal C'.
\]

Hence the coordinate can be removed from every descendant predicate state without changing acceptance or rejection.

The same subset argument shows that an \(F\) coordinate is absorbing and closes the family immediately.

Thus status compression is exact whenever \(P/F\) was certified over the complete represented continuation set.

## 5. Combined A/B/C recursion

Use the following actions.

### A — close by certified failure

If any active coordinate becomes \(F\), reject the whole current source family.

### B — discharge certified success

If one or more unresolved coordinates become \(P\), remove them from the active predicate frontier without splitting the source interval.

### C — exact source refinement

If unresolved coordinates remain and no A/B action decides them, refine the source parameter interval by an exact next-bit residue class.

For one-bit refinement of a finite nonsingleton integer interval \(I\), the existing source-interval theorem gives

\[
|I_{\rm child}|<|I|.
\]

No C-action is needed at a singleton merely to make the interval rank decrease.

## 6. Combined well-founded rank

Let

\[
u=\#\{j:\sigma_j=U\}
\]

be the number of unresolved predicate coordinates.  Define

\[
\boxed{
\mathcal M(I,\sigma)=\bigl(|I|,u\bigr)
}
\]

with lexicographic order on \(\mathbb N\times\mathbb N\).

Then:

- A terminates the branch;
- B leaves \(|I|\) unchanged and strictly decreases \(u\);
- C on a nonsingleton leaves the status count arbitrary but strictly decreases \(|I|\).

Therefore every nonterminal A/B/C action strictly advances a well-founded process, and no single branch can undergo infinitely many exact family refinements or predicate discharges.

More explicitly, starting with interval size \(N\) and \(u_0\) unresolved coordinates, the number of B-actions along a branch is at most \(u_0\), while the number of one-bit C-actions before singleton identification is at most

\[
\lceil\log_2 N\rceil
\]

under the existing parity-halving interval refinement.

Thus a coarse per-branch action bound is

\[
\boxed{
N_{\rm actions}
\le
u_0+\lceil\log_2 N\rceil
}
\]

before either A-closing, all predicate coordinates being discharged, or singleton identification.

This is a branch-depth bound, not a total-tree-size bound.

## 7. Transition control is not predicate state

A crucial scope rule is

\[
\boxed{
\text{predicate coordinate discharged}
\not\Rightarrow
\text{source transition coordinate dispensable}.
}
\]

For example, after the dyadic source boundary comparison has become \(P\), future parity generation may still require the projective source state

\[
Q_d=(y\bmod2^d,3^q\bmod2^d).
\]

The previously proved generic \(Y\)-minimality theorem therefore remains intact.

The gain from the active frontier is different: already decided observations no longer multiply the decision-state space, and future theorems are allowed to use coarser transition control whenever the remaining active predicate is shown not to query the discarded information.

## 8. State architecture

A safe finite-horizon family state is therefore conceptually

\[
\boxed{
\mathfrak S
=
\left(
Q_d,
\Pi_d(I),
\sigma_{\rm active},
S_{\rm active}
\right),
}
\]

where

- \(Q_d\): transition control;
- \(\Pi_d(I)\): projective interval payload when finite lookahead suffices;
- \(\sigma_{\rm active}\): unresolved/P/F status information;
- \(S_{\rm active}\): only the correction/ballot/critical data still queried by unresolved predicate coordinates.

Whenever a coordinate is certified \(P\), its associated observation fields may be deleted from \(S_{\rm active}\), provided they are not independently needed by \(Q_d\) or another unresolved predicate.

This is a dependency-aware quotient rather than a blind tuple projection.

## 9. DSD audit

### Exact / closed

- stable P/F predicate coordinates can be forgotten/absorbed by subset monotonicity;
- existing source-boundary predicates supply exact family-level P/F states;
- the ballot-minimum threshold supplies exact finite-horizon P/F conditions for that coordinate;
- the combined A/B/C recursion is well founded on the SAFE finite source forest;
- transition control and predicate observations are formally separated.

### Not a complexity proof

The rank proves termination of every branch.  It does not bound the total number of distinct branches by a polynomial and does not yet prove enough B-merging to avoid a large tree.

### Not inferred

- correction-language membership is not discharged merely by storing correction residues;
- critical-prefix constraints are not discarded unless independently certified;
- generic \(Y\) transition states are not merged by this theorem;
- universal Route-B membership and the Collatz conjecture remain open.

## 10. Next bottleneck

The next useful target is not another generic source quotient.  It is to expand the set of exact P/F certificates for the remaining active interior coordinates.

The existing lazy-boundary theorem suggests the first candidate: correction observations localize to two frontiers.  If a word is decomposed as

\[
W=UMV,
\]

with a sufficiently long left block \(U\) for the dyadic observation and a suffix \(V\) containing sufficiently many ones for the normalized ternary observation, then the entire middle block \(M\) is invisible to those two correction boundary coordinates.

Formalizing that two-front middle-invisibility theorem is the next step toward family closure without singleton expansion.

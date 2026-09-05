# A0 s=1 Route-B formation-cylinder renewal theorem

Date: 2026-08-31

Status: **exact formation-automaton theorem / macrostate extraction**.

This note strengthens the existing formation target-residue description.  The
old path-count lemma records that a fixed nonincreasing rank path contributes
at most one target residue modulo `3^K`.  Here we retain enough information to
transport the entire incoming carry family, the outgoing carry, all
intermediate carry constraints, and exact block composition.

Nothing in this note is a global Collatz proof.

---

## 1. Formation recurrence

For a fixed nonincreasing rank path

\[
a_0\ge a_1\ge\cdots\ge a_K\ge0,
\]

write

\[
d_j=2(2^{a_j}-2^{a_{j+1}}).
\]

The established formation recurrence is

\[
\boxed{
 c_{j+1}=\frac{2c_j+d_j}{3}.
}
\]

A step is legal only when the numerator is divisible by 3.

---

## 2. Formation Cylinder Theorem

### Theorem

For every fixed rank path of length `K`, there exists a unique pair

\[
(\rho_K,\gamma_K),
\qquad 0\le\rho_K<3^K,
\]

such that

\[
\boxed{
 c_0=\rho_K+3^K n
}
\]

is exactly the set of incoming carries for which all first `K` formation
steps are integral, and on the same integer parameter `n`,

\[
\boxed{
 c_K=\gamma_K+2^K n.
}
\]

Thus one fixed rank path is an exact arithmetic cylinder from a ternary source
family to a dyadically scaled outgoing carry family.

### Induction

At depth zero,

\[
\rho_0=\gamma_0=0.
\]

Suppose after `j` steps

\[
c_0=\rho_j+3^j n,
\qquad
c_j=\gamma_j+2^j n.
\]

The next step is integral iff

\[
2\gamma_j+d_j+2^{j+1}n\equiv0\pmod3.
\]

Since `2^(j+1)` is invertible modulo 3, exactly one

\[
\tau_j\in\{0,1,2\}
\]

satisfies

\[
\boxed{
\tau_j\equiv
-(2\gamma_j+d_j)(2^{j+1})^{-1}
\pmod3.
}
\]

Write

\[
n=\tau_j+3n'.
\]

Then

\[
\boxed{
\rho_{j+1}=\rho_j+3^j\tau_j
}
\]

and

\[
\boxed{
\gamma_{j+1}
=
\frac{2\gamma_j+d_j+2^{j+1}\tau_j}{3}.
}
\]

The residue digit is unique at every step, so the final source cylinder is
unique modulo `3^K`.

---

## 3. Every intermediate carry uses the same family parameter

Let `(rho_j,gamma_j)` be the summary of the first `j` transitions and let
`rho_K` be the final source residue.  Because the final cylinder refines every
prefix cylinder,

\[
\rho_K\equiv\rho_j\pmod{3^j}.
\]

Define

\[
\nu_j=\frac{\rho_K-\rho_j}{3^j},
\qquad
\beta_j=\gamma_j+2^j\nu_j.
\]

For a final-family member

\[
c_0=\rho_K+3^K n,
\]

we obtain at every intermediate depth

\[
\boxed{
 c_j=\beta_j+2^j3^{K-j}n.
}
\]

The coefficient of `n` is strictly positive.

Therefore a conjunction of any fixed carry corridors

\[
L_j\le c_j\le U_j,
\qquad 0\le j\le K,
\]

reduces exactly to one integer interval

\[
\boxed{
N_-\le n\le N_+.
}
\]

In particular, all-carry nonpositivity or nonnegativity is one half-line in
`n`.  No individual carry-family representatives need to be enumerated.

This is stronger than keeping only an endpoint target residue.

---

## 4. Exact block composition

Let a left block `P` have summary

\[
(K,\rho_P,\gamma_P)
\]

and a right block `Q`, beginning at the same boundary rank at which `P` ends,
have summary

\[
(L,\rho_Q,\gamma_Q).
\]

After `P`,

\[
c_{\rm mid}=\gamma_P+2^K n.
\]

For `Q` to begin legally, this must lie in its source cylinder:

\[
\gamma_P+2^K n
\equiv\rho_Q\pmod{3^L}.
\]

Because `2^K` is invertible modulo `3^L`, there is exactly one bridge residue

\[
\boxed{
\tau\equiv
(\rho_Q-\gamma_P)(2^K)^{-1}
\pmod{3^L}.
}
\]

Write

\[
n=\tau+3^L m.
\]

Then the composed source residue is

\[
\boxed{
\rho_{PQ}=\rho_P+3^K\tau,
}
\]

while

\[
\eta=
\frac{\gamma_P+2^K\tau-\rho_Q}{3^L}
\]

gives

\[
\boxed{
\gamma_{PQ}=\gamma_Q+2^L\eta.
}
\]

Thus

\[
\boxed{
(K,\rho_P,\gamma_P)
\odot
(L,\rho_Q,\gamma_Q)
=
(K+L,\rho_{PQ},\gamma_{PQ}).
}
\]

This is exact relation composition.  Associativity follows because both
parenthesizations represent the same composed arithmetic relation.

---

## 5. Path-family cardinality corollary

Starting from rank `k`, a length-`K` formation path is a weakly decreasing
sequence

\[
k=a_0\ge a_1\ge\cdots\ge a_K\ge0.
\]

There are

\[
\boxed{
\binom{K+k}{k}
}
\]

such paths.

Since each path contributes at most one formation source cylinder modulo
`3^K`, before deduplication the full length-`K` formation relation from fixed
rank `k` is a union of at most

\[
\boxed{
\binom{K+k}{k}
}
\]

arithmetic cylinder families, each additionally carrying its exact outgoing
carry map and its exact admissible `n` interval.

For fixed `k`, this is polynomial growth in `K`, not `3^K` enumeration.

This recovers the old formation-path cardinality lemma and strengthens its
state content.

---

## 6. Interface with the 14-root physical forest

The remaining A0 search is already represented by 14 disjoint physical
channel roots

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with finite `m` intervals.  Each binary refinement selects one parity of `m`
and exactly partitions its parent interval.

Separately, the 72-bit physical-address theorem says that after the source
address is completely exposed, every later parity bit is deterministic from
that unique physical `X`.

Consequently the arithmetic part of the next long-membership bridge can now be
organized as a fibered family calculation:

\[
\text{physical channel family}
\longrightarrow
\text{deterministic parity macroblock}
\longrightarrow
\begin{cases}
\text{correction/channel macrostate},\\
\text{phase-covariant ballot macrostate},\\
\text{formation-cylinder macrostate}.
\end{cases}
\]

The three components must be tied to the same physical family parameter; they
must not be proved on unrelated witnesses and then glued afterward.

---

## 7. What has actually closed

The formation arithmetic itself is no longer a step-by-step/singleton
obstruction for a fixed rank path:

- exact source residue family: CLOSED;
- exact outgoing carry family: CLOSED;
- exact intermediate carry path: CLOSED;
- exact sign/corridor filtering as one parameter interval: CLOSED;
- exact macroblock composition: CLOSED;
- fixed-rank path-count compression: CLOSED.

The remaining obstruction has moved one level upward:

> **Deterministic rank-path renewal problem.**  Show that every surviving
> physical Route-B family can determine, certify, or safely partition the
> formation rank path of its next long deterministic macroblock using a
> recursively renewable state, without reverting to singleton orbit
> enumeration.

Equivalently, the missing piece is no longer the arithmetic action *given* a
rank path.  It is the semantic rule that selects/partitions the rank path from
the actual deterministic Route-B orbit.

---

## 8. DSD audit

✅ formation domain and legality rule are explicit;

✅ a fixed rank path has one exact ternary source cylinder;

✅ all intermediate/output carries use one common family parameter;

✅ fixed finite sign/interval predicates remain exact under family transport;

✅ adjacent formation macrostates compose exactly;

✅ fixed-rank family count is bounded by the proved path count;

✅ same-parameter discipline prevents cross-witness gluing when joined to the
physical/dyadic channel;

⚠️ deterministic physical orbit -> formation rank-path selection/partition is
not yet proved recursively;

⚠️ no finite or well-founded renewal theorem for arbitrary long Route-B
segments is proved here;

❌ no Route-B global closure is claimed;

❌ no Collatz conjecture proof is claimed.

## Gate update

The next narrow gate is

\[
\boxed{
\textbf{G4-S2: deterministic formation rank-path renewal.}
}
\]

A successful G4-S2 theorem should take one physical channel family plus its
current semantic macrostate and return a finite family partition whose next
formation macrostates are certified, with either exact state recurrence or a
well-founded descent rank preventing indefinite refinement.

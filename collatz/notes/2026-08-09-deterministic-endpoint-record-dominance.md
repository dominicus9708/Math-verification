# Deterministic endpoint dominance for coefficient-stopping records

Date: 2026-08-09

Status: **DERIVED LEMMA + SCOPE SEPARATION FROM MIN-SURVIVOR DOMINANCE**

This note concerns deterministic future evolution of already fixed integer starts and the inverse record function

\[
M(B)=\max_{1\le n<2^B}\tau_c(n),
\]

not future canonical lifts used in the exact `mu(K)` search.

## 1. Why the earlier counterexample does not apply here

The global endpoint-only dominance rule failed for `mu(K)` because a future canonical lift changes an endpoint by `3^q`, so equal current endpoints with different `q` need not have equal lifted futures.

For a fixed actual integer start after all relevant start bits are fixed, there is no future canonical lift.  If two trajectories reach the same actual endpoint `y`, their subsequent numerical orbit from `y` is identical.

Only their accumulated depth and odd-count credit differ.

Therefore endpoint merging remains useful for deterministic coefficient-stopping records, but it requires a different theorem and objective.

## 2. Mechanical coefficient boundary

Let

\[
\alpha=\log_3 2,
\qquad
a_k=\lceil\alpha k\rceil.
\]

A state `(k,q,y)` survives the coefficient barrier for `j` additional actual steps iff

\[
q+u_j(y)\ge a_{k+j},
\]

where `u_j(y)` is the number of odd entries in the first `j` future steps of the fixed orbit starting at `y`.

For an integer depth difference `h>=0`, the elementary ceiling inequality gives

\[
\boxed{
a_{n+h}-a_n\le\lceil\alpha h\rceil.}
\]

## 3. Same-endpoint later-arrival dominance

Consider two fixed-trajectory states with the same endpoint:

\[
S_1=(k_1,q_1,y),
\qquad
S_2=(k_2,q_2,y),
\]

and assume

\[
\boxed{k_1\ge k_2}
\]

and

\[
\boxed{
q_1-q_2
\ge
\left\lceil\alpha(k_1-k_2)\right\rceil.
}
\]

Then state 1 dominates state 2 for the **total coefficient stopping time**.

### Proof

Put

\[
h=k_1-k_2\ge0.
\]

If state 2 survives `j` future steps, then

\[
q_2+u_j(y)\ge a_{k_2+j}.
\]

Using the assumed credit difference,

\[
q_1+u_j(y)
\ge
q_2+u_j(y)+\lceil\alpha h\rceil
\ge
 a_{k_2+j}+\lceil\alpha h\rceil.
\]

But

\[
a_{k_1+j}
=a_{k_2+j+h}
\le
 a_{k_2+j}+\lceil\alpha h\rceil.
\]

Hence

\[
q_1+u_j(y)\ge a_{k_1+j}.
\]

So state 1 survives at least as many **additional** steps after the merge as state 2.
Since also `k_1>=k_2`, its total coefficient-stopping depth is no smaller.

Therefore state 2 cannot set a larger deterministic record and may be removed in a max-stopping computation.

## 4. Same-depth case

When

\[
k_1=k_2,
\]

the criterion reduces to

\[
q_1\ge q_2.
\]

Thus among fixed actual trajectories that meet at the same depth and same endpoint, only the largest accumulated odd-count can matter for the future coefficient-stopping record.

This same-depth deterministic statement is valid even though the analogous canonical-lift statement for `mu(K)` is false.

## 5. Cross-depth examples already present in the repository

The existing branch profiles contain merges

\[
T^{56}(703)=13211=T^{54}(1583).
\]

Their accumulated odd counts are

\[
q_{56}(703)=38,
\qquad
q_{54}(1583)=36.
\]

Here

\[
k_1-k_2=2,
\qquad
\lceil2\alpha\rceil=2,
\qquad
q_1-q_2=2,
\]

so the dominance criterion holds at equality.
Indeed the exact coefficient stopping times are

\[
\tau_c(703)=81,
\qquad
\tau_c(1583)=78.
\]

Similarly,

\[
T^{73}(10087)=28403=T^{72}(15131),
\]

with

\[
q_{73}(10087)=47,
\qquad
q_{72}(15131)=46.
\]

Again the criterion holds at equality because

\[
\lceil\alpha\rceil=1,
\]

and the exact stopping times are

\[
\tau_c(10087)=105,
\qquad
\tau_c(15131)=78.
\]

These numerical values are checks, not ingredients of the proof.

## 6. Important non-example

Another repository merge is

\[
T^{135}(432923)=86751245=T^{137}(577231).
\]

The first state arrives **earlier**:

\[
135<137.
\]

Although its coefficient-credit requirement is not worse in the simple additional-step comparison, the theorem above does not apply because total stopping time includes the two already accumulated steps of the later state.

Indeed

\[
\tau_c(432923)=149,
\qquad
\tau_c(577231)=151.
\]

Thus the condition `k_1>=k_2` is essential for this simple total-record dominance rule.

## 7. Record-function consequence

When computing

\[
M(B)=\max_{n<2^B}\tau_c(n),
\]

one may propagate fixed trajectories and maintain, for each encountered endpoint `y`, only labels `(k,q)` that are not dominated by the preorder

\[
\boxed{
(k_1,q_1)\succeq(k_2,q_2)
\quad\text{if}\quad
k_1\ge k_2
\text{ and }
q_1-q_2\ge\lceil\alpha(k_1-k_2)\rceil.
}
\]

This is a safe max-record quotient.

It is separate from the finite-horizon min-plus quotient used to compute `mu(K)`.

## 8. Relation to the proof target

The repository already uses the generalized inverse relation

\[
M(B)>K
\iff
\mu(K)<2^B.
\]

Therefore any structural upper bound on `M(B)` translates into growth of `mu(K)`.
The deterministic endpoint quotient is relevant to that route because it can remove merged trajectories that cannot improve the record.

No asymptotic bound on `M(B)` is proved here; only the exact merge-pruning criterion is established.

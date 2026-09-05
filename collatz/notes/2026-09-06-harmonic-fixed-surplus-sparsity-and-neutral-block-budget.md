# Harmonic fixed-surplus sparsity and the neutral-block budget

Date: 2026-09-06

## Status

- **SAFE LEMMA:** on any hypothetical nonperiodic positive-integer orbit that never descends below its start, visits to every fixed Beatty-surplus strip at completed odd-event checkpoints are `O_N(q^(1/9))`.
- **SAFE CONSEQUENCE:** the formal `d=2, e=delta` neutral macro-pair channel has zero asymptotic density on any such actual orbit.
- **AUDIT CORRECTION:** the neutral Sturmian path remains a genuine barrier to a purely symbolic fixed-Q7 statewise proof, but it is not an asymptotically persistent path of a hypothetical minimal divergent positive integer once the previously proved harmonic corridor is included.
- **OPEN:** control the remaining unbounded sublinear critical meander and transfer that control to the finite selector/candidate language strongly enough for terminal extinction.

No Collatz proof is claimed.

---

## 1. Previously proved harmonic input

For a fixed odd positive integer `N>=3` with a nonperiodic odd-to-odd Syracuse orbit

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}},
\qquad
A_i=\sum_{j<i}v_j,
\]

assume the orbit never descends below its start.  This is automatic for a hypothetical minimal positive counterexample: if an iterate fell below `N`, minimality would make that smaller iterate converge and hence make `N` converge.

The previously audited harmonic-correction theorem gives

\[
\boxed{
\sum_{i=0}^{q-1}\lambda_i
\le C_N q^{1/9},
\qquad
\lambda_i:=\frac{2^{A_i}}{3^i},
}
\]

for all sufficiently large `q`, with a constant `C_N` depending on the fixed start.

The proof uses only the exact product identity, distinctness of a nonperiodic orbit, the fact that post-initial odd states lie in `1,5 mod 6`, and the maximal reciprocal sum of distinct admissible states.  It does not assume Collatz convergence or a parity-density theorem.

Source already in the repository:

`collatz/notes/2026-08-11-harmonic-correction-corridor.md`.

---

## 2. Bridge to Beatty surplus

Let

\[
\Theta_i:=\frac{3^i}{2^{A_i}}=\lambda_i^{-1}.
\]

At the completed odd-event binary checkpoint `L=A_i`, the exact coordinate bridge gives

\[
\boxed{
d_{A_i}
=\left\lfloor\log_3\Theta_i\right\rfloor.
}
\]

Therefore if

\[
0\le d_{A_i}\le D,
\]

then

\[
\Theta_i<3^{D+1}
\]

and hence

\[
\boxed{
\lambda_i>3^{-(D+1)}.
}
\]

---

## 3. Fixed-surplus visit bound

Define

\[
V_D(q)
:=
\#\{0\le i<q:0\le d_{A_i}\le D\}.
\]

Every counted index contributes more than `3^{-(D+1)}` to the harmonic sum.  Thus

\[
3^{-(D+1)}V_D(q)
<
\sum_{i<q}\lambda_i
\le C_Nq^{1/9}.
\]

Consequently

\[
\boxed{
V_D(q)
\le
3^{D+1}C_Nq^{1/9}.
}
\]

For every fixed `D`,

\[
\boxed{
V_D(q)=O_N(q^{1/9})=o(q).
}
\]

Status: **SAFE LEMMA**.

For the neutral level `d=2` specifically,

\[
\boxed{
\#\{i<q:d_{A_i}=2\}
\le27C_Nq^{1/9}.
}
\]

---

## 4. Consequence for the neutral Beatty macro-pair channel

A fully neutral Beatty macro-pair satisfies

\[
d=2,
\qquad
e_k=\delta_k
\]

throughout the block.

The allowed macro-pairs are

\[
AB,\ BA,\ BB
\]

with respectively 3, 3, and 4 Beatty rises.  Under `e=delta`, those rises are actual odd parity events.  Hence every disjoint fully neutral macro-pair contains at least three completed odd-event checkpoints with surplus `d=2`.

If `N_neut(q)` is the number of disjoint fully neutral macro-pairs encountered before the first `q` completed odd events, then

\[
\boxed{
N_{\rm neut}(q)
\le\frac13V_2(q)
\le9C_Nq^{1/9}.
}
\]

Thus

\[
\boxed{
N_{\rm neut}(q)=o(q).
}
\]

Status: **SAFE CONSEQUENCE**.

So the exactly neutral ratio-one macro-pair channel cannot occupy positive asymptotic density on a hypothetical minimal divergent positive-integer orbit.

---

## 5. Reconciliation with the new Q7 barrier

The recently proved Q7 boundary-following barrier remains correct:

- in the unrestricted symbolic `(d,z)` graph, the path `d=2, e=delta` exists forever;
- Q7 reverse potential cannot kill it pathwise, and its local maximum potential stays below the coefficient scale needed at `d=2`.

The present lemma says something different:

> the full arithmetic of an actual fixed positive integer satisfying the minimal-counterexample no-descent condition cannot spend asymptotically many macro-pairs on that formal neutral path.

Therefore the correct DSD interpretation is

\[
\boxed{
\text{Q7 neutral path}
=
\text{barrier to pure finite-state statewise killing},
}
\]

not

\[
\text{a surviving asymptotic terminal branch of an actual positive integer}.
\]

This distinction removes an unnecessary duplicate terminal gate.

---

## 6. Relation to the `F_44` same-integer certificate

The exact `F_44` meet-in-the-middle certificate independently shows that the root-aligned neutral word has

\[
\#I_{46}=1,
\qquad
\#I_{47}=0.
\]

That is a finite same-integer cross-base fact.

The harmonic fixed-strip lemma is asymptotic and pathwise for any fixed hypothetical minimal divergent start, but its constant depends on that start.

The two results therefore have complementary scopes:

- `F_44` MITM: strong finite exact cross-base extinction at one selector layer;
- harmonic sparsity: parameter-universal exponent `1/9` for every fixed actual no-descent nonperiodic orbit, but with start-dependent constant.

Neither should be substituted for the other.

---

## 7. What remains after removing the neutral asymptotic branch

The earlier R2 audit already shows that a genuine eventual coefficient-survival candidate must form an **unbounded sublinear critical meander**:

\[
\text{signed skew}
\gtrsim
(8/9-o(1))\log_2 i
\]

on a density-one set of odd-event indices, while the López--Stoll rational noncyclic density condition requires

\[
\liminf\frac{s_i}{i}=0.
\]

Thus the surviving asymptotic obstacle is not a bounded `d=2` Sturmian channel.  It is

\[
\boxed{
\text{unbounded but sublinear surplus/skew meander}
}
\]

whose low fixed strips are sparse but which must return arbitrarily close to critical density on a sublinear scale.

This is precisely the regime in which:

1. fixed-Q reverse potential becomes too weak at high surplus;
2. adaptive strong-reverse residues become exponentially rare;
3. global selector min/max and global Fourier-energy mixing hit the support barrier;
4. support-aware Hamming/tail-budget transfer and same-integer cross-base structure are still required.

---

## 8. Revised next target

The highest-value analytic target is now a **moving-strip selector transfer theorem**, not a fixed-neutral-tail exclusion.

One useful form is to transfer the harmonic moving-strip sparsity to the actual finite selector/canonical candidate language with enough quantitative dependence on the start/selector depth to obtain a uniform log budget.

Equivalently, combine

\[
\boxed{
\#\{i<q:s_i\le\delta\log_2q\}
=O_N(q^{1/9+\delta}),
\qquad \delta<8/9,
}
\]

with the support-aware Beatty/Hamming contraction on the complementary high-meander region, while retaining the integer atom-floor closure.

This avoids trying to solve the bare critical Sturmian conjugacy problem and focuses the proof program on the genuinely surviving DSD cross-base gate.

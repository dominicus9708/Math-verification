# Cerdà 2-adic survival sets — independent reproduction audit

Date: 2026-09-07

Source family:
- Miguel Cerdá Bennassar, *I. 2-adic Structure of Tails and Survival Sets in the Collatz Dynamics*, Zenodo DOI `10.5281/zenodo.18831439`.
- Miguel Cerdá Bennassar, *II. Cylinder collision, bit non-reuse and effective non-degeneracy in the 2-adic Collatz dynamics*, Zenodo DOI `10.5281/zenodo.18831527`, current maintenance version as of 2026-09-07.

Status: **REPRODUCTION AUDIT COMPLETE.** The exact geometric decay of the restricted survival-set Haar measure is independently derivable from finite valuation cylinders and is upgraded from `PROVISIONALLY SAFE / REPRODUCTION AUDIT PENDING` to **SAFE WITHIN ITS RESTRICTED SURVIVAL DEFINITION**. This does not imply emptiness of the infinite survivor and does not prove Collatz.

---

## 1. Compressed odd map

For an odd 2-adic integer `x`, define

\[
k(x)=v_2(3x+1)\ge1,
\qquad
D(x)=\frac{3x+1}{2^{k(x)}}.
\]

For a finite exact valuation itinerary

\[
\mathbf k=(k_0,k_1,\ldots,k_m),
\qquad k_i\ge1,
\]

write

\[
K_j:=\sum_{i=0}^{j-1}k_i.
\]

The orbit relation is

\[
x_{i+1}=D(x_i),
\qquad
3x_i+1=2^{k_i}x_{i+1}.
\]

---

## 2. Exact finite itinerary cylinder

Iterating the inverse affine relation gives

\[
3^m x_0=2^{K_m}x_m-C_{\mathbf k}
\]

for an integer constant `C_k` determined by the finite itinerary. Since `3^m` is a 2-adic unit and `x_m` is odd, fixing `k_0,...,k_{m-1}` selects exactly one odd residue class modulo

\[
2^{K_m+1}.
\]

Equivalently, with Haar measure normalized so that the odd 2-adic integers have mass one,

\[
\boxed{
\mu(\mathcal C(k_0,\ldots,k_{m-1}))=2^{-K_m}.
}
\]

This is the run-length form of the standard finite parity-vector cylinder bijection.

Distinct exact valuation itineraries are disjoint: the valuation sequence is recovered directly from the orbit by `v_2(3x_i+1)`. Thus no additional probabilistic independence assumption is needed.

**DSD status: SAFE EXACT CYLINDER FACT.**

---

## 3. Exact half-decay of the restricted survivor

Fix the initial class `C_{k_0}`. The restricted survival condition used in the audited Cerdà framework is that each subsequent compressed odd state avoids the valuation-one branch, i.e.

\[
k_i\ge2
\]

for each required survival step.

For one further step, the conditional Haar mass is

\[
\sum_{k\ge2}2^{-k}=\frac12.
\]

For `N` further restricted steps, disjoint cylinder summation gives

\[
\frac{\mu(S_N^*\cap C_{k_0})}{\mu(C_{k_0})}
=
\sum_{k_1,\ldots,k_N\ge2}
2^{-(k_1+\cdots+k_N)}
=
\left(\sum_{k\ge2}2^{-k}\right)^N
=2^{-N}.
\]

Hence

\[
\boxed{
\mu(S_N^*\cap C_{k_0})=2^{-N}\mu(C_{k_0}).
}
\]

In particular, by continuity from above,

\[
\boxed{
\mu(S_\infty^*\cap C_{k_0})=0.
}
\]

This reproduces the quantitative theorem without importing a stochastic model and explains the paper-II `bit non-reuse` statement as disjointness of exact finite valuation cylinders.

**DSD verdict: SAFE / ABSORBABLE AS A MEASURE THEOREM.**

---

## 4. What this theorem does not prove

The reproduced theorem is measure-theoretic. It does not give

\[
\mu(S_\infty^*)=0
\Longrightarrow
S_\infty^*=\varnothing.
\]

A singleton or any Haar-null 2-adic set may remain.

Nor does escape from this restricted survivor imply convergence. Leaving the survivor can mean entering the valuation-one class `C_1`. For ordinary integers,

\[
9\in C_2,
\qquad
D(9)=7\in C_1,
\qquad
D(7)=11>7.
\]

Thus `entry into C_1` is not itself a strict-descent terminal event.

The exact terminal upgrade still requires a separate theorem that tracks the same ordinary integer after exit.

---

## 5. Relation to the later Cerdà series

The author's later 2026 papers develop stronger `bit budget`, `portal`, and `rigid regime` reductions. Current consolidated descriptions explicitly retain a remaining entry-map / invariance / arithmetic criterion rather than presenting the local half-decay theorem alone as a complete Collatz proof.

This audit therefore absorbs only what has been independently reconstructed here:

1. exact finite valuation cylinders;
2. noncollision of distinct finite valuation itineraries;
3. exact factor-`1/2` survival decay per restricted step;
4. Haar-null infinite restricted survivor.

Any stronger pointwise claim about all positive integers must be audited under its own hypotheses and cannot be inferred from items 1–4.

---

## 6. Citation policy

### Positive citation

Cerdà II may be cited positively for the exact cylinder/noncollision structure and exact restricted-survival measure decay.

### Boundary citation

The same paper family is also useful as an explicit external reminder that

\[
\text{Haar measure zero}\not\Rightarrow\text{emptiness}.
\]

### Prohibited upgrade

Do not cite the measure theorem as pointwise convergence, and do not replace the ordinary-integer terminal gate by a purely 2-adic density statement.

---

## 7. Revision of the 2026-09-06 audit

The earlier note

`collatz/notes/2026-09-06-external-cerda-2adic-survival-set-audit.md`

classified the multi-step quantitative theorem as `PROVISIONALLY SAFE / REPRODUCTION AUDIT PENDING`.

The present independent cylinder summation closes that pending item:

\[
\boxed{
\text{MULTI-STEP RESTRICTED SURVIVAL MEASURE THEOREM: SAFE.}
}
\]

The earlier terminal-hinge warning remains unchanged:

\[
\boxed{
\text{MEASURE ZERO / RESTRICTED ESCAPE}\not\Rightarrow\text{COLLATZ CONVERGENCE}.
}
\]
# DSD audit / partial absorption — Cerdà 2-adic tail and survival-set framework

Date: 2026-09-06

Source: Miguel Cerdá Bennassar, *Estructura 2-ádica de las colas y conjuntos de supervivencia en la dinámica de Collatz*, Zenodo DOI `10.5281/zenodo.18685073` (February 2026), with the follow-up *Colisión de cilindros, no reutilización de bits y no degeneración efectiva en la dinámica 2-ádica de Collatz*.

Status: **PARTIAL ABSORPTION.**  The local valuation-class arithmetic and one-step cylinder bisection are useful exact structure.  The paper is commendably explicit that measure-zero survival is weaker than emptiness.  However, the claimed equivalence between emptiness of the restricted survival set and convergence in `C_2` uses an unproved `k'=1 -> convergence to 1` bridge and is not established by the displayed argument.

---

## 1. Accelerated odd map

Use

\[
D(p)=\frac{3p+1}{2^{v_2(3p+1)}}
\]

on positive odd integers.

Define

\[
C_k=\{p:v_2(3p+1)=k\}.
\]

---

## 2. SAFE local theorem: exact valuation class

For every `k>=1`, the exact condition

\[
v_2(3p+1)=k
\]

selects exactly one odd residue class modulo

\[
2^{k+1}.
\]

Write

\[
p=e_k+2^{k+1}r.
\]

Then

\[
D(p)=A_k+6r,
\]

with `A_k` determined by the valuation class; for `k>=2`,

\[
A_k\equiv1\pmod4.
\]

DSD status:

\[
\boxed{\textbf{SAFE / ABSORBABLE}.}
\]

This is compatible with the internal canonical-lift/valuation-coordinate language and can be used as an exact local normal form.

---

## 3. SAFE one-step bisection

For `k>=2`,

\[
D(p)=A_k+6r\equiv1+2r\pmod4.
\]

Hence

\[
r\text{ odd}\iff D(p)\equiv3\pmod4\iff v_2(3D(p)+1)=1,
\]

whereas

\[
r\text{ even}\iff D(p)\equiv1\pmod4\iff v_2(3D(p)+1)\ge2.
\]

Thus, inside a fixed `C_k` cylinder, exactly half of the `2`-adic parameter classes enter the next valuation-one branch and half remain in `C_{>=2}`.

DSD status:

\[
\boxed{\textbf{SAFE ONE-STEP CYLINDER FACT}.}
\]

This is structurally useful for Gate-A/tail-budget comparisons.

---

## 4. Restricted survival sets

The paper defines, for an initial valuation class `C_{k_0}`,

\[
S_N^*=
\{p_0:\ r_n\equiv0\pmod2,\ p_n\ne1,\ 0\le n<N\}.
\]

This means the trajectory avoids the `k'=1` branch for `N` successive accelerated odd steps and has not already hit `1`.

The paper derives a deterministic measure bound of the form

\[
\mu(S_N^*)\le2^{-N}\mu(C_{k_0}),
\]

and consequently

\[
\mu(S_\infty^*)=0.
\]

The follow-up paper is particularly important methodologically because it explicitly states

\[
\boxed{
\mu(S_\infty^*)=0
\not\Rightarrow
S_\infty^*=\varnothing.
}
\]

DSD assessment:

- the **measure-zero vs emptiness distinction is fully absorbable and should be cited as external corroboration of the internal atom-floor rule**;
- the exact multi-step pullback/bisection proof should be independently regression-tested before being used as a quantitative internal lemma, because the iterated coordinate scale depends on the valuation itinerary.

Status for the multi-step quantitative theorem at this stage:

\[
\boxed{\textbf{PROVISIONALLY SAFE / REPRODUCTION AUDIT PENDING}.}
\]

No emptiness conclusion is imported from measure decay.

---

## 5. Hinge gap in the claimed equivalence theorem

The paper claims, for `k_0=2`, equivalence between

1. every orbit starting in `C_2` eventually reaches `1`; and
2. `S_\infty^*=emptyset`.

The forward implication is immediate.

The reverse proof says that if an orbit leaves `S_N^*`, then either it has hit `1`, or some `r_n` is odd and therefore the orbit enters the `k'=1` branch, which is asserted to lead by strict descents to `1`.

That last assertion is not a property of the accelerated Collatz map.

For example,

\[
7\in C_1,
\qquad
D(7)=11>7.
\]

Starting from the claimed base class `C_2`,

\[
9\in C_2,
\qquad
D(9)=7\in C_1,
\qquad
D(7)=11>7.
\]

Thus entering `C_1` does not initiate a chain of strict decreases.

More importantly, universal convergence of every orbit once it visits `C_1` is itself a nontrivial global claim and is not proved by the local valuation classification.

Therefore the displayed proof only establishes

\[
S_\infty^*=\varnothing
\Longrightarrow
\text{every }C_2\text{ orbit eventually hits either }1\text{ or }C_1,
\]

not

\[
S_\infty^*=\varnothing
\Longrightarrow
\text{every }C_2\text{ orbit reaches }1.
\]

DSD status:

\[
\boxed{\textbf{EQUIVALENCE HINGE OPEN / NOT ABSORBED}.}
\]

This does not prove that the equivalence statement is false; it shows that the displayed implication is incomplete.

---

## 6. Internal comparison

The external survival-set framework and the internal DSD program meet at a useful boundary.

### External contribution worth absorbing

- exact local `2`-adic valuation cylinders;
- affine parameterization inside a valuation class;
- one-step half-splitting of the `C_{>=2}` retention condition;
- explicit acknowledgement that zero Haar measure is not emptiness.

### Internal program is stricter on the terminal bridge

The internal atom-floor principle requires an **unnormalized finite atomic mass with every surviving ordinary-integer atom carrying weight at least one** before using

\[
W<1\Rightarrow\emptyset.
\]

Likewise, the internal inverse-limit criterion distinguishes a nonempty `2`-adic ghost survivor from a positive ordinary integer.

Thus the internal rule is:

\[
\boxed{
\text{2-adic survival density }0
\text{ is informative but never a pointwise closure by itself.}
}
\]

---

## 7. Anti-pattern extracted

### SURV-1 — escape from a restricted survivor set is not convergence

If a survivor set is defined only by avoidance of one branch `B`, then

\[
x\notin S_\infty
\]

means merely that the trajectory eventually enters `B` (or a separately excluded terminal state).  To conclude convergence, one must prove that **every entry into `B` is terminally good**.

Forbidden upgrade:

\[
\text{eventually enters branch }B
\Rightarrow
\text{converges}
\]

without a branch-closure theorem.

### SURV-2 — measure zero is not emptiness

This is explicitly recognized by the follow-up paper and is fully adopted as a permanent DSD rule.

---

## 8. Final verdict

\[
\boxed{
\text{Local 2-adic class structure: ABSORB.}
}
\]

\[
\boxed{
\text{Measure-zero survival: useful statistical/structural fact, not emptiness.}
}
\]

\[
\boxed{
S_\infty^*=\varnothing\iff\text{Collatz on }C_2:
\text{ reverse direction not established by the displayed proof.}
}
\]

The paper is therefore valuable precisely as the user proposed: rigorous intermediate structure is kept, while the unsupported terminal jump becomes a regression test for the internal proof architecture.

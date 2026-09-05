# Gate C2 absolute-count and support-barrier audit

Date: 2026-09-06

Status: **INTEGERITY CLOSED + MIN/MAX ROUTE BARRIER + SUPPORT-AWARE REPLACEMENT TARGET.**

This note audits the proposed Gate-C2 route

\[
\text{candidate count contracts}\to C<1\to C=0.
\]

The integer step is valid for a fixed ternary selector layer.  The naive attempt to obtain enough contraction from the global selector-min/max Beatty bridge is not: the global positive-minimum hypothesis necessarily fails once dyadic child resolution exceeds selector support.  A support-aware occupied-fibre correlation theorem is therefore required.

Nothing here proves the Collatz conjecture.

---

## 1. Fixed selector layers are finite integer families

For

\[
\mathcal C_m
=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\},
\]

we have exactly

\[
\boxed{|\mathcal C_m|=2^m.}
\]

Let `R_L` be a nested exact dangerous/coefficient-surviving dyadic family at depth `L`, and define

\[
I_{m,L}
:=
|\mathcal C_m\cap R_L|.
\]

Then

\[
\boxed{I_{m,L}\in\mathbb Z_{\ge0}}
\]

and, because the conditions are nested in `L`,

\[
I_{m,L+1}\le I_{m,L}.
\]

The existing growing-resolution transport identity is therefore an identity for actual integer selector counts, not merely for a normalized probability.

At a Beatty rise, with weighted one-child count `D_{m,L}` and signed child correlation `K_{m,L}`,

\[
\boxed{
2I_{m,L+1}
=
2I_{m,L}-D_{m,L}+K_{m,L}.
}
\]

The doubled form removes all apparent half-integer ambiguity.  The existing `m44_full_mass_transport_certificate.cpp` checks this identity directly using integer subset-sum counts.

Status: **SAFE / CLOSED.**

---

## 2. Fixed-layer integer closure criterion

Suppose a collection of certified scales gives

\[
I_{m,L+1}
\le
(1-\delta_{m,L})I_{m,L},
\qquad
0\le\delta_{m,L}<1.
\]

Define the cumulative logarithmic contraction budget

\[
\boxed{
A_m(H)
:=
\sum_{L<H}
-\log(1-\delta_{m,L}).
}
\]

Since initially `I_{m,0}<=2^m`,

\[
I_{m,H}
\le
2^m e^{-A_m(H)}.
\]

Hence

\[
\boxed{
A_m(H)>m\log2
\Longrightarrow
I_{m,H}<1
\Longrightarrow
I_{m,H}=0.
}
\]

The last implication is exact integerity, not a density argument.

This is the valid form of Gate C2 for a fixed selector layer.

### Logical consequence

If one could prove this criterion for **every finite `m`**, with an `H=H(m)` allowed to depend arbitrarily on `m`, then every finite recursively-sufficient selector layer would be eliminated.  No uniform finite `H` for all `m` is logically required.

However, a proof still needs a symbolic mechanism valid for arbitrary `m`; checking finitely many layers cannot establish that universal statement.

Status: **SAFE CONDITIONAL CLOSURE CRITERION.**

---

## 3. Joint-scale version when a magnitude window is used

The earlier recursive-sufficiency/first-crossing audit gives the all-range window

\[
m\le K_{\rm all}\log_2H+O(1),
\qquad
K_{\rm all}
=
\frac{14.3}{\log_2 3}
\approx9.022295476.
\]

If one chooses to eliminate all these layers simultaneously at horizon `H`, then the total initial selector count is at most

\[
\sum_{m\le M(H)}2^m
<2^{M(H)+1}
=H^{K_{\rm all}+o(1)}.
\]

Thus a uniform contraction budget `A_*(H)` over those layers closes the union if

\[
\boxed{
A_*(H)>(M(H)+1)\log2,
}
\]

or asymptotically, a sufficient condition is

\[
\boxed{
\liminf_{H\to\infty}
\frac{A_*(H)}{\log H}
>K_{\rm all}.
}
\]

This joint formulation is stronger than the logically minimal layer-by-layer criterion, but is useful when comparing asymptotic rates.

Status: **SAFE CONDITIONAL CRITERION.**

---

## 4. Exact support barrier for the global min/max lemma

The selector min/max repair lemma assumes, on the **entire child modulus**, that

\[
0<a\le C(x)\le b.
\]

At parent depth `L`, the child group has size

\[
2M_L=2^{L-1}.
\]

An `m`-selector layer has only `2^m` assignments, so its child count function has support of size at most `2^m`.

Therefore a necessary condition for the global lower bound `a>0` is

\[
2^m\ge2^{L-1},
\]

i.e.

\[
\boxed{L\le m+1.}
\]

Once

\[
L-1>m,
\]

some child residue necessarily has multiplicity zero, so the global min/max ratio satisfies

\[
\boxed{\rho=h_{\min}/h_{\max}=0.}
\]

This is the physical-space counterpart of the already-proved selector Fourier support barrier

\[
E_{d,r}\ge2^{r-d}-1.
\]

It is a cardinality obstruction, not a computational limitation.

For a translated low-ternary cylinder with only `d=m-Q` free high selector digits, the same obstruction occurs even earlier, with `d` replacing `m`.

Status: **SAFE BARRIER.**

---

## 5. The global min/max + Beatty bridge cannot by itself close C2

Let

\[
\alpha=\log_3 2,
\qquad
b_L=\lceil\alpha L\rceil.
\]

The number of Beatty rises in the entire maximal support-compatible window

\[
1\le L\le m+1
\]

is exactly

\[
\boxed{
R_m
=b_{m+2}-b_1
=\lceil\alpha(m+2)\rceil-1.
}
\]

Since

\[
\alpha<1,
\]

we have

\[
R_m=\alpha m+O(1)<m
\]

for all sufficiently large `m`; in fact the exact integer check gives `R_m<m` for every `m>=4`.

Now take the strongest possible contraction supplied by the **current strong min/max Beatty certificate**:

\[
\delta_{m cert}
=
\frac{c_*}{4}(3\rho-1).
\]

Because

\[
0<c_*\le1,
\qquad
\rho\le1,
\]

necessarily

\[
\boxed{
\delta_{m cert}\le\frac12.
}
\]

Thus even if every support-compatible Beatty rise attained the formal maximum `delta=1/2`, the strongest bound derivable from this certificate alone would be only

\[
I_{m}\nobreak\lesssim
2^m\left(\frac12\right)^{R_m}
=2^{m-R_m}.
\]

For `m>=4`,

\[
m-R_m\ge1,
\]

so this upper bound never falls below one.

Therefore

\[
\boxed{
\text{global min/max mixing}
+
\text{Beatty one-child exposure}
\text{ alone cannot certify fixed-layer extinction.}
}
\]

This is a **proof-strategy barrier**, not a statement that the actual selector count cannot die.  Zero-child pruning, occupied-fibre correlations, root-global minimality, or other exact constraints may remove much more mass than this coarse certificate sees.

Status: **SAFE BARRIER ON THIS CERTIFICATE ARCHITECTURE.**

---

## 6. The elementary `1/L` fallback is even further from C2

The self-contained Beatty bridge gives at most, when `rho<=1`,

\[
\delta_L
\le
\frac1{5L}
\]

as the largest contraction coefficient obtainable from that particular lower-bound formula.

Even if one ignores the support barrier and formally lets this best-case certificate run through a joint horizon `H`, Beatty rises have density `alpha`, so its logarithmic budget has leading coefficient only

\[
\boxed{
\frac\alpha5\log H.
}
\]

But the all-range selector window needs a budget exceeding

\[
K_{\rm all}\log H.
\]

Since

\[
K_{\rm all}=14.3\alpha,
\]

we have exactly

\[
\boxed{
\frac{K_{\rm all}}{\alpha/5}=71.5.
}
\]

Thus the elementary fallback remains useful for normalized mass decay and independent auditing, but its present rate certificate cannot close the all-range absolute-count window.

Status: **STRATEGY-RATE BARRIER.**

---

## 7. Support-aware replacement: occupied-fibre contraction

The exact child-transport identity suggests the correct replacement.

For a fixed selector layer, define at a rise with `I_{m,L}>0`

\[
\boxed{
\Delta_{m,L}^{\rm occ}
:=
\frac{D_{m,L}-K_{m,L}}
{2I_{m,L}}.
}
\]

Then exactly

\[
\boxed{
I_{m,L+1}
=
(1-\Delta_{m,L}^{\rm occ})I_{m,L}.
}
\]

A sign-robust sufficient quantity is

\[
\underline\Delta_{m,L}^{\rm occ}
:=
\frac{(D_{m,L}-|K_{m,L}|)_+}
{2I_{m,L}}.
\]

This formulation only asks about selector mass that is actually present on surviving fibres.  It does **not** require every residue of the exponentially larger dyadic group to carry positive selector multiplicity.

Hence it survives the cardinality regime

\[
L\gg m
\]

where global min/max and global selector-energy mixing must fail.

A direct sufficient terminal theorem for layer `m` is therefore

\[
\boxed{
\sum_{L<H}
-\log\left(1-left(1-\underline\Delta_{m,L}^{\rm occ}\right)
>m\log2.
}
\]

A weaker but easier sufficient condition follows from `-log(1-x)>=x`:

\[
\boxed{
\sum_{L<H}
\underline\Delta_{m,L}^{\rm occ}
>m\log2
\Longrightarrow
I_{m,H}=0.
}
\]

This is the new preferred C2 target.

Status: **SAFE REDUCTION / OPEN ESTIMATE.**

---

## 8. Relation to Gate F and Gate S

The previous Gate-S min/max theorem remains useful in its natural pre-support regime, especially for finite calibration and for proving that child orientation cannot repair pruning while the selector distribution is genuinely spread across the whole child group.

It should no longer be treated as the asymptotic terminal theorem by itself.

The long-range target is instead one of the following equivalent-strength families of statements:

1. direct occupied-fibre lower bound on `D-K`;
2. support-aware spectral complementarity controlling `K` only where `D` lives;
3. root-global low-strip killing after Gate-A tail transfer;
4. a deterministic formation/carry theorem forcing extinction of each finite selector layer.

This aligns with the 2026-08-25 terminal roadmap: the principal unresolved issue remains transfer from symbolic/dyadic pruning to the **actual canonical selector language**.

---

## 9. Important audit concerning L7

The old arbitrary later-block Hensel/L7 maximality route must **not** be used to fill the support-aware gap.

The terminal roadmap explicitly withdrew

\[
\boxed{
\text{arbitrary later-block Hensel maximality}
}
\]

because of root pullback/globalization failure.

Finite L7 calculations remain diagnostics where their hypotheses are explicitly valid, but they are not reinstated as a terminal pruning theorem.

Status: **PROHIBITED UPGRADE.**

---

## 10. DSD audit classification

### CLOSED / SAFE

1. `C_L`, `D_L`, and the selector survivor quantities in the fixed-family transport are integer counts.
2. The doubled child-transport identity is exact.
3. `A_m(H)>m log 2` implies fixed-layer extinction by integerity.
4. The global min/max positive-lower-bound hypothesis is impossible once `L-1>m`.
5. The number of Beatty rises before that support barrier is `alpha m+O(1)`.

### BARRIER

The present **global min/max + Beatty one-child certificate alone** cannot accumulate enough certified bit loss to force `2^m` candidates below one for arbitrary large `m`.

### OPEN

Prove a support-aware estimate on the actual occupied selector fibres, for example enough cumulative positivity of

\[
D_{m,L}-K_{m,L}
\]

or of the robust form

\[
D_{m,L}-|K_{m,L}|.
\]

### PROHIBITED UPGRADES

1. Do not extend `rho>1/3` past the selector support barrier by ignoring zero fibres.
2. Do not infer occupied-fibre mixing from global Fourier mixing once the modulus is larger than selector support.
3. Do not use fixed `m=44` contraction percentages as an arbitrary-`m` theorem.
4. Do not revive arbitrary later-block L7 maximality.
5. Do not confuse the failure of this certificate architecture with evidence for a Collatz counterexample.

---

## 11. Revised next target

The highest-value next calculation is now to replace the global extrema `(h_min,h_max)` by **occupied-fibre transport statistics** at exact finite selector layers:

\[
\boxed{
\left(
I_{m,L},
D_{m,L},
K_{m,L},
\Delta_{m,L}^{\rm occ}
\right).
}
\]

The goal is not another survivor percentage.  It is to identify a state variable or root-global condition under which

\[
\sum_L\underline\Delta_{m,L}^{\rm occ}
\]

can be proved to grow at least linearly in `m`, with coefficient large enough to exceed `log 2`, or to diverge for every fixed layer until extinction.

If no such occupied-fibre law appears, return to the Gate-A/Gate-B bounded-surplus architecture rather than forcing global selector equidistribution beyond its exact support limit.

Reproducibility certificate:

`collatz/src/gateC2_absolute_count_budget_certificate.py`

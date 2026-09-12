# MATH-082 — one-paid resolution-bit Bellman wedge through macro depth 3

Date: 2026-09-12

Status: `EXACT SUFFICIENT WEDGE / DEPTH-2,3 TERMINAL REDUCTION / LONGER CHAINS OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- Paid-count layers `2<=r<=13` are not analyzed here.
- This note strengthens the one-paid side of the MATH-060 Bellman program; it is not an ordinary-descent theorem by itself.

## 1. Coarse source-resolution bit budget

MATH-061 proves that every audited pre-first-cell `u=0` source anchor satisfies

\[
Y<2^{73}.
\]

After a composed one-paid path has accumulated exact shortcut/modulus depth `H`, its source lies in one residue class modulo `2^H`. Therefore

\[
H\ge73
\Longrightarrow
\text{at most one ordinary source anchor survives}.
\]

Define the coarse unresolved bit budget

\[
\boxed{
B(H):=\max(0,73-H).
}
\]

This is a deterministic upper budget coming from the 73-bit anchor ceiling. It is distinct from the actual multiplicity resolution height

\[
R_{res}(M)=\lceil\log_2M\rceil.
\]

The two quantities must not be conflated.

## 2. Resolution-bit Bellman potential

Let

\[
\lambda=\frac{19}{503}.
\]

Use the potential

\[
\boxed{
H_{bit}(H):=-\lambda B(H).
}
\]

At the chain root, `H=0` and `B=73`. For a composed path of total shortcut length `H` and accumulated penalty `P`, the total reduced cost including this potential is

\[
J_{bit}
=\mathcal P-\lambda H
+H_{bit}(H)-H_{bit}(0).
\]

Hence exactly

\[
\boxed{
J_{bit}=\mathcal P
\quad(H\le73),
}
\]

and

\[
\boxed{
J_{bit}=\mathcal P-\lambda(H-73)
\quad(H>73).
}
\]

Thus the first 73 exact source-resolution bits absorb the corresponding length charge in the Bellman comparison. Only terminal overshoot beyond the audited source-resolution ceiling remains to be paid analytically.

## 3. Universal one-paid penalty lower bound

Every one-paid macro has exactly one paid odd event at slack

\[
u=1.
\]

Its penalty atom is

\[
p=\frac16\Omega.
\]

The boundary phase satisfies

\[
\frac12<\Omega\le1,
\]

so strictly

\[
\boxed{p>\frac1{12}}.
\]

For a chain of `t` one-paid macros,

\[
\boxed{
\mathcal P>\frac{t}{12}.
}
\]

Therefore a phase-free sufficient condition for a terminal chain is

\[
H\le73,
\]

or, when `H>73`,

\[
\frac{t}{12}-\lambda(H-73)\ge0.
\]

At `lambda=19/503` this is

\[
\boxed{
228(H-73)\le503t.
}
\]

Because the actual penalty is strictly larger than `t/12`, equality in the displayed rational test is still safe.

This criterion depends only on macro count and accumulated exact source-resolution depth. No phase enumeration or ordinary-integer continuation is required.

## 4. Stronger exact phase-interval test

A composed MATH-061 PathCylinder stores

\[
\mathcal P=\beta\Omega_0,
\qquad
\Omega_0\in(\Omega_{lo},\Omega_{hi})
\]

with exact rational `beta` and source phase interval.

Therefore

\[
\beta\Omega_{lo}
\]

is a rigorous infimum for the accumulated penalty. A stronger sufficient test is

\[
\boxed{
\beta\Omega_{lo}
-\lambda(H-73)\ge0
}
\]

when `H>73`; for `H<=73`, positivity of the accumulated one-paid penalty is already sufficient for this reduced-cost test.

## 5. Macro depth 2

Starting from the 857 one-paid source cylinders that are still multi-source after their first macro, exact MATH-061 composition produces

\[
\boxed{1,137}
\]

new singleton handoffs and

\[
\boxed{11,389}
\]

multi-source survivors.

The singleton total-length distribution is

\[
\begin{array}{c|rrrrrrrrrr}
H&69&70&71&72&73&74&75&76&77&78\\
\hline
\#&128&353&321&130&139&37&14&11&3&1
\end{array}
\]

The phase-free wedge certifies

\[
\boxed{1,136/1,137}
\]

without ordinary continuation.

The sole phase-free exception has

\[
t=2,\qquad H=78.
\]

For that exact cylinder, the stronger phase-infimum margin is

\[
\beta\Omega_{lo}
-\frac{19}{503}\cdot5
=
\frac{745936686450315127}{6982634218288398336}
>0.
\]

Hence

\[
\boxed{1,137/1,137}
\]

depth-2 terminal handoffs are Bellman-safe under the coarse-bit potential plus exact phase interval.

This means that, for the **penalty/reduced-cost certificate**, none of the 1,137 ordinary terminal trajectories needs to be followed. MATH-061's direct ordinary descent checks remain valid independent closure evidence; they are not retroactively reclassified as unnecessary for every theorem purpose.

## 6. Macro depth 3

Extending the 11,389 multi-source depth-2 survivors by the canonical 910 one-paid cylinders gives exactly

\[
\boxed{11,511}
\]

new singleton handoffs and

\[
\boxed{85,803}
\]

multi-source survivors.

The terminal total-length distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
H&69&70&71&72&73&74&75&76&77&78&79&80&81&82&83&84\\
\hline
\#&1059&3286&3721&1256&1362&430&104&172&63&19&17&6&8&4&1&3
\end{array}
\]

The phase-free wedge certifies

\[
\boxed{11,489/11,511}.
\]

Only 22 handoffs lie outside the universal phase-free region. The exact phase-interval penalty infimum certifies 20 more, leaving only

\[
\boxed{2}
\]

uncertified by the analytic Bellman test.

Both have

\[
t=3,\qquad H=84.
\]

Retaining them as ordinary same-integer states and continuing them directly gives floor hits in respectively

\[
\boxed{1\text{ and }10}
\]

shortcut steps.

Thus the combined analytic-plus-ordinary terminal treatment reduces the depth-3 ordinary-continuation workload from 11,511 terminal handoffs to two explicit states.

## 7. DSD interpretation

The result supports a sharp division of labor.

### Analytic cost channel

Most terminal handoffs are removed from the low-cost bad-path search by the accumulated penalty plus the source-resolution potential.

### Exact compatibility channel

The composed cylinder construction still preserves exact dyadic source compatibility. The bit potential does not license merging incompatible source cylinders.

### Ordinary handoff channel

Only states not certified by the analytic sufficient test are materialized as ordinary integers and continued. Singleton resolution alone is not called descent.

This is exactly the claim hierarchy required by the recent DSD audits.

## 8. Relation to the MATH-060 overhead

The bit potential has endpoint range at most

\[
73\lambda.
\]

MATH-060 retained a conservative additive allowance of 89 shortcut steps. Thus the coarse 73-bit resolution potential fits inside that allowance, leaving a nominal

\[
\boxed{89-73=16}
\]

step-equivalent buffer for other endpoint/potential overhead.

This arithmetic compatibility does not by itself prove that all other Bellman state components fit in the remaining 16-step allowance.

## 9. Computational consequence

Naive exact composition begins to expand rapidly after macro depth 4. MATH-082 shows that the next implementation should apply the resolution/penalty wedge **before** ordinary terminal continuation and before large state materialization.

The next exact state quotient should retain only:

1. multi-source compatible cylinders;
2. terminal singleton cylinders outside the universal wedge;
3. among those, only terminal cylinders outside the exact phase-infimum test;
4. explicit ordinary integers only for the small remainder.

This changes the intended depth-5--24 search from 'enumerate all singleton handoffs and continue them' to 'prune almost all terminal handoffs analytically at creation time'.

## 10. Claim boundary

Established:

- exact coarse bit-budget potential identity;
- universal one-paid lower bound `P>t/12`;
- sufficient wedge `228(H-73)<=503t`;
- exact phase-infimum strengthening;
- depth-2 and depth-3 exact terminal counts and pruning counts;
- same-integer descent of the two remaining depth-3 states.

Not established:

- closure of all one-paid chains through macro depth 24;
- that the coarse bit potential is a complete Bellman potential;
- that the remaining 16-step overhead is sufficient for every other state component;
- the global `19/503` penalty lower bound;
- first-cell emptiness;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math082_onepaid_resolution_wedge_certificate.py`

# R1 current-floor dependency audit

Date: 2026-09-06

Status: **DEPENDENCY CORRECTION.**  The finite `m=44` selector certificates remain exact statements about the enumerated selector families, but the promotion of their endpoint to a continuous global verified floor `V_33` depends on the recursively-sufficient ternary Cantor-core coverage imported from Ansari (2025).  The 2026-09-06 audit of that coverage found that the printed induction used to establish the nested `F_n` family as recursively sufficient fails already at `F_1 -> F_2`.  Therefore every later result whose universal scope uses `V_33` as a lower bound for a hypothetical minimal counterexample must be read as **CONDITIONAL ON REPAIRED TERNARY COVERAGE**.

This note corrects dependency labels only.  It does not invalidate the exact finite computations inside the `m=44` selector family, and it does not prove or disprove the Collatz conjecture.

---

## 1. Exact source of the `m=44` global-floor interpretation

The original bootstrap note

`collatz/notes/2026-08-12-m44-bootstrap-priority-and-window-floor.md`

states explicitly that

\[
V_0=4\cdot3^{44}+2
\]

is promoted to a global verified floor by combining Barina's published finite verification with **Ansari's recursively sufficient intersection sieve**.  It then identifies the next members of that asserted recursively-sufficient intersection with the `m=44` ternary-selector block

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

Thus the statement

\[
\boxed{\text{every hypothetical minimal counterexample above the finite record lies in this selector block}}
\]

was not an independent consequence of the finite trajectory/Hensel certificates.  It used the global recursive-sufficiency coverage theorem.

Status: **DEPENDENCY IDENTIFIED.**

---

## 2. Exact source of `V_33`

The later note

`collatz/notes/2026-08-14-m44-a32-shifted-layer-hybrid-closure.md`

certifies the complete shifted `a_32=1` selector layer

\[
\mathcal A_{32}^{\rm shift}
=
\left\{
4(3^{44}+3^{32})+3
+4\sum_{i=0}^{31}a_i3^i:
 a_i\in\{0,1\}
\right\}.
\]

Its finite computation is exact:

- `2^32` selector assignments are partitioned;
- `4,159,095,994` are removed by the exact class theorem;
- `135,871,302` retained representatives are followed explicitly;
- every followed representative descends below itself;
- zero failures occur in that finite selector layer.

The same note then invokes Ansari's asserted recursively-sufficient core to say that, once both `a_32=0` and `a_32=1` blocks are exhausted, the next possible minimal-counterexample member of the core first turns on `a_33`.  From that **coverage step** it promotes the selector computation to the continuous floor

\[
\boxed{
V_{33}=4(3^{44}+3^{33})+2
=3,939,105,844,976,711,153,618.
}
\]

and hence

\[
\boxed{
N_0=V_{33}+1
=4(3^{44}+3^{33})+3
=3,939,105,844,976,711,153,619.
}
\]

Therefore:

\[
\boxed{
\text{finite closure of the two selector layers: SAFE}
}
\]

but

\[
\boxed{
\text{continuous global floor }V_{33}:\text{ CONDITIONAL ON COVERAGE}.
}
\]

---

## 3. Why the coverage dependency is currently open

The 2026-09-06 Gate-F coverage audit checked Ansari's printed recursive-sufficiency induction directly.

At the first nontrivial step,

\[
F_1\bmod36=\{3,7,15,19,27,31\},
\]

while

\[
F_2\bmod36=\{3,7,15,19\}.
\]

Hence

\[
F_1\setminus F_2
=(36\mathbb N_0+27)\cup(36\mathbb N_0+31).
\]

The auxiliary equality printed in the induction does not reproduce this difference.  The `31 mod 36` progression has since been repaired by an explicit smaller merge, but the universal recursion of

\[
\boxed{36\mathbb N_0+27}
\]

remains open, as do the higher removed layers.

Accordingly the implication

\[
\text{hypothetical minimal counterexample}
\Longrightarrow
\text{infinite ternary `0/1` core}
\]

is presently **OPEN / CONDITIONAL** in this repository.

---

## 4. Effect on the current-resonance R1 theorem

The note

`collatz/notes/2026-08-14-global-first-crossing-isolation-through-current-resonance.md`

sets

\[
N_0:=V_{33}+1
\]

and uses this very large start floor in the Diophantine estimate that isolates, for

\[
1\le q\le137,528,045,312,
\]

the unique surviving first-crossing coefficient cell

\[
\boxed{
(A,q)
=(217,976,794,617,
137,528,045,312).
}
\]

The finite Worley/Dujella enumeration and exact logarithmic inequalities in that certificate remain mathematically correct **under the stated hypothesis `N>=N_0`**.

What is no longer established unconditionally is that every hypothetical minimal counterexample must satisfy that hypothesis.

Therefore the correct status is

\[
\boxed{
N\ge V_{33}+1
\Longrightarrow
\text{current-resonance isolation: SAFE},
}
\]

but

\[
\boxed{
\text{all hypothetical minimal counterexamples satisfy }N\ge V_{33}+1:
\text{ CONDITIONAL}.
}
\]

Consequently the interpretation

\[
\boxed{
\text{the universal R1 proof tree has only the current resonance left}
}
\]

must be downgraded to

\[
\boxed{
\text{the ternary-coverage / }m=44\text{ branch has only that resonance left}
}
\]

until the coverage theorem is repaired.

---

## 5. Universal R1 fallback that survives this audit

An older R1 route does not use the `V_33` ternary floor.

It combines:

1. an exact audit of every ordinary integer `2<=n<=4614`, showing no paradoxical first coefficient crossing in that range;
2. the published Rozier--Terracol finite/paradoxical frontier as quoted in the repository, according to which an additional paradoxical start must exceed `2.8e19`;
3. the mechanical first-crossing envelope and continued-fraction/Legendre analysis.

This gives the existing lower odd-event requirement

\[
\boxed{
H>5.395570552\times10^9
}
\]

for an R1 renewal-floor counterexample, subject to the external theorem being used exactly as cited.

This result does **not** require the ternary recursively-sufficient Cantor-core coverage and therefore remains the current universal fallback in the R1 branch.

It is much weaker than the `V_33`-based isolation, but it is logically independent of the reopened Gate-F coverage.

---

## 6. DSD dependency table

### SAFE

1. Exact finite `m=44` selector-layer enumerations and trajectory certificates.
2. Exact values of `V_33` and `N_0` as arithmetic boundaries of those selector layers.
3. The current-resonance Diophantine certificate **conditional only on the explicit assumption `N>=N_0`**.
4. The older `2.8e19` / `5.395570552e9` R1 fallback, subject to its stated external Rozier--Terracol input.

### CONDITIONAL

1. `V_33` as a continuous global verified floor for all ordinary integers.
2. `N>=V_33+1` for every hypothetical minimal counterexample.
3. Universal reduction of R1 to the single current resonance.
4. Any later theorem that imports the `m=44` selector floor without separately proving global coverage.

### OPEN

1. `F_map^cover` / repaired recursive sufficiency of the ternary `0/1` core.
2. `COV_1`, beginning with universal recursion of `36N_0+27`.
3. Higher digit-`2` removed layers `COV_n`.

### PROHIBITED UPGRADES

1. Do not cite `V_33` as an unconditional minimal-counterexample lower bound while coverage is open.
2. Do not discard the exact `m=44` calculations; the coverage problem changes their scope, not their finite correctness.
3. Do not describe the current resonance as the sole universal R1 obstruction without the coverage qualifier.
4. Do not replace the weaker universal R1 floor by the stronger selector-conditional one silently.

---

## 7. Revised proof architecture

The R1 branch now has two parallel scales:

### Universal branch

\[
\boxed{
\text{ordinary minimal-counterexample assumptions}
\Longrightarrow
N>2.8\times10^{19},
\quad
H>5.395570552\times10^9
}
\]

with the external paradoxical-frontier theorem as stated.

### Selector-conditional branch

\[
\boxed{
F_{\rm map}^{\rm cover}
\Longrightarrow
N\ge V_{33}+1
\Longrightarrow
(A,q)=(217976794617,137528045312)
}
\]

through the current verified selector calculations.

The stronger branch remains valuable as a conditional stress test and as a target for the finite selector program.  It must not be substituted for the universal branch until coverage is repaired.

---

## 8. Next target

Further dangerous-core / joint correction-address work should therefore be labeled in one of two ways:

1. **universal**, using only the weaker independent floor; or
2. **selector-conditional**, using `V_33` and the isolated current resonance.

The two regimes must not be merged silently.

# R1 current resonance: exact buffered core `B=76`

Date: 2026-09-06

Status: **SAFE FIXED-CELL GLOBAL CO-ORDER / CONDITIONAL GLOBAL MINIMAL-COUNTEREXAMPLE USE.**

The existing buffered-core theorem gives a global pairwise co-order result inside each fixed initial odd-position fibre.  For the current fixed coefficient cell

\[
(A,q)=(217,976,794,617,137,528,045,312),
\]

the least buffered core is exactly

\[
\boxed{B=76.}
\]

This is stronger than the local 25-axis dangerous-core localization because it controls every pair of safe-tail completions globally, not merely elementary edges.  It is also more expensive combinatorially.  Using this resonance as the sole universal R1 cell remains conditional on the reopened ternary-coverage theorem.

---

## 1. Buffered-core theorem recalled

At first coefficient crossing let

\[
M=2^A,
\qquad
P=3^q,
\qquad
D=M-P>0,
\]

and for a parity word let `x` be the canonical start, `y` the endpoint, and

\[
z=x-y.
\]

The exact identity is

\[
\boxed{Mz=Dx-R.}
\]

If two admissible odd-position vectors agree in their first `B` odd positions, then their tail correction difference obeys

\[
2^B\mid\Delta R,
\qquad
|\Delta R|<q3^{q-1}.
\]

The same congruence gives

\[
2^B\mid\Delta x.
\]

Therefore, if

\[
\boxed{D2^B>q3^{q-1},}
\]

then for every two distinct states in the same `B`-core fibre

\[
\boxed{
\operatorname{sgn}(\Delta z)=\operatorname{sgn}(\Delta x).
}
\]

Equivalently

\[
\boxed{x_1<x_2\iff z_1<z_2.}
\]

This is a **global pairwise theorem** and avoids the false unique-sink shortcut.

---

## 2. Exact minimal `B`

Write

\[
\varepsilon=\frac{2^A}{3^q}-1.
\]

The buffered inequality is equivalent to

\[
\varepsilon2^B>\frac q3.
\]

With

\[
E=A\ln2-q\ln3,
\qquad
\varepsilon=e^E-1,
\]

the accompanying exact rational certificate proves

\[
E<\ln\left(1+\frac{q}{3\cdot2^{75}}\right)
\]

but

\[
E>\ln\left(1+\frac{q}{3\cdot2^{76}}\right).
\]

Hence

\[
\boxed{
D2^{75}\le q3^{q-1},
\qquad
D2^{76}>q3^{q-1}.
}
\]

Therefore

\[
\boxed{B(q)=76.}
\]

Status: **SAFE EXACT FIXED-CELL RESULT.**

---

## 3. Paradoxical-start consequence

At a paradoxical first crossing,

\[
z=x-y\le0,
\]

so

\[
Dx\le R<q3^{q-1}.
\]

Since

\[
D2^{76}>q3^{q-1},
\]

we get

\[
\boxed{x<2^{76}.}
\]

Thus the first 76 parity bits determine the ordinary start `x` itself, not merely its residue modulo `2^76`.

This does **not** imply that only `2^76` brute-force work remains.  The proof program still needs a structured way to identify which small canonical starts are compatible with all other constraints.

---

## 4. Odd-position horizon

The `i`-th odd position satisfies the first-crossing admissibility bound

\[
\alpha_i\le\lfloor(i-1)\log_2 3\rfloor.
\]

For `i=76`,

\[
\boxed{
\alpha_{76}\le\lfloor75\log_2 3\rfloor=118.
}
\]

Therefore all information in the first 76 odd-position coordinates occurs within at most the first

\[
\boxed{119}
\]

parity positions.

This gives a finite time-window representation of the buffered core, but the number of admissible odd-position prefixes is still very large.

---

## 5. Exact prefix-state count

The constrained odd-position lattice

\[
0\le\alpha_1<\cdots<\alpha_{76},
\qquad
\alpha_i\le\lfloor(i-1)\log_2 3\rfloor
\]

has exactly

\[
\boxed{
15,537,359,898,820,273,235,593,329,305,889
}
\]

admissible prefixes.

Therefore:

\[
\boxed{
B=76\text{ is a logical finite core, not a directly enumerable small state space.}
}
\]

A root-global transfer or arithmetic intersection theorem is still required.

---

## 6. Relation to the earlier 25-axis result

The local dangerous-axis theorem gives

\[
h(q)=25.
\]

The two reductions serve different purposes:

### `h=25`

- identifies exactly where an elementary local order reversal can occur;
- smaller interaction support;
- does not by itself prove common global minimizers over the safe tail.

### `B=76`

- larger core;
- proves total pairwise co-order over every completion sharing the core;
- gives `x<2^76` for a paradoxical start.

Thus the current architecture should prefer `B=76` whenever a rigorous global tail elimination is required, while `h=25` remains useful for designing a more compressed transfer.

---

## 7. Audit of the old `L=77` m44 obstruction

An earlier exact verifier at parity depth `L=77` found zero intersection between a restricted survivor language and the `m=44` ternary selector core.

However that survivor language imposed, among other conditions, **L7 residue maximality on every aligned 7-bit block**.

The later DSD terminal audit explicitly withdrew arbitrary later-block Hensel/L7 maximality because root pullback/globalization fails in general.

Therefore the numerical `L=77` intersection-zero certificate remains exact for its declared restricted language, but it cannot be inserted into the current SAFE root-global proof chain as if every actual minimal counterexample satisfied those later-block L7 conditions.

In particular:

\[
\boxed{
B=76\text{ does NOT rehabilitate the old L77 shortcut.}
}
\]

A new cross-place certificate must use root-globalized conditions only.

---

## 8. Dependency labels

### SAFE

1. The buffered-core theorem itself.
2. `B=76` for the fixed numerical resonance.
3. `x<2^76` under paradoxical first-crossing survival at this fixed cell.
4. `alpha_76<=118`.
5. The exact admissible-prefix count.

### CONDITIONAL

The claim that every hypothetical minimal counterexample is forced to this fixed resonance, because that used the coverage-dependent `V_33` floor.

### REJECTED SHORTCUT

Using the old all-block `L7` `L=77` zero-intersection computation as a root-global theorem.

### OPEN

A root-global same-integer / selector intersection theorem exploiting `B=76` or the sharper local `h=25` without invalid later-block assumptions.

---

## 9. Regression certificate

`collatz/src/r1_current_resonance_buffered_core76_certificate.py`

proves the `B=75/76` threshold using exact rational logarithmic intervals and checks the combinatorial prefix count.

---

## 10. Next target

The next highest-value finite calculation is not a raw enumeration of the 76-odd-position lattice.

It is to combine:

1. `x<2^76`;
2. root-level Hensel/predecessor constraints only;
3. the exact `m=44` ternary subset-sum coordinate when working conditionally inside the selector branch;
4. coefficient survival through the at-most-119-position buffered window.

The result should be a root-global meet-in-the-middle or transfer certificate that tests the same-integer intersection without imposing any later-block Hensel maximality.

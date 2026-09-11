# MATH-061 — exact one-paid cylinder composition and 73-bit resolution handoff

Date: 2026-09-11
Status: `EXACT COMPOSITION LAW / TWO-MACRO REGRESSION / SINGLETON DESCENT CLOSED / LONGER APERIODIC CHAINS OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-061 continues the MATH-059 arithmetic-progression macro representation. It does not prove the `19/503` global Bellman slope.

## 1. Canonical one-paid cylinder

A MATH-059 one-paid macro has exact form

\[
Y=A+2^H s,
\qquad
Y'=B+3^Q s,
\qquad
0\le s<M,
\]

where

- `H` is the full shortcut length of the macro;
- `Q` is its total odd-step count;
- the source phase belongs to an exact rational interval `I`;
- the target phase is `g I` for an exact rational multiplier `g`;
- the macro penalty is `beta Omega` for source phase `Omega`.

The modulus really is `2^H`, not a looser bookkeeping modulus. This is the macro form of the exact parity-cylinder fact that a length-`H` shortcut word fixes one starting residue modulo `2^H`.

## 2. Exact composition law

Suppose a composed path already has

\[
Y_0=A+2^H s,
\qquad
Y_1=B+3^Q s.
\]

Let the next macro require

\[
Y_1\equiv A_2\pmod{2^{H_2}}.
\]

Because `3^Q` is odd, it is invertible modulo `2^{H_2}`. Therefore the matching condition fixes

\[
\boxed{s\equiv r\pmod{2^{H_2}}}
\]

for one exact residue `r`.

Write

\[
s=r+2^{H_2}t.
\]

Then

\[
\boxed{
Y_0=A_*+2^{H+H_2}t
}
\]

and the next endpoint again has the canonical form

\[
\boxed{
Y_2=B_*+3^{Q+Q_2}t.
}
\]

Thus the arithmetic-progression cylinder family is closed under exact macro composition.

This is the key non-enumerative update: appending a macro does not branch over every endpoint lift. It adds one dyadic congruence to the existing cylinder.

## 3. Phase and penalty also compose without history enumeration

If the current phase is

\[
\Omega_1=g\Omega_0
\]

and the next cylinder accepts phase interval `I_2`, source compatibility is exactly

\[
\Omega_0\in I\cap g^{-1}I_2.
\]

If the current accumulated penalty is

\[
\mathcal P=\beta\Omega_0
\]

and the appended edge has local coefficient `beta_2`, then

\[
\boxed{
\mathcal P'
=(\beta+g\beta_2)\Omega_0.
}
\]

Therefore one composed state still carries one source phase interval, one phase multiplier, and one scalar penalty coefficient. Internal parity history is unnecessary once these exact future-complete coordinates are retained.

## 4. 73-bit resolution handoff

MATH-057/058 gives the uniform pre-first-cell `u=0` anchor bound

\[
Y<2^{73}.
\]

After composing macros of total shortcut length `H`, the source anchor lies in one residue class modulo `2^H`:

\[
Y=A+2^H s.
\]

Hence

\[
\boxed{
H\ge73
\Longrightarrow
\text{at most one ordinary source anchor survives in the audited anchor range.}
}
\]

This is not a density claim. It is an exact resolution statement. Once a path cylinder reaches 73 accumulated shortcut bits, the remaining source multiplicity is zero or one.

That singleton can then be checked as an ordinary integer rather than represented by a parity-word family.

## 5. Exact two-macro regression

The corrected MATH-058/MATH-059 system contains exactly

\[
\boxed{910}
\]

one-paid macro cylinders for `1<=L<=71`.

Every ordered pair was composed with the exact dyadic congruence and exact phase-overlap test.

The exact result is

\[
\boxed{12,530}
\]

nonempty two-macro composed cylinders.

Among them,

\[
\boxed{1,141}
\]

have source multiplicity exactly one.

For each such singleton, the exact ordinary target anchor was continued under the shortcut Collatz map. Every one reaches

\[
\le2^{71}
\]

within at most

\[
\boxed{71}
\]

additional shortcut steps.

Therefore all 1,141 singleton two-macro states are incompatible with a hypothetical minimal counterexample above the frozen published floor.

This is a same-integer closure, not a statistical elimination.

## 6. Relation to the existing periodic negative-ghost theorem

The repository already proves that an eventually-periodic coefficient-surviving parity tail has periodic fixed point

\[
x=\frac{C(p)}{2^H-3^S}<0
\]

because persistent coefficient survival forces `3^S>2^H`. A finite preperiod cannot pull this negative rational ghost back to a positive ordinary start.

Thus the periodic part of an infinite symbolic survivor is already closed.

MATH-061 does not duplicate that theorem. Its role is different:

- the negative-ghost theorem closes genuinely repeated periodic tails at the symbolic boundary;
- the cylinder-composition law handles finite same-integer macro concatenations and exposes when a finite path has reached ordinary-integer resolution;
- the remaining hard case is an **aperiodic** sequence of compatible macro cylinders whose cumulative penalty might stay below the MATH-060 target slope.

## 7. DSD audit

### SAFE

- exact macro source/target arithmetic-progressions;
- closure of the representation under composition;
- exact phase-interval pullback under composition;
- exact min-plus coefficient update `beta -> beta + g beta_2`;
- 73-bit singleton handoff under the audited anchor ceiling;
- exact two-macro counts `12,530` and singleton count `1,141`;
- exact direct descent of all 1,141 singleton targets to the frozen floor within 71 shortcut steps.

### OPEN

- arbitrary-length aperiodic one-paid cylinder chains;
- mixed one-paid / multi-paid cylinder composition;
- a global Bellman potential proving mean penalty at least `19/503`;
- first-cell emptiness and later-cell coverage.

### PROHIBITED UPGRADES

- two-macro singleton closure `=>` all one-paid chains closed;
- 73-bit source resolution `=>` the number of length-73 parity cylinders is small;
- eventually-periodic negative-ghost closure `=>` aperiodic paths are closed;
- finite exact singleton checks `=>` Collatz proof.

## 8. Next target

The next calculation should no longer enumerate endpoint lifts. It should recursively compose cylinders while applying the exact 73-bit singleton handoff.

For the Bellman objective, only aperiodic composed states with more than one unresolved ordinary source need remain symbolic. Mixed multi-paid macros should then be added only where a one-paid chain cannot already be closed by singleton descent or the periodic negative-ghost theorem.

## Reproducibility

`collatz/src/2026_09_11_math061_onepaid_cylinder_composition_certificate.py`

# MATH-037 — coefficient-language Hensel collision frontier

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FIRST NON-VACUOUS HENSEL PRUNING IN COEFFICIENT LANGUAGE / FINITE EXACT`
- Scope: coefficient-surviving parity prefixes under the frozen published-floor spine.

## 1. Why this calculation was needed

MATH-013 showed that unrestricted symbolic Hensel classes collide already at depth 24, but the coefficient-surviving candidate language is much thinner.

An exact external-partition scan of that language found:

- no Hensel class collision through depth 33;
- exactly five collision classes at depth 34.

The new certificate independently re-extracts all five depth-34 collisions from the minimal `q=22` layer.

Thus root-Hensel maximality is vacuous on the coefficient-surviving language through depth 33 and becomes non-vacuous for the first time at depth 34.

## 2. Exact depth-34 structure

For a prefix word `w`, write

\[
C(w)=h(w)3^q+r(w),\qquad0\le r(w)<3^q.
\]

The Hensel class key is

\[
\kappa(w)=(q,r(w)).
\]

At depth 34 all five collisions lie at

\[
\boxed{q=22}.
\]

The five exact class residues are

\[
\boxed{
4{,}015{,}726{,}592,
4{,}559{,}922{,}176,
5{,}240{,}166{,}656,
8{,}585{,}544{,}704,
9{,}875{,}489{,}792
}.
\]

Every collision has

\[
\boxed{\Delta h=4}.
\]

Equivalently, the two corrections in each class differ by

\[
\boxed{4\cdot3^{22}}.
\]

## 3. Same-integer interpretation

For a length-34 prefix,

\[
T^{34}(N)=\frac{3^{22}N+C}{2^{34}}.
\]

If the larger correction exceeds the smaller one by `4*3^22`, then the larger-correction competitor starting from `N-4` reaches the same depth-34 endpoint as the smaller-correction word starting from `N`.

Because the first-cell starts are all far above 4, root minimality makes the smaller-correction representative inadmissible.

The five excluded ordinary-start residue classes modulo `2^34` are

\[
\boxed{
5{,}348{,}744{,}191,
7{,}435{,}082{,}751,
11{,}843{,}133{,}439,
15{,}231{,}450{,}879,
15{,}257{,}926{,}655
}.
\]

For each one the competing residue is exactly four smaller.

Therefore the first non-vacuous Hensel pruning in the actual coefficient language is not merely symbolic: it excludes five concrete low-34-bit ordinary-start residue classes throughout the current first-cell window.

## 4. DSD interpretation

- `D`: the Hensel class and ordinary-start residue are both retained.
- `R`: exact depth-34, exact `q=22`, exact modulo `3^22` and `2^34` data.
- `S`: only coefficient-surviving words are admitted.
- `E`: the lower-correction member of each of the five classes is excluded by a legal positive credit of 4.
- `T`: class collision is translated back to the same ordinary-integer endpoint identity.
- `C`: the targeted q=22 scan reproduces all five classes reported by the prior full external-partition audit.
- `N`: `ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.
- `O`: five low-34-bit residue classes are removed; the first cell remains open.

## 5. What this changes about the calculation direction

A full class-max DP grows too quickly: coefficient-surviving state counts already reach

\[
41{,}347{,}483
\]

at depth 32.

But actual Hensel collisions are absent through 33 and only five appear at 34. Hence the efficient direction is no longer to materialize every Hensel class. Instead, calculation should track **collision events and their descendants**, while separately detecting genuinely new even/odd class intersections.

This is the sparse Hensel-event route.

## 6. Prohibited upgrades

- Five excluded residues modulo `2^34` do not imply the first cell is empty.
- Sparse collisions at depth 34 do not imply collisions stay sparse at arbitrary depth.
- A Hensel class collision is candidate-excluding only when its positive ordinary-start credit is legal; here the credit is exactly 4 and is legal in the first-cell range.
- The absence of collisions through depth 33 is a finite exact result, not an asymptotic theorem.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth34_collision_certificate.cpp`

Certificate commit:

`1da66a0245af8b8baa3d2c20ab5ceecf47785593`

The global Collatz status remains `OPEN`.

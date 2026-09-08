# MATH-037 — two-sided coefficient-language Hensel collision frontier

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / FIRST TWO-SIDED COEFFICIENT-LANGUAGE HENSEL COLLISION / FINITE EXACT`
- Scope correction: **MATH-040 supersedes the former interpretation that this was the first non-vacuous root-Hensel pruning.**

## 1. Corrected scope

This calculation requires **both** colliding Hensel-class representatives to satisfy the frozen published-floor coefficient-survival condition.

Within that two-sided language, the exact result is:

- no Hensel class collision through depth 33;
- exactly five collision classes at depth 34;
- all five lie at `q=22`.

This remains a valid finite structural result.

However, actual root-Hensel maximality is asymmetric: the candidate must be coefficient-surviving, while its competitor may be an arbitrary parity word in the same class. MATH-040 shows that this one-sided pruning already begins at depth 6.

Therefore this file must not be cited as the first global Hensel-pruning frontier.

## 2. Exact depth-34 structure

For a prefix word `w`, write

\[
C(w)=h(w)3^q+r(w),\qquad0\le r(w)<3^q.
\]

The Hensel class key is

\[
\kappa(w)=(q,r(w)).
\]

At depth 34 all five two-sided collisions lie at

\[
\boxed{q=22}.
\]

Their exact class residues are

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
\boxed{\Delta h=4},
\]

so

\[
C_{\rm high}-C_{\rm low}=4\cdot3^{22}.
\]

## 3. Same-integer interpretation

For a length-34 prefix,

\[
T^{34}(N)=\frac{3^{22}N+C}{2^{34}}.
\]

Thus the larger-correction representative at start `N-4` reaches the same endpoint as the lower-correction representative at start `N`.

The five lower-correction ordinary-start residue classes modulo `2^34` are

\[
\boxed{
5{,}348{,}744{,}191,
7{,}435{,}082{,}751,
11{,}843{,}133{,}439,
15{,}231{,}450{,}879,
15{,}257{,}926{,}655
}.
\]

Those five classes are genuinely excluded; the scope correction changes only the claim that they were the **first** Hensel exclusions.

## 4. DSD interpretation

- `D`: two coefficient-surviving representatives in one Hensel class.
- `R`: exact depth 34, `q=22`, modulo `3^22` and modulo `2^34`.
- `S`: symmetric coefficient-language selection on both sides.
- `E`: lower-correction member excluded by credit 4.
- `T`: exact same-endpoint transfer to start `N-4`.
- `C`: five classes independently reproduced by the targeted q=22 certificate.
- `N`: `ESTABLISHED_WITHIN_SCOPE / FINITE EXACT / SCOPE REVISED BY MATH-040`.
- `O`: first two-sided coefficient-language collision frontier; **not** the first one-sided root-Hensel pruning frontier.

## 5. Calculation-direction revision

The sparse two-sided collision route remains useful for studying internal collision geometry, but it is no longer the primary root-Hensel pruning engine.

The primary route after MATH-040 is

\[
\boxed{
\text{coefficient-surviving candidate}
\longrightarrow
\text{unrestricted Hensel class maximum}.
}
\]

MATH-040 and later targeted reverse-Hensel work should control candidate-exclusion claims.

## 6. Prohibited upgrades

- depth 34 = first actual Hensel pruning — **SUPERSEDED / PROHIBITED**;
- absence of two-sided collisions through 33 ⇒ Hensel maximality vacuous — **PROHIBITED**;
- five excluded residues ⇒ first cell empty — **PROHIBITED**;
- sparse two-sided events ⇒ sparse one-sided domination — **PROHIBITED**.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_coefficient_hensel_depth34_collision_certificate.cpp`

Original certificate commit:

`1da66a0245af8b8baa3d2c20ab5ceecf47785593`

Selection-scope correction:

`collatz/notes/2026-09-08-one-sided-root-hensel-selection-correction.md`

MATH-040 note commit:

`a2a5c1dd2e9f712fd81b30b327fd17a814c5e792`

The global Collatz status remains `OPEN`.

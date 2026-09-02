# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation.

## Input family

Exact retained roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary source certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`.

Each root is an exact affine source cylinder

\[
X=r+2^h m
\]

with a finite integer parameter interval and exact parity-bit refinement.

## Closed/rejected routes that must not be restarted

### Terminal right-H target-dominance ternary filter

The terminal 28-gate dominance problem is solved exactly.

Its complete existence condition is

\[
z_H\bmod3\in\{0,1\}
\iff
Z\bmod3\in\{1,2\}.
\]

But every genuine positive-one-count checkpoint already satisfies `3∤Z` from the correction identity modulo 3.

Therefore this gate is **redundant for pruning** and removes zero genuine candidates.

Canonical objects:

- `../theorems/TERMINAL_28GATE_DOMINANCE_SATURATION.md`;
- `../audits/TERMINAL_DOMINANCE_GATE_REDUNDANCY.md`.

Do not restart a 28-gate carry enumeration in the hope that target-dominance existence alone will determine a narrow `z_H mod3^28` set.

### Dominance-only weak CRT channel

`Z mod2^27` plus the automatic `Z mod3 in {1,2}` condition does not isolate a checkpoint.

For fixed `X`, the debit-compatible checkpoint interval has width

\[
37\cdot2^{33}
=789(3\cdot2^{27})+2^{27}.
\]

Thus each accepted weak CRT class occurs at least 789 times, at least 1,578 checkpoints across the two accepted mod-3 classes before other constraints.

### `P_min` as a sole deep-root strategy

Finite exact scans through ordinary-X exposure depth `h=72` found no physical-score whole-family closures for completed roots `f=29,32,35,37`.

This is execution evidence only, not a theorem. Record:

- `../experiments/2026-09-02-deep-root-Pmin-to72.md`.

`P_min` remains valid and useful as a secondary pruning predicate.

## Closed synchronized seams retained for later use

1. A **full** coherent pair `Z mod2^27 × z_H mod3^28` exposes at most one ordinary checkpoint `Z` in the independent SAFE corridor.
2. An exposed ordinary `Z` contracts every source root to an exact debit-compatible parameter fiber.
3. Terminal ternary precision is fully absorbed inside the current right-H block, so no checkpoint ternary residue must cross the critical cut after that predicate is discharged.
4. Fixed-`(h,q)` correction is injective.
5. Dyadic prefix and ternary suffix correction localization and exact block correction composition are available.

The full CRT seam is **conditional**: use it only if a stronger exact state really supplies a full `z_H mod3^28` observation.

## Principal active object — source-controlled full correction membership

For a candidate ordinary source/checkpoint pair, define the required correction

\[
\boxed{C_{req}=2^{t_0}Z-3^{j_0}X.}
\]

A valid pre-bridge word `W` must satisfy simultaneously

\[
|W|=t_0,
\qquad
q(W)=j_0,
\qquad
C(W)=C_{req},
\]

and belong to the exact Route-B formation language induced by the source/control constraints.

Fixed-`(t_0,j_0)` correction injectivity means that **if** such a word exists it is unique. It does not provide existence or an inverse algorithm by itself.

The next computation must therefore solve a constrained correction-language inversion/join problem rather than a free target-dominance residue problem.

## Exact source-controlled interfaces to exploit

### 1. Source prefix channel

At an active source depth `h`, the exact prefix state is

\[
T^h(X)=y+3^q m,
\]

with

\[
X=r+2^h m.
\]

Refining the next parity bit is an exact affine child transformation.

### 2. Required correction modulo powers of two

For any `K<=t_0`, because `2^{t_0}Z` vanishes modulo `2^K`,

\[
\boxed{C_{req}\equiv-3^{j_0}X\pmod{2^K}.}
\]

Thus the source cylinder directly supplies a dyadic correction target without requiring `Z`.

This is a source-controlled observation, not an independent membership theorem.

### 3. Correction composition

For a split `W=AB` with right block one-count `q_B`,

\[
C(AB)=3^{q_B}C(A)+2^{|A|}C(B).
\]

This exact law permits meet/join or grammar-recursive inversion while retaining only the residues and controls queried by the current block.

### 4. H/L grammar

The exact H/L grammar represents the same target-dominance formation language. It may be used as a block recursion for correction realization; do not treat it as an independent probabilistic sparsity factor.

### 5. Physical score

When a source-controlled block family remains large, attach the exact directed `P_min` label for whole-family physical rejection. Do not merge different future-control classes merely because their physical labels agree.

## Immediate theorem / algorithm target

Construct an exact **source-controlled correction inverse quotient**.

A useful state should answer:

> Given a source prefix/control class and a required correction observation, can any legal H/L/pre-bridge completion realize that correction?

Minimum desired properties:

1. exact prefix control sufficient for future parity/source refinement;
2. predicate-relative correction residue, activated only at the precision the current block can observe;
3. exact block/grammar transition using correction composition;
4. legal merge theorem showing when two histories have identical future realization sets;
5. ability to emit either exact rejection or a smaller family requiring another predicate;
6. optional `P_min` secondary label only inside an exact future-control class.

## First practical milestone

Before attempting all `t_0` steps, build and certify the inverse quotient on finite block depths and compare against direct correction-language enumeration.

The regression must separately test:

- same source/control + same quotient -> same future correction realizability;
- different source controls are not silently merged;
- fixed-`(h,q)` injectivity is respected;
- dyadic observation is not promoted to full membership;
- block composition reproduces direct correction exactly.

Once the quotient is certified, apply it first to the deep retained roots where ordinary-X exposure and checkpoint-conditioned fibers are smallest.

## DSD audit rules

Allowed:

- exact correction composition;
- source prefix/control as an active state coordinate;
- predicate-relative residue forgetting after a block has discharged it;
- fixed-`(h,q)` injectivity after existence is established;
- finite inverse-quotient regressions as implementation evidence;
- secondary `P_min` pruning within exact future-control classes.

Forbidden:

- `adic mismatch -> membership rejection` unless the exact active language gate requires that equality;
- terminal target-dominance existence -> full correction membership;
- terminal dominance -> full `z_H mod3^28`;
- checkpoint/source exposure -> same orbit automatically;
- correction injectivity -> existence;
- finite inverse regression -> universal theorem;
- `P_min` finite non-closure -> proof that physical pruning can never work;
- marginal density multiplication;
- later refined bounds used retroactively.

## Global warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`. Route-A, `s>=2`, remaining formation sectors, and global branch completeness remain separate obligations.
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
6. Exact prefix discharge restarts the same correction equation on the residual suffix.
7. For an exact `(Y,Z,n,q)` residual instance, valuation decoding gives zero or one realizing parity word.

The full CRT seam is **conditional**: use it only if a stronger exact state really supplies a full `z_H mod3^28` observation.

## Principal active object — source-family correction realization

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

and the exact Route-B formation/source-control obligations.

The exact-pair inversion problem is now closed: fixed-`(t_0,j_0)` correction injectivity plus the residual valuation decoder reconstructs the unique possible word, or rejects.

The unresolved S10 problem is therefore **not** free correction-language inversion for one exact pair. It is compressed execution over the enormous affine source/checkpoint families while preserving every future formation predicate.

Canonical objects:

- `../theorems/SOURCE_CONTROLLED_RESIDUAL_CORRECTION_RECURSION.md`;
- `../theorems/RESIDUAL_VALUATION_JUMP_DECODER.md`;
- `../theorems/AFFINE_VALUATION_CYLINDER_JUMP.md`;
- `../audits/S10_EXACT_PAIR_INVERSION_HANDOFF_AUDIT.md`.

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

### 2. Source dyadic correction observation is redundant

For any `K<=t_0`,

\[
C_{req}\equiv-3^{j_0}X\pmod{2^K}.
\]

When the exact source parity prefix/control through depth `K` is already present, this is the same information and must not be counted as an independent pruning coordinate.

### 3. Residual correction recursion

For an exact realized prefix `A` with state `Y=T^{|A|}(X)`, the full correction equation restarts exactly on the suffix:

\[
C(B)=2^{|B|}Z-3^{q(B)}Y.
\]

Historical prefix correction may then be forgotten if all remaining source/formation controls are preserved.

### 4. Residual valuation decoder

For an exact remaining instance

\[
R=2^nZ-3^qY,
\]

with `q>0`, the next 1-position is forced by

\[
\boxed{a=v_2(R).}
\]

The forced prefix `0^a1` is discharged exactly and the same residual problem restarts.

### 5. Endpoint-free affine valuation jump

Before the remaining endpoint depth is reached,

\[
v_2(R)=v_2(Y).
\]

For an affine current-state family

\[
Y=y+A m,
\qquad A\text{ odd},
\]

the branch `v2(Y)=a` is exactly one parameter residue

\[
\boxed{
m\equiv(2^a-y)A^{-1}\pmod{2^{a+1}}.
}
\]

Writing `m=rho_a+2^(a+1)k`, the complete forced block `0^a1` jumps to another exact affine cylinder

\[
Y'=y'_a+3A k.
\]

Thus source-family refinement can operate by odd-event jumps rather than one parity bit at a time.

### 6. H/L grammar and physical score

H/L/pre-bridge controls remain separate exact future-language coordinates. They must be updated across every valuation jump before histories may merge.

`P_min` remains an optional secondary label only within an exact future-control class.

## Immediate theorem / algorithm target

Construct an exact **valuation-cylinder formation transducer** over the retained roots.

A useful state should contain:

1. affine current-state cylinder `(y,A,[m_lo,m_hi])`;
2. remaining length and one-count controls;
3. exact H/L/pre-bridge future-control state;
4. any active checkpoint/debit state at its certified resolution;
5. optional `P_min` only inside the same exact future-control class.

One transition should:

1. partition the parameter interval by `v2(y+A m)=a`;
2. jump the forced block `0^a1` exactly;
3. update remaining counters and formation controls;
4. reject any child violating an active exact predicate;
5. merge children only under a proved future-realizability equivalence.

## First practical milestone

Build and certify the valuation-cylinder transducer at finite depths and compare it against the existing bitwise source-channel transducer.

The regression must separately test:

- exact partition of the parent parameter interval;
- identical parity words/end states to bitwise refinement;
- exact update of ballot/H-L control across `0^a1`;
- no merge across distinct future controls;
- residual correction recursion agrees with direct correction composition;
- endpoint information is not used before its actual resolution is required.

Then apply the jump transducer first to the deepest retained roots, where the source parameter intervals are smallest, before widening to all 14 roots.

## DSD audit rules

Allowed:

- exact correction composition and residual recursion;
- exact-pair valuation decoding;
- affine valuation-cylinder partition and forced zero-run jump;
- source prefix/control as an active state coordinate;
- predicate-relative forgetting after a block has discharged it;
- finite transducer regressions as implementation evidence;
- secondary `P_min` pruning within exact future-control classes.

Forbidden:

- exact-pair uniqueness -> family-level uniqueness;
- equal valuation/residual -> legal merge when future controls differ;
- `adic mismatch -> membership rejection` unless the exact active language gate requires that equality;
- terminal target-dominance existence -> full correction membership;
- terminal dominance -> full `z_H mod3^28`;
- checkpoint/source exposure -> same orbit automatically;
- finite transducer regression -> universal Route-B closure;
- `P_min` finite non-closure -> proof that physical pruning can never work;
- marginal density multiplication;
- later refined bounds used retroactively.

## Global warning

Even complete closure of all 14 current Route-B roots would close only `A0, s=1, Route-B`. Route-A, `s>=2`, remaining formation sectors, and global branch completeness remain separate obligations.

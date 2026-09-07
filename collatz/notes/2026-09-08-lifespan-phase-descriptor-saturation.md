# Lifespan phase-descriptor saturation — MATH-023

Date: 2026-09-08

Status: `CONFIRMED / FINITE DIAGNOSTIC / SATURATED / NO MATERIAL COMPRESSION`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## 1. Question after MATH-022

MATH-022 classifies the `17,745` right offsets in `0<=r<=10^7` that survive every coefficient prefix through depth 61, and computes

\[
L_{\max}(r)=\max_{1025\le b\le1363}L(b,r).
\]

Every audited state satisfies

\[
L(b,r)<3r+1,
\]

but enumerating every right offset separately is still a finite bootstrap rather than a structural all-offset rule.

A natural DSD compression candidate is the lower-prefix phase

\[
\boxed{(q_{61},\;y\bmod2^m)},
\qquad y=T^{61}(r).
\]

The question is whether this smaller descriptor determines the finite output metric `L_max(r)` while merging a useful number of the 17,745 states.

## 2. Exact aliasing audit

For each `m`, states are grouped by

\[
(q_{61},y\bmod2^m).
\]

A group is called **conflicting** when it contains two audited offsets with different `L_max` values.

Selected exact results:

| m | classes | conflicting classes | states inside conflicting classes | max distinct lifespans in one class |
|---:|---:|---:|---:|---:|
| 11 | 8,910 | 4,818 | 13,605 | 8 |
| 20 | 17,702 | 41 | 82 | 2 |
| 24 | 17,742 | 2 | 4 | 2 |
| 25 | 17,743 | 1 | 2 | 2 |
| 26 | 17,744 | 0 | 0 | 1 |

Thus the phase resolution must be raised to 26 bits before the **finite lifespan metric** becomes unambiguous on this audited domain.

## 3. Exact m=25 obstruction

At 25 bits the final conflicting class has

\[
\boxed{q_{61}=41},
\]

\[
\boxed{y\bmod2^{25}=11,114,030}.
\]

It contains

\[
r_1=702,631,
\qquad L_{\max}(r_1)=210,
\]

and

\[
r_2=7,066,623,
\qquad L_{\max}(r_2)=177.
\]

Therefore

\[
(q_{61},y\bmod2^{25})\text{ equal}
\not\Rightarrow
L_{\max}\text{ equal}
\]

inside the exact MATH-022 finite domain.

This is a direct AP-2 / finite-state-aliasing counterexample against truncating the lifespan computation to 25 endpoint bits.

## 4. Why m=26 is not useful compression

At 26 bits there is no lifespan ambiguity, but the number of classes is

\[
17,744
\]

for

\[
17,745
\]

input states.

So only one pair is merged.

One such equal-metric pair is

\[
q_{61}=40,
\qquad y\bmod2^{26}=1,641,329,
\]

with

\[
r=311,291
\]

and

\[
r=311,295,
\]

both having

\[
L_{\max}=171.
\]

The reduction factor is only

\[
\frac{17,745}{17,744}\approx1.000056.
\]

That is computationally negligible.

Moreover, equality of this **finite output metric** does not prove that the two states are interchangeable for every downstream Collatz/Hensel calculation.  Therefore even this lone merge is not promoted to a general state quotient.

## 5. DSD route decision

The phase-descriptor route behaves as follows:

- low `m`: useful compression but unacceptable aliasing;
- high `m`: ambiguity disappears only after almost all original state identity has returned.

Hence

\[
\boxed{
(q_{61},y\bmod2^m)\text{ lifespan compression}
=\texttt{SATURATED / NO MATERIAL COMPRESSION}.
}
\]

The next route should **not** continue increasing `m`.

The better target is an inequality or monotone quantity that upper-bounds lifespan directly, ideally proving

\[
L(b,r)<3r+1
\]

from a smaller structural descriptor rather than reconstructing the trajectory phase at nearly full resolution.

## 6. Scope

MATH-023 is deliberately weaker than a full-state quotient theorem.

It establishes only the aliasing behavior of the finite metric

\[
L_{\max}(r)
\]

on the MATH-022 domain `0<=r<=10^7`.

It does not establish:

- equivalence of trajectories sharing 26 phase bits;
- equivalence for offsets above `10^7`;
- arbitrary-depth endpoint-state compression;
- first-cell or Collatz closure.

## 7. Prohibited upgrades

Do not infer

\[
L_{\max}\text{ equal}\Rightarrow\text{same Collatz state}.
\]

Do not use the `m=26` finite no-conflict observation as a universal 26-bit right-congruence theorem.

Do not infer that the failure of this compression route invalidates the MATH-021/MATH-022 linear-halo bootstrap.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_lifespan_phase_descriptor_saturation_certificate.cpp`

Certificate commit:

`6057f4c0a12288dce92936c65fc40a351bdb7908`

## Next target

Search the audited survivor data for a **lifespan upper-bound descriptor** rather than an exact phase identity descriptor.

High-value candidates are quantities that can be propagated monotonically or bounded without preserving the full endpoint phase, such as:

1. coefficient-surplus budget over a fixed future window;
2. earliest unavoidable even-step deficit;
3. an exact upper envelope for future odd-count accumulation from the 340 address labels;
4. a DSD dominance relation that proves one lower state cannot outlive another.

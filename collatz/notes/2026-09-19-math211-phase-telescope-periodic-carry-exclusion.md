# MATH-211 — phase-telescope exclusion of periodic full-boundary carry cycles

Date: 2026-09-19

Status: `EXACT APERIODICITY REDUCTION / PERIODIC FULL-BOUNDARY CARRY BRANCH CLOSED / r=10 OPEN`

## 1. Purpose

MATH-205 gives the exact ordinary carry recurrence between canonical factors.
MATH-207 gives the coefficient telescope for complete boundary blocks.

This note combines them to remove periodic full-boundary factor/carry cycles without enumerating depths or paid-count layers.

## 2. Full boundary factors

Let the (i)-th complete boundary factor be
[
A_i+2^{H_i}tlongmapsto B_i+3^{Q_i}t.
]

Its legal phase transition is
[
oxed{
rac{3^{Q_i}}{2^{H_i}}=rac{omega_i}{omega_{i+1}}.
}
]

For a chain of (m) factors,
[
oxed{
rac{3^{sum_iQ_i}}{2^{sum_iH_i}}
=
rac{omega_0}{omega_m}.
}
]

## 3. Periodic full-state return would force an impossible power equality

Suppose a nonempty full-boundary state cycle returned to the same phase:
[
omega_m=omega_0.
]

Then
[
3^{Q_{m cyc}}=2^{H_{m cyc}},
]
where
[
Q_{m cyc}=sum_iQ_i>0,qquad
H_{m cyc}=sum_iH_i>0.
]

Unique prime factorization gives a contradiction.

Hence
[
oxed{
	ext{no nonempty legal complete-boundary chain can return to the same phase.}
}
]

Therefore no exact periodic carry cycle can exist in the complete state
[
(	ext{phase},	ext{factor type},d,	ext{legality state}).
]

## 4. Relation to the MATH-205 carry-cycle equation

For a symbolic transition cycle, MATH-205 gives
[
2^Z d_m=3^Qd_0+K.
]

A full-state carry cycle would additionally require
[
d_m=d_0
]
and return of the accompanying factor/phase state.

The phase return is already impossible before solving
[
(2^Z-3^Q)d_0=K.
]

Thus rational/integer carry-cycle candidates obtained from the algebraic carry equation are irrelevant unless their phase state also closes; no legal nonempty phase closure exists.

## 5. What periodic means here

This theorem excludes periodicity of the **complete proof-facing boundary state**.

It does not claim that:

- the scalar carry (d) cannot repeat at different phases;
- a factor label cannot reappear later;
- an ordinary Collatz orbit cannot revisit some coarse descriptor;
- every infinite survivor is periodic.

The surviving hard core is genuinely aperiodic in the complete boundary state.

## 6. r=10 consequence

For repeated (r=10)-tagged dangerous boundary transfers, any infinite survivor must be aperiodic in phase/full factor state.

Therefore the remaining (r=10) problem is not a cycle-detection problem.

It is exactly the aperiodic shrinking-resonance problem:
[
oxed{
	ext{Hensel-extremal}
cap
{jge0}
cap
{
u_2(C_R)ge13}
}
]
under the common recurrence.

This narrows the final closure target without any (r)- or depth-layer enumeration.

## 7. Claim boundary

Established:

- no nonempty exact full-boundary phase cycle;
- hence no periodic complete factor/carry state cycle;
- periodic carry-cycle algebra need not be separately enumerated.

Not established:

- exclusion of aperiodic nonzero-carry paths;
- (r=10) closure;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

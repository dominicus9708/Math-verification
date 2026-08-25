# Fixed-Q plateau-swap healing and asymptotic fibre compatibility

Date: 2026-08-26

Status: **exact algebraic healing lemma + asymptotic compatibility reduction.**  This note shows that a fixed-depth root-globalized backtrace filter cannot destroy the positive-density late plateau fibres used by the triangular Fourier argument on the harmonic hard core.  It does not cover growing inverse depth Q(i), and it is not a proof of the Collatz conjecture.

## 1. Context after the L7 scope correction

The 2026-08-25 L7 scope audit withdrew unconditional later-block residue maximality.  The local Hensel arithmetic remains exact, but a local predecessor x'<x need not satisfy x'<N at the original root.

The repeated root-backtrace filters survive that audit because they contain an explicit headroom inequality proving the alternate ancestor is below N.

The question addressed here is narrower:

> If a valid fixed-Q root-backtrace condition is imposed on the harmonic hard core, can it split the late `01 <-> 10` plateau fibres so severely that the triangular Fourier decay disappears?

The answer is no, for fixed Q.

## 2. Odd-event affine residue recurrence

At fixed inverse depth Q, work modulo

\[
M=3^Q.
\]

For an odd-event gap `v>=1`, define

\[
\boxed{
F_v(y)=(3y+1)2^{-v}\pmod{3^Q}.
}
\]

This is the residue recurrence used by the phase-adaptive backtrace certificates.

Consider a local time-expanded plateau swap `01 <-> 10`.  In odd-gap coordinates it moves one odd event by one binary step, so two adjacent gaps change as

\[
(a,b)\longleftrightarrow(a+1,b-1),
\qquad b\ge2.
\]

Both sides have the same total binary length and the same number of odd events.

## 3. Exact local residue defect

Starting from any residue y,

\[
F_b(F_a(y))
=
(9y+3+2^a)2^{-(a+b)},
\]

while

\[
F_{b-1}(F_{a+1}(y))
=
(9y+3+2^{a+1})2^{-(a+b)}.
\]

Therefore

\[
\boxed{
F_{b-1}(F_{a+1}(y))-F_b(F_a(y))
=2^{-b}\pmod{3^Q}.
}
\]

The defect is independent of y and is a 3-adic unit:

\[
\boxed{v_3(\Delta_0)=0.}
\]

Reversing the swap changes only the sign.

## 4. Exact Q-step healing

After the two affected gaps, suppose both words share the same future odd-gap sequence `v_1,v_2,...`.

For the residue difference,

\[
\Delta_{t+1}
=3\,2^{-v_{t+1}}\Delta_t
\pmod{3^Q}.
\]

Since every power of 2 is a unit modulo `3^Q`,

\[
\boxed{
v_3(\Delta_t)=t
\qquad(0\le t<Q),
}
\]

and hence

\[
\boxed{
\Delta_Q=0\pmod{3^Q}.
}
\]

Thus a single plateau swap can alter the fixed-Q endpoint residue only for a bounded future window.  After Q common odd-event updates the two residue states are exactly identical again.

This is a finite-memory theorem, not a mixing heuristic.

Regression certificate:

`collatz/src/q_fixed_plateau_swap_healing_certificate.py`

checks 295,200 exact cases for `1<=Q<=8`, all starting residues, local gaps in the tested range, and a nonconstant common suffix.

## 5. Height and coefficient coordinates

For an interior mixed plateau pair beginning at strictly positive relative height, `01 <-> 10` preserves:

1. the total odd count across the pair;
2. the coefficient-survival condition outside the pair;
3. strict open positivity, because the two intermediate heights differ by one but both remain nonnegative when the pair begins above the boundary;
4. the post-pair height exactly.

Thus the only fixed-Q backtrace coordinate with a persistent local difference is the residue modulo `3^Q`, and Section 4 shows that even this difference heals after Q common odd events.

## 6. Only low-height times can activate fixed-Q backtrace

The previously proved fixed-Q barrier gives the necessary condition

\[
0\le h_i\le H_Q,
\qquad
H_Q=\left\lfloor Q\log_2(3/2)\right\rfloor,
\]

for a fixed-Q root-backtrace witness to fire.

On the nonperiodic no-first-descent harmonic hard core,

\[
\#\{i<q:h_i\le H_0\}
=O_{N,H_0}(q^{1/9})
\]

for every fixed height strip `H_0`.

Use `H_Q+1` to absorb the one-step height perturbation inside a plateau swap.

A plateau site can change a fixed-Q backtrace decision only if either

- its own local height perturbation meets the active strip, or
- one of the next Q residue states lies at a time where the fixed-Q predicate is active.

Consequently the number of plateau sites whose orientation can affect the fixed-Q filter is bounded by

\[
\boxed{
O_Q\!\left(\#\{i<q:h_i\le H_Q+1\}\right)
=O_{N,Q}(q^{1/9})
=o(q).
}
\]

A concrete non-optimized covering constant is obtained by charging at most `Q+2` preceding/local mixed sites to each active low-height event.

## 7. Asymptotic transparency to a linear mixed fibre

Suppose a late Beatty fibre contains

\[
n(q)\ge c q
\]

mixed plateau coordinates for some fixed `c>0`; the existing triangular assembly uses such a linear mixed-coordinate regime.

Delete every plateau site contaminated by the fixed-Q backtrace filter as in Section 6.  The clean set has

\[
\boxed{
n_{\rm clean}(q)=n(q)-o(q)=cq-o(q).
}
\]

Hence fixed-Q conditioning removes only a zero-density subset of the plateau coordinates.

The triangular near-one defect-code proof may therefore be run on the clean coordinates.  Removing `o(q)` factors can change only a subexponential prefactor and cannot erase a previously positive linear Fourier-decay exponent.

In particular, if the unconditioned triangular fibre has

\[
2^{-m}\sum_k P_F(k)
\le 2^{-\eta n(q)+o(q)}
\qquad(\eta>0),
\]

then after imposing any fixed-Q root-backtrace filter one still has a positive exponent of the same asymptotic order:

\[
\boxed{
2^{-m}\sum_k P_{F,Q}(k)
\le 2^{-\eta n(q)+o(q)}.
}
\]

The `o(q)` term absorbs the deleted contaminated coordinates and finite-state boundary data.  This statement is about compatibility of the fixed-Q conditioning with the already established triangular mechanism; it is not a standalone global survivor theorem.

## 8. Audit of the other root conditions

### 8.1 Root-globalized low-bit lock

If a previously fixed root label is known modulo `2^P`, any later plateau swap whose first changed binary position is `j>=P` has root translation divisible by `2^j`, hence preserves the lock modulo `2^P`.

### 8.2 Root credit-1 and higher root-Hensel filters

These are globally safe root filters, but they are not required to define the triangular harmonic upper-bound fibre.  If conditioning on them complicates the plateau product, they may simply be omitted: dropping a necessary filter enlarges the candidate set, so an upper bound proved on the enlarged set remains valid.

This is preferable to silently assuming fibre invariance that has not been proved.

### 8.3 Arbitrary later-block Hensel maximality

This condition is not part of the admissible hard-core conditioning after the 2026-08-25 scope correction.  It must not be reintroduced.

### 8.4 Growing inverse depth

The present theorem is explicitly fixed-Q.  If a future terminal route uses

\[
Q=Q(i)\to\infty,
\]

the healing window also grows, and the fixed-strip sparsity argument no longer applies automatically.  Growing-Q compatibility remains a separate problem.

## 9. DSD-style split of the obstruction

The compatibility chain is now

\[
\boxed{
\begin{array}{c}
\text{late mixed plateau swap}\\
\Downarrow\\
\text{height/odd count remerge immediately}\\
\Downarrow\\
\text{fixed-Q residue defect is a 3-adic unit}\\
\Downarrow\\
v_3(\Delta_t)=t\\
\Downarrow\\
\text{exact healing after Q common odd events}\\
\Downarrow\\
\text{only }O_{N,Q}(q^{1/9})\text{ low-height opportunities matter}\\
\Downarrow\\
\text{only }o(q)\text{ plateau sites are contaminated}\\
\Downarrow\\
\text{positive-density triangular Fourier decay survives.}
\end{array}
}
\]

Thus **fixed-Q root-safe backtrace conditioning is no longer a fibre-compatibility obstruction**.

## 10. Revised remaining frontier

The next unresolved compatibility questions are no longer ordinary fixed-Q conditions.  The serious possibilities are:

1. a genuinely growing-depth `Q(i)` root-backtrace theorem;
2. a nonlocal condition that is indispensable to the hard-core geometry and can contaminate a positive density of late plateau swaps;
3. reconnecting the triangular harmonic branch to a full minimal-counterexample covering argument across all scaling families.

The next proof calculation should therefore audit the global branch decomposition itself, rather than spend more effort on fixed-Q fibre invariance.

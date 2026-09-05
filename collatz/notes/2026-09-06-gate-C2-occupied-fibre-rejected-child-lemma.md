# Gate C2 occupied-fibre rejected-child lemma

Date: 2026-09-06

Status: **SAFE EXACT LEMMA + FINITE m=44 DIAGNOSTIC + OPEN RECURRENCE GATE.**

This note sharpens the absolute-count Gate-C2 audit.  The signed transport term `K_L` has an exact elementary interpretation: `D_L-K_L` is twice the selector mass placed in the child that the Collatz coefficient-survivor tree rejects.

This removes an unnecessary abstraction from the terminal integer-count problem.

Nothing here proves the Collatz conjecture.

---

## 1. One one-child parent

At a parent residue `r`, let the selector masses in its two dyadic children be

\[
c_0,c_1\in\mathbb Z_{\ge0},
\qquad
c=c_0+c_1,
\qquad
u=c_0-c_1.
\]

At a one-child Beatty parent exactly one child survives.  Let

\[
v=b_0-b_1\in\{+1,-1\}
\]

encode its orientation.

### Child 0 survives

Then `v=+1`, child 1 is rejected, and

\[
c-vu
=(c_0+c_1)-(c_0-c_1)
=2c_1.
\]

### Child 1 survives

Then `v=-1`, child 0 is rejected, and

\[
c-vu
=(c_0+c_1)+(c_0-c_1)
=2c_0.
\]

Hence in both cases

\[
\boxed{
c-vu=2c_{\rm rejected}.}
\]

Status: **SAFE EXACT IDENTITY.**

---

## 2. Aggregate identity

Let `D_L` be the total selector mass on one-child parents and `K_L` the signed repair term.  Define

\[
E_L
:=
\sum_{r\in D_L} c_{\rm rejected}(r).
\]

Then summing the local identity gives

\[
\boxed{D_L-K_L=2E_L.}
\]

Substituting into the exact child-transport equation

\[
C_{L+1}
=C_L-\frac{D_L}{2}+\frac{K_L}{2}
\]

yields the simpler integer form

\[
\boxed{C_{L+1}=C_L-E_L.}
\]

Thus `E_L` is literally the number of currently surviving selector assignments whose next dyadic child is rejected at this rise.

No probability, normalization, or limiting argument is present.

Status: **SAFE EXACT INTEGER TRANSPORT.**

---

## 3. Strict loss needs only one rejected occupied child

Because

\[
E_L\in\mathbb Z_{\ge0},
\]

we have

\[
\boxed{
E_L>0
\iff
C_{L+1}<C_L.
}
\]

Moreover every positive loss removes at least one actual selector integer:

\[
E_L>0
\Longrightarrow
C_{L+1}\le C_L-1.
\]

Therefore, for a fixed selector layer of initial size `2^m`, at most `2^m` positive-loss events can occur before extinction.

A qualitative terminal criterion is consequently enough:

> If, whenever a fixed layer still has a survivor, the future contains another scale with `E_L>0`, then that layer must become empty after finitely many such losses.

Equivalently, a nonempty fixed layer can survive forever only if its count eventually stabilizes and

\[
\boxed{E_L=0}
\]

at every sufficiently late Beatty rise.

This is weaker than requiring a uniform positive contraction fraction or a divergent normalized loss sum.

Status: **SAFE FINITE-SET CLOSURE LEMMA.**

---

## 4. What an immortal stabilized layer would mean

Suppose for contradiction that some fixed layer has

\[
C_L=C_*>0
\]

for all sufficiently large `L`.

Then every remaining selector integer must avoid rejection forever.  At each sufficiently late Beatty rise, every occupied one-child parent must place all of its selector mass in the unique surviving child.

Thus eventual survival forces an exact orientation-lock condition:

\[
\boxed{
\text{occupied selector child}
=
\text{unique coefficient-surviving child}
}
\]

whenever an occupied path reaches a one-child boundary.

Alternatively the path can avoid the boundary by remaining at positive coefficient surplus.

Hence the terminal problem separates into two deterministic escape modes:

1. **high-surplus escape:** an immortal path eventually avoids one-child boundary exposure;
2. **orientation-lock escape:** it reaches one-child boundaries but always chooses the surviving child.

This is precisely where the older Gate-A/Gate-B architecture re-enters:

- Gate A must prevent permanent high-surplus escape or force recurrent return to a controlled strip in the actual canonical language;
- Gate B/support-aware cross-base control must prevent perfect orientation locking on every such return.

Status: **SAFE STRUCTURAL REDUCTION.**

---

## 5. Robust observable without knowing the sign of K

The exact identity uses `K_L`, but the existing finite certificate also provides

\[
|K_L|\le U_L,
\qquad
U_L=\sum_r|u(r)|.
\]

Therefore

\[
E_L
=\frac{D_L-K_L}{2}
\ge
\frac{D_L-U_L}{2}.
\]

Define the robust occupied-fibre fractional loss

\[
\boxed{
\underline\Delta_L^{\rm occ}
:=
\frac{D_L-U_L}{2C_L}.
}
\]

Whenever

\[
D_L>U_L,
\]

we have an exact strict integer loss regardless of boundary orientation.

Unlike global `h_min/h_max`, the quantities `C,D,U` are evaluated only on the actual occupied selector mass and remain meaningful after dyadic resolution exceeds selector support.

Status: **SAFE SUPPORT-AWARE SUFFICIENT CONDITION.**

---

## 6. Full m=44 finite diagnostic through depth 26

The authoritative `m44_full_mass_transport_certificate.cpp` gives all Beatty rises through `L=25` and certifies

\[
U_L<D_L
\]

at every one of them.

Using

\[
\underline\Delta_L^{\rm occ}
=
\frac{D_L-U_L}{2C_L},
\]

the selected later values are

\[
\begin{array}{c|c}
L&\underline\Delta_L^{\rm occ}\\\hline
17&0.1136430754\\
19&0.0884399409\\
20&0.1471791592\\
22&0.0945589667\\
23&0.1510713590\\
25&0.0948597033
\end{array}
\]

Using all fifteen certified rise rows `L=3,4,6,7,9,11,12,14,15,17,19,20,22,23,25`, their robust product gives

\[
\boxed{
-\log_2\prod_L(1-\underline\Delta_L^{\rm occ})
\approx4.01493210\text{ bits}.
}
\]

The actual exact depth-26 mass is

\[
C_{26}=1,087,765,074,138,
\]

so the actual loss from the initial `2^44` family is

\[
\boxed{
44-\log_2 C_{26}
\approx4.01549585\text{ bits}.
}
\]

Thus the orientation-independent `D-U` bound accounts for almost all of the observed finite loss through depth 26.

This is encouraging evidence that `K` is very small at these pre-support scales, but it is **FINITE ONLY**.  The selector support barrier prevents extrapolating this global-mixing behaviour to arbitrary larger dyadic resolution.

Status: **FINITE EXACT/ROBUST DIAGNOSTIC.**

---

## 7. Why this changes the preferred terminal target

The previous normalized-mass target asked for a divergent sum of positive fractional losses.

For a fixed finite selector layer, integerity permits a weaker statement.  It is enough to rule out eventual stabilization:

\[
\boxed{
C_L>0
\Longrightarrow
\exists L'>L:\ E_{L'}>0.
}
\]

If this implication holds for every `L` after some finite prefix, repeated application must exhaust the finite layer.

A practical stronger target is

\[
\boxed{
\text{every sufficiently late return to a fixed low-surplus state set}
\Longrightarrow
E_L>0\text{ within a bounded block}.
}
\]

Together with a root-global theorem that every immortal canonical candidate returns to that state set infinitely often, this would close the fixed-layer branch without needing any density-to-single-path upgrade.

This provides a direct bridge to the terminal roadmap:

\[
\boxed{
\text{Gate A: recurrent controlled-strip return}
\ +
\text{Gate B: occupied rejected-child event}
\Longrightarrow
\text{fixed-layer extinction by integerity}.
}
\]

Under this formulation, a separate Gate C measure-to-integer argument becomes largely bookkeeping once Gates A and B are truly stated on the actual canonical selector language.

Status: **NEW CONDITIONAL ARCHITECTURE.**

---

## 8. Remaining difficulty

The hard theorem has not disappeared.  It has been localized.

One must prove that an actual minimal-counterexample candidate cannot simultaneously satisfy forever:

1. coefficient surplus stays away from every killing strip, or
2. whenever it enters a one-child state, its ternary/canonical child orientation always matches the unique surviving dyadic orientation.

The symbolic Beatty boundary theorem controls class mass, not an individual occupied path.  The global selector min/max lemma cannot be continued beyond the support barrier.  Therefore neither result alone proves this recurrence/mismatch statement.

The next proof target is a **root-global, support-aware recurrence or orientation-mismatch theorem**, not stronger global equidistribution.

---

## 9. DSD audit

### SAFE

1. `D-K=2E_rejected` exactly.
2. `C_{L+1}=C_L-E_L` exactly at a one-child rise.
3. Any positive `E_L` removes at least one actual selector assignment.
4. A fixed finite layer cannot undergo infinitely many positive integer losses without becoming empty.
5. `D>U` is a sign-free sufficient condition for strict occupied-fibre loss.

### FINITE ONLY

The m=44 robust loss through depth 26 and its approximately `4.015`-bit reduction.

### OPEN

Prove recurrent occupied-fibre loss for every hypothetical immortal canonical selector layer, preferably through the Gate-A/Gate-B low-surplus state architecture.

### PROHIBITED UPGRADES

1. Do not extrapolate `U/D` from m=44 through L=25.
2. Do not infer individual-path boundary recurrence from the symbolic constant boundary fraction.
3. Do not restore global min/max positivity after the selector support barrier.
4. Do not revive arbitrary later-block Hensel/L7 maximality.

---

## 10. Reproducibility

Algebra and finite-budget certificate:

`collatz/src/gateC2_occupied_fibre_rejected_child_certificate.py`

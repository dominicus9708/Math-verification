# COV-1 first-coefficient-crossing audit on `27 mod 36`

Date: 2026-09-06

Status: **SAFE WORD-LEVEL REDUCTION + EXACT FINITE CERTIFICATE THROUGH BINARY DEPTH 38; GLOBAL FIRST-CROSSING EXCLUSION OPEN.**

This note concerns the first unresolved recursive-sufficiency coverage branch

\[
\boxed{N=36k+27.}
\]

An exact word-level scan finds no paradoxical first coefficient crossing through depth 38, but the result is finite only.  The existing mechanical-envelope theorem does not by itself globalize this observation because the missing datum is the same-integer dyadic/CRT address.

Nothing here proves the Collatz conjecture or closes `COV_1`.

---

## 1. First-crossing word

For a parity prefix `w` of length `L`, odd count `q`, and correction `C(w)`, write

\[
\boxed{
T^L(N)=\frac{3^qN+C(w)}{2^L}.
}
\]

At the **first coefficient crossing**,

\[
3^{q_i}\ge2^i\qquad(i<L),
\]

while

\[
3^q<2^L.
\]

Put

\[
\boxed{D:=2^L-3^q>0.}
\]

The existing mechanical-envelope theorem proves that, for fixed `L`, the Beatty/mechanical first-crossing word maximizes `C(w)` over the full first-crossing language.  That theorem controls the real allowance

\[
C(w)/D,
\]

but not the actual dyadic start residue of each word.

---

## 2. Canonical dyadic residue

The parity word determines the unique canonical start residue

\[
\boxed{
r(w)
\equiv
-C(w)3^{-q}
\pmod{2^L},
\qquad 0\le r(w)<2^L.
}
\]

On the COV-1 root the first two shortcut bits are `11`, so

\[
r(w)\equiv3\pmod4.
\]

Every ordinary integer with prefix `w` is

\[
N=r+a2^L,
\qquad a\in\mathbb N_0.
\]

---

## 3. Exact intersection with `36k+27`

Since `L>=2`, the condition

\[
N\equiv27\pmod{36}
\]

is equivalent to one congruence modulo `9` after the fixed `3 mod 4` head is removed.

Because `2^L` is a unit modulo `9`, there is a unique

\[
\boxed{a_0\in\{0,1,\ldots,8\}}
\]

such that

\[
\boxed{
N_0:=r+a_0 2^L
\equiv27\pmod{36}.
}
\]

`N_0` is the least nonnegative integer in the intersection of the parity cylinder with the progression.

All other members of that intersection are

\[
\boxed{
N_t=N_0+9t\,2^L,
\qquad t\ge0.
}
\]

Status: **SAFE CRT FACT.**

---

## 4. Why only the least representative must be tested

Let

\[
Y_t:=T^L(N_t).
\]

Since replacing `N` by `N+2^L` replaces the endpoint by `Y+3^q`,

\[
Y_t=Y_0+9t\,3^q.
\]

Therefore

\[
\begin{aligned}
N_t-Y_t
&=(N_0-Y_0)+9t(2^L-3^q)\\
&=(N_0-Y_0)+9tD.
\end{aligned}
\]

Because

\[
D>0,
\]
we obtain the exact monotonicity

\[
\boxed{
N_t-Y_t\ge N_0-Y_0.
}
\]

Hence

\[
\boxed{
T^L(N_0)<N_0
\Longrightarrow
T^L(N_t)<N_t\text{ for every }t\ge0.
}
\]

Conversely, a paradoxical first crossing anywhere in this parity/progression intersection would already occur at its least representative `N_0`.

Thus each first-crossing parity word requires exactly one integer test.

Status: **SAFE EXACT REDUCTION.**

---

## 5. Equivalent correction inequality

Using

\[
2^LY_0=3^qN_0+C(w),
\]

we have

\[
2^L(N_0-Y_0)
=(2^L-3^q)N_0-C(w)
=DN_0-C(w).
\]

Therefore the crossing is paradoxical exactly when

\[
\boxed{
DN_0\le C(w).
}
\]

Equivalently,

\[
\boxed{
N_0\le\frac{C(w)}D.
}
\]

The mechanical-envelope theorem gives an upper bound on the right-hand side, but `N_0` depends on the same word's dyadic residue.  This is the unresolved cross-base interaction.

---

## 6. Exact finite audit through `L<=38`

`collatz/src/cov1_first_crossing_mod36_certificate.cpp` generates every root-`11` first-crossing word through

\[
\boxed{L\le38}
\]

using exact integer arithmetic.

For each word it:

1. computes `C(w)` and `q`;
2. reconstructs `r(w) mod 2^L`;
3. solves the unique `a_0 in {0,...,8}`;
4. forms the least actual progression member `N_0`;
5. computes the exact crossing endpoint `Y_0`;
6. rejects the run if `Y_0>=N_0`.

The total number of first-crossing words tested is

\[
\boxed{150,456,308.}
\]

Result:

\[
\boxed{
\#\{w:L\le38,\ T^L(N_0(w))\ge N_0(w)\}=0.
}
\]

Status: **FINITE ONLY.**

---

## 7. Closest finite case

The smallest observed positive descent margin is

\[
\boxed{N_0-T^L(N_0)=17.}
\]

It occurs at

\[
\boxed{
L=27,
\qquad q=17,
\qquad N_0=495,
\qquad T^{27}(495)=478.
}
\]

The parity word in time order is

\[
\boxed{
111101110111010110110100010.
}
\]

Thus even the closest case in the finite scan still descends strictly, but the margin `17` is small enough that no useful uniform positive-gap extrapolation is justified.

---

## 8. Relation to the earlier depth-18 cylinder coincidence

A direct dyadic-cylinder calculation had found that through depth 18 the number of `36k+27` cylinders with no uniform forward descent exactly matched the coefficient-surviving ballot count.

The present calculation explains the precise content of that coincidence:

> through the audited range, every first coefficient crossing available on the COV-1 root already gives actual descent at the least `27 mod 36` representative, hence at every member of that cylinder/progression intersection.

The statement is now checked directly through depth 38 rather than inferred from aggregate counts.

It remains a finite phenomenon until a cross-base theorem is proved.

---

## 9. Why the mechanical envelope does not finish the proof

For any first-crossing word,

\[
C(w)\le C_{\rm mech}(L).
\]

Hence a paradoxical crossing would require

\[
N_0\le\frac{C_{\rm mech}(L)}{D}.
\]

This is useful as an Archimedean screen.

However different words have different canonical residues `r(w)`, and therefore different CRT representatives `N_0(w)`.  Remainder ordering does not automatically co-order these dyadic representatives.

Accordingly,

\[
\boxed{
C(w)\le C_{\rm mech}
\not\Rightarrow
DN_0(w)>C(w).
}
\]

without an additional same-integer/cross-base statement.

Status: **GLOBALIZATION OPEN.**

---

## 10. Handoff to the global R1 theorem

The repository already contains an externally supported R1 lower-bound theorem.

For a nonperiodic renewal-floor obstruction whose first coefficient crossing survives above its start, the Rozier--Terracol paradoxical frontier plus the first-crossing ceiling imply

\[
\boxed{N>2.8\times10^{19}}
\]

and

\[
\boxed{H>5.395570552\times10^9}
\]

odd events before the first coefficient crossing.

Therefore the new finite COV-1 certificate should be viewed as a low-depth exact front end to that global result, not as an asymptotic substitute for it.

In particular, if a hypothetical nonrecursive member of `36N_0+27` is a nonperiodic renewal floor and has finite coefficient stopping time, the only surviving R1 branch is already forced into the extreme-depth regime handled by the existing R1 architecture.

No claim is made here about the separate infinite-coefficient-survival branch or a positive periodic cycle branch.

---

## 11. DSD audit

### SAFE

1. one first-crossing word gives one canonical dyadic residue;
2. its intersection with `27 mod 36` has one least CRT representative `N_0`;
3. crossing descent margin increases strictly along all later members of that intersection;
4. therefore testing `N_0` is sufficient for the whole word-cylinder/progression intersection;
5. the exact finite scan through `L<=38` contains 150,456,308 first-crossing words and zero paradoxical cases.

### FINITE ONLY

1. zero paradoxical words through depth 38;
2. minimum observed descent margin `17`;
3. any apparent agreement between direct-descent and coefficient-survival languages at finite depth.

### OPEN

1. arbitrary-depth exclusion of paradoxical first crossings in `27 mod 36`;
2. a theorem coupling the mechanical correction order to the CRT/dyadic start address;
3. COV-1;
4. the infinite coefficient-survival aperiodic branch.

### PROHIBITED UPGRADES

1. Do not extrapolate `0/150,456,308` to all depths.
2. Do not infer cross-base co-ordering from the mechanical remainder envelope.
3. Do not replace the R1 extreme-depth branch by the finite depth-38 computation.
4. Do not claim that every COV-1 obstruction has finite coefficient stopping time.

---

## 12. Next target

The exact remaining first-crossing question is now

\[
\boxed{
DN_0(w)-C(w)>0
}
\]

for every root-`11` first-crossing word `w`, where `N_0(w)` is the least `27 mod 36` CRT lift of its canonical dyadic address.

A useful theorem must therefore control a **joint** statistic of

\[
(C(w),\ r(w)\bmod2^L,\ N_0(w)\bmod9),
\]

not `C(w)` alone.

This is a natural target for the existing mixed-interaction / dangerous-axis decomposition or an exact joint Fourier transfer.

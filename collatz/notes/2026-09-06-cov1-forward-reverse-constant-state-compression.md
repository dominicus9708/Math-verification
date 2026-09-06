# COV-1: forward/reverse constant-state compression

Date: 2026-09-06

Status: **SAFE EXACT STATE REDUCTION.**  The shallow mixed `2`-adic / `3`-adic certificate tree can be expressed without carrying the full affine turning intercept.  The target residue needed by every reverse turn is already encoded in the standard forward parity-affine constant.

This is a structural reduction, not a proof that the mixed survivor tree terminates.

---

## 1. Standard forward parity-affine constant

For a fixed shortcut parity prefix of length `h`, let

\[
s_h
\]

be the number of odd states among the first `h` steps.  Then there is a unique nonnegative integer `C_h` such that

\[
\boxed{
T^h(n)
=
\frac{3^{s_h}n+C_h}{2^h}.
}
\]

Starting from

\[
C_0=0,
\]

the constant obeys the exact recurrence

\[
\boxed{
C_{j+1}
=
\begin{cases}
C_j,&\varepsilon_j=0,\\
3C_j+2^j,&\varepsilon_j=1,
\end{cases}
}
\]

where `epsilon_j` is the parity bit at step `j`.

Thus `C_h` is determined solely by the parity word.

Status: **CLASSICAL / SAFE.**

---

## 2. Affine branch for `x=36k+27`

For `h>=2`, split

\[
k=2^{h-2}u+c,
\qquad
0\le c<2^{h-2}.
\]

The first `h` parity bits are fixed on this cylinder.  If their odd count is `s_h`, then

\[
\boxed{
T^h(36k+27)
=3^{s_h+2}u+B_h.
}
\]

Indeed the coefficient of `u` is

\[
36\cdot2^{h-2}\frac{3^{s_h}}{2^h}
=9\,3^{s_h}
=3^{s_h+2}.
\]

Put

\[
v_h:=s_h+2.
\]

The full intercept `B_h` can be large, but inverse integrality only needs

\[
B_h\pmod{3^{v_h}}.
\]

---

## 3. Exact compression identity

Substitute

\[
n=36(2^{h-2}u+c)+27
\]

into the standard parity-affine formula:

\[
2^hT^h(n)
=3^{s_h}n+C_h.
\]

The left side is

\[
2^h(3^{s_h+2}u+B_h).
\]

The `u` coefficients agree.  Comparing intercepts gives

\[
2^hB_h
=
3^{s_h}(36c+27)+C_h.
\]

But

\[
3^{s_h}(36c+27)
=
4c\,3^{s_h+2}+3^{s_h+3},
\]

which is divisible by

\[
3^{s_h+2}.
\]

Therefore

\[
\boxed{
2^hB_h
\equiv
C_h
\pmod{3^{s_h+2}}.
}
\]

Since `2` is a unit modulo every power of `3`,

\[
\boxed{
B_h
\equiv
2^{-h}C_h
\pmod{3^{s_h+2}}.
}
\]

Status: **SAFE EXACT THEOREM.**

---

## 4. Consequence for reverse-turn admissibility

Let a reverse word have inverse-odd positions

\[
p_0<p_1<\cdots
\]

and normalized reverse sum

\[
S_v
:=
\sum_{a=0}^{v-1}
3^a2^{-p_a-1}
\pmod{3^v}.
\]

At a turning branch with

\[
v=s_h+2,
\]

the first `v` inverse-odd steps are compatible iff

\[
S_v\equiv B_h\pmod{3^v}.
\]

Using Section 3,

\[
\boxed{
2^hS_v
\equiv
C_h
\pmod{3^v}.
}
\]

Equivalently,

\[
\boxed{
2^h
\sum_{a=0}^{s_h+1}
3^a2^{-p_a-1}
\equiv
C_h
\pmod{3^{s_h+2}}.
}
\]

This is the exact **forward-constant / reverse-constant matching equation**.

The mixed tree no longer needs to regard the forward affine branch and the reverse `3`-adic cylinder as unrelated constructions.

---

## 5. Direct target-state recurrence

Define the inverse target state

\[
R_h:=B_h\pmod{3^{v_h}}.
\]

Refine one dyadic bit by writing

\[
u=2u'+d,
\qquad d\in\{0,1\}.
\]

The next turning parity is

\[
\varepsilon_h\equiv d+B_h\pmod2.
\]

### Even child

If `epsilon_h=0`, then

\[
v_{h+1}=v_h
\]

and

\[
B_{h+1}
=
\frac{3^{v_h}d+B_h}{2}.
\]

Modulo `3^(v_h)`,

\[
\boxed{
R_{h+1}
=2^{-1}R_h.
}
\]

### Odd child

If `epsilon_h=1`, then

\[
v_{h+1}=v_h+1
\]

and

\[
B_{h+1}
=
\frac{3^{v_h+1}d+3B_h+1}{2}.
\]

Thus

\[
\boxed{
R_{h+1}
=2^{-1}(3R_h+1)
\pmod{3^{v_h+1}}.
}
\]

Hence the target state itself evolves by the same two affine forms as the shortcut map, but in a changing `3`-adic modulus.

Status: **SAFE.**

---

## 6. Reduced mixed state

The previous mixed-tree description carried data of the form

\[
(h,s_h,B_h,\text{dyadic cylinder},\text{inverse residue},\ldots).
\]

For deciding whether an inverse turn can begin, the full `B_h` is unnecessary.  It is enough to retain

\[
\boxed{
\mathcal S_h
=
(h,s_h,C_h\bmod3^{s_h+2})
}
\]

or equivalently

\[
(h,v_h,R_h).
\]

Additional state is still needed for:

- endpoint intercept descent;
- inverse-word position budget;
- positivity;
- whether a cylinder has already been certified by another path.

But the cross-base **compatibility** state is now reduced to one parity-affine constant modulo the exact available `3`-adic capacity.

---

## 7. Connection to the existing Beatty state

The coefficient-survivor branch already tracks

\[
s_h
\]

against the Beatty barrier

\[
b_h=\lceil h\log_3 2\rceil.
\]

The new state shares the same odd count `s_h`.  Therefore a natural combined state is

\[
\boxed{
(h,\sigma_h,R_h),
\qquad
\sigma_h=s_h-b_h,
}
\]

with `R_h` carried modulo `3^(s_h+2)`.

This does **not** yet give a finite-state automaton because the modulus grows with `s_h`.

The next question is whether only a bounded number of low `3`-adic digits of `R_h` influence the existence of a reduced contracting reverse turn.  If such a bound exists, the mixed tree acquires a finite quotient.  If not, the amount of required `3`-adic information must be quantified rather than assumed away.

---

## 8. DSD audit

### SAFE

1. Standard parity-affine recurrence for `C_h`.
2. Branch coefficient `3^(s_h+2)`.
3. Compression identity `2^h B_h == C_h mod 3^(s_h+2)`.
4. Forward/reverse constant matching equation.
5. Exact even/odd target-state recurrences.

### OPEN

1. A bounded-memory quotient of `R_h`.
2. A theorem that every dangerous mixed survivor state eventually admits descent or a smaller merge.
3. Any terminal implication from state-count decay to emptiness.
4. Full COV-1.

### PROHIBITED UPGRADES

1. Do not call the compressed state finite-state merely because `B_h` was eliminated.
2. Do not identify target-state evolution with proof of Collatz convergence.
3. Do not discard endpoint/intercept inequalities after solving the congruence gate.
4. Do not infer universal coverage from finite state coincidences.

---

## 9. Regression certificate

`collatz/src/cov1_mixed_forward_reverse_constant_state_certificate.py`

checks every dyadic branch through `h<=12`, verifies

\[
2^hB_h\equiv C_h\pmod{3^{s_h+2}},
\]

and checks the exact child target recurrences.

---

## 10. Next target

The next calculation should test **how many low ternary digits of `R_h` are actually needed** to decide the existence of short reduced inverse turns on Beatty-surviving branches.

A practical audit is:

1. enumerate coefficient-surviving parity states through a moderate `h`;
2. group them by `(Beatty slack, R_h mod 3^Q)` for small fixed `Q`;
3. test whether reverse-turn admissibility and affine descent are identical inside each group;
4. increase `Q` until either a stable quotient emerges or explicit collisions show that unbounded `3`-adic memory is genuinely necessary.

That experiment directly targets the remaining state-complexity question without confusing finite agreement with a theorem.

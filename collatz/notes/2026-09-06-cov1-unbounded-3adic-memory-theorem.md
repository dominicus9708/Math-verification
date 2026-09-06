# COV-1: unbounded `3`-adic memory is necessary

Date: 2026-09-06

Status: **SAFE GENERAL OBSTRUCTION TO FIXED-`Q` STATE QUOTIENTS.**  The mixed forward/reverse state cannot be reduced to a fixed number `Q` of low ternary digits of the inverse target, even if Beatty slack is retained.  For every finite `Q`, there exist two coefficient-surviving parity states with the same

\[
(\sigma_h,R_h\bmod3^Q)
\]

but opposite answers to the minimal contracting reverse-congruence gate.

This does not prove that no other finite-state encoding exists.  It proves that the specific proposed quotient by a fixed low-resolution target `R_h mod 3^Q` is impossible uniformly in the depth.

---

## 1. Two parity families

Define

\[
A_t:=11111001\,1^t,
\]

and

\[
B_t:=11011011\,1^t,
\]

for

\[
t\ge0.
\]

Both words have length

\[
h=t+8
\]

and odd count

\[
s=t+6.
\]

Hence their inverse target modulus exponent is

\[
v=s+2=t+8=h.
\]

The two base words satisfy the coefficient-survivor inequalities at every prefix.  Appending an odd bit increases the odd count by one while the Beatty barrier can rise by at most one, so every `A_t` and `B_t` remains coefficient-surviving.

Since the two words have the same `h` and `s`, they also have the same Beatty slack

\[
\sigma_h=s-b_h.
\]

Status: **SAFE.**

---

## 2. Forward parity constants

Let

\[
C_A(t),\qquad C_B(t)
\]

be the standard constants in

\[
T^h(n)=\frac{3^s n+C}{2^h}.
\]

At `t=0`, direct recurrence gives

\[
\boxed{
C_A(0)=761,
\qquad
C_B(0)=1085.
}
\]

Thus

\[
C_B(0)-C_A(0)=324=4\cdot3^4.
\]

Every later appended bit is odd.  Therefore both constants obey the same update

\[
C(t+1)=3C(t)+2^{t+8}.
\]

Subtracting gives

\[
\boxed{
C_B(t)-C_A(t)
=4\cdot3^{t+4}.
}
\]

---

## 3. Target states agree to arbitrarily high finite resolution

The compressed inverse target is

\[
R=2^{-h}C\pmod{3^h}.
\]

Because `2` is a `3`-adic unit,

\[
v_3(R_B(t)-R_A(t))
=
v_3(C_B(t)-C_A(t))
=t+4.
\]

Therefore

\[
\boxed{
R_A(t)
\equiv
R_B(t)
\pmod{3^{t+4}},
}
\]

while they are distinct modulo

\[
3^{t+5}.
\]

For any requested finite target resolution `Q>=4`, choose

\[
t=Q-4.
\]

Then the two states have identical low `Q` ternary digits.

For `Q<=4`, the base pair `A_0,B_0` already agrees modulo `3^Q`.

Thus for every finite

\[
Q\ge1
\]

there is a pair with the same

\[
(\sigma_h,R_h\bmod3^Q).
\]

The remaining task is to prove that their reverse compatibility differs.

---

## 4. Minimal contracting reverse-turn gate

For both families,

\[
v=h.
\]

Test the minimal inverse-odd count

\[
q=v=h.
\]

The contraction position budget is

\[
P
=h-1+\lfloor(q-s)\log_2 3\rfloor.
\]

Since

\[
q-s=2
\]

and

\[
\lfloor2\log_2 3\rfloor=3,
\]

we obtain

\[
\boxed{P=h+2.}
\]

Therefore a minimal-turn reverse word is determined by choosing exactly `h` inverse-odd positions from

\[
0,1,\ldots,h+2.
\]

Equivalently, exactly three positions are not used by inverse-odd steps.

The reverse target sum is

\[
S_h
=
\sum_{a=0}^{h-1}
3^a2^{-p_a-1}
\pmod{3^h}.
\]

Compatibility means

\[
S_h=R_h.
\]

---

## 5. `A_t` is compatible for every `t`

At `t=0`, `h=8`.  Choose inverse-odd positions

\[
\boxed{
(0,1,3,4,5,6,8,9).
}
\]

A direct exact modular evaluation gives

\[
S_8=4283=R_A(0)\pmod{3^8}.
\]

Hence `A_0` is compatible.

Now suppose `A_t` is compatible using positions

\[
p_0<\cdots<p_{h-1}.
\]

Construct the next position set by prepending `0` and shifting all old positions by one:

\[
\boxed{
0,\ p_0+1,\ldots,p_{h-1}+1.
}
\]

The new reverse sum is

\[
\begin{aligned}
S_{h+1}
&=
2^{-1}
+
\sum_{a=0}^{h-1}
3^{a+1}2^{-(p_a+1)-1}\\
&=
\frac12+rac32S_h\\
&=
\frac{3S_h+1}{2}.
\end{aligned}
\]

The forward target under an appended odd bit obeys exactly the same recurrence:

\[
R_A(t+1)
=
\frac{3R_A(t)+1}{2}
\pmod{3^{h+1}}.
\]

Thus compatibility propagates inductively.

Therefore

\[
\boxed{
A_t\text{ is minimal-turn reverse compatible for every }t\ge0.
}
\]

An explicit equivalent family of omitted positions is

\[
\boxed{
(t+2,\ t+7,\ t+10)
}
\]

inside the available range `0,...,t+10`.

Status: **SAFE GENERAL CONSTRUCTION.**

---

## 6. `B_0` is not compatible

At `t=0`, again `h=8` and the available positions are

\[
0,1,\ldots,10.
\]

There are exactly

\[
\binom{11}{8}=165
\]

possible inverse-odd position sets.

Exact enumeration shows that none has target sum

\[
R_B(0)=5822\pmod{3^8}.
\]

This is a finite exact base certificate, not a sampling statement.

Status: **SAFE FINITE BASE OBSTRUCTION.**

---

## 7. Noncompatibility propagates for the entire `B_t` family

First note that

\[
R_B(0)=5822\equiv8\pmod9.
\]

Under an appended odd bit,

\[
R'=rac{3R+1}{2}.
\]

If

\[
R\equiv8\pmod9,
\]

then

\[
R'\equiv8\pmod9.
\]

Hence

\[
\boxed{
R_B(t)\equiv8\pmod9
\quad\text{for every }t\ge0.
}
\]

Assume for contradiction that some `B_t`, `t>=1`, is compatible.

A compatible word has `h` inverse-odd positions chosen from `h+3` available positions, so only three positions are omitted.

Modulo `3`, all terms except the first are divisible by `3`.  Since

\[
R_B(t)\equiv2\pmod3,
\]

the first inverse-odd position `p_0` must be even.

Because only three earlier positions can be omitted,

\[
p_0\le3.
\]

Therefore

\[
p_0\in\{0,2\}.
\]

### Case `p_0=2`

Modulo `9`, the first reverse term is

\[
2^{-3}\equiv8\pmod9.
\]

The second term is

\[
3\,2^{-p_1-1}\equiv3\text{ or }6\pmod9,
\]

and every later term is divisible by `9`.

Thus

\[
S_h\not\equiv8\pmod9,
\]

contradicting the target residue.

So `p_0=2` is impossible.

### Case `p_0=0`

Delete that first inverse-odd position and subtract one from every remaining position.

The resulting set has exactly `h-1` inverse-odd positions in the correct budget for `B_(t-1)`.

Moreover

\[
S_h
=
\frac{3S_{h-1}+1}{2},
\]

so

\[
S_{h-1}
=
\frac{2S_h-1}{3}.
\]

The same inverse recurrence relates

\[
R_B(t)
\]

to

\[
R_B(t-1).
\]

Therefore compatibility of `B_t` would imply compatibility of `B_(t-1)`.

Repeating eventually implies compatibility of `B_0`, contradicting Section 6.

Hence

\[
\boxed{
B_t\text{ is not minimal-turn reverse compatible for any }t\ge0.
}
\]

Status: **SAFE GENERAL NONCOMPATIBILITY THEOREM.**

---

## 8. Fixed-`Q` quotient impossibility theorem

Combine Sections 1--7.

For every integer

\[
Q\ge1,
\]

choose

\[
t=\max(0,Q-4).
\]

Then `A_t` and `B_t`:

1. are both coefficient-surviving;
2. have the same depth `h`;
3. have the same odd count `s`;
4. have the same Beatty slack `sigma_h`;
5. satisfy
   \[
   R_A(t)\equiv R_B(t)\pmod{3^Q};
   \]
6. but have opposite minimal-turn reverse compatibility.

Therefore:

\[
\boxed{
\textbf{No fixed finite }Q
\textbf{ makes }
(\sigma_h,R_h\bmod3^Q)
\textbf{ a complete compatibility state uniformly in }h.
}
\]

Equivalently, the amount of `3`-adic information required to decide this gate is genuinely unbounded along the mixed survivor tree.

---

## 9. Interpretation

This sharply changes the state-compression target.

The failure is not that the tested values `Q=1,...,10` happened to be too small.  Every fixed `Q` fails.

Thus a successful proof architecture must allow at least one of:

1. a growing `3`-adic resolution `Q(h)`;
2. a different symbolic state that captures the needed high digits without storing them literally;
3. a global analytic argument that bypasses pointwise reverse compatibility;
4. a multi-turn or other merge architecture whose decision variable is not this target residue alone.

A fixed finite automaton obtained merely by truncating `R_h` is now pruned from the proof tree.

---

## 10. Relation to Gate F

Earlier, `F_unif` required a growing ternary modulus and was repaired by explicitly controlling the moving low-height strip rather than pretending a fixed modulus sufficed.

The present theorem shows an analogous phenomenon in COV-1:

\[
\boxed{
\text{growing scale is not an implementation nuisance; it is structurally necessary.}
}
\]

This parallel is useful for DSD methodology.  Fixed-parameter success must not be promoted to a growing-resolution theorem unless the growing parameter is tracked explicitly.

---

## 11. DSD audit

### SAFE

1. The two infinite parity families are coefficient-surviving.
2. Their target difference has exact `3`-adic valuation `t+4`.
3. `A_t` is reverse compatible for every `t`.
4. `B_t` is reverse incompatible for every `t`.
5. Every fixed target truncation `R mod 3^Q` fails to decide the gate uniformly.

### REJECTED

- any fixed-`Q` finite quotient based on `(Beatty slack, R mod 3^Q)`;
- extrapolating finite target-state grouping into a finite-state theorem.

### OPEN

1. The minimal growth rate of a sufficient resolution `Q(h)`.
2. Whether a compressed symbolic representation can replace literal `Q(h)` digits.
3. Endpoint descent and multi-turn compatibility beyond the minimal congruence gate.
4. Full COV-1.

### PROHIBITED UPGRADES

1. Do not infer that no finite-state proof of any kind exists; only this truncation architecture is ruled out.
2. Do not infer that `B_t` represents counterexamples; it only fails one reverse-turn gate.
3. Do not confuse reverse compatibility with endpoint descent or recursion.
4. Do not infer Collatz divergence from unbounded state memory.

---

## 12. Regression certificate

`collatz/src/cov1_unbounded_3adic_memory_witness_certificate.py`

checks the exact base obstruction and verifies the general formulas on a long finite regression range.  The all-`t` result itself is proved algebraically in Sections 5 and 7.

---

## 13. Next target

The next quantitative question is now well posed:

\[
\boxed{
\text{How fast must }Q(h)\text{ grow to decide the relevant reverse gate?}
}
\]

The witness family proves only

\[
Q(h)\not=O(1).
\]

For the displayed pair,

\[
Q\sim h-4,
\]

so it is natural to test whether a **linear lower bound** on required `3`-adic memory can be proved for some survivor family, or whether a different encoding reduces the information cost to logarithmic or sublinear size.

That memory-growth problem is now a cleaner next target than further shallow-cylinder enumeration.

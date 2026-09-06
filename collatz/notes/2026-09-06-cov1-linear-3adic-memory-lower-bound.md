# COV-1: linear lower bound on ternary target memory

Date: 2026-09-06

Status: **SAFE CONSEQUENCE OF THE UNBOUNDED-MEMORY WITNESS FAMILY.**  The preceding `A_t/B_t` construction does more than rule out fixed target resolution.  It forces any depth-dependent truncation of the form

\[
(\sigma_h,R_h\bmod3^{Q(h)})
\]

that claims to decide the minimal reverse-compatibility gate for **all** coefficient-surviving states at depth `h` to retain essentially the full linear number of ternary target digits.

This is a lower bound for this specific state representation and gate.  It is not a lower bound on all possible proof encodings or algorithms for Collatz.

---

## 1. Recall the witness pair

For every

\[
t\ge0,
\]

define

\[
A_t=11111001\,1^t,
\qquad
B_t=11011011\,1^t.
\]

They have

\[
h=t+8,
\qquad
s=t+6,
\qquad
v=s+2=h,
\]

and the same Beatty slack.

Their target states satisfy

\[
v_3(R_B(t)-R_A(t))=t+4.
\]

Since

\[
t=h-8,
\]
this becomes

\[
\boxed{
v_3(R_B-R_A)=h-4.}
\]

Therefore

\[
\boxed{
R_A\equiv R_B\pmod{3^{h-4}},
}
\]

but

\[
R_A\not\equiv R_B\pmod{3^{h-3}}.
\]

At the same time, `A_t` passes the minimal contracting reverse-congruence gate while `B_t` fails it.

---

## 2. Necessary resolution theorem

Suppose a depth-dependent state representation keeps only

\[
\boxed{
(\sigma_h,R_h\bmod3^{Q(h)})
}
\]

and claims that this information is sufficient to decide the minimal reverse-compatibility gate for every coefficient-surviving state of depth `h`.

Fix any

\[
h\ge8
\]

and take

\[
t=h-8.
\]

If

\[
Q(h)\le h-4,
\]

then the two witness states satisfy

\[
R_A(t)\equiv R_B(t)\pmod{3^{Q(h)}}
\]

and have the same Beatty slack.  The truncated states are therefore identical, yet their correct compatibility answers are different.

This contradicts completeness of the truncated state.

Hence necessarily

\[
\boxed{
Q(h)\ge h-3
\qquad\text{for every }h\ge8.
}
\]

Status: **SAFE THEOREM.**

---

## 3. Asymptotic consequence

The lower bound implies

\[
\liminf_{h\to\infty}\frac{Q(h)}h\ge1.
\]

More concretely, all of the following are impossible for a complete target-truncation state of this form:

\[
Q(h)=O(1),
\]

\[
Q(h)=O(\log h),
\]

\[
Q(h)=h^\alpha\quad(0<\alpha<1),
\]

and, more generally,

\[
Q(h)\le h-4
\]

at even one depth `h>=8` if completeness is claimed at that depth.

Thus this representation does not merely require growing memory.  It requires essentially one new ternary digit of target information per additional forward depth.

---

## 4. Information interpretation

A target residue modulo

\[
3^{Q(h)}
\]

contains

\[
Q(h)\log_2 3
\]

bits of raw information.

The necessary bound gives

\[
\boxed{
\text{raw target-state information}
\ge
(h-3)\log_2 3
}
\]

bits if the state is represented literally by its ternary residue.

This is a statement about the literal residue encoding only.  A symbolic representation could in principle encode the same high-order information more compactly if it exploits algebraic structure.  The theorem therefore rules out **truncation**, not compression in every possible sense.

---

## 5. Relation to the full modulus

For the witness family,

\[
v=s+2=h.
\]

The complete inverse target lives modulo

\[
3^h.
\]

The necessary resolution

\[
Q(h)\ge h-3
\]

shows that a complete truncation may discard at most the top three ternary digits on this family.

Equivalently, the fraction of target digits that must be retained tends to one:

\[
\boxed{
\frac{Q(h)}v\ge1-\frac3h\to1.
}
\]

This is substantially stronger than a generic statement that the modulus has to grow.

---

## 6. Consequence for proof architecture

The proposed route

> carry Beatty slack plus a short low-ternary signature of the turning target

is now ruled out quantitatively.

A viable architecture must instead do at least one of the following:

1. carry almost the full target residue, but manipulate it symbolically rather than by enumeration;
2. identify a different invariant that decides compatibility without reconstructing `R_h` digit by digit;
3. avoid pointwise minimal-turn compatibility and return to aggregate/spectral arguments;
4. use a multi-turn/global merge theorem whose state does not factor through this target residue.

This makes the aggregate Gate-S/Gate-F branch comparatively more attractive again: its goal is to control distributions of growing residues rather than compress every residue into bounded memory.

---

## 7. DSD audit

### SAFE

1. Witness target difference has exact valuation `h-4`.
2. Same low `h-4` ternary digits can correspond to opposite gate answers.
3. Any complete truncation of the declared form requires `Q(h)>=h-3`.
4. Literal target-memory cost is therefore linear in `h`.

### REJECTED

- fixed-resolution target states;
- logarithmic or sublinear target truncations;
- the hope that only a bounded low-ternary window controls minimal reverse compatibility.

### OPEN

1. Symbolic compression that retains high-digit information implicitly.
2. Aggregate distributional control without pointwise compatibility states.
3. Multi-turn/global merge states.
4. Full COV-1.

### PROHIBITED UPGRADES

1. Do not claim a linear lower bound for all Collatz algorithms or proofs.
2. Do not identify literal residue-bit complexity with computational complexity in general.
3. Do not infer divergence or counterexamples from high state-memory requirements.
4. Do not assume `Q=h-3` is sufficient; it is only necessary for this witness obstruction.

---

## 8. Dependency

This theorem depends only on the general witness theorem in

`2026-09-06-cov1-unbounded-3adic-memory-theorem.md`.

The regression evidence is provided by

`collatz/src/cov1_unbounded_3adic_memory_witness_certificate.py`.

---

## 9. Revised next target

The memory-growth question for literal truncation is now closed sharply enough to prune it.

The next highest-value target is no longer to estimate `Q(h)`.  It is to determine whether the high-resolution target admits a **symbolic algebraic representation** that can be transported in aggregate.

The exact identity

\[
2^hB_h\equiv C_h\pmod{3^{s_h+2}}
\]

suggests working directly with the parity-affine polynomial/constant `C_h` and its distribution over the Beatty-surviving language, rather than with the expanded ternary digits of `R_h`.

That returns the coverage problem to a form closer to the existing Fourier/selector machinery and avoids a state representation that has now been proved essentially full-resolution.

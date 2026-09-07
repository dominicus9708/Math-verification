# Tong Niu (2026) parity-vector / paradoxical-sequence paper — DSD absorption audit

Date: 2026-09-07

Source: Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:`2605.13886` (May 2026).

Status: **A — SAFE EXTERNAL THEOREMS + FINITE/CONJECTURAL NUMERICAL LAYER.** The paper explicitly separates three unconditional theorems from one finite numerical observation and makes no claim to prove Collatz or Terras's coefficient-stopping-time conjecture. This scope separation is compatible with the current DSD proof architecture.

---

## 1. Setup and affine identity

For the shortcut map

\[
T(n)=\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even},
\end{cases}
\]

let `V_k(n)` be the length-`k` parity vector and `q_k(n)` its odd count. Then

\[
T^k(n)=\frac{3^{q_k(n)}}{2^k}n+E_k(n),
\]

where the remainder depends only on the parity vector.

The coefficient stopping time is

\[
\tau(n)=\min\{k\ge1:3^{q_k(n)}<2^k\},
\]

while ordinary stopping time is

\[
t(n)=\min\{k\ge1:T^k(n)<n\}.
\]

Since `E_k(n)>=0`,

\[
\tau(n)\le t(n).
\]

Equality is Terras's CST conjecture and is **not** claimed by the paper.

---

## 2. Theorem 2 — exact finite parity-vector cylinder count

For every binary word `w` of length `k`, the set

\[
S_w=\{n>0:V_k(n)=w\}
\]

is exactly one residue class modulo `2^k`.

Consequently, for every finite interval `[1,N]`,

\[
\left|\#(S_w\cap[1,N])-\frac{N}{2^k}\right|\le1.
\]

This is an exact finite form of the classical parity-vector equidistribution fact.

### DSD status

\[
\boxed{\textbf{A — SAFE EXTERNAL THEOREM}.}
\]

### Internal use

This is directly compatible with the repository's canonical dyadic-address language. It supports exact finite word-to-residue bookkeeping but does not imply that a restricted exceptional language is empty.

---

## 3. Theorem 4 — analytic enumeration of paradoxical words

For fixed length `k` and a parity word `w` of weight `q`, let `n_w` be its unique canonical residue representative modulo `2^k`, and write the affine remainder as `r_w`.

The paper proves that the corresponding length-`k` sequence is paradoxical exactly when

\[
3^q<2^k
\]

and

\[
n\le R_w:=\frac{2^k r_w}{2^k-3^q},
\]

subject to the stated acyclicity/trivial-cycle exclusion.

Thus the number of paradoxical starts at every fixed length is finite and can be counted analytically from parity words without trajectory simulation.

### DSD status

\[
\boxed{\textbf{A — SAFE EXTERNAL THEOREM}.}
\]

### Internal relation

This theorem expresses exactly the same joint structure that the current first-universal-cell program must preserve:

\[
\text{coefficient condition}
+\text{same-word correction}
+\text{same-word dyadic address}.
\]

It therefore independently supports the repository decision to reject a correction-only or density-only closure.

It does **not** eliminate the giant first universal cell; the hard problem is still which enormous parity words have canonical starts in the surviving ordinary-integer window while satisfying all prefix constraints.

---

## 4. Theorem 7 — bounded-length paradoxical starts have density zero

For each fixed `K`, the union of starts having an acyclic paradoxical sequence of some length at most `K` is finite, with an explicit bound obtained by summing the fixed-length analytic counts.

Therefore its natural density is zero.

### DSD status

\[
\boxed{\textbf{A — SAFE, BUT FIXED-}K\textbf{ ONLY}.}
\]

### Prohibited upgrade

Do not infer

\[
K\text{ fixed density zero}
\Longrightarrow
\text{no paradoxical sequence at unbounded length}.
\]

The current universal cell occurs at an astronomically large length, so the theorem is a finite-length structural result, not a terminal Collatz closure.

---

## 5. Numerical best-approximation observation

The paper reports that the known paradoxical `(j,q)` ratios in the Rozier--Terracol finite enumeration reduce to a small list associated with left convergents, left semiconvergents, or one Stern--Brocot mediant of

\[
\log_3 2.
\]

It then states a conjecture extending this pattern to all paradoxical sequences.

### DSD status

\[
\boxed{\textbf{FINITE NUMERICAL OBSERVATION / CONJECTURE}.}
\]

The observed continued-fraction/Farey structure is highly relevant to the internal first-crossing resonance program, but it must not be imported as a universal theorem.

---

## 6. Finite CST computation

The paper computationally checks `tau(n)=t(n)` through a stated finite range. This is useful regression evidence only.

### DSD status

\[
\boxed{\textbf{FINITE ONLY}.}
\]

The paper itself explicitly says that it does not prove the CST conjecture.

---

## 7. What is positively absorbed

1. exact parity-word `mod 2^k` cylinder uniqueness;
2. sharp finite count deviation at most one;
3. exact wordwise criterion for paradoxical starts;
4. analytic fixed-length enumeration/finiteness;
5. fixed-bounded-length density-zero conclusion.

These can be cited as valid external prior art with their hypotheses unchanged.

---

## 8. What remains non-importable

1. universal CST equality `tau=t`;
2. universal finiteness of all paradoxical starts over unbounded length;
3. the proposed all-length continued-fraction/Stern--Brocot classification;
4. any claim that density zero or finite fixed-length counts imply emptiness of the universal exceptional set.

---

## 9. Citation role in the current repository

Niu (2026) is a **positive prior-art citation**, not a failed-proof citation.

It should be used to support:

- exact dyadic parity-cylinder bookkeeping;
- the word-specific correction/address nature of paradoxicality;
- the distinction between unconditional finite-length theorems and conjectural global structure.

The numerical best-approximation observation may be cited only as finite evidence/conjectural motivation for the internal Farey program.

---

## 10. Final verdict

\[
\boxed{
\text{Niu Theorems 2, 4, 7: SAFE EXTERNAL PRIOR ART.}
}
\]

\[
\boxed{
\text{Best-approximation all-length extension and CST: OPEN / NOT IMPORTED.}
}
\]

This paper is an example of a source that survives DSD audit precisely because it preserves the finite/universal and theorem/conjecture boundaries explicitly.
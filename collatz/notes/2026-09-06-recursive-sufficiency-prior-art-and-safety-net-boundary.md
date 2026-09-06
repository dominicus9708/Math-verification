# Recursive-sufficiency prior-art audit and the safety-net limitation

Date: 2026-09-06

Status: **PRIOR-ART / SCOPE AUDIT.**  External material inspected on 2026-09-06 independently reports the same first defect in Ansari's ternary induction that this repository found by direct residue calculation.  It also gives replacement recursively sufficient parity-prefix sieves.  Those replacements are useful for computational sieving, but they do **not** restore the theorem needed here that every hypothetical minimal counterexample belongs to the infinite ternary `0/1` selector core.

This note records the distinction so that a valid replacement sieve is not silently promoted into a replacement coverage theorem.

---

## 1. Primary paper

Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471--480 (2025), DOI `10.7546/nntdm.2025.31.3.471-480`.

The journal page describes the paper as introducing recursive sufficiency and a sequence of sieves with elimination percentage tending to `100%`.

The present repository's direct audit found that the printed induction used to make the original ternary `F_n` family recursively sufficient fails already at `F_1 -> F_2`.

---

## 2. Independent public audit located

A 2026 public audit in the repository `jkolantree/BSC`, file

`applications/Collatz_Recursive_Sufficiency_Audit.md`,

records the same exact first removed layer:

\[
F_1\setminus F_2
=
(36\mathbb N_0+27)
\cup
(36\mathbb N_0+31).
\]

It closes the `31 mod 36` progression by the same kind of exact undirected merge and leaves

\[
36\mathbb N_0+27
\]

unresolved.

It explicitly states that the assertion that every original `F_n` is recursively sufficient remains open from that audit's perspective.

This independently corroborates the DSD decision to demote the old ternary-core coverage claim from SAFE to CONDITIONAL/OPEN.

The external audit is not treated as a proof substitute for this repository's own residue certificate; it is prior-art confirmation.

---

## 3. External unconditional parity-prefix replacement

The same audit defines, for `m>=1`,

\[
U_m
=
\{n\ge1:7s_j(n)>4j\text{ for every }1\le j\le m\},
\]

where `s_j(n)` counts odd shortcut states in the first `j` terms.

It proves that each `U_m` is periodic modulo `2^m`, recursively sufficient, nested, and has exponentially decaying density.

The elementary descent mechanism is:

if for some `j<=m`,

\[
7s_j(n)\le4j,
\]

and no earlier iterate has already dropped below `n`, then every odd state in that prefix is at least `3`, so an odd shortcut step expands by at most `5/3`.  Hence

\[
\frac{T^j(n)}n
\le
\frac{(10/3)^{s_j(n)}}{2^j}
<1.
\]

Thus the complement of `U_m` is recursive.

Status here: **VALID REPLACEMENT RS SIEVE INPUT**, subject to ordinary verification of the displayed elementary inequalities.

---

## 4. Why this does not restore `F_map^cover`

A hypothetical minimal counterexample belongs to **every** recursively sufficient set: if it lay in the complement, that complement member would by definition merge with a smaller integer, contradicting minimal-counterexample status.

Therefore introducing another recursively sufficient set `S` gives

\[
N_{\min}\in S,
\]

not

\[
N_{\min}\in F_n.
\]

The external safety-net construction has the form

\[
H_{n,m}
=
F_n\cup(F_1\cap S_m),
\]

with `H_(n,m)` recursively sufficient even when `F_n` itself is not known to be recursively sufficient.

Hence a hypothetical minimal counterexample satisfies only

\[
N_{\min}
\in
F_n
\cup
(F_1\cap S_m).
\]

This is a **two-branch statement**.  The safety-net branch cannot be deleted merely because its density is small.

Consequently

\[
\boxed{
H_{n,m}\text{ RS}
\not\Longrightarrow
N_{\min}\in F_n.
}
\]

This is the exact point relevant to the present selector program.

---

## 5. Infinite-intersection issue

Even if a nested safety-net family satisfies

\[
d(S_m)\to0,
\]

density zero does not imply that

\[
\bigcap_m S_m
\]

is empty.

A single infinite parity path, or a thin Cantor-like family of paths, can survive all finite stages while the periodic densities tend to zero.

Therefore the argument

\[
d(S_m)\to0
\quad\Rightarrow\quad
\text{eventually no minimal counterexample in }S_m
\]

is prohibited.

This is the same DSD terminal distinction already encountered in the normalized-mass branch:

\[
\boxed{
\text{density decay}\ne\text{set emptiness}.}
\]

---

## 6. Relation to coefficient-survivor language

The coefficient-survivor/Beatty condition uses the stronger prefix lower bound

\[
q_j\ge\lceil j\log_3 2\rceil,
\]

with

\[
\log_3 2\approx0.63093.
\]

The unconditional safety-net threshold `4/7` is about `0.57143`.

Thus a coefficient-surviving parity word automatically satisfies the safety-net inequality at the level of odd-count density once the ceiling is accounted for.  The safety-net therefore does not prune the dangerous Beatty language; it is intentionally a much broader RS sieve.

Accordingly, this replacement is valuable for computational verification but does not supply the cross-base restriction that the ternary selector machinery requires.

---

## 7. Consequence for current proof architecture

The program should retain the following separation:

### SAFE

- exact ternary selector algebra;
- exact dyadic/selector coordinate identity;
- exact mass transport;
- external or elementary RS parity-prefix sieves as independent computational tools.

### OPEN

- universal minimal-counterexample coverage by the infinite ternary `0/1` core;
- full recursion of `36N_0+27`;
- a replacement coverage theorem whose surviving branch still preserves enough ternary product structure for the selector/Fourier machinery.

### PROHIBITED

- using a small-density safety-net as though it were empty;
- using `H_(n,m)` recursive sufficiency as though it proved `F_n` recursive sufficiency;
- claiming that the selector branch is universal merely because a replacement RS sieve exists.

---

## 8. Prior-art status

The public audit also notes classical prior art around parity-vector methods, density stopping-time arguments, sufficient arithmetic progressions, and strongly sufficient sets.  Therefore any later paper from this program should make narrow novelty claims:

- the DSD decomposition and audit architecture;
- the exact corrected removed-layer formulation used here;
- the specific cross-base selector/Beatty transport theorems proved in this repository;
- any genuinely new coverage repair, if obtained.

Broad claims of inventing parity sieves, recursive-sufficiency ideas, or density-based Collatz filtering should be avoided.

---

## 9. Sources inspected

1. Mohammad Ansari (2025), *Recursive sufficiency for the Collatz conjecture and computational verification*, NNTDM 31(3), 471--480, DOI `10.7546/nntdm.2025.31.3.471-480`.
2. `jkolantree/BSC`, `applications/Collatz_Recursive_Sufficiency_Audit.md`, inspected 2026-09-06.

No claim is made here that these are the only discussions or corrections in existence.  The source search was used to establish prior-art and scope boundaries, not exhaustiveness.

# External Collatz literature: absorption matrix and DSD audit

Date: 2026-09-06

Status: **LITERATURE INTEGRATION / NO CLAIM OF COMPLETE PROOF.**

Purpose: classify external Collatz results by whether they can be (i) safely absorbed as proved intermediate theorems, (ii) absorbed only conditionally, or (iii) retained as anti-patterns after a DSD audit failure.  The goal is not to replace external attribution with internal notation, but to connect validated results to the current Gate A/B/C/R1 proof architecture while preserving every hypothesis and quantifier.

---

## 1. DSD absorption protocol

Every external result is assigned one of four labels.

### A — SAFE EXTERNAL THEOREM

A rigorous result whose hypotheses and conclusion can be imported unchanged.

### B — SAFE STRUCTURAL REDUCTION / CONDITIONAL CLOSURE

A rigorous implication of the form

\[
H\Longrightarrow C,
\]

where the hypothesis `H` is not currently proved for all Collatz trajectories.  The implication may be absorbed, but `H` remains an explicit open gate.

### C — PARTIAL ABSORPTION AFTER HINGE FAILURE

Definitions, lemmas, or local identities survive, but one central induction/coverage/quantifier step fails.  Surviving modules are retained and the failed step becomes a regression test.

### D — REJECTED PROOF MECHANISM / ANTI-PATTERN

A claimed closure contains an explicit logical or mathematical failure.  The failure is retained as a rule forbidding the same upgrade internally.

The central DSD rule is:

\[
\boxed{
\text{measure/density/finite-state evidence cannot be upgraded to a universal pointwise theorem without a bridge.}
}
\]

---

## 2. Tao (2019/2022): almost-all orbits attain almost bounded values

Source: Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12, DOI `10.1017/fmp.2022.8`.

### External theorem

For every function

\[
f:\mathbb N_{>0}\to\mathbb R,
\qquad f(N)\to+\infty,
\]

one has

\[
\operatorname{Col}_{\min}(N)<f(N)
\]

for almost all positive integers `N` in logarithmic density.

The proof uses Syracuse first-passage stabilization, a skew random walk on `Z/3^n Z`, and high-frequency characteristic-function/Fourier decay.

### DSD status

\[
\boxed{\textbf{A — SAFE EXTERNAL THEOREM}.}
\]

### What is absorbed

1. The random/typical first-passage transport framework.
2. The legitimacy of using `3`-adic characteristic functions and high-frequency Fourier decay to control large exceptional families statistically.
3. A benchmark that any internal probabilistic/selector model should at least be compatible with.

### What is not absorbed

Tao's theorem is not a universal statement.  It does not imply that the exceptional set is empty, finite, or disjoint from the positive integers relevant to a hypothetical counterexample.

Therefore the internal rule is

\[
\boxed{
\text{Tao almost-all transport}
\not\Rightarrow
\text{Gate A deterministic occupied-subset contraction}.
}
\]

This directly justifies the internal separation between:

- aggregate/Fourier mixing;
- actual occupied Walsh/Hamming moments;
- atom-floor/coverage closure.

### Relative frontier

External literature is much stronger here in analytic Fourier/renewal technology.  The current internal contribution is not a stronger almost-all theorem; it is the explicit isolation of the additional deterministic gates required to turn such mixing into a pointwise minimal-counterexample exclusion.

---

## 3. Rozier–Terracol (2025): paradoxical sequences

Source: Olivier Rozier and Claude Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948.

The paper uses the shortcut map

\[
T(n)=\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even}.
\end{cases}
\]

For a length-`j` parity prefix with `q` odd states,

\[
T^j(n)=\frac{3^q}{2^j}n+E_j(n).
\]

A sequence is called paradoxical when

\[
3^q<2^j
\]

but nevertheless

\[
T^j(n)\ge n.
\]

### 3.1 Remainder-majorization theorem

For fixed `(j,q)`, moving `1` bits left in the parity word decreases the remainder.  The paper obtains the exact extremal bound

\[
\boxed{
\frac{3^q-2^q}{2^j}
\le E_j(n)
\le
\frac{3^q-2^q}{2^q}.
}
\]

The extrema occur at the two block words with all odd bits placed first or last.

DSD status:

\[
\boxed{\textbf{A — SAFE EXTERNAL THEOREM}.}
\]

This can be used as an external envelope/check for the internal first-crossing correction channel.

### 3.2 Divergence-to-paradox theorem

Rozier–Terracol prove that if a positive integer has infinite stopping time, then infinitely many paradoxical sequences arise from dyadic multiples of that integer.

DSD status:

\[
\boxed{\textbf{A — SAFE EXTERNAL REDUCTION}.}
\]

This strongly supports the internal R1 strategy: a divergent/minimal-counterexample branch must eventually feed the paradoxical-first-crossing language rather than avoiding it forever.

### 3.3 Computed gap

The paper reports exactly 593 paradoxical sequences starting at integers `<=4614`, and no further ones below the then-used verified range `2.8e19`.

DSD status:

\[
\boxed{\textbf{FINITE EXTERNAL CERTIFICATE / NOT AN ASYMPTOTIC THEOREM}.}
\]

### Internal relation

The present internal R1 program goes further in the following narrow directions:

- exact Farey isolation of the first universal coefficient-crossing cell under the modern verified floor;
- dangerous-axis and buffered-core co-order reductions;
- same-integer/Hensel constraints on root prefixes;
- exact `27 mod 36` first-crossing tests through finite depth.

No literature-priority claim is made.

---

## 4. López–Stoll (2009): 2-adic conjugacy over Sturmian words

Source: Josefina López and Peter Stoll, *The 3x+1 Conjugacy Map over a Sturmian Word*, Integers 9 (2009), 141–162, DOI `10.1515/INTEG.2009.014`.

### External structure

The parity vector of a `2`-adic integer is an infinite binary word, and the inverse conjugacy map `Phi` gives the unique `x in Z_2` with a prescribed parity word.

The paper studies mechanical/Sturmian aperiodic words and derives a generalized continued-fraction representation in the `2`-adic metric.

It explicitly notes that the relation between aperiodic parity words and rational/eventually-periodic images remains delicate/open.

### DSD status

\[
\boxed{\textbf{A — SAFE EXTERNAL 2-ADIC STRUCTURE}.}
\]

### Internal absorption

This supports the exact distinction used by the current terminal gate:

\[
\text{infinite symbolic parity path}
\neq
\text{positive ordinary integer orbit}.
\]

The internal inverse-limit criterion

\[
k_\infty\in\mathbb N_0
\iff
\text{its finite dyadic residues eventually stabilize}
\]

and the negative/eventually-periodic ghost classification are to be viewed as an application of the same conjugacy framework, not as a replacement for it.

### Anti-upgrade rule

A Sturmian/mechanical symbolic survivor is not a Collatz counterexample merely because it exists in `Z_2`.

---

## 5. Monks et al.: sufficient and strongly sufficient sets

Sources include:

- Kenneth M. Monks, *The sufficiency of arithmetic progressions for the 3x+1 conjecture*, Proc. Amer. Math. Soc. 134 (2006), 2861–2872.
- Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, Maria Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, Discrete Mathematics 313 (2013), 468–489.

### External theorem

Every nonconstant arithmetic progression is sufficient in the merge sense.  The later paper develops strongly sufficient sets and proves, among other results, residue classes that every divergent orbit or nontrivial cycle must intersect.

### DSD status

\[
\boxed{\textbf{A — SAFE EXTERNAL COVERAGE/ROUTING RESULTS}.}
\]

### Crucial distinction

Merge sufficiency gives

\[
n\leftrightarrow m\in S,
\]

but does not require

\[
m<n.
\]

Therefore it cannot replace recursive sufficiency in a minimal-counterexample induction.

Internal rule:

\[
\boxed{
\text{sufficient / strongly sufficient}
\neq
\text{recursively sufficient}.
}
\]

### Structural use

These results remain valuable as:

- routing constraints on divergent/cyclic branches;
- independent residue safety nets;
- checks against proposed exceptional languages.

They are not a substitute for `COV_n`.

---

## 6. Ansari (2025): recursive sufficiency

Source: Mohammad M. Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471–480 (2025), DOI `10.7546/nntdm.2025.31.3.471-480`.

### 6.1 Definitions and basic induction

The paper defines an integer `n>1` to be recursive if there is an `m<n` that merges with `n`, and a set `F` to be recursively sufficient when its complement is recursive.

Theorem 2.1 gives the useful finite-interval principle:

\[
F\text{ recursively sufficient}
\Longrightarrow
\bigl([1,N]\text{ satisfies Collatz}
\iff F\cap[1,N]\text{ does}\bigr).
\]

The proof is a standard strong induction on `n`.

DSD status:

\[
\boxed{\textbf{A — DEFINITIONS + BASIC INTERVAL REDUCTION ABSORBABLE}.}
\]

### 6.2 Ternary sieve induction failure

The paper then defines

\[
F_n=
\left\{
4\left(3^n k+\sum_{i=0}^{n-1}a_i3^i\right)+3:
 k\ge0,\ a_i\in\{0,1\}
\right\}
\]

and claims every `F_n` is recursively sufficient.

A DSD residue audit of the first nontrivial step gives

\[
F_1\pmod{36}=\{3,7,15,19,27,31\},
\]

\[
F_2\pmod{36}=\{3,7,15,19\}.
\]

Thus

\[
\boxed{
F_1\setminus F_2
=(36\mathbb N_0+27)\cup(36\mathbb N_0+31).
}
\]

The printed auxiliary construction in Lemma 3.1 identifies `F_(n+1)` with a different set difference.  At `n=1` its residue classes do not equal `F_2`; therefore the displayed induction hinge does not prove the claim.

DSD status:

\[
\boxed{\textbf{C — PARTIAL ABSORPTION; TERNARY COVERAGE REOPENED}.}
\]

### 6.3 Corrected internal replacement

The exact removed layer is

\[
A_n=F_n\setminus F_{n+1}
=
\left\{
4\left(3^{n+1}p+2\cdot3^n+
\sum_{i=0}^{n-1}a_i3^i\right)+3
\right\}.
\]

Hence the correct sufficient induction target is

\[
F_n\text{ recursively sufficient}
+ A_n\text{ recursive}
\Longrightarrow
F_{n+1}\text{ recursively sufficient}.
\]

The first unresolved branch is

\[
\boxed{36\mathbb N_0+27}.
\]

This is the current `COV_1` gate.

### Anti-pattern extracted

Do not infer an exact recursive-sufficiency sieve from an auxiliary symbolic decomposition without checking the literal residue-set identity at the first nontrivial level.

---

## 7. Moore–Schulman exponential-sum conjecture

Source: Cristopher Moore and Leonard J. Schulman, *Tree Codes and a Conjecture on Exponential Sums*, arXiv:1308.6007.

The paper poses, rather than proves, a uniform exponential-sum gap for the incomplete orbit

\[
e(3^k m/2^n),\qquad k=O(n).
\]

### DSD status

\[
\boxed{\textbf{B — OPEN EXTERNAL CONJECTURE / NOT IMPORTABLE AS A LEMMA}.}
\]

This is directly relevant to the internal selector Walsh/Riesz-product gate because such a gap would yield much stronger mixing than currently available.

### Anti-upgrade rule

Do not replace the present sparse-regime Gate A proof obligation by citing full-subgroup exponential-sum results or the Moore–Schulman conjecture as though the needed linear-length incomplete-orbit bound were known.

---

## 8. Conditional entropy/transport completion programs

Recent preprints such as *Collatz Dynamics IV: Uniform Entropy–Transport Closure Beyond "Almost All"* formulate deterministic closure from explicit extra gates such as:

- uniform high-frequency bounds;
- residue-coupled transport;
- finite Gate-B certificates;
- parity large-deviation or Walsh small-bias hypotheses.

When the author explicitly states these as conditions rather than proved Collatz facts, the correct DSD classification is

\[
\boxed{\textbf{B — CONDITIONAL ARCHITECTURE, NOT A FAILED PROOF}.}
\]

### Internal absorption

The hierarchy

\[
\text{Walsh small-bias}
\Rightarrow
\text{good-block frequency}
\Rightarrow
\text{transport contraction}
\]

is structurally close to the internal Gate-A occupied-Walsh and Hamming-moment program.

The internal computation adds two useful barriers:

1. arbitrary occupied-subset contraction is false;
2. fixed finite `Q` / sublinear `3`-adic memory is insufficient for the mixed deterministic state.

Thus these conditional external frameworks are useful roadmaps, but their number-theoretic activation gate remains the same essential difficulty.

---

## 9. Current comparative frontier

### External literature is clearly ahead in

1. rigorous almost-all/log-density results (Tao);
2. sophisticated renewal/high-frequency `3`-adic Fourier analysis;
3. established `2`-adic conjugacy theory;
4. classical cycle and sufficient-set theory.

### Current internal program is further specialized in

1. DSD-separated deterministic gates after average mixing;
2. exact same-integer / Hensel / atom-floor bridges;
3. explicit detection of false finite-state and fixed-memory upgrades;
4. correction of the Ansari ternary recursive-sufficiency induction;
5. root-global rather than arbitrary later-block Hensel auditing;
6. exact paradoxical first-crossing resonance isolation under a verified floor.

These are proof-architecture comparisons, not priority or publication-quality claims.

---

## 10. What should be structurally absorbed now

### R1

Absorb Rozier–Terracol:

- paradoxical-sequence definition;
- remainder partial order/extremal bounds;
- infinite stopping time => infinitely many paradoxical sequences.

Keep the internal Farey/mechanical/same-integer refinement as the stricter gate.

### Gate A

Absorb Tao's high-frequency transport as an external benchmark and source of valid analytic techniques.

Do **not** use it to eliminate every occupied deterministic fibre.

### Gate C / terminal

Absorb López–Stoll `2`-adic conjugacy language and preserve the integer-vs-`Z_2` distinction.

### Coverage

Absorb Monks sufficiency as a routing safety net.

Absorb Ansari's recursive-sufficiency definition and finite-interval induction.

Do not use Ansari Lemma 3.1 as a validated ternary-core coverage theorem; use the corrected `COV_n` removed-layer formulation.

---

## 11. Next deep-audit queue

1. Claimed `2`-adic ergodic/equidistribution proofs:
   audit the exact bridge from Haar-a.e. or natural-density contraction to **every individual natural integer**.
2. Claimed finite-state proofs:
   check whether the finite quotient preserves all carry/history information needed for arbitrary horizon.
3. Claimed parity-density/block-contraction proofs:
   search for the step replacing a frequency/density law by a pointwise law on one hypothetical divergent orbit.
4. Claimed cycle-exclusion proofs:
   separate “no cycle of a restricted symbolic type” from “no nontrivial cycle”.

Each failure should be converted into a named DSD regression test rather than merely recorded as a rejected paper.

---

## 12. Current DSD verdict

\[
\boxed{
\text{Validated external intermediate theorems are assets; failed global closures are boundary data.}
}
\]

The literature audit therefore does not run in parallel with the proof program.  It becomes part of the proof program itself:

\[
\text{external theorem}
\to
\text{hypothesis-preserving absorption}
\to
\text{internal gate strengthening},
\]

or

\[
\text{external hinge failure}
\to
\text{explicit counterexample/quantifier audit}
\to
\text{internal prohibited-upgrade rule}.
\]

# External Collatz literature vs current DSD proof frontier

Date: 2026-09-06

Status: **COMPARATIVE AUDIT — GLOBAL COLLATZ CONJECTURE REMAINS OPEN.**

This note compares the current repository's proof program with both established Collatz literature and recent claimed-resolution manuscripts.  It distinguishes:

1. established or peer-reviewed partial results that should be treated as reliable external inputs;
2. recent structural work that overlaps the repository's current gates;
3. claimed full proofs whose key bridges require DSD audit;
4. places where the repository is genuinely ahead only in *audit granularity*, not in theorem strength.

No priority claim is made unless independently established.

---

## 1. Established external benchmark

### 1.1 Tao (2019/2022): almost-all descent

Tao proves that for every function `f(N)->infinity`, almost every Collatz orbit in logarithmic density reaches below `f(N)`.  The proof uses a Syracuse first-passage variable, high-frequency Fourier decay, and a skew random walk on `Z/3^n Z`.

DSD comparison:

- External theorem strength is far beyond anything in this repository for an almost-all statement.
- The repository's selector Fourier work, harmonic moving-strip bounds, and `3`-adic mixing diagnostics overlap conceptually but do **not** subsume Tao's theorem.
- Tao's result cannot be promoted from logarithmic-density almost-all to every integer.  The exceptional set may be zero-density yet nonempty.

Audit label: **SAFE EXTERNAL THEOREM / NO UNIVERSAL COVERAGE UPGRADE.**

### 1.2 Barina (2025): computational verification through `2^71`

Barina's published distributed verification raises the verified convergence floor to `2^71`.

DSD comparison:

- External computation is stronger and more independently validated than the repository's finite integer scans.
- The repository now uses `B0=2^71` only as a finite verified floor and derives the parity-prefix minimality strip from it.
- The finite verification itself does not imply convergence above the floor.

Audit label: **SAFE EXTERNAL COMPUTATIONAL FLOOR.**

### 1.3 Monks (2006): every arithmetic progression is sufficient

Monks proves every nonconstant arithmetic progression is a sufficient set for the `3x+1` conjecture.

Important DSD distinction:

\[
\text{sufficient}\neq\text{recursively sufficient}.
\]

Sufficiency only gives orbit intersection with some element of the set.  The current COV program needs a **smaller** merge for minimal-counterexample descent.

Therefore Monks' theorem does not close

\[
36\mathbb N_0+27\text{ recursive?}
\]

or any `COV_n` layer by itself.

Audit label: **SAFE EXTERNAL THEOREM / INSUFFICIENT FOR COV.**

### 1.4 López–Stoll: Sturmian / `3x+1` conjugacy

The López–Stoll Sturmian conjugacy work directly overlaps the repository's Beatty-neutral boundary.

The current formal neutral path

\[
d_n=2,\qquad e_n=\delta_n
\]

lies exactly on the critical mechanical/Sturmian slope.  The literature already shows that aperiodic symbolic parity words and their `2`-adic images are delicate at this boundary.

DSD comparison:

- External work is conceptually earlier and broader on conjugacy/Sturmian structure.
- The repository's contribution is not the existence of the boundary, but its integration with root-Hensel maximality, selector coverage, tail budgets, and same-integer tests.

Audit label: **SAFE PRIOR ART / CURRENT WORK = CROSS-GATE INTEGRATION.**

---

## 2. Ansari (2025) recursive-sufficiency paper

Ansari introduces recursive sufficiency and a decreasing ternary family `F_n`, aiming to place any minimal counterexample inside the infinite ternary `0/1` core.

The printed induction uses an auxiliary identity of the form

\[
F_{n+1}=F'_n\setminus A'_n.
\]

The repository rechecked the first nontrivial step exactly.

Modulo `36`,

\[
F_1=\{3,7,15,19,27,31\},
\]

whereas

\[
F_2=\{3,7,15,19\}.
\]

Hence

\[
F_1\setminus F_2
=\{27,31\}\pmod{36}.
\]

But the printed auxiliary sets at `n=1` give a different difference set. Therefore the published induction equality fails at the first nontrivial step.

DSD verdict:

\[
\boxed{\text{PRINTED PROOF STEP FALSE}.}
\]

This does **not** prove that the theorem itself is false.  It means universal ternary-core coverage is currently unproved.

The repository repaired the set identity directly:

\[
F_n\setminus F_{n+1}
=
\left\{
4\left(3^{n+1}p+2\cdot3^n+\sum_{i<n}a_i3^i\right)+3
\right\}.
\]

This transforms coverage into explicit `COV_n` digit-`2` elimination problems.

Current first open layer:

\[
36\mathbb N_0+27.
\]

Audit label: **CORE PROOF GAP VERIFIED / THEOREM STATUS OPEN.**

---

## 3. Spectral-gap Collatz programs: exact DSD lesson

A 2026 Syracuse transfer-operator project proved a genuine uniform spectral gap on finite `2`-adic quotients, then initially tried to infer elimination of nontrivial Collatz cycles.

The authors later retracted that implication after a decisive control experiment: the `3x-1` map has known nontrivial cycles yet satisfies the same spectral-gap certificate.

Thus

\[
\boxed{
\text{annealed / averaged spectral mixing}
\not\Rightarrow
\text{deterministic orbit cycle elimination}.
}
\]

This is almost exactly the DSD barrier already encountered internally:

- fixed-`Q` or averaged transfer contraction can erase pathwise information;
- a measure/spectral gap need not exclude exceptional deterministic paths;
- one must retain a same-integer / quenched bridge.

DSD verdict on the retracted implication: **FALSE; SELF-CORRECTED BY EXTERNAL AUTHORS.**

The spectral-gap theorem itself may remain valid as an operator theorem.

This is an especially valuable external regression test for the repository's Gate A/Fourier and Gate C pathwise bridges.

---

## 4. Recent deterministic block-contraction claims

A recent indexed manuscript claims a fixed block length (notably `K=21`) forcing at least one accelerated odd Collatz step with

\[
\nu_2(3n+1)\ge2,
\]

and derives deterministic block contraction.

Any universal fixed-window statement of this form is false.

For

\[
n_0=2^r-1,
\]

one has

\[
\nu_2(n_0+1)=r.
\]

Whenever `n≡3 mod 4` and

\[
S(n)=\frac{3n+1}{2},
\]

there is the exact countdown identity

\[
\boxed{
\nu_2(S(n)+1)=\nu_2(n+1)-1.
}
\]

Hence `n0=2^r-1` has exactly `r-1` consecutive accelerated odd steps with

\[
\nu_2(3n+1)=1.
\]

Taking `r=22` gives **21 consecutive** single-halving accelerated steps.

Therefore

\[
\boxed{
\text{no universal fixed }K=21\text{ valuation-window lemma can hold.}
}
\]

The executable certificate is

`collatz/src/external_fixed_block_single_halving_counterexample.py`.

Important scope: this refutes a fixed-window lemma of the stated valuation form.  If a manuscript's potential `Phi` contains additional state variables, that separate inequality must be audited from the full text before declaring every theorem in the paper false.

Audit label: **ROOT WINDOW CLAIM FALSE AS A UNIVERSAL STATEMENT.**

---

## 5. Recent entropic/spectral 'proof' frameworks

Several 2025–2026 manuscripts encode Collatz as an annealed Markov/transfer/entropy process on `Z_2` and prove or claim spectral gaps, entropy decay, or heat-flow absorption.

A more careful recent version explicitly distinguishes:

- unconditional annealed spectral/Dirichlet results;
- deterministic Collatz hitting-time conclusions only under an extra uniform refresh/minorization condition.

DSD classification:

\[
\boxed{
\text{annealed theorem = potentially valid},\qquad
\text{quenched deterministic closure = separate gate}.
}
\]

The decisive DSD question is not whether the operator has a gap.  It is whether the actual deterministic parity history satisfies a bridge strong enough to inherit that gap.

A proof title claiming the full Collatz conjecture is therefore not justified solely by an annealed spectral theorem.

Audit label: **CONDITIONAL / QUENCHED-BRIDGE REQUIRED**, unless the full deterministic bridge is independently proved.

---

## 6. Recent 'complete resolution via analytic number theory + finite computation'

A 2025 indexed manuscript claims a full proof based on:

1. uniform small-ball / phase-separation estimates;
2. a finite computational sieve below a parameter cutoff;
3. a finite-automaton maximum-cycle-mean certificate.

The public abstract alone is not sufficient for a responsible refutation.  DSD requires a full-text audit of three exact gates:

### Gate CR-1 — cycles vs divergence

Eliminating all nontrivial cycles does not eliminate divergent nonperiodic trajectories.

The proof must show that its analytic and automaton gates cover **both** obstruction types.

### Gate CR-2 — finite parameter cutoff vs all integers

A finite check in a derived parameter `k<400` is universal only if every possible counterexample is rigorously mapped into either that finite domain or the analytic domain beyond it.

### Gate CR-3 — small-ball estimate quantifiers

A probabilistic/averaged concentration estimate must be uniform over the deterministic CRT windows actually generated by every admissible Collatz path.  Average-case or density-one control is insufficient.

Current label: **OPEN_DEEP_AUDIT — no error asserted until full text is checked.**

---

## 7. Public 'odd-step proportion <= 1/2' proof claims

Some complete-proof manuscripts emphasize that under the raw Collatz map, an odd step is followed by an even step and therefore the odd-step proportion cannot exceed one half.

That statement alone is true but does not imply contraction.

An odd step followed by the forced single halving has leading multiplier

\[
\frac{3n+1}{2n}\to\frac32>1.
\]

Thus

\[
\boxed{
\text{odd frequency}\le1/2
\not\Rightarrow
\text{negative logarithmic drift}.
}
\]

One must control the **total `2`-adic valuation sum**, not merely the number of even raw steps.

If a full proof promotes the `1/2` frequency statement directly into global contraction, that bridge is invalid.  Full-text verification is still required before assigning the error to a particular manuscript theorem.

Audit label: **TRUE LEMMA / INSUFFICIENT BRIDGE.**

---

## 8. Where established external work is ahead of the repository

The repository must not overstate its position.

External literature is clearly ahead in:

1. Tao's rigorous almost-all theorem and sophisticated `3`-adic Fourier/renewal analysis;
2. Barina's independently published and massively distributed finite verification;
3. classical sufficient-set and `2`-adic conjugacy theory;
4. decades of cycle lower bounds, stopping-time density results, and Diophantine estimates.

The current repository does not replace these results.

---

## 9. Where the current DSD calculation is ahead of the audited proof-claim manuscripts

Relative to the recent *claimed full proofs*, the repository is ahead in **dependency resolution**, not global theorem strength.

### 9.1 Same-integer discipline

The repository repeatedly separates:

\[
\text{symbolic path exists}
\]

from

\[
\text{positive ordinary integer realizes that path}.
\]

This prevents `2`-adic ghosts, annealed paths, or formal Beatty sequences from being promoted to integer counterexamples/proofs.

### 9.2 Measure vs emptiness discipline

Mass/Fourier/spectral decay is never used to conclude an infinite set is empty unless an integer atom floor is separately established.

### 9.3 Root vs later-block discipline

Root-Hensel minimality is used only where the smaller predecessor refers to the original minimal counterexample.  Arbitrary later-block maximality was explicitly withdrawn after globalization failed.

### 9.4 Coverage dependency tracking

When the Ansari ternary coverage proof failed, every downstream `V33` / current-resonance claim that depended on it was downgraded rather than silently retained.

### 9.5 Current universal reduction

Using only the verified floor `2^71`, the repository has derived a universal parity-prefix/Farey restriction whose first possible first-crossing cell is

\[
(A_0,q_0)
=(114208327604,72057431991),
\]

with a root-safe Hensel-maximal prefix depth of `195`.

This is not known here as a published external theorem.  It is therefore a potentially original **reduction**, not a Collatz proof.

### 9.6 Exact COV repair target

Instead of relying on the flawed ternary induction, the repository identifies the exact removed layer

\[
A_n=F_n\setminus F_{n+1}
\]

and the first unresolved recursive class

\[
36\mathbb N_0+27.
\]

This is a more precise proof obligation than merely citing the broken coverage theorem.

---

## 10. Current global status

No audited external paper currently supplies a verified full proof that can simply be imported to close the repository.

The strongest responsible classification is:

\[
\boxed{
\begin{array}{ll}
\text{Tao / Barina / Monks / classical theory}&\textbf{SAFE EXTERNAL INPUTS},\\
\text{Ansari ternary recursive-sufficiency proof}&\textbf{PRINTED INDUCTION GAP},\\
\text{spectral gap }\Rightarrow\text{ deterministic cycles}&\textbf{FALSE / RETRACTED},\\
\text{fixed }K=21\text{ single-halving window}&\textbf{FALSE},\\
\text{annealed spectral proof frameworks}&\textbf{QUENCHED BRIDGE OPEN},\\
\text{recent complete-resolution manuscripts}&\textbf{DEEP AUDIT REQUIRED},\\
\text{current repository global proof}&\textbf{OPEN}.
\end{array}
}
\]

---

## 11. Next external-audit targets

Highest-value next audits:

1. obtain the full text/artifacts of the 2025 `analytic number theory + finite computation` complete-resolution claim and audit its uniform small-ball quantifiers and coverage partition;
2. audit the deterministic block-contraction manuscript beyond the already-refuted fixed-window root lemma, separating any surviving graph results from the global contraction claim;
3. compare the current universal Farey first-cell reduction with the strongest published lower bounds on total stopping time / first descent;
4. compare root-Hensel depth-195 maximality with the López–Stoll `2`-adic conjugacy and known parity-vector inverse formulas;
5. keep the self-retracted spectral-gap project as a permanent DSD regression test for `annealed -> deterministic` overreach.

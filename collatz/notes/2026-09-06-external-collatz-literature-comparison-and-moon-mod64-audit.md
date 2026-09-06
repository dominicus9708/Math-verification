# External Collatz literature comparison and mod-64 LP audit

Date: 2026-09-06

Status: **COMPARATIVE DSD AUDIT.** This note compares the current repository proof program with established Collatz literature and selected recent claimed resolutions. It does not claim priority or a proof of the Collatz conjecture.

## 1. Established external frontier

### Tao — almost all orbits attain almost bounded values

Tao proves that for any function `f(N)->infinity`, almost every Collatz orbit attains a value below `f(N)` in logarithmic density. The proof uses an approximate transport theorem for a first-passage random variable and high-frequency characteristic-function estimates for a skew random walk on a 3-adic cyclic group.

**External advantage:** this is a rigorous asymptotic theorem covering almost all integers and uses a mature 3-adic probabilistic/renewal framework far beyond the theorem strength of the present repository.

**Internal complement:** the current DSD program studies exact minimal-counterexample, same-integer, Hensel, Beatty, and cross-base constraints. These are not stronger than Tao's theorem globally, but they target the exceptional set that an almost-all theorem is allowed to leave behind.

### Barina — exhaustive verification through `2^71`

Barina (2025) proves by distributed computation that all starting values below `2^71` converge.

**External advantage:** this is the strongest published exhaustive verification floor currently used by the universal branch.

**Internal use:** the present parity-prefix recursively-sufficient spine starts from this floor and converts minimality above the floor into a near-critical odd-density condition. The internal work is therefore downstream of, not superior to, Barina's computational theorem.

### Hercher — no nontrivial `m`-cycles for `m<=91`

Hercher proves that any nontrivial Collatz cycle must have at least 92 local minima and discusses the enormous lower bound on odd members needed for the next exclusion stage.

**External advantage:** this is a rigorous global cycle theorem.

**Internal complement:** the present first-crossing/Farey program focuses on divergent/minimal-counterexample trajectories and same-integer address constraints, not merely cycles. It should not be described as superseding Hercher's cycle theorem.

### López–Stoll — 2-adic conjugacy, Sturmian/critical-density boundary

López and Stoll prove that if a rational 2-adic integer had a non-cyclic trajectory, its parity density would have to lie at the critical value `log_3 2` in the liminf sense. They also study Sturmian parity vectors under the 3x+1 conjugacy.

**External advantage:** this gives a genuine theorem at the exact critical-density boundary that repeatedly appears in the present DSD calculations.

**Internal complement:** the repository adds exact finite root-Hensel, canonical-lift, ghost, Beatty, and same-integer certificates inside this critical regime. Those are refinements of the exceptional boundary, not a replacement for the external theorem.

### Moore–Schulman — incomplete powers-of-three exponential-sum conjecture

The Moore–Schulman conjecture on exponential sums of powers of 3 modulo powers of 2 is substantially stronger than the selector-Walsh mixing estimate needed by one internal route.

**Audit rule:** this conjecture is an external open input and must never be imported as a theorem. The current repository correctly treats the near-linear incomplete-orbit Fourier cancellation route as OPEN.

## 2. Ansari (2025) recursive sufficiency — useful concept, printed induction gap

Ansari introduces recursively sufficient sets and proposes a decreasing ternary `0/1` sieve family `F_n` whose intersection would cover hypothetical minimal counterexamples.

The concept of recursive sufficiency is useful and remains part of the present project vocabulary.

However, direct residue audit of the printed induction gives

\[
F_1\bmod36=\{3,7,15,19,27,31\},
\]

and

\[
F_2\bmod36=\{3,7,15,19\}.
\]

Hence

\[
F_1\setminus F_2
=(36\mathbb N_0+27)\cup(36\mathbb N_0+31).
\]

The printed auxiliary identity used to close the induction does not reproduce this exact difference already at `n=1`.

**DSD verdict:** the published induction is not verified as written. This does not prove the recursively-sufficient statement false; it reopens the coverage theorem.

The current repository is ahead of the printed proof only in **audit/repair resolution**, not in proving the missing global theorem. It derives the exact removed layer

\[
A_n=F_n\setminus F_{n+1}
\]

directly and isolates `36N_0+27` as the first unresolved coverage class.

## 3. Moon 2025 mod-64 LP claimed proof — exact state-aliasing failure

A recent claimed computer-assisted proof reduces the odd-to-odd Collatz map to the 31 nontrivial odd residue classes modulo 64. It defines

\[
k(r)=v_2(3r+1)
\]

and a deterministic successor

\[
r'=(3r+1)/2^{k(r)}\pmod{64}
\]

from the residue `r` alone, then solves a finite LP for a corrected Lyapunov potential.

This quotient is not faithful to the actual accelerated Collatz map.

Take three ordinary positive integers in the same residue class:

\[
21\equiv85\equiv149\equiv21\pmod{64}.
\]

Then

\[
3\cdot21+1=64,
\qquad
v_2=6,
\qquad
T_{odd}(21)=1,
\]

\[
3\cdot85+1=256,
\qquad
v_2=8,
\qquad
T_{odd}(85)=1,
\]

and

\[
3\cdot149+1=448=64\cdot7,
\qquad
v_2=6,
\qquad
T_{odd}(149)=7.
\]

Therefore exact valuation and successor are not functions of `n mod 64`.

In general, for

\[
n=21+64t,
\]

one has

\[
3n+1=64(1+3t),
\]

so the valuation beyond the forced factor `2^6` and the resulting odd successor depend on the higher binary digits encoded by `t`.

Thus

\[
\boxed{
\text{the deterministic 31-state transition graph is not a quotient of the actual odd Collatz dynamics.}
}
\]

There is a second representative-substitution problem if the drift inequality uses

\[
\log(3+1/r)
\]

with `r` the small residue representative. The true odd-step multiplicative term is

\[
\log(3+1/n),
\]

which varies inside the residue class.

**DSD classification:**

- `STATE_ALIASING`: higher bits change the transition while the finite state is unchanged;
- `REPRESENTATIVE_SUBSTITUTION`: a residue representative is substituted for the actual integer in a non-residue-invariant term.

The accompanying exact certificate is

`collatz/src/external_moon_mod64_state_aliasing_certificate.py`.

The LP certificate may be internally correct for the artificially defined 31-state graph; that does not imply it is a Lyapunov certificate for the full Collatz map.

## 4. Comparison with the present DSD finite-state audits

The mod-64 failure is precisely the kind of error the current repository repeatedly guards against.

Examples:

1. Fixed-Q reverse-potential arguments are explicitly labeled barriers when a formal 2-adic path survives; they are not promoted to positive-integer statements.
2. Hensel maximality is applied only to the original root prefix unless a valid pullback/globalization theorem is proved; arbitrary later-block reuse was withdrawn.
3. Fixed finite `Q` truncation of the mixed state was proved insufficient by an infinite witness family, with the lower bound `Q(h)>=h-3` for that architecture.
4. Canonical finite-support conditions are kept separate from symbolic 2-adic paths.

Hence the current calculations are ahead of this particular claimed proof in **state-faithfulness discipline**.

## 5. Other recent claimed resolutions

Searches in current research indexes return several 2025 claimed complete proofs based on finite automata, residue graphs, collapse depth, maximum-cycle-mean certificates, or analytic+finite hybrid gates.

These should not be rejected merely because they are preprints or recent. Each needs a root-hinge audit.

The priority tests are:

1. **Finite-state faithfulness:** does the state determine every transition quantity actually used by the proof?
2. **Coverage:** does the finite certificate cover divergent trajectories as well as cycles?
3. **Quantifier preservation:** is a statement proved for all states, or only for averages / most residues / bounded windows?
4. **Representative invariance:** are expressions involving the actual integer replaced by a residue representative without a uniform bound?
5. **Finite-to-infinite closure:** does a verified cutoff plus asymptotic argument truly cover every remaining case?
6. **Cycle-vs-divergence separation:** excluding nontrivial cycles is not enough to exclude divergent aperiodic trajectories.

At the present stage, abstracts alone are insufficient to classify the other claimed resolutions as mathematically false. Full theorem-level audit is required.

## 6. Where the external literature is clearly ahead

The present project must not overstate its position.

External established literature is ahead in:

- Tao's rigorous almost-all orbit theorem;
- Barina's exhaustive verified range;
- Hercher/Simons–de Weger cycle lower bounds;
- López–Stoll's general 2-adic conjugacy and critical-density theorem;
- mature stochastic, renewal, Diophantine, and difference-inequality theory surveyed by Lagarias.

The current repository does not supersede these results.

## 7. Where the present calculations are comparatively ahead

Relative to the audited *claimed proof* literature, the current DSD program is stronger in a narrower sense:

### A. State-faithful cross-base bookkeeping

It keeps separate:

- binary parity prefix;
- exact 2-adic canonical residue;
- 3-adic/Hensel correction class;
- ordinary-positive-integer finite-support condition;
- selector-family coverage.

### B. Explicit barrier logging

Several tempting proof routes have been disproved internally rather than silently reused:

- arbitrary occupied-subset macro contraction;
- uniform contraction of every surplus stratum;
- fixed-Q pathwise low-strip elimination;
- arbitrary later-block Hensel maximality;
- bounded/sublinear ternary state memory in the mixed architecture;
- single-anchor inverse-merge coverage of `36k+27`.

### C. Universal first-crossing reduction independent of the broken ternary coverage

Using the verified floor and parity-prefix minimality strip, the current universal branch isolates the first possible Farey cell

\[
(A,q)=
(114208327604,72057431991),
\]

with a second larger cell before the previously conditional resonance, and gives root-Hensel safety through depth 195 for the first cell.

These are genuine exact reductions, but they do **not** yet close the remaining cell.

### D. Coverage audit of recursive sufficiency

The project identified the exact failure in the printed ternary induction, downgraded all dependent `V_33` conclusions from universal to conditional, and built an independent parity-prefix recursively-sufficient route instead.

This audit discipline is currently one of the strongest parts of the project.

## 8. Overall verdict

The correct comparative statement is:

\[
\boxed{
\text{The project is not ahead of established Collatz mathematics in theorem strength.}
}

but

\[
\boxed{
\text{it is ahead of several recent claimed proofs in dependency auditing, state faithfulness, and exact barrier localization.}
}

The unresolved core remains substantial:

- universal first-crossing cell closure;
- genuinely aperiodic positive-integer survivor exclusion;
- or an alternative universal route bypassing those gates.

The Collatz conjecture remains OPEN.

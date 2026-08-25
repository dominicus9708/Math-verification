# DSD audit: Stage 4 versus globalization budgets

Date: 2026-08-26

Status: **structural proof-program audit.** This checkpoint separates exact reductions, finite certificates, branch-local exponential budgets, and genuinely asymptotic gaps. It is not a proof of the Collatz conjecture.

## 1. Audit rule

Use only the DSD state/channel/transition/aggregation architecture. No DSD physical dynamics is imported.

The present Collatz program is separated into the following descriptive layers:

1. **formation layer** — the recursively sufficient ternary selector family
   \[
   \mathcal C_m=\left\{4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:a_i\in\{0,1\}\right\};
   \]
2. **binary address layer** — the unique canonical parity-prefix address of the same integer;
3. **coefficient-survival layer** — the prefix condition \(3^{q_h}\ge2^h\);
4. **Hensel/maximality layer** — correction classes and smaller-root credits;
5. **renewal-height layer** — Stage-4 relative-height states;
6. **aggregation layer** — dyadic language mass, selector mass, and their conditional amplification.

A conclusion may be transferred between layers only when the same integer, domain, horizon, and conditioning are preserved.

## 2. Exact reductions that survive the audit

### 2.1 Finite-address deterministic tail

For a fixed start bound \(B\le2^L\), canonical lift branching ends after depth \(L\). Any surviving start \(r<B\) has only its ordinary deterministic Collatz continuation thereafter.

For the two current resonance layers this gives:

- \(m=44\): at most a 73-bit canonical-address frontier;
- \(m=45\): at most a 74-bit canonical-address frontier.

This removes an infinite *address-choice* tree, but not the deterministic survival problem.

### 2.2 Survivor Hensel multiplicity is not an exponential channel

For coefficient-surviving words,

\[
R\le q3^{q-1},
\]

and two surviving same-Hensel siblings satisfy

\[
0<d=\frac{R'-R}{3^q}<\frac q3.
\]

Hence the relevant endpoint/Hensel Pareto fibre has at most \(O(H)\) candidates and contributes only \(O(\log H)=o(H)\) information.

The exponential obstruction therefore does not come from uncontrolled Hensel multiplicity.

### 2.3 Terminal maximality is a valid backward implication

The concatenation identity

\[
R_{ws}=3^rR_w+2^hC_s
\]

preserves a positive same-Hensel root credit under a common suffix. Therefore terminal whole-prefix maximality at a horizon implies maximality at every earlier prefix.

This route is algebraically distinct from the older repeated local L7/L14 pullback route and must not inherit conclusions from that older route unless the domains are explicitly re-verified.

## 3. Stage-4 branch-local reductions

The renewal-height argument progressively removes states:

\[
\text{unbounded height}\to\{0,1,2,3,4\}\to\{0,1,2\}\to\boxed{\{0,1\}}.
\]

On the final two-state recurrent core the L7-only certificate permits an average per-window amplification scale \(K=117\). Adding simultaneous L7/L14 maximality raises that branch-local allowance to \(K=150\), but still requires genuine same-address selector loss at both states.

The remaining sufficient selector losses for the strengthened two-state branch are approximately:

\[
33.36\%\quad(z=1),
\qquad
82.27\%\quad(z=0).
\]

Here the relative renewal height is denoted by **\(z\)** in this audit. This avoids the existing notation collision in which \(H\) is used both for binary horizon and for relative height in different notes.

## 4. Critical budget-separation rule

The constants

\[
K=15,25,56,117,150
\]

must **not** be multiplied, averaged, or interpreted as cumulative progress. They belong to different conditioned state spaces obtained after different escape sectors have already been removed.

Likewise, two exclusion rates must remain distinct:

### Stage-4 local L7 budget

\[
\eta>\frac7{50}=0.14.
\]

For the original 28-step renewal formulation, \(K<15\) is sufficient because

\[
\frac{\log_2 15}{28}\approx0.139531807<0.14.
\]

### General coefficient-formation budget

\[
\delta_{\rm form}
=1-H_2(\log_3 2)
\approx0.05004447281166946.
\]

This is a different language and a different asymptotic bookkeeping problem. The Stage-4 number \(\log_2(15)/28\) is larger than \(\delta_{\rm form}\), so the local \(K<15\) theorem cannot simply be substituted for the global same-address exponent \(\beta\).

This is a DSD aggregation boundary: **branch-local conditional amplification is not the same descriptor as global selector amplification.**

## 5. Finite versus asymptotic separation

The coherent-ballot certificate gives a very large exact finite gate: for current large recursively sufficient layers, including \(m=44,45\), additive correction cannot create a coefficient-subcritical no-descent path through depth 301,993.

This is powerful finite pruning, but it is not an all-horizon theorem.

The general whole-prefix safe horizon is

\[
H_{\rm safe}(m)\sim\rho m,
\qquad
\rho\approx4.29447379207261.
\]

Formation exclusion available by that horizon is only

\[
\delta_{\rm form}\rho\,m
\approx0.2149146769m,
\]

leaving about

\[
0.7850853231m
\]

raw selector bits unaccounted for. Therefore the linear safe horizon, by itself, cannot close the recursively sufficient family by counting.

## 6. Current open exponential channel

After the surviving reductions, the genuinely exponential obstruction can be stated as:

> Can the fixed ternary 0/1 selector family continue to land, at the **same integer addresses**, on the exceptionally sparse dyadic coefficient-surviving/terminal language at a rate sufficient to defeat deterministic exclusion?

Equivalent current formulations include:

1. the Stage-4 two-state selector correlation at renewal heights \(z=1\) and \(z=0\);
2. the global same-address amplification exponent \(\beta\);
3. the terminal intersection
   \[
   \mathcal C_m\cap\mathcal S_{H_{\rm safe}(m)}\cap\mathcal M_{H_{\rm safe}(m)};
   \]
4. the resonant triadic carry-cancellation problem after the forced initial `11` removes the Hensel inverse from the large Fourier modes.

These are related views of the same cross-base bottleneck, but equivalence between them must itself be proved rather than assumed.

## 7. Two-exponent globalization checkpoint

Let

\[
\beta=\limsup_{H\to\infty}\frac{\log_2\Xi_H}{H}
\]

be the same-address selector amplification exponent and

\[
\gamma=\limsup_{H\to\infty}\frac{\log_2G_H}{H}
\]

be the nearest-root-credit exponent in the unrestricted whole-prefix formulation.

A sufficient global budget is

\[
\boxed{
\gamma+(\log_2 3)\beta
<
(\log_2 3)\delta_{\rm form}
\approx0.07931861277485554.
}
\]

The survivor-Hensel linear-credit theorem shows that one important multiplicity channel has zero exponential rate, but it does not by itself set the unrestricted \(\gamma\) in the preceding criterion to zero. The domain distinction must be preserved.

## 8. Next calculation after this audit

The next proof search should not add another independent local maximality filter. The L7/L14 experiment already shows diminishing returns.

The preferred target is a **same-address transfer operator** on the final renewal core \(z\in\{0,1\}\):

- state: renewal height, mechanical phase, and only the minimal selector residue/carry information required for exact continuation;
- transition: one normalized 28-step block;
- escape: any transition into the already controlled \(z\ge2\) sector;
- weight: exact ternary-selector mass divided by the corresponding dyadic mass;
- theorem target: a uniform weighted spectral-radius/joint-transfer bound strong enough to beat the certified two-state deterministic exclusion.

This attacks the remaining correlation directly and provides a natural bridge to the resonant triadic carry formulation.

## 9. Audit verdict

- **Exact algebraic identities:** retained.
- **Finite certificates:** retained with their stated horizons only.
- **Hensel/endpoint multiplicity as an exponential obstruction:** removed on the coefficient-surviving domain.
- **Repeated local maximality as the main route:** deprioritized.
- **Stage-4 branch budgets and global formation budgets:** explicitly separated.
- **Remaining principal obstruction:** same-integer ternary-selector / dyadic-address correlation.
- **Collatz conjecture:** still open in this program.

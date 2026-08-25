# DSD terminal proof-chain roadmap for the Collatz program

Date: 2026-08-25

## Status

Consolidated proof architecture and dependency map.

This document separates proved structural lemmas, exact finite certificates, negative/barrier results, and genuinely open terminal gates.

No Collatz proof is claimed.

---

## 1. Status vocabulary

Every future result in this line should be tagged by one of four statuses.

### SAFE LEMMA
A mathematical implication proved independently of a finite search horizon.

### FINITE CERTIFICATE
An exact exhaustive computation over a declared finite state space or parameter range.

### BARRIER
A proved obstruction or negative control showing that a proposed proof architecture cannot close in its naive form.

### OPEN GATE
A statement still required for the terminal proof chain.

This vocabulary is intended to prevent finite pruning percentages from being confused with progress toward an asymptotic proof.

---

## 2. Unified coefficient coordinate

For completed odd-event depth `q`, let

\[
A_q=\sum_{j<q}v_j,
\qquad
\Theta_q=\frac{3^q}{2^{A_q}}.
\]

Two previously separate coordinates are exact logarithmic projections of the same scalar:

\[
\boxed{
 s_q=\lfloor\log_2\Theta_q\rfloor,
 \qquad
 d_{A_q}=\lfloor\log_3\Theta_q\rfloor.
}
\]

Status: **SAFE LEMMA**.

Thus signed skew, Beatty surplus, and adaptive reverse scale are not independent proof variables.  The core scale variable is `Theta`.

The canonical formation/lift condition remains:

\[
\boxed{
N\in\mathbb N_{>0}
\iff
(t_q)\text{ has finite support},
}
\]

for the infinite completed-event code.

Status: **SAFE LEMMA**.

The current record integer audit shows that eventual zero lift digits do not by themselves keep `Theta`, `s`, or `d` uniformly small.

Status: **FINITE CERTIFICATE / NEGATIVE CONTROL**.

---

## 3. High-surplus structural control

Let

\[
b(n)=\min\{q:3^q\ge2^n\},
\qquad
d_n=q_n-b(n).
\]

For a coefficient-surviving parity prefix,

\[
d_n\ge0.
\]

The Beatty boundary word has the exact local restrictions:

- no `PP`;
- no `RRR`;
- plateau-to-plateau macrocycles are `A=PR` or `B=PRR`;
- `AA` is forbidden;
- every pair of macrocycles is `AB`, `BA`, or `BB`.

Status: **SAFE LEMMA**.

With

\[
W(d)=\left(\frac32\right)^d,
\]

the normalized dyadic weighted extension satisfies

\[
\boxed{
\mathbb E W(d_{\rm out})
\le
\frac{3125}{3456}W(d_{\rm in})
}
\]

over every pair of Beatty macrocycles.

Status: **SAFE LEMMA**.

This is the present asymptotic mechanism for controlling the high-surplus tail.

### Critical limitation

This expectation is currently established for the unrestricted dyadic extension process after coefficient-survival rejection.  It has not yet been transferred to the actual canonical / ternary-selector candidate language strongly enough to rule out exceptional paths.

This missing transfer is **OPEN GATE A**.

---

## 4. Low-surplus finite-state mechanism

At fixed ternary resolution `Q`, after endpoint decoupling (`q_n>=Q`), define

\[
z_n=2^{-n}R_n\pmod{3^Q}.
\]

Then the DSD local state

\[
(d_n,z_n)
\]

has the exact one-step update

\[
d_{n+1}=d_n+e_n-\delta_n,
\]

and

\[
z_{n+1}=2^{-1}z_n
\quad(e_n=0),
\]

\[
z_{n+1}=2^{-1}(3z_n+1)
\quad(e_n=1)
\]

modulo `3^Q`.

Status: **SAFE LEMMA**.

Reverse exponent strings carry potential

\[
\Lambda=\frac{3^r}{2^K}.
\]

For a bounded surplus strip `0<=d<D`, finite `(d,z)` transfer tables and exact reverse witnesses can therefore be built and audited.

Existing Q7/H24-H25 cross-place computations demonstrate nontrivial finite elimination and block contraction.

Status: **FINITE CERTIFICATE**.

### Required upgrade

Once Gate A supplies uniform return/tightness of actual candidate mass inside a fixed strip, one must prove a finite-state spectral / block gap:

\[
\boxed{
\exists D,Q,r,\varepsilon>0:
\quad
\mathcal T_{D,Q}^{(r)}
\text{ loses at least an }\varepsilon\text{ fraction of candidate mass.}
}
\]

The exact form may be substochastic matrix spectral radius `<1`, a block-minorization inequality, or an equivalent finite combinatorial statement.

This is **OPEN GATE B**.

Unlike Gate A, Gate B is expected to be finite-state once the correct strip and conditioning are fixed.

---

## 5. Reverse mechanism: what is and is not available

At depth `Q`, every reverse potential satisfies

\[
\Lambda\le\left(\frac32\right)^Q.
\]

Therefore a fixed Q cannot attack arbitrarily large surplus.

Status: **BARRIER**.

More strongly, if `G_Q(d)` is the set of endpoint residues admitting some reverse code with

\[
\Lambda>3^d,
\]

then for every `1<t<2`, uniformly in `Q`,

\[
\boxed{
\frac{|G_Q(d)|}{2\cdot3^{Q-1}}
\le
\frac32\frac{A_t}{1-A_t}3^{-td},
\qquad
A_t=\frac{3^{t-1}}{2^t-1}<1.
}
\]

Hence strong reverse residues become exponentially rare with surplus, regardless of how large `Q` is chosen.

Status: **SAFE LEMMA / BARRIER**.

Consequences:

1. fixed-Q uniform statewise elimination is impossible on the unbounded surplus axis;
2. naive adaptive-Q uniform-density elimination is also impossible;
3. reverse minimality remains useful only in a bounded low strip or through a non-generic arithmetic correlation with actual minimal-counterexample residues.

The terminal architecture should therefore not rely on strong-reverse residues having positive generic density at large `d`.

---

## 6. Terminal three-gate chain

The surviving main line is now:

\[
\boxed{
\text{Gate A: tail tightness}
\longrightarrow
\text{Gate B: low-strip elimination}
\longrightarrow
\text{Gate C: minimal-counterexample closure}.
}
\]

### OPEN GATE A — candidate-language tail tightness

Required statement, one useful form:

There exist `a>1`, a finite strip height `D`, and constants `r` and `sigma<1` such that the actual canonical / selector candidate measure satisfies a Foster-Lyapunov-type inequality

\[
\boxed{
\mathbb E_{\rm candidate}[a^{d_{n+r}}\mid\mathcal F_n]
\le
\sigma a^{d_n}+C\,\mathbf 1_{d_n<D}.
}
\]

A weaker block/tail formulation is acceptable if it implies that a uniform positive fraction of surviving candidate mass repeatedly enters `d<D`.

The already-proved Beatty macro Lyapunov rule supplies the drift component.  The missing ingredient is transfer from dyadic extension mass to the actual canonical / ternary-selector language.

### OPEN GATE B — finite low-strip loss

Conditioned on repeated visits to `0<=d<D`, prove that a fixed finite-state block has a nonzero killing gap.

A target form is

\[
\boxed{
\mu(S_{n+r}\cap\{d<D\})
\le
(1-\varepsilon)
\mu(S_n\cap\{d<D\}).
}
\]

The existing `(d,z)` reverse DP, root-level minimality filters, and exact cross-place certificates are the raw material for this gate.

### OPEN GATE C — density loss to integer nonexistence

Even geometric decay of a candidate measure is not automatically the nonexistence of one exceptional positive integer path.

The final step must use the canonical formation/minimal-counterexample structure.

One target is to show that a hypothetical minimal counterexample determines an infinite nested sequence of candidate cylinders whose mass cannot obey the Gate-A/Gate-B contraction while the canonical lift digits are eventually zero.

Equivalently, derive a contradiction between

\[
\boxed{t_q=0\text{ eventually}}
\]

and the recurrent loss forced by Gates A and B.

This is **OPEN GATE C**.

---

## 7. Auxiliary route: arithmetic correlation

A secondary route remains logically possible:

\[
\text{eventual-zero lift / minimality}
\Longrightarrow
\text{atypically frequent membership in rare strong-reverse residues}.
\]

Because universal reverse rarity is already proved, such a result would have to be an exceptional arithmetic correlation, not a generic density statement.

Status: **OPEN AUXILIARY ROUTE**.

This route should not replace Gate A unless a concrete forcing congruence is found.

---

## 8. Routes currently closed or demoted

The following should not be reopened without a genuinely new mechanism.

1. Pure fixed-Q reverse elimination of all surplus states — **closed by fixed-Q ceiling**.
2. Adaptive Q chosen only to recover a positive generic residue density — **closed by universal reverse rarity**.
3. Uniform bounded return time to `d=0` along every surviving path — **false by exact record excursion**.
4. Stopped-tree energy closure using coefficient survival alone — **blocked by selector/coefficient dimension mismatch**.
5. Arbitrary later-block Hensel maximality — **withdrawn because of root pullback/globalization failure**.
6. Treating finite m=44 survivor percentages as proof progress percentages — **invalid interpretation**.

---

## 9. Practical next-work order

The next work should be performed in this order.

### Step A1 — conditional tail transfer diagnostic

Measure the Beatty Lyapunov weighted factor after conditioning on the actual canonical selector language, rather than on unrestricted dyadic extensions.

Goal: determine whether selector conditioning destroys, preserves, or improves the factor `3125/3456`.

### Step A2 — derive a symbolic comparison inequality

If the finite diagnostic remains contracting, identify the exact static mixing quantity needed to compare selector-conditioned mass to dyadic mass.

Candidate forms include bounded Radon-Nikodym ratios on a fixed low ternary cylinder, convolution min/max ratios, or a ballot/cycle-lemma endpoint bound.

### Step A3 — prove candidate tail tightness

Upgrade the diagnostic to a horizon-independent bound.

Only after this succeeds should the program invest heavily in optimizing the low-strip DP.

### Step B1 — choose the smallest useful strip

Use the reverse ceiling and existing Q7 data to determine a finite `D,Q` pair with a robust finite-state killing gap.

### Step B2 — certify the block spectral gap

Produce a small, exact integer/rational matrix certificate or equivalent exhaustive transition certificate.

### Step C1 — formulate the nested-cylinder contradiction

Translate repeated candidate-mass contraction into an obstruction for an eventually constant canonical representative `rho_q=N`.

### Step C2 — terminal audit

Independently verify that every implication used is root-global and does not rely on density-zero implying emptiness.

---

## 10. Current assessment

The program has moved from broad finite pruning to a narrow structural chain.

The main unresolved mathematical difficulty is no longer locating a useful local Collatz filter.  Several such filters and exact finite-state rules already exist.

The central open problem is:

\[
\boxed{
\text{transfer the Beatty high-surplus Lyapunov drift to the actual canonical candidate language.}
}
\]

If Gate A is proved, Gate B becomes a finite-state closure problem and Gate C becomes the final minimal-counterexample/globalization problem.

Until Gate A is established, no numerical survivor percentage should be interpreted as proximity to a Collatz proof.

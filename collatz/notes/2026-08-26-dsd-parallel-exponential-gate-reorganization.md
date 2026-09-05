# DSD parallel reorganization: exponential coefficient-survival gate

Date: 2026-08-26

Status: **derived proof-program reorganization from already recorded lemmas.** This note uses DSD only as a dependency/audit framework. It identifies a stronger route from no-descent to coefficient survival and shows that the unrestricted root-credit exponent `gamma` need not remain on the principal globalization chain if the same-address correlation branch can be closed. It is not a proof of the Collatz conjecture.

## 1. Why this reorganization was attempted

The previous active frontier was organized around two global exponential channels:

\[
\gamma+(\log_2 3)\beta
<
(\log_2 3)\delta_{\rm form}.
\]

Here `beta` controls same-address selector amplification and `gamma` controls unrestricted whole-prefix root credit.

That formulation is valid as a sufficient route, but DSD dependency separation asks whether both channels are genuinely upstream necessities or whether one appeared only because an intermediate implication was too weak.

The relevant layers are:

1. recursively sufficient formation layer `C_m`;
2. actual no-descent condition for a minimal counterexample;
3. coefficient-survival language `S_H`;
4. same-address selector/survivor aggregation;
5. optional Hensel/maximality/root-credit refinement.

The key question is whether layer 2 can be transferred directly to layer 3 far beyond the previous root-safe horizon.

## 2. Reused first-crossing theorem

The buffered-core and fixed-first-crossing reductions already record the following fact.

At a paradoxical first coefficient crossing of length `sigma`, with

\[
\sigma=\lceil q\log_2 3\rceil,
\qquad
D=2^\sigma-3^q>0,
\]

a no-descent start obeys

\[
x<\frac{q3^{q-1}}D.
\]

Writing

\[
D=3^q\left(e^{\sigma\log2-q\log3}-1\right)
\]

and using the recorded global Rhin-type lower bound

\[
\sigma\log2-q\log3\ge\sigma^{-13.3},
\]

the project obtained

\[
\boxed{x<\sigma^{14.3}}
\]

up to harmless endpoint conventions. The sharper mechanical correction estimate gives the same polynomial conclusion, and an asymptotically stronger `8.616` exponent is also recorded after its effective threshold.

The important point here is not the best exponent. It is that the start of a paradoxical first crossing is bounded **polynomially in the first-crossing horizon**.

## 3. Exponential gate on the recursively sufficient layer

The recursively sufficient depth-`m` selector family is

\[
\mathcal C_m
=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\},
\]

so every member satisfies

\[
\boxed{x\ge N_{\min}(m):=4\cdot3^m+3.}
\]

Suppose `x in C_m` has no descent through a horizon `H`, but coefficient survival first fails at some `sigma<=H`.

Because this is the **first** coefficient failure and the actual orbit has not descended, `sigma` is precisely a paradoxical first coefficient crossing in the domain of the preceding bound. Hence

\[
N_{\min}(m)
\le x
<\sigma^{14.3}
\le H^{14.3}.
\]

Therefore any horizon satisfying

\[
H^{14.3}\le N_{\min}(m)
\]

is automatically coefficient-safe for a no-descent selector start.

Define

\[
\boxed{
H_{\rm Rhin}(m)
:=
\left\lfloor
(4\cdot3^m+3)^{1/14.3}
\right\rfloor.
}
\]

Then, subject only to the already recorded first-crossing lemma,

\[
\boxed{
T^j(x)\ge x\ \forall j\le H_{\rm Rhin}(m)
\Longrightarrow
3^{q_j(x)}\ge2^j\ \forall j\le H_{\rm Rhin}(m)
}
\]

for every `x in C_m`.

Asymptotically,

\[
\boxed{
H_{\rm Rhin}(m)
=2^{\kappa_{13.3}m+O(1)},
\qquad
\kappa_{13.3}
=
\frac{\log_2 3}{14.3}
\approx0.110836538512.
}
\]

Using the stronger asymptotic first-crossing exponent `8.616` after its effective threshold would improve the exponent to

\[
\boxed{
\kappa_{7.616}
=
\frac{\log_2 3}{8.616}
\approx0.183955721996.
}
\]

The unconditional `14.3` route is sufficient for the structural reorganization and avoids depending on an explicit value of the stronger threshold.

## 4. Parallel envelope with the finite coherent-ballot theorem

The later coherent-ballot certificate proves that every recursively sufficient layer

\[
m\ge20
\]

has

\[
\boxed{
\text{no descent through }301{,}993
\Longrightarrow
\text{coefficient survival through }301{,}993.
}
\]

The two gates should not compete. They operate on different useful scales and can be combined by taking their maximum:

\[
\boxed{
H_*(m)
:=
\max\left\{
301{,}993,
H_{\rm Rhin}(m)
\right\},
\qquad m\ge20.
}
\]

Numerically, the Rhin gate first exceeds `301,993` at

\[
\boxed{m=163.}
\]

Thus the natural parallel division is:

- `20<=m<=162`: the exact finite coherent-ballot theorem supplies the stronger gate;
- `m>=163`: the first-crossing/Rhin gate eventually dominates and then grows exponentially in `m`.

This is a genuine dependency simplification: the global argument is no longer confined to the old root-safe linear horizon `H_safe(m)~4.294m`.

## 5. External finite verification removes the lowest formation layers

David Barina's 2025 computational verification establishes Collatz convergence for every positive start below

\[
2^{71}.
\]

The largest start in `C_m` is

\[
N_{\max}(m)=6\cdot3^m+1.
\]

Direct comparison gives

\[
N_{\max}(43)
=1{,}969{,}541{,}804{,}367{,}222{,}465{,}763
<2^{71},
\]

while

\[
N_{\min}(44)
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}527
>2^{71}.
\]

Hence, if external computational verification is admitted as the finite base certificate,

\[
\boxed{m\le43}
\]

is already covered, and the first recursively sufficient layer not covered by that external range is exactly

\[
\boxed{m=44.}
\]

Reference: D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81, 810 (2025), DOI 10.1007/s11227-025-07337-0.

## 6. One-exponent same-address closure criterion

Let `S_H` denote the coefficient-surviving binary language through depth `H`, and let `nu_H` be uniform dyadic measure.

With

\[
\alpha=\log_3 2,
\qquad
\delta_{\rm form}=1-H_2(\alpha),
\]

we have the standard entropy upper bound

\[
\boxed{
\nu_H(S_H)
\le
2^{-\delta_{\rm form}H+o(H)},
\qquad
\delta_{\rm form}
\approx0.05004447281166946.
}
\]

Let `mu_m` be the uniform probability measure on `C_m`, viewed at the same dyadic horizon, and define the same-address amplification

\[
\boxed{
\Xi_{m,H}
:=
\frac{\mu_m(S_H)}{\nu_H(S_H)}
}
\]

whenever `S_H` is nonempty.

Then

\[
|C_m\cap S_H|
=2^m\mu_m(S_H)
\le
2^{m-\delta_{\rm form}H+o(H)}\Xi_{m,H}.
\]

Consequently, for any chosen gate sequence `H=H(m)`, it is enough to prove

\[
\boxed{
\log_2\Xi_{m,H(m)}
\le
(\delta_{\rm form}-\varepsilon_m)H(m)
}
\]

with

\[
\boxed{
\varepsilon_mH(m)-m\to+\infty.
}
\]

Then

\[
|C_m\cap S_{H(m)}|<1
\]

for all sufficiently large `m`, hence the intersection is empty.

For the exponentially growing gate `H_Rhin(m)`, any fixed positive spectral gap

\[
\beta<\delta_{\rm form}
\]

is far stronger than necessary: even a gap `epsilon_m` tending to zero is sufficient provided

\[
\varepsilon_m\gg m/H_{\rm Rhin}(m).
\]

This is substantially weaker quantitatively than the old linear-horizon requirement

\[
c(\delta_{\rm form}-\beta)>1.
\]

## 7. Why gamma can leave the principal chain

The old two-exponent criterion introduced unrestricted root credit because it used terminal/maximality to certify a sufficiently long valid horizon.

The new chain obtains a long coefficient-survival horizon **before** any terminal/maximality comparison:

\[
\boxed{
\text{minimal counterexample}
\to
\text{no descent}
\to
\text{first-crossing gate}
\to
\text{coefficient-survival language}
\to
\text{same-address exclusion}.
}
\]

Therefore the unrestricted root-credit exponent `gamma` is not needed on this principal chain.

This does **not** prove `gamma=0`, and it does not invalidate the earlier two-exponent criterion. It changes its role:

- `gamma`/terminal maximality becomes a fallback or auxiliary pruning channel;
- same-address selector/survivor correlation becomes the only exponential channel that must be closed on the reorganized principal route.

## 8. Parallel proof branches after the DSD reorganization

The remaining work can now be run in parallel rather than as one long serial chain.

### Branch A — arithmetic gate audit

Verify publication-level details of the already recorded first-crossing estimate:

- mechanical-boundary/correction normalization;
- the exact global Rhin constant/exponent used in the `14.3` bound;
- endpoint strict inequalities.

At the project level the structural lemma is already present; this branch is mainly a proof-audit task.

### Branch B — same-address carry/correlation theorem

Continue the active multi-resolution two-sided carry program and bound

\[
\Xi_{m,H_*(m)}.
\]

The crucial simplification is the new scale separation:

\[
H_*(m)/m\to\infty.
\]

For large `m`, the Beatty boundary supplies order `H_*` plateau opportunities while the ternary selector contains only `m` free digits. The current carry theorem should therefore be reformulated to exploit this asymmetric scale rather than only the previous `H=O(m)` address-exhaustion regime.

### Branch C — finite middle layers

The external `2^71` computation covers `m<=43`.

The first unverified recursively sufficient layer is `m=44`. The finite coherent gate covers all `m>=44` through depth `301,993`, so the finite interval

\[
44\le m\le162
\]

can be attacked independently by exact carry certificates / finite same-address calculations without waiting for the asymptotic branch.

### Branch D — Stage-4 z=0,1 machinery

Retain the final renewal core

\[
z\in\{0,1\}
\]

as a local diagnostic and possible finite-layer accelerator.

It no longer needs to be treated as a mandatory global predecessor of the same-address theorem. A later equivalence theorem may reconnect it to the global carry descriptor, but that equivalence should not be assumed.

### Branch E — terminal/Hensel route

Keep whole-prefix maximality and `gamma` as a fallback branch. Do not delete those results; simply stop making the primary correlation proof depend on them.

## 9. DSD dependency graph

The reorganized principal chain is

\[
\boxed{
\mathcal C_m
\xrightarrow{\text{minimality}}
D_{m,H}
\xrightarrow{\text{first-crossing gate}}
S_H
\xrightarrow{\text{same-address carry}}
\varnothing.
}
\]

The parallel supporting channels are

\[
\begin{array}{c}
\text{finite coherent-ballot gate}\\
\text{two-sided carry/spectral genealogy}\\
\text{Stage-4 }z=0,1\\
\text{terminal/Hensel fallback}\\
\text{external finite verification}
\end{array}
\]

and are merged only at explicitly shared domains/horizons.

This is the useful DSD contribution here: not a new arithmetic identity, but removal of an unnecessary serial dependency and alignment of each existing theorem with the layer where it is strongest.

## 10. Audit verdict

The exploration produces a real simplification rather than a cosmetic relabeling.

1. The previously emphasized root-safe horizon `~4.294m` is not the longest available no-descent-to-coefficient-survival gate.
2. The existing first-crossing polynomial bound yields an **exponential-in-m** coefficient-survival gate on recursively sufficient starts.
3. The finite `301,993` theorem and the exponential gate form a natural envelope, with crossover at `m=163`.
4. External verification through `2^71` covers all recursively sufficient layers through `m=43`; `m=44` is exactly the first uncovered layer.
5. The global proof search can therefore be reorganized around one principal exponential obstruction: the same-integer ternary-selector / coefficient-survivor correlation.
6. The previous `gamma` branch is retained as a fallback, not discarded or falsely declared solved.
7. The Collatz conjecture remains open: the decisive same-address correlation/carry theorem is still missing.

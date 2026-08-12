# External verification frontier update and exclusion of the m=46 `1000` branch

Date: 2026-08-12

Status: **rigorous finite frontier update + exact branch exclusion obtained by combining the project’s DK/local-square defect bounds with published computational verification and the draft ternary-prefix correction budget**. This does not prove Collatz.

## 1. Published external verification floor

David Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025), reports computational verification of convergence for every positive starting integer below

\[
\boxed{2^{71}}.
\]

The author’s official project status page still lists `2^71` as the verified computational limit in its 2026-07 generated status.

The project also uses the later recursively-sufficient extension

\[
L=4\cdot3^{44}+2
\]

as a stronger finite lower floor when parameterizing a hypothetical minimal counterexample; that separate reduction is recorded in the draft branch.

## 2. Recompute the upper-CF first-crossing frontier

For a primitive upper continued-fraction first crossing with exponent pair `(A,H)`, put

\[
P=\frac{2^A}{3^H}>1.
\]

The exact Denjoy--Koksma correction bound together with `g>=4` gives

\[
\boxed{
N\le
\frac{H/(6\ln2)+1/3-4P}{P-1}.
}
\]

For the consecutive large upper convergents relevant here:

\[
(A,H)=(630,138,897,\;397,573,379)
\]

gives

\[
N_{\max}\approx9.031843916\times10^{17},
\]

and

\[
(A,H)=(10,439,860,591,\;6,586,818,670)
\]

gives

\[
\boxed{
N_{\max}\approx1.564531754\times10^{20}.
}
\]

Both lie strictly below

\[
2^{71}\approx2.361183241\times10^{21}.
\]

Therefore both upper-CF first-crossing layers are excluded by the published exhaustive convergence verification.

The next upper convergent is

\[
\boxed{
(A,H)=
(217,976,794,617,\;137,528,045,312).
}
\]

Its DK ceiling is

\[
\boxed{
N_{\max}\approx3.679778065\times10^{22},
}
\]

which is above the published verification floor.

Hence the first externally unresolved upper-CF resonance is exactly the same resonance already isolated independently in the draft branch:

\[
\boxed{
A=217,976,794,617,
\qquad
H=137,528,045,312.
}
\]

This aligns the main renewal/Christoffel route with the draft E/O-defect/recursive-core route.

## 3. Certified finite window at the new frontier

The draft rational DK certificate proves, without floating logarithms, that every paradoxical first-crossing candidate at this resonance satisfies

\[
\boxed{
x<36,797,925,187,243,805,015,225<2^{75}.}
\]

Together with recursive sufficiency, the clean search window is

\[
4\cdot3^{44}+2<x<2^{75}.
\]

The `m=46` ternary layer is parameterized by

\[
x=4\left(3^{46}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

and its high four free trits are restricted to

\[
0000,0001,0010,0011,
0100,0101,0110,0111,
1000.
\]

## 4. Universal local-square lower defect count at this resonance

Use the critical parity Sturmian word of slope

\[
\beta=1/\log_2 3.
\]

The convergents include

\[
\frac{41}{65},
\qquad
\frac{53}{84},
\qquad
\frac{306}{485}.
\]

Let `u` be the standard factor of parity length

\[
L=84
\]

with

\[
K=53
\]

odd symbols. Its affine multiplier is

\[
\frac{3^{53}}{2^{84}}
=1.002090314041086\ldots>1.
\]

The next standard word contains `u^2`, and the classical Sturmian recurrence formula gives

\[
R_\beta(168)=168-1+485+84=736.
\]

Thus every critical factor of parity length `736` contains this square.

At the current resonance, for every zero-defect odd event,

\[
x_q<2\left(N+\frac H3\right).
\]

Since `N<2^75` and `H<2^38`,

\[
2\left(N+\frac H3\right)<2^{77}<2^{84}.
\]

The local repeated-block jump lemma therefore forbids `u^2` inside any completely zero-defect interval.

If `465` consecutive odd-event coordinates had zero defect, their critical parity span would be at least

\[
\lfloor464\log_2 3\rfloor+1=736,
\]

contradiction.

Hence every zero-defect run has length at most `464`.

Let

\[
r_*:=\#\{q:h_q>0\}.
\]

Then

\[
H-r_*\le464(r_*+1),
\]

so

\[
\boxed{
r_*\ge
\left\lceil\frac{H-464}{465}\right\rceil
=295,759,237.}
\]

This lower bound applies throughout the whole next-resonance first-crossing window, independently of the ternary prefix.

## 5. Run-aware upper defect count in the `1000` branch

The independently audited defect-run theorem gives

\[
\Delta S\ge\frac5{48}r_*.
\]

The draft rational ternary-prefix budget applies this to each high free-trit prefix in the `m=46` layer.

For the largest surviving high-four prefix

\[
\boxed{1000}
\]

it gives the exact necessary upper bound

\[
\boxed{r_*\le285,942,279.}
\]

But Section 4 gives simultaneously

\[
\boxed{r_*\ge295,759,237.}
\]

Since

\[
295,759,237>285,942,279,
\]

we obtain the exact contradiction

\[
\boxed{
\text{no first-crossing candidate exists in the }m=46\text{ high-four }1000\text{ branch}.}
\]

## 6. Consequence for the previous terminal computations

The draft branch previously excluded zero, one, and two defects in the final 20 odd positions of the `1000` branch through exact ternary/discrete-log endpoint calculations.

The present global lower-vs-upper defect contradiction is stronger for branch existence: it eliminates the entire `1000` branch before terminal defect geometry is considered.

Those terminal computations remain valid independent certificates and useful models for later branches, but they are no longer needed to keep `1000` alive or dead.

## 7. What remains at the new resonance

The local-square lower bound

\[
r_*\ge295,759,237
\]

is much smaller than the run-aware upper budgets of the remaining `m=46` high-four prefixes `0000` through `0111`, whose certified upper allowances range from about `6.16` to `11.61` billion defects.

The other three recursive 44-digit affine blocks (`m=44` and the two `m=45` blocks) also remain below the current magnitude ceiling.

Therefore the next proof target is no longer the old `10,439,860,591 / 6,586,818,670` resonance and no longer the `m=46,1000` subbranch. It is the remaining recursive core at

\[
\boxed{
(A,H)=
(217,976,794,617,\;137,528,045,312)
}

subject to:

1. the exact four-block ternary parameterization;
2. the high-resolution dyadic defect-address causality theorem;
3. the universal repeated local-square requirement `r_*>=295,759,237`;
4. branch-dependent correction-loss upper budgets;
5. the ordinary-integer late-lift condition.

## External / project references

- David Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81, 810 (2025), DOI 10.1007/s11227-025-07337-0.
- Barina convergence-verification project status page, generated July 2026: verified computational limit `2^71`.
- Draft note `2026-08-09-rational-dk-next-resonance-certificate.md`.
- Draft note `2026-08-09-next-resonance-four-block-core.md`.
- Draft note `2026-08-10-rational-ternary-prefix-run-budget.md`.
- Main note `2026-08-12-local-square-jump-polylog-defect-floor.md`.

# Survivor polynomial and semiring bridge

Date: 2026-08-09

Status: **DERIVED ORGANIZING IDENTITY + ROUTE DIAGNOSTIC**

This note unifies the coefficient-survivor counting, minimal-survivor, and Fourier-transfer calculations as different evaluations of one exact residue-support object.

## 1. Survivor residue set

Let `P_K` be the set of length-`K` parity words satisfying the coefficient barrier at every prefix,

\[
3^{q_j}\ge2^j
\qquad(1\le j\le K).
\]

By the classical parity-vector bijection, every such word determines exactly one canonical residue

\[
r(w)\in\{0,1,\ldots,2^K-1\}.
\]

Let

\[
A_K=\{r(w):w\in P_K\}.
\]

The map `w -> r(w)` is injective at fixed depth, so the residue indicator has only coefficients zero or one.

## 2. Survivor polynomial

Define

\[
\boxed{
F_K(z)=\sum_{r\in A_K}z^r.
}
\]

Then three quantities already studied separately in the repository are immediate projections of `F_K`.

### Count

\[
\boxed{F_K(1)=|A_K|=|P_K|.}
\]

### Minimal survivor

For `K>=1`,

\[
\boxed{
\mu(K)=\min A_K
}
\]

is the lowest exponent appearing in `F_K`.
Equivalently, because all coefficients are nonnegative, it is the tropical / min-plus valuation of the polynomial support.

### Fourier transform

Let

\[
N=2^K,
\qquad
\omega=e^{2\pi i/N}.
\]

The unnormalized Fourier coefficient of the survivor residue indicator is

\[
\boxed{
\widehat A_K(t)=F_K(\omega^t).
}
\]

The normalized coefficient used in the current Fourier-transfer notes is

\[
\widehat\nu_K(t)=\frac{F_K(\omega^t)}{|A_K|}.
\]

Thus counting, minimum search, and Fourier cancellation are not independent models.  They are different evaluations of the same residue support.

## 3. Edge-factor representation

In the canonical lift formulation, a parity path exposes binary lift bits

\[
c_0,c_1,\ldots,c_{K-1}\in\{0,1\}
\]

and

\[
\boxed{
r(w)=\sum_{k=0}^{K-1}c_k2^k.}
\]

Therefore the path monomial factors as

\[
z^{r(w)}
=
\prod_{k=0}^{K-1}z^{c_k2^k}.
\]

The exact finite-horizon E/O transfer from `finite-horizon-minplus-transfer.md` can consequently be evaluated in several semirings using the same sparse transition skeleton:

1. **Boolean:** keep only support / reachability;
2. **natural-number:** edge weight `1`, sum path counts;
3. **polynomial:** edge weight `z^{c2^k}`, producing `F_K(z)`;
4. **min-plus:** edge cost `c2^k`, producing `mu(K)`;
5. **complex Fourier:** edge phase `exp(2 pi i t c 2^k / 2^K)`, producing `F_K(omega^t)`.

This is the clean algebraic interpretation of the E/O-channel matrix program.

## 4. Four-channel mod-32 decomposition

For `K>=5`, every coefficient survivor lies in one of

\[
A_K\subset
7+32\mathbb Z
\;\cup\;
15+32\mathbb Z
\;\cup\;
27+32\mathbb Z
\;\cup\;
31+32\mathbb Z.
\]

Hence

\[
\boxed{
F_K(z)
=
\sum_{a\in\{7,15,27,31\}}
z^a G_{K,a}(z^{32}),
}
\]

where each `G_{K,a}` has nonnegative 0/1 coefficients.

The global minimum is the minimum among the four branch valuations, exactly matching the current branch-profile computation.

## 5. Important Fourier resolution limitation

The current Fourier program has considered bounds near the generic square-root scale

\[
|\widehat\nu_K(t)|
\lesssim
|A_K|^{-1/2}.
\]

Such a bound can be a strong equidistribution statement, but **by itself it cannot certify the absence of one exceptional small residue**.

Indeed, adding or removing a single residue `r_0` changes every unnormalized Fourier coefficient by a complex number of magnitude exactly one:

\[
\widehat A_K(t)
\mapsto
\widehat A_K(t)+\omega^{tr_0}.
\]

For the normalized transform, the perturbation scale is therefore approximately

\[
\boxed{|A_K|^{-1}.}
\]

When `|A_K|` is exponentially large,

\[
|A_K|^{-1}
\ll
|A_K|^{-1/2}.
\]

Consequently, a theorem that only bounds individual Fourier magnitudes at square-root scale has insufficient resolution to distinguish a survivor set with no small residue from a nearby set differing by one small residue.

This does **not** make Fourier analysis useless.  It means that a Fourier proof of a lower bound on `mu(K)` must use additional information, for example:

- a sufficiently strong multi-frequency discrepancy theorem;
- phase correlations rather than only magnitude bounds;
- arithmetic restrictions on admissible residues;
- a certificate on a bounded interval;
- or a hybrid with the exact min-plus / canonical-lift structure.

## 6. Exact interval-count identity

For any interval `I` in `Z/NZ`, Fourier inversion gives

\[
\boxed{
|A_K\cap I|
=
\frac1N
\sum_{t=0}^{N-1}
\widehat A_K(t)
\overline{\widehat{1_I}(t)}.
}
\]

Separating the zero frequency,

\[
|A_K\cap I|
=
\frac{|A_K||I|}{N}
+
\frac1N
\sum_{t\ne0}
\widehat A_K(t)
\overline{\widehat{1_I}(t)}.
\]

Thus the exact Fourier bridge to a small-residue theorem is an **interval-count certificate**, not merely decay of a few fixed frequencies.

If the right-hand side can be proved strictly smaller than one in absolute upper bound while the count is nonnegative integral, then the interval is empty.
The difficulty is obtaining sufficiently strong control over the weighted nonzero-frequency sum.

## 7. Consequence for current proof routes

The repository now has three exact representations of the same object:

\[
\boxed{
\text{survivor support}
\longleftrightarrow
F_K(z)
\longleftrightarrow
\begin{cases}
\text{count},\\
\text{min-plus minimum},\\
\text{Fourier values}.
\end{cases}
}
\]

The min-plus route directly targets the lowest occupied exponent and therefore has the correct resolution for `mu(K)`.
The Fourier route can still provide a powerful global distribution input, but a square-root-scale magnitude theorem alone should no longer be treated as a sufficient downstream target for excluding a single polynomial-size candidate.

The safe next hybrid target is to use Fourier or transfer estimates to certify **blocks of endpoint/carry states** that cannot contain a low-cost min-plus path, with final exclusion performed by the exact finite-horizon quotient.

# DSD cylinder-transition audit: Q=7 -> 8 -> 9

Date: 2026-08-25

## Purpose

The previous audit isolated a scale-separated symbolic reverse rule.  The next question is not whether the global survivor total decreases, but whether **every surviving low-ternary cylinder contracts when the ternary resolution is refined**.

This is the finite transition-operator test needed before attempting a recursive proof.

Parameters held fixed:

- canonical `m=44` ternary-selector core,
- `Bmax=20`,
- `Kmax=36`,
- nested root-fullmax depth `H=24` for the combined filter.

The scale-separation inequality is valid at Q=7,8,9.  The reverse-correction bounds are

- Q7: `78,794,979,080,474,198,016`
- Q8: `236,384,937,241,422,594,048`
- Q9: `709,154,811,724,267,782,144`

all below

`Nmin = 3,939,083,608,734,444,931,527`.

Therefore the same coefficient-sign reverse rule is exact at all three resolutions.

## Exact global survivor counts

### Q=7

Cross-place only:

`1,155,412,831,747`

Cross-place intersected with root-fullmax H24:

`784,787,338,151`

### Q=8

Cross-place only:

`553,606,034,398`

Cross-place intersected with root-fullmax H24:

`373,717,485,431`

Combined survivor fraction of the full `2^44` core:

`0.0212433795599622` = about `2.12434%`.

### Q=9

Cross-place only:

`374,105,911,439`

Cross-place intersected with root-fullmax H24:

`254,500,051,362`

Combined survivor fraction:

`0.0144666530196673` = about `1.44667%`.

Thus the safe finite exclusion fraction reaches about `98.5533%` at Q9/B20/H24.

## Parent -> child transition test

A Q-level cylinder is indexed by the low selector mask `a_0,...,a_(Q-1)`.

When Q is increased by one, every parent mask has exactly two child masks, according to the new selector digit.

For each parent, we compared

`(survivors in its two Q+1 children) / (survivors in the Q parent)`.

This is stronger than comparing global totals because it checks the **worst cylinder**.

## Q7 -> Q8

Cross-place transition ratio:

- minimum: `0.20200514484611573`
- maximum: `0.7353826587072224`

The worst cross-place parent is mask `116`.

Combined cross-place + root-H24 transition ratio:

- minimum: `0.2043849101421026`
- maximum:

\[
\boxed{\rho_7=0.7274757109901708<1}
\]

The worst combined parent is also mask `116`.

Therefore **all 128 Q7 parents contract strictly** when refined to Q8 under the combined safe filter.

Global ratios are

- cross-place: `0.47914132437056295`
- combined: `0.4762022362790638`.

## Q8 -> Q9

Cross-place transition ratio:

- minimum: `0.4181723169169933`
- maximum: `0.9246817045801337`

Combined transition ratio:

- minimum: `0.42551145854794387`
- maximum:

\[
\boxed{\rho_8=0.9330214834722416<1}
\]

The worst parent is mask `167`.

Therefore **all 256 Q8 parents also contract strictly** when refined to Q9.

Global ratios are

- cross-place: `0.6757619826991386`
- combined: `0.6809958358477415`.

## Interpretation

This is the first finite result in the current line that has the shape needed for a recursive theorem:

\[
\forall\text{ parent cylinders }C,
\qquad
\mu(S_{Q+1}\cap C)\le \rho_Q\,\mu(S_Q\cap C),
\qquad \rho_Q<1.
\]

At the two tested transitions,

\[
\rho_7\approx0.72748,
\qquad
\rho_8\approx0.93302.
\]

So the contraction is not merely an average phenomenon.

However, the margin weakens at Q8->Q9.  Therefore we do **not** yet have a Q-independent constant `rho<1`.  A single later transition with ratio 1 would defeat a one-step uniform-contraction proof, although a bounded multi-step contraction theorem could still survive.

## DSD reading

The logical chain is now:

1. low ternary selector mask = describable cylinder;
2. dyadic/ternary residues = finite state coordinates;
3. scale separation = removal of irrelevant absolute-magnitude detail;
4. root/forward/reverse rules = admissible state eliminations;
5. parent-to-child survivor mass = transition operator;
6. worst-row contraction `rho_Q` = closure quantity.

The central proof target is therefore no longer a raw survivor count.  It is a bound on the norm of the survivor transition operator.

A sufficient eventual theorem would be either:

### One-step form

There exist `Q0` and `rho<1` such that for every `Q>=Q0`, every Q-cylinder satisfies

\[
\mu(S_{Q+1}\cap C)\le\rho\,\mu(S_Q\cap C).
\]

### Bounded-block form

There exist fixed `r>=1` and `rho<1` such that every surviving Q-cylinder contracts after at most `r` further selector digits:

\[
\mu(S_{Q+r}\cap C)\le\rho\,\mu(S_Q\cap C).
\]

The bounded-block form is the more robust next target because the observed one-step margin is not stationary.

## Next exact boundary

For `m=44`, `Bmax=20`, `Kmax=36`, the scale-separated correction bound remains valid through Q=10:

\[
2^{55}3^{10}=2,127,464,435,172,803,346,432<N_{\min}.
\]

At Q=11 the simple bound exceeds `Nmin`, so either the full correction comparison must be restored or the ternary depth `m` must be increased.

Therefore Q9->Q10 is the next natural finite transition test before changing scale.

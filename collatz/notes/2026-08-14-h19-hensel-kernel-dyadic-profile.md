# Fixed-Hensel dyadic kernel profile of the hard `H_19` fibre

Date: 2026-08-14

Status: **exact finite fibre enumeration and mixed-place kernel certificate**.  This is a small-block model of the full gate boundary problem.  It identifies how fixing progressively more 3-adic correction digits collapses the remaining dyadic address freedom.  It is not a Collatz proof.

## 1. Hard mechanical block

Use

\[
H_{19}=1101101101011011010,
\]

which has twelve mechanical odd symbols.

For an actual length-19 orientation `v`, let `(Sigma,M)` be its relative-height state against `H_19`, let `R_v` be its affine correction, and let

\[
\rho_v=[-3^{-q}R_v]_{2^{19}}
\]

be its canonical block start residue for its fixed odd count `q`.

Two fibres are enumerated exactly:

- neutral: `(Sigma,M)=(0,0)`, `q=12`;
- one-slack: `(Sigma,M)=(-1,-1)`, `q=11`.

Their exact sizes are

\[
\boxed{|\mathcal F_0|=2652,}
\qquad
\boxed{|\mathcal F_{-1}|=11433.}
\]

## 2. Fixed-Hensel kernel

For a Hensel depth `J`, partition a fibre by

\[
R_v\pmod{3^J}.
\]

Inside one class, define the dyadic kernel differences

\[
\rho_u-\rho_v\pmod{2^{19}}.
\]

The union over all equal-Hensel classes is denoted `K_J`.

This is the exact finite version of the full-gate question:

> after a correction target has been fixed through `J` ternary digits, how much dyadic-address motion is still available without changing those Hensel digits?

## 3. Neutral fibre profile

Every neutral orientation begins with the mandatory `11`, so every dyadic kernel difference is divisible by four.  Normalize by this forced factor and view

\[
(\rho_u-\rho_v)/4\pmod{2^{17}}.
\]

The exact profile is

\[
\boxed{
\begin{array}{c|r|r|r|r}
J&\#\text{Hensel classes}&\max\text{ class size}&|K_J|&\text{full normalized low bits}\\\hline
1&2&1499&107821&14\\
2&6&961&36195&13\\
3&18&477&11885&12\\
4&50&181&3777&10\\
5&127&86&1273&9\\
6&292&31&401&8\\
7&589&17&115&6\\
8&1048&8&39&5\\
9&1619&4&9&3\\
10&2234&2&3&1\\
11&2652&1&1&0
\end{array}
}
\]

At `J=10`, the raw dyadic kernel is exactly

\[
\boxed{
\{0,116508,407780\}
\pmod{2^{19}},
}
\]

where the two nonzero elements are negatives of one another.

At

\[
\boxed{J=11}
\]

the correction map is injective on the entire neutral fibre: fixing eleven Hensel digits fixes the orientation, and therefore the dyadic block, uniquely.

## 4. One-slack fibre profile

The one-slack fibre does not have the mandatory low factor four, so use raw dyadic differences modulo `2^19`.

The exact table is

\[
\boxed{
\begin{array}{c|r|r|r|r}
J&\#\text{Hensel classes}&\max\text{ class size}&|K_J|&\text{full low dyadic bits}\\\hline
1&2&6457&514195&16\\
2&6&4073&191853&15\\
3&18&1977&63075&14\\
4&54&744&20935&12\\
5&150&341&7021&11\\
6&389&122&2305&10\\
7&921&64&761&8\\
8&1933&29&243&7\\
9&3633&13&83&6\\
10&5989&6&23&4\\
11&8818&3&7&2\\
12&11433&1&1&0
\end{array}
}
\]

At the full odd-count depth

\[
J=q=11,
\]

the kernel is exactly

\[
\boxed{
K_{11}
=\{0,\pm1,\pm2,\pm4\}
\pmod{2^{19}}.
}
\]

At `J=12` the correction residue is injective on the fibre.

## 5. Full-Hensel kernel equals the integer-credit channel

For two same-length, same-odd-count orientations,

\[
\rho_u-\rho_v
\equiv
-3^{-q}(R_u-R_v)
\pmod{2^L}.
\]

If they lie in the same full Hensel class modulo `3^q`, write

\[
R_u-R_v=3^q\Delta.
\]

Then

\[
\boxed{
\rho_u-\rho_v\equiv-\Delta\pmod{2^L}.
}
\]

Thus the dyadic kernel at `J=q` is literally the set of ordinary integer predecessor credits, with sign reversed.

For the hard neutral `H_19` fibre there is no nonzero `J=12` kernel, hence no immediate same-state integer credit.

For the one-slack fibre, the exact positive credits are

\[
\boxed{\Delta\in\{1,2,4\}.}
\]

This explains why a small positive incoming slack can create local predecessor relations while the neutral hard phase does not.

## 6. Mixed-place interpretation

The tables show a sharp tradeoff:

- at shallow Hensel depth, the same correction class can still move many low dyadic bits;
- every additional ternary digit reduces the kernel;
- near the full odd-count depth, only a tiny discrete credit set remains;
- one more ternary digit makes the local correction map injective.

Therefore Hensel and dyadic freedom are not independent marginal resources.  The relevant renormalized state is the **kernel profile** over a fixed Hensel target.

The gate-wide explicit cube of the companion theorem provides a large cross-base *section*.  The present `H_19` computation demonstrates what must additionally be controlled for a proof: the dyadic image of the full Hensel fibre, including its kernel beyond that section.

## 7. Proof-program consequence

At a large Euclidean gate the low Hensel digits supplied by the explicit pair cube should be viewed as the flexible tail.  The unresolved information lies in the remaining high Hensel digits and in the kernel of the map from full same-state orientations to those low digits.

The immediate next invariant is therefore

\[
\boxed{
\mathcal K_J(\text{gate state})
=
\{\Delta\rho:\Delta R\equiv0\pmod{3^J}\}.
}
\]

A terminal boundary theorem must show that, after the early first-defect channel and the ordinary zero-lift target are imposed, the required dyadic correction is outside this kernel image for the relevant high Hensel target.
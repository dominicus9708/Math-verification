# Adaptive reverse edge rarity and the fixed-slack barrier

Date: 2026-08-25

## Status

Safe reverse-code counting theorem plus an exact finite DP audit through `Q=14`.

This is a proof-strategy barrier / transversality diagnostic.  No Collatz proof is claimed.

## 1. Reverse potential and the threshold resolution

For an odd-to-odd reverse code with

- `r` inverse odd events,
- positive inverse exponents `a_1,...,a_r`,
- total binary exponent

\[
K=\sum_{j=1}^r a_j\ge r,
\]

define

\[
\Lambda=\frac{3^r}{2^K}.
\]

To attack a forward surplus scale `d`, first use the coarse threshold

\[
\Lambda>3^d.
\]

Define the first ternary resolution at which this is even possible:

\[
\boxed{
Q_*(d)=\min\left\{Q\ge1:\left(\frac32\right)^Q>3^d\right\}.
}
\]

The first values are

\[
Q_*(1)=3,
\quad
Q_*(2)=6,
\quad
Q_*(3)=9,
\quad
Q_*(4)=11,
\quad
Q_*(5)=14.
\]

## 2. Edge-rarity theorem

At the exact threshold resolution `Q=Q_*(d)`, suppose a reverse code satisfies

\[
\Lambda>3^d.
\]

Because `r<=Q`, if `r<Q` then

\[
\Lambda
\le
\left(\frac32\right)^r
\le
\left(\frac32\right)^{Q_*(d)-1}
\le
3^d,
\]

a contradiction.

Hence

\[
r=Q_*(d).
\]

Now minimality of `Q_*(d)` gives

\[
\left(\frac32\right)^{Q_*(d)}
\le
\frac32\,3^d
<2\,3^d.
\]

If `K>=Q_*(d)+1`, then

\[
\Lambda
\le
\frac12\left(\frac32\right)^{Q_*(d)}
<3^d,
\]

again impossible.

Therefore

\[
\boxed{r=K=Q_*(d)}.
\]

Since every inverse exponent is at least one, this forces

\[
\boxed{a_1=\cdots=a_{Q_*}=1}.
\]

Repeated `a=1` inversion is possible through depth `Q_*` for exactly one endpoint residue:

\[
\boxed{z\equiv-1\pmod{3^{Q_*}}}.
\]

Thus among the `2\cdot3^{Q_*-1}` endpoint residues not divisible by 3, the favorable fraction at the first possible adaptive resolution is exactly

\[
\boxed{
\frac{1}{2\cdot3^{Q_*(d)-1}}.
}
\]

This tends rapidly to zero as `d` grows.

## 3. Exact finite confirmation

The compressed reverse-potential DP was rebuilt independently through `Q=14` with exact integer comparisons.

At the threshold points it gives:

| surplus threshold | `Q_*(d)` | favorable residues | admissible residues | fraction |
|---:|---:|---:|---:|---:|
| `3^1` | 3 | 1 | 18 | 0.0555555556 |
| `3^2` | 6 | 1 | 486 | 0.00205761317 |
| `3^3` | 9 | 1 | 13,122 | 0.0000762078951 |
| `3^4` | 11 | 1 | 118,098 | 0.00000846754390 |
| `3^5` | 14 | 1 | 3,188,646 | 0.000000313612737 |

In every case the unique favorable residue is the all-`a=1` class

\[
z=-1\pmod{3^Q}.
\]

The finite certificate also records all strict counts for thresholds

\[
1,3,9,27,81,243
\]

at every `Q<=14`.

The truncation `KMAX=24` is exact for these strict positive-potential counts: for `Q<=14`, any `K>=23` satisfies

\[
\frac{3^r}{2^K}
\le
\frac{3^{14}}{2^{23}}
<1.
\]

## 4. Fixed additive slack theorem

Now allow

\[
Q=Q_*(d)+c,
\]

where `c>=0` is additive resolution slack.

Write

\[
h=Q-r,
\qquad
K=r+e,
\qquad e\ge0.
\]

If `h>=c+1`, then `r<=Q_*(d)-1`, so the code cannot beat `3^d` by the definition of `Q_*`.

Therefore every favorable code must satisfy

\[
0\le h\le c.
\]

Furthermore,

\[
\frac{3^r}{2^{r+e}}>3^d
\]

and the minimality estimate

\[
\frac{(3/2)^{Q_*}}{3^d}\le\frac32
\]

imply

\[
\boxed{
2^e<\left(\frac32\right)^{c-h+1}.
}
\]

For fixed `(c,h)`, let `E(c,h)` be the largest integer satisfying this inequality.

For fixed `r,e`, the number of positive exponent strings with total excess `e` is

\[
\binom{r+e-1}{e}.
\]

Each exponent string determines at most one endpoint residue modulo `3^r`, and therefore at most

\[
3^h
\]

lifts modulo `3^Q`.

Hence the number `G(d,c)` of potentially favorable residues obeys the safe union bound

\[
\boxed{
G(d,c)
\le
\sum_{h=0}^{c}
3^h
\sum_{e=0}^{E(c,h)}
\binom{Q-h+e-1}{e}.
}
\]

For every fixed `c`, all `E(c,h)` are fixed constants.  The numerator is therefore only polynomial in `Q_*(d)`, whereas the number of admissible residues is

\[
2\cdot3^{Q-1}.
\]

Consequently

\[
\boxed{
\frac{G(d,c)}{2\cdot3^{Q-1}}
\longrightarrow0
\qquad(d\to\infty)
}
\]

for every fixed additive slack `c`.

Thus replacing `Q_*(d)` by `Q_*(d)+1`, `Q_*(d)+2`, or any other fixed additive margin cannot yield a uniform positive residue density.

## 5. A stronger sublinear-slack consequence

Since

\[
E(c,h)<c+1,
\]

a crude version of the preceding union bound is

\[
G(d,c)
\le
(c+1)^2\,3^c\,(Q+c)^c.
\]

Therefore, if the additive slack is allowed to grow but still satisfies

\[
\boxed{
c=o\!\left(\frac{Q}{\log Q}\right),}
\]

then

\[
\log G=o(Q),
\]

while the admissible residue count has logarithm asymptotic to `Q log 3`.

Hence even in this wider regime,

\[
\boxed{
\frac{G(d,c)}{2\cdot3^{Q-1}}\to0.
}
\]

This is only a **necessary scale warning** for any proof that requires a uniform positive fraction of favorable residues.  It does not say that slack of order `Q/log Q` is sufficient.

## 6. Comparison with the stopped-tree dimension barrier

This obstruction is distinct from the earlier stopped-tree energy dimension barrier.

The stopped-tree calculation concerns the intersection of

- the ternary selector dimension, and
- the binary coefficient-survival language.

The present theorem appears one layer earlier.  It says that even before intersecting with the selector, the reverse mechanism is arithmetically sparse when `Q` is chosen only near the coefficient threshold.

Thus the two barriers should not be conflated:

1. **reverse edge rarity:** near-minimal adaptive reverse resolution has too few strong residue classes for a uniform-density argument;
2. **selector dimension barrier:** generic same-integer intersection is too weak for the stopped-tree energy criterion.

A successful cross-place theorem must overcome both, or avoid relying on uniform density altogether.

## 7. Consequence for the current proof architecture

The naive adaptive plan

\[
Q\approx2.7095d+O(1)
\]

is now ruled out as a source of a uniform positive transversality fraction.

The surviving routes are narrower:

- allow genuinely growing resolution slack and analyze its entropy cost;
- prove arithmetic correlation forcing the actual minimal-counterexample residue into the rare strong reverse classes more often than generic density predicts;
- or combine the reverse mechanism with a different root-global minimality condition so that uniform residue density is not required.

The fact that the hard-core condition can give `Q=o(q)` on a subsequence is still useful: the rarity may be subexponential in the full odd-event depth.  Therefore this negative result does not close the adaptive route completely; it specifies the strength the missing cross-place theorem must have.

## 8. Reproducibility

Exact reverse DP:

`collatz/src/dsd_reverse_edge_rarity_q14_certificate.cpp`

Expected final line:

`PASS`

Fixed-slack union-bound certificate:

`collatz/src/dsd_reverse_fixed_slack_union_bound_certificate.py`

Expected final line:

`PASS`

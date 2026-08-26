# First global resonance: compressed terminal Hensel ladder to ten defects

Date: 2026-08-26

Status: **exact finite theorem** in the repaired first-global-resonance branch. It strengthens the terminal low-support ladder without using the disputed ternary recursively-sufficient selector, repeated L7/L14 pullback, random sampling, floating point, or an independence assumption. It does **not** prove the Collatz conjecture.

## 1. Setup

At the repaired first global binary resonance

\[
(A_0,Q_0)=(114208327604,72057431991),
\]

for a final-\(m\) odd-ordinal window define

\[
B_t=b_{Q_0-m+1+t},\qquad
\delta_t=B_t-a_{Q_0-m+1+t}\ge0,
\qquad 0\le t<m.
\]

The endpoint is

\[
 y=2^{-A_0}\sum_{t=0}^{m-1}3^{m-1-t}2^{B_t-\delta_t}\pmod{3^m},
\]

and every admissible endpoint is the ordinary integer satisfying

\[
2^{71}<y,
\qquad
3y<4\cdot2^{71}+3\cdot2^{33},
\qquad
y\equiv3\pmod4.
\]

Ordering gives

\[
\delta_t\le\delta_{t-1}+(B_t-B_{t-1})-1.
\]

Hence every positive run that starts after a zero begins with \(\delta=1\) across a mechanical gap 2.

## 2. Initial positive-run compression

The only apparent large Cartesian factor comes from an initial positive run

\[
\delta_0,\ldots,\delta_{L-1}>0.
\]

Let

\[
q=3^{m-L}.
\]

Its total endpoint correction is a multiple of \(q\). After division by \(q\), the last coordinate \(t=L-1\) has a unit coefficient modulo \(3^L\), and

\[
\delta_{L-1}\pmod{2\cdot3^{L-1}}
\]

runs through one full period of the primitive root 2 modulo \(3^L\).

Therefore

\[
2^{-\delta_{L-1}}
\]

runs through all units modulo \(3^L\). Its normalized contribution is an affine image of those units and consequently occupies **exactly two of the three residue classes modulo 3**, with every lift inside those two classes represented.

All earlier coordinates of the same initial run contribute multiples of 3 after the same normalization, so they do not enlarge this set. Conversely any selected residue tuple has positive ordered representatives because the earlier coordinates can be increased by their periods with no left boundary.

Thus the huge product

\[
\prod_{t=0}^{L-1}(2\cdot3^t)
\]

is replaced, for existence testing, by one exact mod-3 membership test.

For the horizons used here, the admissible ordinary endpoint interval lies below \(q\). If the finite later-run contribution gives

\[
z=y_{\rm mech}+C_{\rm later}\pmod{3^m},
\]

then the ordinary endpoint is forced to be

\[
y=z\bmod q,
\]

and the required initial normalized correction is

\[
h\equiv-\left\lfloor z/q\right\rfloor\pmod{3^L}.
\]

The initial run exists exactly when \(h\) lies in its two allowed mod-3 classes.

This is the compressed triangular/Hensel join used below.

## 3. Six defects at m=58 and the jump to eight defects

The previously certified theorem already gives

\[
D_{\rm tail}(58)\ge6.
\]

The exact six-defect equality layer at \(m=58\) has

\[
3,188,310
\]

compressed finite sequences and exactly one endpoint-compatible class. It is represented by

\[
\operatorname{supp}(\delta)=(0,2,17,18,47,57),
\qquad
\delta=(1,1,1,1,1,1),
\]

with

\[
y=2704820911452840622043.
\]

It extends mechanically to \(m=59\) but fails at \(m=60\).

Therefore support six is absent at \(m=60\). The complete exact support-seven layer at \(m=60\) contains

\[
25,581,232
\]

compressed finite sequences and has no admissible class. Hence

\[
\boxed{D_{\rm tail}(60)\ge8.}
\]

## 4. Eight defects disappear by m=64

Because the final 60 ordinals already require at least eight defects, every final-64 description with fewer than eight defects is impossible by restriction.

It remains only to test exact support eight at \(m=64\). The compressed enumeration contains

\[
203,183,093
\]

finite sequences and no admissible endpoint class. Therefore

\[
\boxed{D_{\rm tail}(64)\ge9.}
\]

For reference, at \(m=60\) the exact support-eight layer is not empty: two compressed structures survive. One disappears immediately after one left extension and the other survives through \(m=63\), then fails at \(m=64\). Thus the jump at \(m=64\) is an exact Hensel-resolution effect, not an assumption of monotone equality classes.

## 5. Unique nine-defect equality at m=64

The complete exact support-nine layer at \(m=64\) contains

\[
\boxed{1,023,618,344}
\]

compressed finite sequences.

Exactly one class survives. In local terminal coordinates its support is

\[
\boxed{
(0,6,25,27,34,51,53,56,61)
}
\]

and its finite later displacements are all 1. The initial coordinate is the unique compatible parity class; its ordinary representative \(\delta_0=1\) gives

\[
\boxed{y=2556679481397564529951.}
\]

## 6. The unique nine-defect class does not lift to m=65

At \(m=65\), a hypothetical support-nine candidate cannot place a new defect in the newly prepended coordinate, because its restriction to the final 64 coordinates would then have support eight, contradicting

\[
D_{\rm tail}(64)\ge9.
\]

Hence the new coordinate must be mechanical and the final-64 restriction must equal the unique nine-defect class above.

The old \(t=0\) defect is now preceded by a zero. The relevant mechanical gap is 2, so ordering forces

\[
\delta=1
\]

there. There is therefore only one possible ordinary Hensel lift. Its exact endpoint residue modulo \(3^{65}\) is outside the admissible ordinary endpoint channel.

Thus no support-nine description exists at \(m=65\), and

\[
\boxed{D_{\rm tail}(65)\ge10.}
\]

## 7. Combination with the 72-step prefix theorem

The independent early boundary theorem gives

\[
D_{72}\ge11.
\]

The earliest ordinal in the final-65 terminal window lies far beyond position 72, so the two displaced supports are disjoint. Therefore every remaining hypothetical first-resonance candidate satisfies

\[
\boxed{r_*\ge11+10=21.}
\]

Using only the coarse charge greater than \(1/12\) per displaced ordinal gives

\[
\boxed{
\frac{E}{3^{Q_0}}>\frac{21}{12}=\frac74.
}
\]

The support lower bound is the main result; this correction bound is only a corollary.

## 8. DSD audit reading

The terminal state now obeys a stricter formation ladder:

\[
D_{\rm tail}(46)\ge2
\to
D_{\rm tail}(50)\ge3
\to
D_{\rm tail}(52)\ge4
\to
D_{\rm tail}(56)\ge5
\to
D_{\rm tail}(58)\ge6
\to
D_{\rm tail}(60)\ge8
\to
D_{\rm tail}(64)\ge9
\to
D_{\rm tail}(65)\ge10.
\]

The notable point is that raising 3-adic resolution repeatedly destroys low-support descriptions of the same global ordinal-transport vector. No independence between the early and late descriptions is assumed; the early dyadic and late 3-adic constraints are separate projections of one common state.

## 9. Audit classification and next target

This is a finite theorem inside the repaired first-global-resonance branch. It is not an asymptotic closure and not a proof of the Collatz conjecture.

The next equality layer is support ten. A direct full Cartesian scan is unnecessary. The correct next implementation is to reuse the compressed initial-run lemma and split the support-ten layer by how many defects occur in the newly exposed left block, so that the already-proved lower bounds on the last 60 and last 64 coordinates prune impossible branches before modular enumeration.

Companion exact certificate:

`collatz/src/first_resonance_terminal_compressed_hensel_ladder_certificate.cpp`.

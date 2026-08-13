# Deterministic plateau cube--slack dichotomy

Date: 2026-08-13

Status: **exact all-word combinatorial theorem**. Every Beatty coefficient-survival boundary word must carry either linearly many deterministic Fourier-cube coordinates or linearly many positive-slack coordinates. Unlike the exponential-prevalence theorem, this statement applies to every individual candidate. It is not a Collatz proof.

## 1. Setup

Put

\[
\alpha:=\log_3 2>1/2,
\qquad
b_t:=\lceil\alpha t\rceil.
\]

For a boundary word `w` of length `L`, define

\[
q_t(w)=\sum_{i=0}^{t-1}w_i,
\qquad
s_t(w):=q_t(w)-b_t\ge0,
\]

with

\[
q_L(w)=b_L.
\]

Let

\[
P_L:=\{0\le j\le L-2:b_{j+1}=b_j\}
\]

be the deterministic plateau starts.

Since `alpha>1/2`, plateau starts are pairwise nonadjacent, and

\[
\boxed{|P_L|=(L-1)-b_{L-1}=(1-\alpha)L+O(1).}
\]

For `j in P_L`, call the pair `(w_j,w_{j+1})` **mixed** if its sum is one.

Let

\[
M_L(w):=\#\{j\in P_L:w_j+w_{j+1}=1\}.
\]

Let

\[
S_L^+(w):=\#\{0\le t\le L-1:s_t(w)>0\}.
\]

## 2. Nonmixed `11` forces a positive-slack witness

Fix `j in P_L` and suppose

\[
w_jw_{j+1}=11.
\]

At time `j`,

\[
q_j\ge b_j.
\]

Because `j` is a plateau start,

\[
b_{j+1}=b_j.
\]

After the first one,

\[
s_{j+1}
=q_j+1-b_{j+1}
\ge1.
\]

Thus every nonmixed `11` plateau pair gives the distinct witness time

\[
\boxed{t=j+1}
\]

with positive slack.

## 3. Nonmixed `00` forces a positive-slack witness

Now suppose

\[
w_jw_{j+1}=00.
\]

Two consecutive Beatty plateaus are impossible because `2 alpha>1`. Hence

\[
b_{j+2}=b_{j+1}+1=b_j+1.
\]

After the two zeroes,

\[
q_{j+2}=q_j.
\]

Survival at time `j+2` requires

\[
q_j=q_{j+2}\ge b_{j+2}=b_j+1.
\]

Therefore

\[
\boxed{s_j=q_j-b_j\ge1.}
\]

So every nonmixed `00` plateau pair gives the distinct witness time

\[
\boxed{t=j}
\]

with positive slack.

## 4. Witnesses from different plateau pairs are distinct

The plateau pairs `(j,j+1)` are disjoint. Their witness times lie inside their own pairs:

- `00` uses `j`;
- `11` uses `j+1`.

Hence different nonmixed plateau pairs produce different positive-slack witness coordinates.

Therefore

\[
\boxed{
S_L^+(w)
\ge
|P_L|-M_L(w).
}
\]

Equivalently,

\[
\boxed{
M_L(w)+S_L^+(w)
\ge|P_L|.
}
\]

This holds for **every** coefficient-survival boundary word.

## 5. Linear deterministic dichotomy

From `max(x,y) >= (x+y)/2`,

\[
\boxed{
\max\{M_L(w),S_L^+(w)\}
\ge\frac{|P_L|}{2}.
}
\]

Thus every boundary word satisfies at least one of

\[
\boxed{
M_L(w)
\ge
\frac{1-\alpha}{2}L+O(1),
}
\]

or

\[
\boxed{
S_L^+(w)
\ge
\frac{1-\alpha}{2}L+O(1).
}
\]

Numerically,

\[
\boxed{
\frac{1-\log_3 2}{2}
\approx0.1845351232.
}
\]

## 6. Interpretation of the two branches

### Cube-rich branch

If `M_L` is large, the deterministic plateau-pair cube theorem supplies linearly many independent `01/10` Boolean coordinates. The Fourier contribution of each fiber is an exact inverse-power-of-three cosine product.

This is the natural branch for the spectral-complementarity argument.

### Slack-rich branch

If `S_L^+` is large, the word spends linearly many time coordinates strictly above the mechanical Beatty barrier.

This is the natural branch for the existing skew/defect, phase-slack cost, dyadic-address, and local backtrace machinery.

Hence the proof program does not need a probabilistic statement saying that a generic word is cube-rich. An exceptional word with few cube coordinates is automatically pushed into the defect-rich channel.

## 7. Relation to DSD-style channel decomposition

The boundary language has acquired an exact exhaustive two-channel partition:

\[
\boxed{
\text{many freely reorientable local coordinates}
\quad\text{or}\quad
\text{many positive-slack coordinates}.
}
\]

Both channels are standard mathematical objects:

- the first is a disjoint hypercube/fourier-factor channel;
- the second is a ballot-height/defect channel.

No candidate is discarded merely by density or probability: every individual boundary word is forced into at least one mathematically controlled branch.

## 8. Next target

A terminal use would prove one of the following uniformly:

1. **cube branch:** linearly many deterministic cube factors force enough Fourier cancellation outside a sparse arithmetic frequency family;
2. **slack branch:** linearly many positive-slack witnesses force an incompatible Archimedean defect budget, dyadic lift pattern, or smaller-predecessor condition.

The spectral-exception splitting lemma then permits the two branches to cover each other's exceptional sets.

# First Euclidean renormalization of the Beatty boundary into a block bridge

Date: 2026-08-13

Status: **exact combinatorial bijection / renormalization theorem**. The time-expanded coefficient-survival boundary of length `L` is compressed to an `H`-step nonnegative bridge whose deterministic block-type word is the next Sturmian word in the continued-fraction / Euclidean hierarchy. The deterministic plateau-pair cube appears exactly as the multiplicity-two neutral transition of one block type. This is not a proof of Collatz.

## 1. Time-expanded mechanical word

Put

\[
\alpha:=\log_3 2\in(1/2,1),
\qquad
b_t:=\lceil\alpha t\rceil.
\]

At a first-crossing boundary prefix of length `L`, assume

\[
H=b_L.
\]

The mechanical time word is

\[
\boxed{m_t=b_{t+1}-b_t\in\{0,1\}}
\qquad(0\le t<L).
\]

It contains exactly `H` ones and `L-H` zeros.

Because `alpha>1/2`, two zeros cannot be consecutive:

\[
\boxed{00\text{ never occurs in }m.}
\]

In the current first-crossing geometry the last mechanical bit is one, so every zero has a following one inside the prefix.

## 2. Canonical block decomposition

Pair every mechanical zero with the one immediately following it:

\[
\boxed{A:=01.}
\]

All remaining unpaired mechanical ones become singleton blocks

\[
\boxed{B:=1.}
\]

Since the zeros are isolated, the `A` blocks are disjoint and this parsing is unique.

Every block contains exactly one mechanical one. Therefore the number of blocks is exactly

\[
\boxed{H.}
\]

The block counts are

\[
\boxed{N_A=L-H,}
\]

\[
\boxed{N_B=H-(L-H)=2H-L.}
\]

## 3. Actual word and block-height increments

Let `w` be any binary word on the same time positions and define the usual Beatty slack

\[
s_t=q_t(w)-b_t.
\]

On one `A=01` mechanical block, the actual two bits can be

\[
00,\quad01,\quad10,\quad11.
\]

Relative to the one mechanical one in the block, their net one-count increments are

\[
\boxed{
00\mapsto-1,
\qquad
01\mapsto0,
\qquad
10\mapsto0,
\qquad
11\mapsto+1.
}
\]

Thus an `A` block has step alphabet

\[
\boxed{-1,0,+1}
\]

with multiplicities

\[
\boxed{1,2,1.}
\]

On a singleton `B=1` block, the actual bit is `0` or `1`, giving

\[
\boxed{0\mapsto-1,
\qquad
1\mapsto0,}
\]

so a `B` block has step alphabet

\[
\boxed{-1,0}
\]

with multiplicities `1,1`.

## 4. Exact equivalence of survival conditions

Let

\[
\Delta_r
:=
(\text{number of actual ones in block }r)-1
\]

and define the block-height process

\[
\boxed{
S_k:=\sum_{r=0}^{k-1}\Delta_r,
\qquad S_0=0.
}
\]

At every block boundary, `S_k` is exactly the original Beatty slack `s_t`.

It remains to check internal points of an `A` block. Its mechanical bits are `01`.

- `00`: the first position leaves the slack unchanged; the possible decrease occurs only at the block end.
- `01`: slack is unchanged throughout.
- `10`: slack first increases by one and returns to its previous value at block end.
- `11`: slack first increases by one and ends one higher.

Therefore, if the slack is nonnegative at the beginning and end of every block, it is automatically nonnegative at the internal point.

For `B` there is no internal point.

Hence

\[
\boxed{
q_t(w)\ge b_t\text{ for every }1\le t\le L
\iff
S_k\ge0\text{ for every }1\le k\le H.
}
\]

If `w` lies on the terminal boundary, `q_L=H`, so

\[
\boxed{S_H=0.}
\]

Thus the full Beatty boundary language is exactly a weighted nonnegative bridge of length `H`.

## 5. The plateau hypercube becomes a neutral-step orientation bit

On an `A` block, the two zero-increment realizations are

\[
01\quad\text{and}\quad10.
\]

Therefore every neutral `A` step has one exact internal Boolean orientation coordinate.

This is precisely the deterministic plateau-pair cube found earlier. In the renormalized bridge it is no longer an auxiliary construction: it is the multiplicity-two coefficient of the neutral transition.

The local transition polynomial of an `A` block is

\[
\boxed{z^{-1}+2+z,}
\]

while that of a `B` block is

\[
\boxed{z^{-1}+1.}
\]

The nonnegative-bridge constraint supplies the boundary truncation at height zero.

## 6. The deterministic block-type word is the next Sturmian word

Let the mechanical one positions be

\[
d_\ell^\star
=
\left\lfloor(\ell-1)\beta\right\rfloor,
\qquad
\beta:=\log_2 3=\alpha^{-1}.
\]

For `ell>=2`, the gap between consecutive mechanical ones is

\[
d_\ell^\star-d_{\ell-1}^\star
\in\{1,2\}.
\]

A gap of two means the current mechanical one is preceded by a zero and hence belongs to an `A=01` block; a gap of one gives a singleton `B=1` block.

Write

\[
\gamma:=\beta-1
=
\log_2(3/2)
\in(0,1).
\]

Because

\[
\lfloor n\beta\rfloor
=n+\lfloor n\gamma\rfloor,
\]

the `A`-block indicator is

\[
\boxed{
\lfloor n\gamma\rfloor-
\lfloor(n-1)\gamma\rfloor
}
\]

(up to the harmless initial singleton convention).

Thus the deterministic `A/B` block word is itself a mechanical Sturmian word, now with slope

\[
\boxed{
\gamma=\log_2(3/2).
}
\]

This is exactly the next Euclidean / continued-fraction coordinate obtained from

\[
\boxed{
\alpha\longmapsto\alpha^{-1}-1.
}
\]

## 7. Exact size compression

The original time prefix has length

\[
L=A-1.
\]

The renormalized bridge has length exactly

\[
H.
\]

At the current isolated resonance this is the compression

\[
217,976,794,616
\longrightarrow
137,528,045,312.
\]

No parity information relevant to coefficient survival is lost: it is stored in

1. the `H` block-height increments;
2. the multiplicity-two neutral orientations of `A` blocks.

## 8. Relation to the odd-only formulation

The block-type word distinguishes whether consecutive mechanical odd events are separated by one or two time steps. Hence the `A/B` sequence is the time-expanded form of the mechanical odd-to-odd valuation word.

This explains why the previously independent-looking objects

- time-expanded Beatty ballots;
- Christoffel / Sturmian words;
- odd-only valuation words;
- deterministic plateau-pair cubes

are all representations of the same Euclidean-renormalized structure.

## 9. Next-level program

The transform

\[
\alpha\mapsto\alpha^{-1}-1
\]

is the Gauss/Euclidean step associated with the first continued-fraction digit.

Therefore the natural next target is a **multiscale Christoffel block decomposition**:

1. apply the same return-word grouping to the deterministic `A/B` Sturmian word;
2. identify equal-net-effect alternative subblocks that provide new independent orientation coordinates;
3. derive their exact canonical-residue valuation shifts;
4. iterate along the continued fraction of `log_3 2` / `log_2 3`.

If the accumulated independent coordinates capture a sufficiently large fraction of the survivor-language entropy, the deep canonical-address problem can be attacked hierarchically rather than by flat residue enumeration.

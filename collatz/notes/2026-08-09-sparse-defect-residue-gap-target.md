# Sparse-defect residue gap target

Date: 2026-08-09

Status: **DERIVED 2-ADIC VALUATION LEMMA + FINITE DIAGNOSTIC + OPEN TARGET**

This note formulates the quantitative obstruction suggested by the next unresolved resonance. It does not assert a global defect-density theorem.

## 1. Mechanical and defect residues

At a first coefficient crossing with total odd count `q`, let

\[
\kappa_i=\lfloor i\log_2 3\rfloor,
\qquad
d_i=\kappa_i-z_i,
\qquad z_i\ge0.
\]

The mechanical correction and an arbitrary admissible correction are

\[
R^*=\sum_i3^{q-1-i}2^{\kappa_i},
\qquad
R=\sum_i3^{q-1-i}2^{d_i}.
\]

The canonical starts satisfy

\[
r^*\equiv-3^{-q}R^*\pmod{2^\sigma},
\qquad
r\equiv-3^{-q}R\pmod{2^\sigma}.
\]

Therefore

\[
\boxed{
r-r^*
\equiv
\sum_{i:z_i>0}
3^{-(i+1)}2^{d_i}(2^{z_i}-1)
\pmod{2^\sigma}.}
\]

## 2. Earliest-defect valuation lemma

For every defect coordinate `z_i>0`, the factor

\[
3^{-(i+1)}(2^{z_i}-1)
\]

is odd modulo every power of two. Hence the corresponding summand has exact 2-adic valuation

\[
v_2= d_i.
\]

The odd positions `d_i` are strictly increasing, so distinct defect summands have distinct valuations. Consequently the summand with smallest `d_i` is unique and cannot be cancelled by the remaining terms.

Thus, whenever at least one defect is present,

\[
\boxed{
v_2(r-r^*)=\min_{i:z_i>0}d_i.}
\]

Equivalently, the first binary bit at which the canonical start differs from the mechanical canonical start is exactly the time position of the earliest displaced odd step.

This is an exact triangularity statement; it requires no probabilistic assumption.

## 3. Low-bit consequence

Modulo `2^B`, only defect terms with

\[
d_i<B
\]

can affect the canonical start. Therefore the low `B` bits determine the defect transfer recursively from the earliest affected time upward, while all defects at positions `d_i>=B` are invisible at that resolution.

This explains both the usefulness and the limitation of a fixed low-bit core:

- it exactly controls the early defect support;
- it cannot by itself force a positive density of defects in a word whose length grows without bound.

The latter is consistent with `eventual-mechanical-tail-limit.md`.

## 4. Quadratic small-start scale at the next resonance

For the next unresolved convergent

\[
q=137,528,045,312,
\]

the rational DK certificate gives

\[
x<36,797,925,187,243,805,015,225.
\]

Exact integer comparison shows

\[
\boxed{x<2q^2.}
\]

Thus the huge first-crossing candidate is not merely `75-bit`; its start is polynomially small in the odd-count scale.

This motivates a quantitative target independent of the particular bit cutoff.

## 5. Sparse-Defect Residue Gap — TARGET

Find explicit `c>0` and `q_0` such that every admissible first-crossing word with sufficiently large `q` obeys

\[
\boxed{
0<r<2q^2
\Longrightarrow
\#\{i:d_i<\kappa_i\}\ge cq.
}
\]

For the current `m=46` branch, the certified upper defect fraction is about `0.10556`, so any theorem with

\[
c>0.10556
\]

would eliminate that whole magnitude layer.

For the high ternary prefix `1000`, `ternary-prefix-defect-budget.md` gives an upper defect fraction below about `0.00260`; therefore even a much weaker positive lower density could eliminate that sub-block.

This target is deliberately separated from the formal-parity statement: a fixed finite prefix can always be extended by an eventually mechanical formal tail. The lower bound, if true, must use the ordinary canonical residue condition at the full first-crossing modulus.

## 6. Exact finite diagnostic

Exhaustive first-crossing enumeration was run for small `q`. Among words with

\[
0<r<2q^2,
\]

the minimum observed number of nonzero defect coordinates is:

| q | minimum defects | example start |
|---:|---:|---:|
| 2 | 0 | 3 |
| 3 | 0 | 11 |
| 4 | 1 | 7 |
| 5 | 2 | 39 |
| 6–8 | no such residue | — |
| 9 | 6 | 127 |
| 10–11 | no such residue | — |
| 12 | 8 | 239 |
| 13 | 8 | 319 |
| 14 | no such residue | — |
| 15 | 9 | 283 |
| 16 | no such residue | — |
| 17 | 9 | 251 |
| 18 | 13 | 167 |
| 19 | 13 | 223 |
| 20–21 | no such residue | — |
| 22 | 19 | 871 |
| 23 | 19 | 927 |

These values are finite diagnostics only. No asymptotic monotonicity or positive-density theorem is inferred from them.

An independent Wolfram exact enumeration reproduces:

\[
q=9:\ (6,127),
\qquad
q=12:\ (8,239),
\qquad
q=13:\ (8,319).
\]

## 7. Relation to recent external work

Kramer (2026, arXiv:2607.10041) studies finite odd-to-odd exponent codes using a combined real drift, 2-adic start representative, and 3-adic endpoint representative. His experiments likewise find that mechanical/near-critical codes retain positive normalized residue rates, while genuine fixed positive orbits must have vanishing residue rates.

The present target is compatible with that obstruction viewpoint but is more specialized:

- it is restricted to exact first coefficient crossings;
- it uses odd-position defects relative to the mechanical cap;
- and it asks for a deterministic lower bound on the number of defects from an ordinary small canonical representative.

No novelty claim should be made for the general idea that near-critical symbolic codes must also satisfy small 2-adic representatives. The project-specific open question is the quantitative defect/residue inequality above.

## 8. Current status

Proved here:

- exact earliest-defect 2-adic valuation identity;
- exact polynomial small-start scale for the specific next resonance.

Computational only:

- the small-q defect table.

Open:

- any uniform positive lower defect density;
- any bound strong enough to contradict the certified defect budgets at the next resonance.
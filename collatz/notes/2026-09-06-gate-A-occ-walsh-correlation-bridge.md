# Gate A_occ: support-aware Walsh-correlation bridge

Date: 2026-09-06

## One-line result

The Beatty macro-pair contraction does not require global selector min/max mixing: for each 5- or 6-bit macro-pair, it is enough to control a finite weighted set of Walsh correlations of the actual selector-conditioned child distribution.  This remains meaningful after the global support barrier `B-2>m` where `c_min=0`.

## Status

- **SAFE LEMMA:** exact Walsh expansion of the macro-pair Lyapunov payoff.
- **SAFE SUFFICIENT CONDITION:** signed/absolute Walsh-correlation criteria for local or aggregate contraction.
- **FINITE-DIMENSIONAL REDUCTION:** only 31 nontrivial Walsh coefficients for `AB/BA`, and 63 for `BB`.
- **BARRIER:** arbitrary occupied subsets need not contract; a singleton all-odd extension expands by `9/4`.
- **OPEN GATE:** prove the required Walsh-correlation bound for the actual recursively sufficient selector/survivor distribution at arbitrarily large scales.

No Collatz proof is claimed.

---

## 1. Beatty macro-pair payoff

Let

\[
a=\frac32.
\]

For one pair of Beatty macrocycles, let the extension word be

\[
u=(u_1,\ldots,u_L)\in\{0,1\}^L,
\]

where `u_i=1` denotes an odd/raising parity choice.  Let `r` be the number of Beatty rises in the macro-pair.

The unrestricted normalized surplus payoff is

\[
g(u)=a^{|u|-r}.
\]

For the three allowed macro-pair types,

\[
(L,r)=
\begin{cases}
(5,3),&AB,BA,\\
(6,4),&BB.
\end{cases}
\]

If a low-surplus prefix hits the coefficient boundary, that child is deleted, so its actual payoff is `0`; hence the unrestricted `g(u)` remains a valid nonnegative upper majorant.

The uniform child means are

\[
\sigma_{AB}=\sigma_{BA}
=\frac1{2^5}\sum_u g(u)
=\frac{3125}{3456}<1,
\]

and

\[
\sigma_{BB}
=\frac1{2^6}\sum_u g(u)
=\frac{15625}{20736}<1.
\]

---

## 2. Why arbitrary occupied subsets cannot satisfy Gate A_occ

At high enough surplus every extension is coefficient-valid.  The all-one word has

\[
|u|=L,
\]

and both macro-pair types have `L-r=2`.  Therefore

\[
\boxed{g(1,\ldots,1)=a^2=\frac94>1.}
\]

So a survivor/selector distribution concentrated on that one child expands.  Consequently the existing `3125/3456` theorem cannot be upgraded to

> every occupied subset contracts.

The missing information is a correlation restriction between the actual selector-conditioned child distribution and the high-payoff parity words.

---

## 3. Exact Walsh expansion

For `S subseteq {1,...,L}`, define the Walsh character

\[
\chi_S(u)=(-1)^{\sum_{i\in S}u_i}.
\]

For any probability distribution `p` on the `2^L` child words, define

\[
\widehat p(S)=\mathbb E_p[\chi_S],
\qquad
\widehat p(\varnothing)=1.
\]

The one-bit identity is

\[
a^{u_i}
=\frac54\left(1-\frac15(-1)^{u_i}\right).
\]

Hence

\[
\begin{aligned}
g(u)
&=a^{-r}\prod_{i=1}^L a^{u_i}\\
&=a^{-r}\left(\frac54\right)^L
\prod_{i=1}^L\left(1-\frac15\chi_{\{i\}}(u)\right).
\end{aligned}
\]

Since

\[
\sigma_P=a^{-r}\left(\frac54\right)^L,
\]

we get the pointwise identity

\[
\boxed{
g(u)=
\sigma_P
\sum_{S\subseteq[L]}
\left(-\frac15\right)^{|S|}\chi_S(u).
}
\]

Averaging under the actual child distribution gives

\[
\boxed{
\mathbb E_p[g]
=\sigma_P
\left[
1+
\sum_{\varnothing\ne S\subseteq[L]}
\left(-\frac15\right)^{|S|}\widehat p(S)
\right].
}
\]

For boundary-deleted children the actual expected payoff is no larger than the right-hand side.

This is the required support-aware replacement for the global `c_max/c_min` argument.

---

## 4. Signed Walsh criterion

Define

\[
\Phi_P(p)=
\sum_{\varnothing\ne S\subseteq[L]}
\left(-\frac15\right)^{|S|}\widehat p(S).
\]

Then a sufficient condition for strict macro-pair contraction is simply

\[
\boxed{
\Phi_P(p)<\frac1{\sigma_P}-1.
}
\]

The exact margins are

\[
\boxed{
\frac1{\sigma_{AB}}-1
=\frac1{\sigma_{BA}}-1
=\frac{331}{3125}
\approx0.10592,
}
\]

and

\[
\boxed{
\frac1{\sigma_{BB}}-1
=\frac{5111}{15625}
\approx0.327104.
}
\]

This criterion is signed: favorable Walsh correlations may cancel unfavorable ones.  It is therefore weaker than any pointwise equidistribution requirement.

---

## 5. Absolute Walsh sufficient condition

Define

\[
\Psi_P(p)=
\sum_{\varnothing\ne S\subseteq[L]}
5^{-|S|}\,|\widehat p(S)|.
\]

Then

\[
\Phi_P(p)\le\Psi_P(p),
\]

so

\[
\boxed{
\Psi_P(p)<\frac1{\sigma_P}-1
}
\]

is a simple sufficient condition.

If all nonempty Walsh biases obey

\[
|\widehat p(S)|\le\beta,
\]

then

\[
\Psi_P(p)
\le
\beta\left[\left(1+\frac15\right)^L-1\right].
\]

Therefore it is enough to have

\[
\boxed{
\beta<\frac{331}{4651}
\approx0.07116749
}
\]

for `AB/BA`, and

\[
\boxed{
\beta<\frac{5111}{31031}
\approx0.16470626
}
\]

for `BB`.

Only `2^5-1=31` or `2^6-1=63` finite local Walsh moments are involved.

---

## 6. Aggregate version: no per-parent uniformity is necessary

Let the occupied parent states be indexed by `s`, with nonnegative Lyapunov-selector weights `omega_s`.  Let `p_s` be the selector-conditioned child distribution from parent `s`.

Because the Walsh formula is linear in `p`, define the weighted aggregate Walsh coefficient

\[
\overline{\widehat p}(S)
=
\frac{\sum_s\omega_s\widehat p_s(S)}{\sum_s\omega_s}.
\]

Then the total macro-pair Lyapunov ratio is bounded by

\[
\boxed{
\frac{W_{\rm out}}{W_{\rm in}}
\le
\sigma_P
\left[
1+
\sum_{\varnothing\ne S}
\left(-\frac15\right)^{|S|}
\overline{\widehat p}(S)
\right].
}
\]

Thus Gate A_occ does **not** require every parent cylinder to mix.  Bad parents may be compensated by good parents, provided the actual weighted aggregate correlation stays below the signed threshold.

This is substantially weaker than the earlier `c_max/c_min` condition.

---

## 7. Relation to the support barrier

The old dense-window transfer requires

\[
c_{\min}(m,B)>0,
\]

which is impossible once

\[
B-2>m.
\]

The Walsh criterion does not require all dyadic residues to be occupied.  It only asks how the actual selector mass is distributed among the fixed `32` or `64` extension words of the next macro-pair.

Therefore the new criterion remains well-defined in the sparse regime and is a genuine candidate bridge for `A_occ`.

Sparse support by itself is not enough: a singleton can have every nonempty Walsh coefficient of magnitude one.  What matters is the correlation pattern, not the number of occupied global dyadic residues.

---

## 8. Total-variation fallback

Let `U` be the uniform distribution on the block.  Since

\[
g_{\max}=\frac94,
\]

while

\[
g_{\min}=a^{-r},
\]

we have

\[
|\mathbb E_p g-\mathbb E_U g|
\le
(g_{\max}-g_{\min})\,\mathrm{TV}(p,U).
\]

Hence sufficient TV bounds are

\[
\boxed{
\mathrm{TV}(p,U)<\frac{331}{6752}
\approx0.04902251
}
\]

for `AB/BA`, and

\[
\boxed{
\mathrm{TV}(p,U)<\frac{269}{2240}
\approx0.12008929
}
\]

for `BB`.

These are stronger than the signed Walsh criterion but provide an independent consistency check.

---

## 9. Uniform-support diagnostic

If `p` is uniform on an arbitrary `k`-element subset, the worst subset is obtained by selecting the `k` largest Hamming-payoff words.

Exact enumeration gives:

- `AB/BA`: every arbitrary uniform support of size at least `27/32` contracts; the worst `k=27` mean is `967/972<1`.
- `BB`: every arbitrary uniform support of size at least `35/64` contracts; the worst `k=35` mean is `419/420<1`.

This is only a diagnostic.  It demonstrates why a pure support-cardinality theorem is too demanding in the sparse regime and why correlation is the right variable.

---

## 10. DSD audit and next theorem target

### SAFE

1. The exact Walsh expansion.
2. The signed and absolute sufficient contraction criteria.
3. The aggregate weighted-parent version.
4. The TV and uniform-support diagnostics.

### NOT SAFE TO UPGRADE

1. Existing additive Fourier decay of canonical residues does not automatically imply these Walsh bounds.
2. Finite `m=44` dense-window mixing does not imply asymptotic Walsh control.
3. Sparse support does not by itself imply contraction.
4. The unrestricted `3125/3456` average cannot be applied to an arbitrary survivor subset.

### OPEN Gate A_occ-W

For each sufficiently late Beatty macro-pair, or for enough macro-pairs to force atom-floor extinction, prove for the **actual recursively sufficient occupied selector distribution** either

\[
\Phi_P<\frac1{\sigma_P}-1,
\]

or an aggregate/cumulative variant with net negative logarithmic drift.

A promising implementation target is a finite-state transfer that carries the 31/63 Walsh moments jointly with the selector/survivor recurrence.  This avoids demanding global dyadic equidistribution.

---

## Reproducibility

Exact algebraic checks:

`collatz/src/gateA_occ_walsh_correlation_certificate.py`

Expected final line:

```text
PASS
```

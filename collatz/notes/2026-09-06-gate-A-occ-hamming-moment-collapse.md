# Gate A_occ: collapse from 31/63 Walsh modes to one Hamming exponential moment

Date: 2026-09-06

## One-line result

For a 5- or 6-step Beatty macro-pair, the Lyapunov payoff depends only on the number `H` of odd choices in that block.  Therefore Gate A_occ does not require separate control of 31/63 Walsh coefficients: it is exactly enough to control the single scalar moment

\[
\mathbb E\left[\left(\frac32\right)^H\right].
\]

## Status

- **SAFE LEMMA:** exact Hamming-moment reduction.
- **SAFE EQUIVALENCE:** local contraction is equivalent to one explicit exponential-moment inequality.
- **SAFE FAILURE CHARACTERIZATION:** noncontraction is equivalent to a finite high-odd-tail excess overcoming the low-odd deficit.
- **FINITE DATA:** earlier sparse diagnostics can now be interpreted directly as measurements of this one moment.
- **OPEN GATE:** prove recurrent/cumulative control of this moment under the actual recursive/canonical survivor conditioning.

No Collatz proof is claimed.

---

## 1. Exact reduction

Let

\[
a=\frac32.
\]

For one Beatty macro-pair let

\[
H=|u|
\]

be the number of odd choices in its `L` parity positions, and let `r` be the number of Beatty rises in the block.

The normalized surplus payoff is

\[
\boxed{g=a^{H-r}.}
\]

Thus for any actual selector/canonical child distribution `p`,

\[
\boxed{
\mathbb E_p[g]
=a^{-r}\mathbb E_p[a^H].
}
\]

Consequently strict local contraction is **exactly equivalent** to

\[
\boxed{
\mathbb E_p\left[\left(\frac32\right)^H\right]
<
\left(\frac32\right)^r.
}
\]

No global residue support, min/max multiplicity, or individual Fourier/Walsh coefficient is present in this statement.

Boundary-invalid descendants may be assigned payoff zero; therefore the unrestricted `a^{H-r}` expression remains a safe upper majorant when coefficient rejection is also imposed.

---

## 2. The two exact thresholds

### AB / BA

Here

\[
L=5,
\qquad
r=3.
\]

Hence it is enough, and for the unrestricted block payoff exactly equivalent, to prove

\[
\boxed{
\mathbb E\left[\left(\frac32\right)^H\right]
<\frac{27}{8}.
}
\]

Under the uniform five-bit distribution,

\[
\mathbb E\left[\left(\frac32\right)^H\right]
=\left(\frac54\right)^5,
\]

which gives

\[
\frac{(5/4)^5}{(3/2)^3}
=\frac{3125}{3456}<1.
\]

### BB

Here

\[
L=6,
\qquad
r=4.
\]

The exact moment threshold is

\[
\boxed{
\mathbb E\left[\left(\frac32\right)^H\right]
<\frac{81}{16}.
}
\]

The uniform six-bit distribution gives

\[
\frac{(5/4)^6}{(3/2)^4}
=\frac{15625}{20736}<1.
\]

---

## 3. Why the Walsh bridge still matters

The preceding result is not a different mechanism from the Walsh bridge; it is its symmetric collapse.

The payoff depends only on Hamming weight, so

\[
\sum_{\varnothing\ne S}
\left(-\frac15\right)^{|S|}\widehat p(S)
\]

uses the Walsh transform only through the level sums

\[
M_k=\sum_{|S|=k}\widehat p(S).
\]

Equivalently, these are Krawtchouk moments of the Hamming-count distribution.

But even those `L` level sums are more information than is needed for contraction: their one required linear combination is precisely

\[
\mathbb E[(3/2)^H].
\]

Thus the hierarchy is

\[
31/63\text{ individual Walsh modes}
\Longrightarrow
5/6\text{ Walsh-level sums}
\Longrightarrow
\boxed{1\text{ exponential Hamming moment}}.
\]

The Walsh representation remains useful if Fourier machinery is used to bound the moment, but it is no longer the theorem target itself.

---

## 4. Exact failure pressure: AB / BA

For `L=5,r=3`, the payoff by Hamming count is

\[
\begin{array}{c|cccccc}
H&0&1&2&3&4&5\\\hline
(3/2)^{H-3}
&8/27&4/9&2/3&1&3/2&9/4.
\end{array}
\]

Let

\[
p_h=\Pr(H=h).
\]

The block fails to contract iff

\[
\sum_h p_h\left[\left(\frac32\right)^{h-3}-1\right]\ge0.
\]

Therefore failure is exactly

\[
\boxed{
\frac12p_4+rac54p_5
\ge
\frac{19}{27}p_0+rac59p_1+rac13p_2.
}
\]

The `H=3` mass is neutral.

So the only source of positive pressure is the high-odd tail `H=4,5`.

---

## 5. Exact failure pressure: BB

For `L=6,r=4`,

\[
\begin{array}{c|ccccccc}
H&0&1&2&3&4&5&6\\\hline
(3/2)^{H-4}
&16/81&8/27&4/9&2/3&1&3/2&9/4.
\end{array}
\]

Noncontraction is exactly

\[
\boxed{
\frac12p_5+rac54p_6
\ge
\frac{65}{81}p_0+rac{19}{27}p_1+rac59p_2+rac13p_3.
}
\]

The `H=4` mass is neutral.

Again, only the two top Hamming layers supply positive pressure.

---

## 6. Structural interpretation

This is the strongest simplification obtained in the current Gate A audit.

To destroy Beatty contraction forever, recursive/canonical survivor selection must repeatedly bias the actual occupied mass strongly enough toward

\[
H\ge r+1.
\]

But for each such atom

\[
d_{\rm out}-d_{\rm in}=H-r>0.
\]

Thus a bad block is not an abstract spectral anomaly: its positive contribution comes exactly from candidate mass whose Beatty surplus rises during that block.

The terminal Gate A problem can therefore be phrased without Fourier language:

\[
\boxed{
\text{Can the actual recursive/canonical survivor process sustain enough}
\left(\frac32\right)^H\text{-weighted high-odd pressure indefinitely?}
}
\]

This is still open, but the state variable required from each short block is now one-dimensional.

---

## 7. Cumulative form

For successive macro-pairs `j`, write `H_j` and `r_j` for the block odd count and Beatty-rise count under the actual aggregate weighted candidate distribution.

Define

\[
R_j
=
\left(\frac32\right)^{-r_j}
\mathbb E_j\left[\left(\frac32\right)^{H_j}\right].
\]

Then

\[
\boxed{
\frac{W_J}{W_0}
\le
\prod_{j<J}R_j.
}
\]

Therefore Gate A does not require `R_j<1` for every `j`.  It is sufficient that

\[
\boxed{
\sum_{j<J}\log R_j\longrightarrow-\infty.
}
\]

This is the most economical current formulation of the high-surplus drift target.

---

## 8. DSD audit

### SAFE

1. The payoff is a function of `H` only.
2. Contraction is exactly the one-moment inequality above.
3. The high-tail excess / low-tail deficit identities are exact.
4. Cumulative negative logarithmic drift is sufficient; every block need not contract.

### NOT SAFE TO UPGRADE

1. Small finite observed values of the Walsh bias do not prove the moment inequality asymptotically.
2. Control of the ordinary mean `E[H]` alone is not enough, because `(3/2)^H` is convex.
3. Selector sparsity alone neither proves nor disproves the moment bound.
4. A single exceptional path can remain after mass decay unless the finite-layer atom-floor / same-integer closure is invoked.

### OPEN

Prove a recursive/canonical mechanism controlling

\[
\mathbb E[(3/2)^H]
\]

on enough successive macro-pairs to force cumulative negative drift.

This replaces the broader Gate A_occ-WR statement by the narrower target **Gate A_occ-H**.

---

## Reproducibility

Exact identities and constants:

`collatz/src/gateA_occ_hamming_moment_collapse_certificate.py`

Expected final line:

```text
PASS
```

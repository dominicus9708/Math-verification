# Gate A tail-budget -> atom-floor closure theorem

Date: 2026-09-06

## One-line result

For a finite recursively sufficient layer `F_m`, high-surplus strata do not need to contract individually.  If a fixed low-surplus region contracts by `rho<1` and the **weighted** high-surplus input fraction stays below

\[
\boxed{
\tau_* = \frac{1-\rho}{9/4-\rho},
}
\]

then the entire selector layer contracts by a fixed factor `lambda<1`; after `O(m)` Beatty macro-pairs its weighted mass falls below the one-atom floor and the layer is empty.

## Status

- **SAFE CONDITIONAL THEOREM:** tail-budget inequality and atom-floor closure.
- **FINITE DIAGNOSTIC:** `m=22`, block `32->37`, `D=8` has more than a factor-50 slack against the crude universal high-tail budget.
- **BARRIER:** requiring every surplus stratum to contract is false even in the finite `m=22` audit.
- **OPEN GATE:** prove horizon-uniform low-strip contraction plus a horizon-uniform/cumulative bound on the weighted high-surplus tail under the actual canonical survivor process.

No Collatz proof is claimed.

---

## 1. Weighted candidate mass

Let

\[
a=\frac32,
\qquad
W(d)=a^d.
\]

For one fixed selector layer `F_m`, let `S_j` be the coefficient/canonical candidate atoms surviving at the start of Beatty macro-pair `j`.

Define

\[
\boxed{
\mathcal W_j
=\sum_{x\in S_j} a^{d_j(x)}.
}
\]

Every surviving coefficient state has

\[
d_j(x)\ge0,
\]

so

\[
S_j\ne\varnothing
\quad\Longrightarrow\quad
\mathcal W_j\ge1.
\]

Thus

\[
\boxed{
\mathcal W_j<1
\quad\Longrightarrow\quad
S_j=\varnothing.
}
\]

This is the unnormalized integer/atom-floor version of the previous `2^{-m}` probability-mass lemma.

---

## 2. Low/high surplus split

Fix a strip height `D` and split

\[
S_j=S_j^{<D}\sqcup S_j^{\ge D}.
\]

Write

\[
\mathcal W_j^{<D}
=\sum_{x\in S_j^{<D}}a^{d_j(x)},
\qquad
\mathcal W_j^{\ge D}
=\sum_{x\in S_j^{\ge D}}a^{d_j(x)}.
\]

Define the weighted high-tail fraction

\[
\boxed{
\tau_j
=\frac{\mathcal W_j^{\ge D}}{\mathcal W_j}.
}
\]

This is the correct tail variable for the Lyapunov argument.  An unweighted count fraction can be misleading because large `d` carries the factor `(3/2)^d`.

---

## 3. Universal high-stratum block ceiling

For every allowed Beatty macro-pair, its length/rise pair is

\[
(L,r)=(5,3)
\quad\text{or}\quad
(6,4).
\]

For an extension with `H` odd choices,

\[
\frac{W(d_{\rm out})}{W(d_{\rm in})}
=a^{H-r}.
\]

Since `H<=L` and in both cases `L-r=2`,

\[
\boxed{
\frac{W(d_{\rm out})}{W(d_{\rm in})}
\le a^2=\frac94.
}
\]

Coefficient/root/canonical rejection only deletes nonnegative contributions and cannot raise this ceiling.

Therefore the entire high-surplus sector always satisfies the crude but universal bound

\[
\boxed{
\mathcal W_{j+1}^{\rm(out\ from\ high)}
\le\frac94\mathcal W_j^{\ge D}.
}
\]

---

## 4. Tail-budget lemma

Assume the low sector satisfies a block bound

\[
\boxed{
\mathcal W_{j+1}^{\rm(out\ from\ low)}
\le\rho\mathcal W_j^{<D}
}
\]

with

\[
0\le\rho<1.
\]

Then

\[
\begin{aligned}
\mathcal W_{j+1}
&\le
\rho\mathcal W_j^{<D}
+\frac94\mathcal W_j^{\ge D}\\
&=
\left[
\rho(1-\tau_j)+\frac94\tau_j
\right]\mathcal W_j.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{\mathcal W_{j+1}}{\mathcal W_j}
\le
\rho+\left(\frac94-\rho\right)\tau_j.
}
\]

Strict whole-layer contraction follows whenever

\[
\boxed{
\tau_j
<
\tau_*(\rho)
:=
\frac{1-\rho}{9/4-\rho}.
}
\]

This allows arbitrarily bad high-surplus child orientation, including the worst possible `9/4` expansion, provided its weighted input mass is sufficiently small.

---

## 5. Uniform atom-floor closure

Suppose there are constants

\[
D<\infty,
\qquad
\rho<1,
\qquad
\tau<\tau_*(\rho)
\]

independent of `m` and of the macro-pair index, such that every relevant surviving `F_m` layer satisfies

\[
\tau_j\le\tau.
\]

Set

\[
\lambda
=
\rho+\left(\frac94-\rho\right)\tau
<1.
\]

Then

\[
\boxed{
\mathcal W_{j+1}
\le\lambda\mathcal W_j.
}
\]

At the initial state every selector atom has `d=0`, so for the full layer

\[
\mathcal W_0=|F_m|=2^m.
\]

Ignoring a fixed finite number of initial alignment steps, which changes only an absolute multiplicative constant, after `J` contracting macro-pairs,

\[
\mathcal W_J
\le
C\,2^m\lambda^J
\]

for some `C` independent of `m`.

Choose

\[
J>
\frac{m\log2+\log C}{-\log\lambda}.
\]

Then

\[
\mathcal W_J<1,
\]

so

\[
S_J=\varnothing.
\]

Therefore

\[
\boxed{
M_F(m)=O(m)
}
\]

under the stated horizon-uniform hypotheses.

This is much stronger than the earlier sufficient record-growth condition

\[
\limsup_{m\to\infty}
\frac{\log_2M_F(m)}m
<0.11083654\ldots.
\]

Indeed `M_F(m)=O(m)` gives

\[
\frac{\log_2M_F(m)}m\to0.
\]

---

## 6. A finite counterexample to stratumwise contraction

The exact sparse diagnostic for `m=22`, block `32->37`, has `r=3`.

For parent surplus `d=8`, the exact Hamming histogram is

\[
H=1:2,
\quad
H=2:3,
\quad
H=3:6,
\quad
H=4:1,
\quad
H=5:2.
\]

Thus

\[
\boxed{
R_{d=8}
=\frac{67}{63}
>1.
}
\]

At `d=9` there is one atom with `H=4`, giving

\[
\boxed{
R_{d=9}=\frac32>1.
}
\]

Hence the stronger statement

> every occupied surplus stratum contracts

is **false even in this finite exact audit**.

The correct theorem must permit a rare expanding tail.

---

## 7. Finite m=22 tail-budget audit

For the same sparse block `32->37`, choose

\[
D=8.
\]

Among the low strata `d=0,...,7`, the worst exact block ratio is

\[
\boxed{
\rho
=\frac{800339}{879282}
\approx0.910218792151.
}
\]

The exact weighted input fraction in the expanding/neutral tail `d>=8` is

\[
\boxed{
\tau
=\frac{203391}{160192007}
\approx0.00126967009034.
}
\]

The universal tail-budget threshold is

\[
\boxed{
\tau_*(\rho)
=\frac{157886}{2356091}
\approx0.0670118429212.
}
\]

Therefore the observed tail occupies only about

\[
\boxed{1.895\%}
\]

of the already crude allowable threshold, i.e. the threshold is more than `52` times larger than the observed weighted tail.

The crude tail-budget estimate gives a factor below one; the exact aggregate histogram is better still:

\[
\boxed{
R_{\rm actual}
=\frac{7819656391}{8650368378}
\approx0.903968021858.
}
\]

The two expanding strata contribute only about `0.14%` of the magnitude of the negative drift supplied by the contracting strata in this finite block.

All of these numerical margins are **FINITE DIAGNOSTICS ONLY**.

---

## 8. What remains to prove

The conditional theorem reduces the asymptotic job to two quantities.

### Low-strip block control

Find fixed `D` and `rho<1` such that the actual recursive/canonical low-surplus mass obeys

\[
\mathcal W_{j+1}^{\rm(out\ from\ low)}
\le\rho\mathcal W_j^{<D}
\]

on enough blocks.

This is close in spirit to the existing Gate B finite-state program.

### High-tail weighted tightness

Prove that

\[
\tau_j
=\frac{\mathcal W_j^{\ge D}}{\mathcal W_j}
\]

is uniformly or cumulatively small enough that

\[
\rho+\left(\frac94-\rho\right)\tau_j
\]

has negative cumulative logarithmic drift.

This is the revised Gate A content.

The important reduction is that **no theorem about contraction inside every high-surplus stratum is required**.

---

## 9. DSD audit

### SAFE

1. Universal block payoff ceiling `9/4`.
2. Tail-budget inequality.
3. Uniform tail-budget + low-strip contraction implies geometric whole-layer decay.
4. Geometric whole-layer decay plus finite `2^m` atom floor implies `M_F(m)=O(m)`.

### FINITE ONLY

1. `m=22`, `32->37`, `D=8` values of `rho`, `tau`, and the `52x` slack.
2. The rare expanding `d=8,9` strata.

### BARRIER

Uniform stratumwise contraction is false.

### OPEN

Prove low-strip contraction and high-tail tightness for the actual canonical recursively sufficient process with constants sufficient for negative cumulative drift.

---

## Reproducibility

Algebra and the exact finite `m=22` constants:

`collatz/src/gateA_tail_budget_atom_floor_certificate.py`

Surplus-stratified exact histograms:

`collatz/src/gateA_occ_surplus_stratified_sparse_diagnostic.cpp`

Expected Python certificate final line:

```text
PASS
```

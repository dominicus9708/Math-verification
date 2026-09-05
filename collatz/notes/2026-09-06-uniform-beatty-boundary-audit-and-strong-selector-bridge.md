# Uniform Beatty-boundary audit and strong selector-repair bridge

Date: 2026-09-06

Status: **EXTERNAL-THEOREM AUDIT PASSED + STRONG CONDITIONAL BRIDGE.**

This note re-audits the 2026-08-13 constant Beatty-boundary theorem after the later 2026-08-26 elementary `2/(5L)` certificate was introduced.

The conclusion is:

\[
\boxed{
\text{the constant boundary theorem survives the audit.}
}
\]

The `2/(5L)` theorem is not a correction of the constant theorem.  It is an independent, weaker, elementary/exact fallback that avoids reliance on an external conditioned-random-walk local theorem.

Consequently the current selector-repair route can be strengthened from harmonic `1/L` loss to constant-order loss at every sufficiently large Beatty rise for which the selector min/max margin is positive.

---

## 1. Symbolic coefficient-survivor language

Put

\[
\alpha=\log_3 2,
\qquad
b_L=\lceil\alpha L\rceil.
\]

For a binary word of length `L`, let `q_j` denote the number of ones in its first `j` positions.

The coefficient-survivor language is

\[
\mathcal R_L
=
\{w:q_j\ge\lceil\alpha j\rceil\text{ for every }1\le j\le L\}.
\]

The terminal Beatty boundary is

\[
\mathcal B_L
=
\{w\in\mathcal R_L:q_L=b_L\}.
\]

Write

\[
C_L^{\rm class}=|\mathcal R_L|,
\qquad
D_L^{\rm class}=|\mathcal B_L|.
\]

The later exact certificate independently proves, at a Beatty rise,

\[
\frac{D_L^{\rm class}}{C_L^{\rm class}}
>\frac{2}{5L}.
\]

The older probabilistic theorem claims the stronger asymptotic statement

\[
\boxed{
\exists c_*>0,\ L_0<\infty:
\quad
\frac{D_L^{\rm class}}{C_L^{\rm class}}\ge c_*
\quad(L\ge L_0).
}
\]

The next sections audit that claim.

---

## 2. Exponential tilt is exact

Under the uniform word-counting measure `P`, each bit is Bernoulli `1/2`.

Under the tilted measure `Q`, take

\[
Q(X_i=1)=\alpha,
\qquad
Q(X_i=0)=1-\alpha.
\]

Define

\[
S_j=q_j-\alpha j.
\]

Then `E_Q S_j=0`, the increments are bounded, have positive finite variance, and belong to the normal domain of attraction.

Because `alpha` is irrational,

\[
q_j\ge\lceil\alpha j\rceil
\iff
S_j>0.
\]

Thus coefficient survival is exactly the event

\[
\tau^->L,
\qquad
\tau^-:=\min\{j\ge1:S_j\le0\}.
\]

Let

\[
\delta_L=b_L-\alpha L\in(0,1).
\]

Then the boundary event is exactly

\[
\{\tau^->L,S_L=\delta_L\}.
\]

For a word with terminal displacement `S_L=x`, the Radon--Nikodym factor has the form

\[
\frac{dP}{dQ}=A_L e^{-\theta x},
\qquad
\theta=\log\frac{\alpha}{1-\alpha}>0.
\]

Therefore

\[
\boxed{
\frac{D_L^{\rm class}}{C_L^{\rm class}}
=
\frac{Q(\tau^->L,S_L=\delta_L)}
{\sum_{s\ge0}e^{-\theta s}
Q(\tau^->L,S_L=\delta_L+s)}.
}
\]

Status: **SAFE EXACT REDUCTION.**

---

## 3. Audit of the Vatutin--Wachtel hypotheses

Reference:

V. A. Vatutin and V. Wachtel, *Local probabilities for random walks conditioned to stay positive*, Probability Theory and Related Fields 143 (2009), arXiv:0711.1302.

Their lattice theorem applies to an `(h,a)`-lattice random walk in a stable domain of attraction and gives a uniform small-deviation local asymptotic in terms of the strict ascending-ladder-height renewal function `H`.

For the present increment

\[
X_i-\alpha\in\{-\alpha,1-\alpha\},
\]

we have:

1. **mean zero:** exact;
2. **finite positive variance:** `alpha(1-alpha)>0`;
3. **normal domain of attraction:** automatic for bounded nondegenerate increments;
4. **lattice form:**
   \[
   \{-\alpha,1-\alpha\}
   =(1-\alpha)+\{-1,0\},
   \]
   so span `h=1`, shift `a=1-alpha`;
5. **boundary endpoint:** choosing the integer lattice coordinate `x=b_L-L` gives
   \[
   aL+x=\delta_L\in(0,1);
   \]
6. **small-deviation regime:** since the normal scale `c_L` is of order `sqrt(L)`, any auxiliary sequence tending to zero sufficiently slowly still has `delta'_L c_L -> infinity`, so the uniformly bounded endpoint `delta_L` lies in the theorem's small-deviation window eventually.

Thus the moving Beatty endpoint is within the theorem's stated uniform lattice regime.

Status: **AUDIT PASSED.**

---

## 4. Numerator lower bound

Vatutin--Wachtel's lattice small-deviation theorem gives, after multiplying the conditional probability by `Q(tau^->L)`,

\[
Q(\tau^->L,S_L=x)
\sim
\frac{g(0)H(x)}{Lc_L}
\]

uniformly for permitted small positive lattice endpoints.

Their renewal function is defined by

\[
H(u)
=
\mathbf 1_{\{u>0\}}
+
\sum_{k\ge1}
P(\chi_1^++\cdots+\chi_k^+<u).
\]

Therefore

\[
\boxed{H(u)\ge1\quad(u>0).}
\]

Since `delta_L in (0,1)`, there exists `c_1>0` such that

\[
\boxed{
Q(\tau^->L,S_L=\delta_L)
\ge
\frac{c_1}{Lc_L}
}
\]

for all sufficiently large `L`.

Status: **SAFE CONSEQUENCE OF THE CITED THEOREM.**

---

## 5. Denominator upper bound

Vatutin--Wachtel Lemma 19 gives the unconditioned local upper estimate

\[
Q(S_L\in[x,x+1),\tau^->L)
\le
C\frac{H(x)}{Lc_L}
\]

for `0<x<=c_L`.

Because the support spacing is one, the interval

\[
[\delta_L+s,\delta_L+s+1)
\]

contains exactly one permitted time-`L` lattice point.

In the finite-variance case the ladder renewal function has at most linear growth,

\[
H(x)\le C'(1+x).
\]

Therefore

\[
\sum_{0\le s\le c_L}
e^{-\theta s}
Q(\tau^->L,S_L=\delta_L+s)
\le
\frac{C_2}{Lc_L}
\sum_{s\ge0}e^{-\theta s}(1+s)
\le
\frac{C_3}{Lc_L}.
\]

For `s>c_L`, an ordinary lattice local-limit upper bound `O(1/c_L)` together with the exponential weight `e^{-theta s}` gives

\[
O(c_L^{-1}e^{-\theta c_L})
=o((Lc_L)^{-1}).
\]

Hence the full denominator is at most

\[
\boxed{C_4/(Lc_L)}
\]

eventually.

Status: **SAFE CONSEQUENCE OF STANDARD LOCAL/RENEWAL ESTIMATES.**

---

## 6. Constant Beatty-boundary fraction survives

Combining the previous two sections,

\[
\boxed{
\frac{D_L^{\rm class}}{C_L^{\rm class}}
\ge
c_*:=\frac{c_1}{C_4}>0
}
\]

for every sufficiently large `L`.

Thus the 2026-08-13 constant-boundary theorem remains valid under the present audit.

The exact `2/(5L)` lower bound remains valuable because it is:

- elementary;
- independent of an external probability theorem;
- exact at every certified finite scale;
- a fallback if one chooses to make the proof stack self-contained.

But it is not the strongest available symbolic asymptotic input.

---

## 7. Strong selector-weighted exposure

Let the exact selector multiplicity satisfy

\[
0<a_L\le C_L(x)\le B_L,
\qquad
\rho_L=\frac{a_L}{B_L}.
\]

For a one-child parent set `D` inside a parent survivor set `R`, the selector-weight transfer gives

\[
\frac{S_D}{S_R}
\ge
\rho_L\frac{|D|}{|R|}.
\]

At a sufficiently large Beatty rise, the constant symbolic boundary theorem therefore gives

\[
\boxed{
\frac{S_{D_L}}{S_{R_L}}
\ge
c_*\rho_L.
}
\]

Status: **SAFE CONDITIONAL BRIDGE**, conditional only on exact fibre identification (`F_map`).

---

## 8. Strong one-rise contraction

The selector min/max one-child repair lemma loses at least

\[
\delta(\rho_L)
=
\frac{3\rho_L-1}{4\rho_L}
\]

of selector mass carried by the one-child parent set whenever `rho_L>1/3`.

Multiplying by the strong weighted exposure,

\[
\delta(\rho_L)c_*\rho_L
=
\boxed{
\frac{c_*}{4}(3\rho_L-1).
}
\]

Thus at every sufficiently large rise with `rho_L>1/3`,

\[
\boxed{
\mu_{L+1}
\le
\left(
1-\frac{c_*}{4}(3\rho_L-1)
\right)\mu_L.
}
\]

Status: **STRONG SAFE CONDITIONAL LEMMA.**

This supersedes the elementary fallback loss

\[
\frac{3\rho_L-1}{10L}
\]

when the external constant-boundary theorem is admitted.

---

## 9. Gate S becomes substantially weaker

Define

\[
m_L=(3\rho_L-1)_+.
\]

Using non-expansion when no positive certified loss is available,

\[
\mu_N
\le
C\exp\left(
-\frac{c_*}{4}
\sum_{\substack{L<N\\L\text{ rise}}}m_L
\right).
\]

Therefore the primary Gate-S target is now only

\[
\boxed{
\sum_{L\text{ rise}}(3\rho_L-1)_+=+\infty.
}
\]

There is **no `1/L` weight** in the strong route.

Consequences:

### Fixed-margin infinitely often

If there exists `eta>0` such that

\[
\rho_L\ge\frac13+\eta
\]

for infinitely many rises, then each such rise loses at least

\[
\boxed{3c_*\eta/4}
\]

of normalized candidate mass, and therefore `mu_L -> 0`.

### Positive-density good rises

If the number of good rises through `N` is at least `beta N+O(1)`, then

\[
\boxed{
\mu_N\le C e^{-(3c_*\eta\beta/4)N}.
}
\]

### One good rise per multiplicative block

If every sufficiently large block `[lambda^j,lambda^{j+1})` contains at least one rise with the same fixed margin `eta`, then the number of certified contractions through `N` is `~log N/log lambda`, giving polynomial decay.

Thus even extremely sparse but endlessly recurring fixed-margin good rises are enough for mere mass decay.

---

## 10. Discrepancy and Fourier versions

With one-sided relative selector deviations

\[
h_L(x)\ge(1-d_L)\bar h_L,
\qquad
h_L(x)\le(1+u_L)\bar h_L,
\]

we have

\[
3\rho_L-1
\ge
\frac{2-3d_L-u_L}{1+u_L}.
\]

Hence the strong Gate-S sufficient target is

\[
\boxed{
\sum_{L\text{ rise}}
\frac{(2-3d_L-u_L)_+}{1+u_L}
=+\infty.
}
\]

For symmetric discrepancy `epsilon_L`,

\[
3\rho_L-1
\ge
\frac{2(1-2\varepsilon_L)}{1+\varepsilon_L},
\]

so it suffices that

\[
\boxed{
\sum_{L\text{ rise}}
\frac{(1-2\varepsilon_L)_+}{1+\varepsilon_L}
=+\infty.
}
\]

For the normalized exact-selector Fourier tail

\[
\Theta_L
=
\frac{\sum_{t\ne0}|\widehat h_L(t)|}
{\widehat h_L(0)},
\qquad
\varepsilon_L\le\Theta_L,
\]

it suffices that

\[
\boxed{
\sum_{L\text{ rise}}
\frac{(1-2\Theta_L)_+}{1+\Theta_L}
=+\infty.
}
\]

Again there is no harmonic `1/L` factor in the strong route.

---

## 11. DSD audit classification

### SAFE / CLOSED symbolic channel

1. exact coefficient-survivor language;
2. exact tilt identity;
3. all hypotheses of the cited lattice conditioned-walk theorem are satisfied;
4. constant Beatty-boundary fraction `c_*>0` for all sufficiently large depths;
5. elementary `2/(5L)` lower bound remains an independent fallback.

### SAFE CONDITIONAL bridge

1. weighted boundary exposure `>=c_* rho_L`;
2. total rise loss `>=c_*(3rho_L-1)/4`;
3. divergence of the unweighted positive selector margins implies normalized mass decay.

These still require exact fibre identification/normalization.

### OPEN

1. `F_map`: selector-to-canonical coefficient-fibre identification;
2. `F_unif`: growing-Q moving low-height strip control, where needed by the chosen transfer theorem;
3. strong Gate S: prove enough exact-selector good rises/margins;
4. terminal pathwise Gate C.

### PROHIBITED UPGRADES

1. Do not use the constant `c_*` as a known numerical value; the theorem proves existence, not the observed `~0.07` value.
2. Do not transfer the symbolic class boundary fraction to selector-weighted mass without `F_map`/cross-base control.
3. Do not infer terminal emptiness from normalized mass decay.
4. Do not discard the elementary `1/L` route; it remains the self-contained fallback and an independent audit check.

---

## 12. Revised priority

The symbolic Beatty boundary is no longer a bottleneck even in the strong asymptotic sense.

The proof effort should now focus on

\[
\boxed{
F_{\rm map}
\longrightarrow
\text{exact selector transfer}
\longrightarrow
\sum_{L\text{ rise}}(3\rho_L-1)_+=\infty
}
\]

and separately on the terminal integer-path obstruction.

The next coordinate audit should identify exactly what the Beatty binary word means relative to the canonical valuation/skew variables before any canonical lift digit is equated with a coefficient child bit.

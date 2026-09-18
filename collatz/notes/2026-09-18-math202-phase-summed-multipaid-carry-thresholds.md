# MATH-202 — exact phase-summed multi-paid surplus and carry-valuation thresholds

Date: 2026-09-18

Status: `EXACT STRUCTURAL SHARPENING / r=2..21 OVERSHOOT THRESHOLDS / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-185 proves that every exact multi-paid cluster with paid count

[
r\ge2
]

has positive local reduced-cost drift at the MATH-060 target slope

[
\lambda=\frac{19}{503}.
]

Its proof deliberately used coarse universal paid-atom bounds.

MATH-186 then shows that a possible Bellman deficit can occur only in a singleton overshoot

[
z:=L-R>0,
]

with lower bound

[
\Delta\mathcal B
\ge
\epsilon_r-\lambda z,
qquad
\epsilon_r:=\mathcal P_r-\lambda h_r.
]

MATH-193 adds the exact overshoot compatibility condition

[
\nu_2(C_R)\ge z.
]

The purpose of this note is to replace the coarse lower bound on `epsilon_r` by the exact finite MATH-179 phase partition for every

[
2\le r\le21.
]

The result gives a paid-count-dependent **minimum overshoot depth** and therefore a minimum carry valuation for every potentially dangerous singleton.

No paid layer or first-cell closure is claimed.

## 2. Exact MATH-179 phase clock

Put

[
m(j)=\lfloor j\log_2(3/2)\rfloor
]

and

[
\tau_j
=
\frac{3^j}{2^{j+m(j)+1}}.
]

For normalized cluster-entry phase

[
\varpi\in(1/2,1],
]

MATH-179 gives

[
\boxed{
\varpi_j
=
\varpi
\frac{
2^{j+m(j)+\mathbf1_{\{\varpi\le\tau_j\}}}
}{
3^j
}.
}
]

The first-return local cluster length is

[
\boxed{
h_r(\varpi)
=
r+1+m(r)+\mathbf1_{\{\varpi\le\tau_r\}}.
}
]

## 3. Phase-summed paid-penalty lower bound

At the `j`th paid odd event the current paid slack satisfies

[
u_j\ge1.
]

Hence its exact atom

[
p_j
=
\frac{1-2^{-u_j}}3\,\varpi_j
]

obeys

[
\boxed{
p_j\ge\frac{\varpi_j}{6}.
}
]

Therefore

[
\boxed{
\mathcal P_r
\ge
\frac16\sum_{j=0}^{r-1}\varpi_j.
}
]

This retains the entire deterministic MATH-179 phase evolution instead of replacing every paid atom separately by `>1/12`.

Define

[
\boxed{
\underline\epsilon_r
:=
\inf_{\varpi\in(1/2,1]}
\left[
\frac16\sum_{j=0}^{r-1}\varpi_j
-
\lambda h_r(\varpi)
\right].
}
]

Then every exact `r`-paid first-return cluster satisfies

[
\boxed{
\epsilon_r\ge\underline\epsilon_r.
}
]

## 4. Why the infimum is finite and exact

For fixed `r`, split `(1/2,1]` by the finite cut set

[
\left\{\tau_1,\ldots,\tau_r\right\}.
]

Inside each open phase cell:

- every indicator `1_{varpi<=tau_j}` is constant;
- every `varpi_j` is a rational multiple of `varpi`;
- `h_r` is constant.

Thus the displayed surplus lower bound is affine increasing in `varpi` on each cell, and its infimum is its exact rational left-end value.

Every cut point `varpi=tau_j` is also evaluated separately, because the `<=` convention can change one or more phase multipliers there.

Hence the global lower bound is obtained by a finite exact Fraction comparison; no floating-point optimization is used.

## 5. Exact threshold table

Let

[
\boxed{
z_{\min}(r)
:=
\left\lceil
\frac{\underline\epsilon_r}{\lambda}
\right\rceil.
}
]

The exact phase-cell audit gives:

| r | exact `epsilon_r` lower bound | `epsilon_lb/lambda` | necessary `z_min` |
|---:|---:|---:|---:|
| 2 | 101/18108 | 101/684 | 1 |
| 3 | 3643/48288 | 3643/1824 | 2 |
| 4 | 16081/144864 | 16081/5472 | 3 |
| 5 | 80435/386304 | 80435/14592 | 6 |
| 6 | 282521/1158912 | 282521/43776 | 7 |
| 7 | 1262159/4400244 | 1262159/166212 | 8 |
| 8 | 4115809/11733984 | 4115809/443232 | 10 |
| 9 | 13808611/35201952 | 726769/69984 | 11 |
| 10 | 45390185/93871872 | 45390185/3545856 | 13 |
| 11 | 147860027/281615616 | 147860027/10637568 | 14 |
| 12 | 640820381/1069259292 | 640820381/40389516 | 16 |
| 13 | 1873261075/2851358112 | 1873261075/107705376 | 18 |
| 14 | 6640308193/9493807104 | 6640308193/358612992 | 19 |
| 15 | 19551818603/25316818944 | 19551818603/956301312 | 21 |
| 16 | 61356587585/75950456832 | 61356587585/2868903936 | 22 |
| 17 | 183985818883/202534551552 | 183985818883/7650410496 | 25 |
| 18 | 722233984561/768998375424 | 722233984561/29047652352 | 25 |
| 19 | 2262462108307/2306995126272 | 2262462108307/87142957056 | 26 |
| 20 | 6444835761809/6151987003392 | 6444835761809/232381218816 | 28 |
| 21 | 20100588522419/18455961010176 | 20100588522419/697143656448 | 29 |

No ratio in the table is an integer, so the displayed ceilings are unambiguous.

## 6. Exact danger implication

MATH-186 gives, for a singleton overshoot of depth

[
z=L-R>0,
]

the exact lower estimate

[
\Delta\mathcal B
\ge
\epsilon_r-\lambda z
\ge
\underline\epsilon_r-\lambda z.
]

Therefore

[
z<z_{\min}(r)
\Longrightarrow
\Delta\mathcal B>0.
]

Hence a potentially nonpositive `r`-paid singleton transfer must satisfy

[
\boxed{
z\ge z_{\min}(r).
}
]

MATH-193 says exact compatibility of the same overshoot requires

[
\nu_2(C_R)\ge z.
]

Combining them:

[
\boxed{
\text{danger}
\Longrightarrow
\nu_2(C_R)
\ge z
\ge z_{\min}(r).
}
]

Thus every remaining danger corridor is a high-valuation 2-adic resonance.

## 7. The r=10 frontier

For the present low-paid frontier,

[
\boxed{
\underline\epsilon_{10}
=
\frac{45390185}{93871872}.
}
]

Dividing by the MATH-060 slope gives

[
\boxed{
\frac{\underline\epsilon_{10}}{\lambda}
=
\frac{45390185}{3545856}
\approx12.8009104.
}
]

Therefore

[
\boxed{
r=10\text{ danger}
\Longrightarrow
z\ge13
}
]

and by MATH-193,

[
\boxed{
r=10\text{ danger}
\Longrightarrow
\nu_2(C_R)\ge13.
}
]

This sharpens the coarse MATH-185/MATH-186 view substantially.

The remaining `r=10` theorem target is therefore not a 278,725-source scan. It is the structural exclusion of states satisfying simultaneously

[
\boxed{
r_R\le r_{\rm bad},
\qquad
r_R<M,
\qquad
\nu_2(C_R)\ge13,
}
]

together with the exact Hensel/legal-transition constraints.

## 8. Higher paid counts

The carry-valuation threshold rises quickly:

[
\begin{aligned}
r=11&:\quad \nu_2(C_R)\ge14,\\
r=12&:\quad \nu_2(C_R)\ge16,\\
r=13&:\quad \nu_2(C_R)\ge18,\\
r=15&:\quad \nu_2(C_R)\ge21,\\
r=17&:\quad \nu_2(C_R)\ge25,\\
r=20&:\quad \nu_2(C_R)\ge28,\\
r=21&:\quad \nu_2(C_R)\ge29.
\end{aligned}
]

This explains structurally why high-paid layers are easier: any Bellman-dangerous overshoot must carry an increasingly deep exact 2-adic divisibility resonance.

It does not retroactively replace their existing exact closure certificates.

## 9. DSD interpretation

The unresolved condition now factors into three channels:

1. **phase/paid channel** determines the exact threshold `z_min(r)`;
2. **address/carry channel** must realize `nu_2(C_R)>=z_min(r)`;
3. **low-address/master-defect channel** must simultaneously place `r_R` inside the bad prefix.

Thus the remaining `r=10` problem is not an undifferentiated collection of AP sources.

It is the intersection

[
\boxed{
\text{Hensel/legal state}
\cap
\{r_R\le r_{\rm bad}\}
\cap
\{\nu_2(C_R)\ge13\}.
}
]

The next non-enumerative target is to prove that this intersection is empty, or that every nonzero transported carry exits it under the exact MATH-091 recurrence.

## 10. Claim boundary

Established:

- exact finite phase-cell lower bound for every `2<=r<=21`;
- exact `z_min(r)` table;
- exact implication `danger => nu_2(C_R)>=z_min(r)`;
- `r=10` danger requires at least 13 overshoot/carry bits.

Not established:

- exclusion of every `r=10` high-valuation carry state;
- closure of `r=10`;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

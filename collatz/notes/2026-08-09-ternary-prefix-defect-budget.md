# Ternary-prefix defect budgets for the next unresolved resonance

Date: 2026-08-09

Status: **DERIVED CERTIFIED BRANCH-AND-BOUND UPPER CHANNEL**

This note couples the rational next-resonance magnitude certificate to the defect-density channel. It is the first direct project transfer from the recursive-sufficiency ternary digits to a quantitative constraint on the first-crossing defect vector. It supplies only an upper defect budget; a matching zero-lift lower bound is still missing.

## 1. Setup

Use the next unresolved convergent

\[
q=137,528,045,312,
\qquad
\sigma=217,976,794,617.
\]

Let `Lambda_-` and `U_S` be the exact rational bounds from `rational-dk-next-resonance-certificate.md`:

\[
\delta=e^{\sigma\ln2-q\ln3}-1\ge\Lambda_->0,
\]

\[
S^*(q)\le U_S.
\]

For a paradoxical candidate,

\[
S(w)\ge\delta x,
\]

so

\[
\Delta S=S^*-S(w)
\le U_S-\Lambda_-x.
\]

## 2. Prefix-dependent defect budget

In the `m=46` core write

\[
x=4(3^{46}+S)+3,
\qquad
S=\sum_{i=0}^{43}a_i3^i.
\]

Fix any high ternary prefix `p` of the free digits and let

\[
S_{\min}(p)
\]

be the value obtained by setting every unfixed lower digit to zero. Define

\[
\boxed{
X_{\min}(p)=4(3^{46}+S_{\min}(p))+3.
}
\]

Every candidate in this prefix block satisfies `x>=X_min(p)`, hence

\[
\boxed{
\Delta S\le A(p):=U_S-\Lambda_-X_{\min}(p).
}
\]

If `A(p)<0`, the whole ternary prefix block is eliminated by magnitude alone.

Otherwise the general defect-count inequality gives

\[
\boxed{
N_{\ge s}(p)
\le
\left\lfloor
\frac{6A(p)}{1-2^{-s}}
\right\rfloor.
}
\]

This bound is monotone: increasing the ternary prefix value can only decrease `A(p)` and tighten every defect-count allowance.

## 3. Certified high-four-prefix table

The rational magnitude certificate leaves exactly nine possible high-four prefixes

\[
0000,0001,0010,0011,
0100,0101,0110,0111,
1000.
\]

Using the minimum integer in each block gives the following safe `z_i>0` bounds.

| high free trits | minimum start | `N_{>0}` upper bound | required cap-match fraction |
|---|---:|---:|---:|
| 0000 | 35,451,752,478,610,004,383,719 | 14,516,878,922 | >= 89.4444% |
| 0001 | 35,500,383,140,446,232,098,923 | 13,992,454,808 | >= 89.8257% |
| 0010 | 35,597,644,464,118,687,529,331 | 12,943,606,581 | >= 90.5884% |
| 0011 | 35,646,275,125,954,915,244,535 | 12,419,182,467 | >= 90.9697% |
| 0100 | 35,889,428,435,136,053,820,555 | 9,797,061,898 | >= 92.8763% |
| 0101 | 35,938,059,096,972,281,535,759 | 9,272,637,784 | >= 93.2576% |
| 0110 | 36,035,320,420,644,736,966,167 | 8,223,789,556 | >= 94.0203% |
| 0111 | 36,083,951,082,480,964,681,371 | 7,699,365,442 | >= 94.4016% |
| 1000 | 36,764,780,348,188,152,694,227 | 357,427,848 | >= 99.7401% |

The percentages are lower bounds obtained from the rational certificate, not floating assumptions. Within each high-four block, turning on additional lower ternary digits increases `x` and therefore tightens the defect budget further.

## 4. Branch-and-bound interpretation

The 44-digit recursive core can now be traversed as a binary prefix tree. A node `p` carries at least two exact monotone pieces of information:

1. a magnitude status (`outside`, `fully inside`, or partially inside the certified upper interval);
2. an Archimedean defect budget `A(p)` and the resulting integer bounds on `N_{>=s}`.

Thus the candidate problem has a natural paired form

\[
\boxed{
\text{ternary 0/1 prefix}
\longrightarrow
X_{\min}(p)
\longrightarrow
A(p)
\longrightarrow
\text{allowed defect channel}.
}
\]

This is a genuine coupling between the recursive-sufficiency core and the project’s defect representation. No statistical independence is assumed.

## 5. What is still missing

The upper defect budget is not by itself an exclusion theorem. `eventual-mechanical-tail-limit.md` proves that every finite coefficient-surviving prefix admits a formal parity extension whose eventual defect density is zero. Therefore a successful branch-and-bound needs a *lower* defect/lift requirement tied to the same ordinary integer.

A sufficient next object would be a certified function

\[
L(p,K)
\]

such that every ordinary integer represented by ternary prefix `p` and surviving through depth `K` must create at least `L(p,K)` nonzero defect coordinates (or, more directly, a late canonical lift). A block can then be removed whenever

\[
L(p,K)>
\left\lfloor12A(p)\right\rfloor.
\]

No such uniform lower function is yet proved. Establishing one is now the direct anti-alignment target.
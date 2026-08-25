# Gate A1: selector-conditioned Lyapunov contraction and the dense-window scale barrier

Date: 2026-08-25

## Status

- **SAFE LEMMA:** pointwise selector-distortion transfer inequality.
- **FINITE CERTIFICATE:** exact `m=44`, depth `10..25` selector-conditioned Lyapunov audit.
- **BARRIER:** pointwise min/max mixing cannot globalize into the sparse binary-depth regime.
- **OPEN GATE:** replace pointwise dense-regime mixing by a sparse-regime / atom-floor mechanism.

No Collatz proof is claimed.

---

## 1. Setup

For the recursively sufficient layer

\[
F_m=\left\{4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:\ a_i\in\{0,1\}\right\},
\]

write

\[
X_m=3^m+\sum_{i=0}^{m-1}a_i3^i.
\]

Because every `N in F_m` is `3 mod 4`, binary parity depth `B` is represented by the reduced residue

\[
y=(N-3)/4=X_m\pmod{2^{B-2}}.
\]

Let

\[
c_{m,B}(r)=\#\{a\in\{0,1\}^m:X_m\equiv r\pmod{2^{B-2}}\}.
\]

Set

\[
c_{\min}(m,B)=\min_r c_{m,B}(r),
\qquad
c_{\max}(m,B)=\max_r c_{m,B}(r).
\]

The Beatty surplus weight is

\[
W(d)=\left(\frac32\right)^d.
\]

The already-proved unrestricted dyadic macrocycle-pair theorem gives

\[
\boxed{\sigma=\frac{3125}{3456}\approx0.904224537037037}
\]

as a uniform upper bound for the normalized weighted extension factor over every pair of Beatty plateau-to-plateau macrocycles.

---

## 2. Selector-distortion transfer lemma

Fix one parent dyadic residue at depth `B` and a future block of length `L`.
Its `2^L` child residues at depth `B+L` partition the selector mass of that parent.

Assume

\[
0<c_{\min}\le c_{m,B+L}(r)\le c_{\max}
\]

for every child residue.

The selector-conditioned probability of any particular child is at most

\[
\frac{c_{\max}}{2^L c_{\min}}.
\]

Therefore, for every nonnegative child payoff `g`,

\[
\mathbb E_{F_m}[g\mid\text{parent}]
\le
\frac{c_{\max}}{c_{\min}}
\frac1{2^L}\sum_{\text{all children}}g.
\]

Apply this with

\[
g=\frac{W(d_{\rm child})}{W(d_{\rm parent})}
\]

and set `g=0` on coefficient-rejected children.  The Beatty macrocycle theorem then gives

\[
\boxed{
\mathbb E_{F_m}
\left[
\frac{W(d_{\rm out})}{W(d_{\rm in})}
\middle|\text{parent}
\right]
\le
\frac{c_{\max}}{c_{\min}}\sigma.
}
\]

Any additional safe descendant filter, including root-fullmax/Hensel maximality, only deletes nonnegative child contributions and cannot worsen this upper bound.

Hence the sufficient local mixing condition is

\[
\boxed{
\frac{c_{\max}}{c_{\min}}<\frac1\sigma
=\frac{3456}{3125}
\approx1.10592.
}
\]

This is a **SAFE LEMMA**.  It turns Gate A transfer into a concrete static selector-mixing quantity wherever `c_min>0`.

---

## 3. Exact m44 selector mixing through depth 25

The exact cyclic subset-sum DP for all `2^44` selectors gives, at depth 25 (`2^23` reduced residues),

\[
\boxed{c_{\min}=2,092,917},
\qquad
\boxed{c_{\max}=2,102,038}.
\]

Thus

\[
\frac{c_{\max}}{c_{\min}}
=1.00435803235388694
\]

and

\[
\boxed{
\sigma\frac{c_{\max}}{c_{\min}}
=0.908165176824622887<1.
}
\]

The certificate checks the stronger exact integer inequality

\[
3125\,c_{\max}<3456\,c_{\min}
\]

at every audited depth `B=10,...,25`.

So, throughout this finite dense window, **every individual parent cylinder** has selector-conditioned Beatty macro-pair weighted contraction.  This conclusion does not require global averaging over the 128 low ternary masks.

---

## 4. Direct conditioned audit

The same certificate independently computes the actual selector-weighted candidate mass on

1. the coefficient-surviving parity language; and
2. the nested root-fullmax language.

For each complete pair of Beatty macrocycles inside the audited range, the exact weighted ratios are:

| block | length | coefficient-conditioned | root-fullmax-conditioned |
|---|---:|---:|---:|
| `10 -> 16` | 6 | `0.554055721795025929` | `0.545765535866284638` |
| `13 -> 18` | 5 | `0.740394442046909394` | `0.740008361948109357` |
| `16 -> 21` | 5 | `0.777705267089399243` | `0.777809154417480202` |
| `18 -> 24` | 6 | `0.614255159448098621` | `0.614980401795388803` |

Therefore the worst direct values are

\[
\boxed{0.777705267089399243}
\]

for coefficient survival and

\[
\boxed{0.777809154417480202}
\]

for root-fullmax conditioning.

Both are not merely below one but below the unrestricted upper bound `3125/3456`.

This is a **FINITE CERTIFICATE**, not an asymptotic theorem.

---

## 5. Why pointwise selector mixing cannot be the terminal Gate-A theorem

The preceding transfer requires `c_min>0` over all reduced dyadic residues.
But `F_m` has only `2^m` atoms, whereas depth `B` has

\[
2^{B-2}
\]

reduced dyadic residues.

Therefore, by pigeonhole,

\[
\boxed{B-2>m\quad\Longrightarrow\quad c_{\min}(m,B)=0.}
\]

Hence the min/max transfer mechanism necessarily fails once the binary depth becomes larger than the selector dimension.

For a core integer of ternary depth `m`, its ordinary size is about `3^m`, so its natural binary reconstruction scale is

\[
B\asymp m\log_2 3>m.
\]

The first-crossing reconstruction theorem makes the same issue explicit: the binary core needed to reconstruct a bounded paradoxical candidate is `B=O(log sigma)`, while its ternary selector depth is also `m=O(log sigma)` with the natural conversion ratio controlled by `log_2 3`.

Thus **pointwise equidistribution over all dyadic residues cannot be the asymptotic terminal bridge.**

This is a **BARRIER** against over-interpreting the excellent m44/B25 mixing.

---

## 6. Atom-floor closure lemma

Give the `2^m` elements of `F_m` equal mass `2^{-m}`.
For any surviving subset `S`,

\[
S\ne\varnothing
\quad\Longrightarrow\quad
\nu_m(S)\ge2^{-m}.
\]

Therefore

\[
\boxed{
\nu_m(S)<2^{-m}
\quad\Longrightarrow\quad
S=\varnothing.
}
\]

Since `W(d)>=1` on the coefficient-surviving region `d>=0`, the same conclusion follows if a weighted survivor mass falls below `2^{-m}`.

Consequently, if one can prove a fixed-block inequality

\[
L_{j+1}\le\rho L_j,
\qquad \rho<1,
\]

for the **actual layer measure** through enough blocks, then after `O(m)` blocks the weighted mass falls below the atom floor and the entire layer is empty.

In particular, a horizon-uniform block contraction of this kind would imply

\[
\boxed{M_F(m)=O(m),}
\]

which is vastly stronger than the previously sufficient target

\[
\limsup_{m\to\infty}\frac{\log_2 M_F(m)}m<0.1839557220\ldots
\]

and it converts measure decay into an exact finite nonexistence statement without using the invalid implication `measure zero => empty`.

This is a **SAFE LEMMA**.

---

## 7. Revised Gate A

The old phrasing

> transfer dyadic Lyapunov drift to the selector language by uniform pointwise mixing at every depth

is too strong and impossible in the sparse regime.

The revised target is:

### Dense window

Use the selector-distortion lemma wherever

\[
c_{\max}/c_{\min}<3456/3125.
\]

This part is now exact and certified at m44/B<=25.

### Sparse/deep window

Find a different same-integer mechanism that continues to reduce the **finite selector-layer mass** after pointwise dyadic mixing has broken down.

Possible forms include:

- a sparse-support Fourier / large-sieve inequality tailored to the actual survivor set rather than `L^infinity` min/max control;
- root-global Hensel/min-plus restrictions that act directly on selector atoms;
- a recurrence for the recursively sufficient core layers;
- or an arithmetic correlation forced by eventual-zero canonical lift/minimality.

The required terminal statement is no longer generic equidistribution.  It is enough to push each finite `F_m` layer below its atom floor.

---

## 8. Reproducibility

Source:

`collatz/src/dsd_gate_a1_selector_conditioned_lyapunov_certificate.cpp`

Build:

```text
g++ -O3 -std=c++17 -fopenmp dsd_gate_a1_selector_conditioned_lyapunov_certificate.cpp -o gate_a1
```

Expected final line:

```text
PASS
```

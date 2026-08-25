# DSD B-axis convolution transfer lemma

Date: 2026-08-25

## Status

Safe finite lemma plus a structural decomposition of the remaining proof task.

No Collatz proof is claimed.

## 1. Endpoint ternary decoupling

For a coefficient-surviving forward prefix of depth `B`,

\[
y_B=T^B(N)=\frac{3^{q_B}N+R_B}{2^B}.
\]

Fix ternary reverse resolution `Q`.

If

\[
q_B\ge Q,
\]

then modulo `3^Q`,

\[
y_B\equiv 2^{-B}R_B\pmod{3^Q},
\]

because `3^{q_B}N` vanishes modulo `3^Q`.

Coefficient survival gives

\[
3^{q_B}\ge2^B.
\]

Hence a sufficient condition for `q_B>=Q` on every coefficient-surviving prefix is

\[
2^B>3^{Q-1}.
\]

In the current window `Q=7,8,9` and `B>=18`, this is automatic.

Therefore the reverse-potential lookup at the endpoint is independent of the fixed low-ternary selector mask.  The dynamical survivor/death set can be regarded as a subset of the dyadic root-residue group alone.

This is the key decoupling needed for a convolution argument.

## 2. Selector group and two distributions

Work in

\[
G=\mathbb Z/2^L\mathbb Z,
\qquad L=H-2=22,
\]

using

\[
z=(N-3)/4.
\]

Let `A_B subset G` be the dyadic root residues surviving the root-fullmax and reverse tests through dynamical depth `B`.

For a fixed low-ternary cylinder `ell=(a_0,...,a_{Q-1})`, the high selectors `a_Q,...,a_{m-1}` induce a multiplicity function

\[
h_{m,Q}(x)
\]

on `G`.

The cylinder survivor mass is a translate-convolution

\[
M_B(\ell)=\sum_{x\in A_B}h_{m,Q}(x-s_\ell),
\]

where `s_ell` is the fixed shift contributed by the low selector digits and by `3^m`.

Let

\[
h_{\min}=\min_x h_{m,Q}(x),
\qquad
h_{\max}=\max_x h_{m,Q}(x).
\]

Then for every translate and every set `A`,

\[
h_{\min}|A|\le M_A(\ell)\le h_{\max}|A|.
\]

Similarly let `c_m(x)` be the multiplicity function for all `m` selector digits and define

\[
c_{\min}=\min_x c_m(x),
\qquad
c_{\max}=\max_x c_m(x).
\]

If `T_A` is the total selector mass of a dyadic set `A`, then

\[
c_{\min}|A|\le T_A\le c_{\max}|A|.
\]

## 3. Uniform contraction lemma

Let

\[
D=A_B\setminus A_{B+r}
\]

be the newly killed dyadic set.

Write

\[
T_B=T_{A_B},
\qquad
T_D=T_B-T_{B+r}.
\]

From the full-selector bounds,

\[
|D|\ge\frac{T_D}{c_{\max}},
\qquad
|A_B|\le\frac{T_B}{c_{\min}}.
\]

For every low-ternary cylinder,

\[
\frac{M_D(\ell)}{M_B(\ell)}
\ge
\frac{h_{\min}}{h_{\max}}
\frac{c_{\min}}{c_{\max}}
\frac{T_D}{T_B}.
\]

Define

\[
\kappa_{m,Q,L}
=
\frac{h_{\min}}{h_{\max}}
\frac{c_{\min}}{c_{\max}},
\]

and

\[
\eta_{Q,B,r}
=
\frac{T_B-T_{B+r}}{T_B}.
\]

Then the worst-cylinder survivor ratio obeys the exact bound

\[
\boxed{
\frac{M_{B+r}(\ell)}{M_B(\ell)}
\le
1-\kappa_{m,Q,L}\eta_{Q,B,r}
}
\]

for every cylinder `ell` with positive mass.

This converts a global dynamical loss into a cylinder-uniform loss using only static selector mixing.

## 4. Exact selector-DP constants at m=44, H=24

The accompanying certificate computes the cyclic subset-sum multiplicities exactly modulo `2^22`.

For all 44 selector digits:

- `c_min = 4,188,525`
- `c_max = 4,199,983`
- `c_min/c_max = 0.997271893719569817`

For high selectors only:

### Q=7

- `h_min = 32,039`
- `h_max = 33,523`
- `h_min/h_max = 0.9557318855711004`
- `kappa = 0.953124547411666539`

### Q=8

- `h_min = 15,871`
- `h_max = 16,878`
- `h_min/h_max = 0.9403365327645455`
- `kappa = 0.937771194763792663`

### Q=9

- `h_min = 7,826`
- `h_max = 8,584`
- `h_min/h_max = 0.9116961789375583`
- `kappa = 0.909208974865954496`

The selector distribution is therefore sufficiently flat that a global dynamical loss of about 3 percent transfers to every low-ternary cylinder with only a small degradation.

## 5. Derived B-axis contraction without per-cylinder enumeration

Using the independently certified global totals from `dsd_b_axis_h24_contraction_certificate.cpp`:

### B18 -> B20

- Q7 derived upper: `0.971889693431788140`
- Q8 derived upper: `0.970923008762487762`
- Q9 derived upper: `0.970858670434963536`

### B20 -> B22

- Q7 derived upper: `0.968427393093597880`
- Q8 derived upper: `0.968165043540233182`
- Q9 derived upper: `0.968535348824879155`

Therefore, without using the previously enumerated per-cylinder maxima, the convolution lemma alone proves on the tested window

\[
\boxed{
M_{B+2}(\ell)<0.972\,M_B(\ell)
}
\]

for `Q in {7,8,9}` and `B in {18,20}`.

The direct per-cylinder certificate gives slightly stronger numerical maxima, as expected, but is no longer logically necessary for proving that a uniform contraction exists on this finite window.

Source:

`collatz/src/dsd_b_axis_uniform_convolution_bound.cpp`

## 6. DSD logical-chain interpretation

The calculation now factors into two largely independent channels.

### Static / describability channel

Selector digits -> cyclic subset-sum distribution -> mixing factor `kappa`.

### Dynamic channel

Root-surviving parity language -> reverse potential -> newly killed density `eta`.

They close through

\[
\delta=\kappa\eta.
\]

Thus the full desired theorem can be reduced to proving two uniform lower bounds:

1. **Static mixing:** there is `kappa_0>0` such that `kappa_{m,Q,L}>=kappa_0` in the chosen scaling regime.
2. **Dynamic loss:** there are fixed `r` and `eta_0>0` such that `eta_{Q,B,r}>=eta_0` for all sufficiently large admissible scales.

Then automatically

\[
M_{B+r}(\ell)
\le
(1-\kappa_0\eta_0)M_B(\ell)
\]

for every cylinder, and iteration gives exponential extinction.

This is substantially sharper than asking directly for a uniform worst-cylinder estimate at every depth.

## 7. Next proof targets

The two remaining analytic tasks are now explicit.

### A. Static mixing lemma

For

\[
h_{m,Q,L}(x)
=[X^x]\prod_{i=Q}^{m-1}(1+X^{3^i})
\quad\text{in }\mathbb Z[X]/(X^{2^L}-1),
\]

prove a lower bound on `h_min/h_max` in a regime where the number of high selector digits exceeds the dyadic resolution by a controlled margin.

A Fourier formulation is

\[
\left|\widehat\nu(t)\right|
=
\prod_{i=Q}^{m-1}
\left|\cos\left(\frac{\pi t3^i}{2^L}\right)\right|,
\qquad t\ne0.
\]

A uniform decay estimate for these products would yield pointwise mixing.

### B. Dynamic-loss lemma

Prove that a fixed positive fraction of the globally surviving dyadic language acquires a reverse-potential witness within a bounded number `r` of additional dynamical steps.

The current finite data suggest `r=2` as the first candidate, but no asymptotic lower bound on `eta` has yet been proved.

The decisive proof problem is therefore no longer an undifferentiated Collatz survivor count.  It is the pair

\[
\boxed{
\text{selector mixing }\kappa_0>0
\quad+\quad
\text{bounded-block dynamic loss }\eta_0>0.
}
\]

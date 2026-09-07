# MATH-031 — exact 22-step tail descriptor + cyclic-window address prefilter

Date: 2026-09-08

Status:

`CONFIRMED / EXACT FINITE PREFILTER / COMPUTATIONAL ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Motivation

After MATH-030, prefix-memory pressure is no longer the main bottleneck.  The dominant finite continuation cost comes from instantiating the 339 internal right-side address labels

\[
b=1025,\ldots,1363
\]

for every depth-61 right-offset survivor.

MATH-031 extends the MATH-011 complete-descriptor/cyclic-window idea from 11 tail steps to 22 tail steps.

## 22-step complete descriptor

For

\[
u=n\bmod2^{22}
\]

let

- `s22(u)` be the number of odd shortcut steps in the next 22 steps;
- `c22(u)` be the exact affine correction;
- `H22(u)` be the minimum current odd-count `q` required to satisfy every coefficient-survival threshold through depths 62..83.

Then

\[
\boxed{q\ge H_{22}(u)}
\]

is equivalent to survival of all 22 local coefficient gates, and if it holds,

\[
\boxed{
T^{22}(n)=\frac{3^{s_{22}(u)}n+c_{22}(u)}{2^{22}}
}
\]

with

\[
q'=q+s_{22}(u).
\]

The certificate exhaustively checks all

\[
2^{22}=4,194,304
\]

residues against the exact composition of two previously audited 11-step blocks.  For every residue it verifies the same threshold, total odd-count, and affine correction.

## Address cyclic-window transform

At depth 61, for one fixed right-offset state `(q,y)`, the address-lifted endpoint is

\[
n_b=y+b3^q.
\]

Set

\[
m=3^q\pmod{2^{22}}
\]

and let

\[
z=m^{-1}y\pmod{2^{22}}.
\]

Because `m` is odd,

\[
n_b\equiv m(z+b)\pmod{2^{22}}.
\]

Hence the 339 address labels become the contiguous cyclic window

\[
z+1025,\ldots,z+1363
\]

in transformed coordinates.

Defining

\[
g_q(t)=\mathbf1[H_{22}(mt)\le q],
\]

all 339 depth-83 survival tests reduce to one length-339 cyclic range query.

## Exact finite result at RMAX=1e9

MATH-028/030 has

\[
\boxed{1,796,718}
\]

depth-61 right-offset survivors.

Instantiating all 339 internal address labels would create

\[
1,796,718\cdot339
=\boxed{609,087,402}
\]

raw address states.

The exact 22-step cyclic-window prefilter leaves only

\[
\boxed{189,767,400}
\]

states that survive coefficient gates through depth 83.

Thus the address-state instantiation layer is reduced by

\[
\frac{609,087,402}{189,767,400}
\approx\boxed{3.20965}.
\]

This is a finite computational reduction.  It does not make a new global Collatz claim.

## q61 breakdown

| q61 | depth-61 leaves | address states surviving to depth83 | average labels per leaf |
|---:|---:|---:|---:|
|39|386,049|5,764,074|14.93|
|40|494,858|26,716,059|53.99|
|41|396,655|43,543,702|109.78|
|42|257,324|44,809,331|174.14|
|43|142,623|33,473,148|234.70|
|44|69,940|19,717,995|281.93|
|45|30,831|9,632,832|312.44|
|46|12,101|3,977,507|328.69|
|47|4,370|1,467,235|335.75|
|48|1,430|483,539|338.14|
|49|384|130,113|338.84|
|50|115|38,983|338.98|
|51|33|11,187|339.00|
|52|5|1,695|339.00|

The strongest benefit is concentrated in the low-surplus `q61` states, as expected from MATH-006/011.

## DSD interpretation

MATH-031 is another case where a complete descriptor is used as a calculation gate rather than post-hoc metadata:

\[
(q,n)
\longrightarrow
(q,u=n\bmod2^{22})
\longrightarrow
H_{22}(u)
\]

for the local survival decision, while the full exact `n` is retained for any state that survives and must be propagated further.

Thus the residue is used only to select an exact local affine transition; it never replaces the exact propagated ordinary endpoint.

## Scope boundary

- The 22-step descriptor is complete only for its 22-step local window.
- The `3.20965x` ratio is specific to the finite `RMAX=10^9`, 339-address dataset.
- It is not a density theorem and not a universal compression factor.
- Address states surviving depth 83 remain open for deeper continuation.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_tail22_cyclic_window_prefilter_certificate.cpp`

Certificate commit:

`63e23a7e598fbd30118ce4717f23bd36acf5ac5d`

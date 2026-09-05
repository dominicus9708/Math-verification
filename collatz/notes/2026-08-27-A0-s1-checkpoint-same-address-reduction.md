# A0 s=1 bridge: finite checkpoint same-address reduction

Date: 2026-08-27

Status: **SAFE exact boundary reduction.** This uses the newly certified `2^72<Z<2^73` checkpoint shell. It does not prove the Collatz conjecture.

## 1. Split

In the hard sector

\[
s=1,
\]
set

\[
t_0=10J_0,
\qquad
j_0=10R_0+1,
\]

and split the A0 block as

\[
X\xrightarrow[t_0]{j_0\text{ odd}} Z
\xrightarrow[U]{P-1\text{ odd}}Y,
\]

where

\[
A_0=t_0+U,
\qquad
Q_0=j_0+(P-1).
\]

The previous exact-rational theorem gives

\[
\boxed{2^{72}<Z<2^{73}}.
\]

The physical start/end satisfy

\[
X<2^{72},
\qquad
Y<2^{72}.
\]

## 2. Pre block: 72-bit start + 47-trit endpoint

A length-72 parity prefix determines one residue modulo `2^72`. Since `X<2^72`, the first 72 parity symbols of the pre block determine the ordinary integer `X` exactly.

For the endpoint, write the pre affine identity

\[
2^{t_0}Z=3^{j_0}X+R_{\rm pre}.
\]

Reduce modulo `3^47`. Since `j0>47`, the start term vanishes. Every correction term except the last 47 odd ordinals also vanishes. Thus those last 47 odd positions determine

\[
Z\pmod{3^{47}}.
\]

Exact integer comparison gives

\[
\boxed{3^{47}>2^{73}>Z}.
\]

Hence the least nonnegative residue is `Z` itself.

Therefore the pre block is a finite-two-ended boundary object:

\[
\boxed{
\text{first 72 parity bits}
\quad|\quad
\text{long pre bridge}
\quad|\quad
\text{last 47 odd positions}
}
\]

with both ordinary boundaries fully exposed.

## 3. Tail block: 73-bit start + 46-trit endpoint

The tail begins at `Z<2^73`. Therefore its first 73 parity symbols determine

\[
Z\pmod{2^{73}},
\]
which is exactly the ordinary integer `Z`.

The tail has `P-1` odd events, far more than 46. Reducing its affine identity modulo `3^46` removes the start term and all but the last 46 odd corrections. Since

\[
Y<2^{72}<3^{46},
\]
those last 46 odd positions determine the complete ordinary endpoint `Y`.

Thus the tail is also a finite-two-ended object:

\[
\boxed{
\text{first 73 parity bits}
\quad|\quad
\text{long tail bridge}
\quad|\quad
\text{last 46 odd positions}.
}
\]

## 4. Same-address checkpoint condition

Define

\[
\mathcal Z_{\rm pre}
\]

to be the set of ordinary checkpoint values `Z` produced by coefficient-surviving s=1 pre words with the allowed physical start band.

Define

\[
\mathcal Z_{\rm tail}
\]

to be the set of ordinary start values `Z` accepted by s=1 tail words ending in the allowed physical endpoint band.

Every full s=1 A0 candidate must satisfy

\[
\boxed{
Z\in
\mathcal Z_{\rm pre}
\cap
\mathcal Z_{\rm tail}
\cap
(2^{72},2^{73}).
}
\]

Conversely, after fixing the same ordinary `Z`, a compatible pre word and tail word concatenate without an additional checkpoint ordering obstruction: the previous s=1 factorization proved that the cross-checkpoint ordering condition is automatic.

The remaining full candidate must additionally satisfy the already-known physical `X,Y` relation for the particular A0 return. Thus checkpoint equality is the central bridge condition, not by itself the final near-return condition.

## 5. Why this is stronger than a carry quotient

The shared object is an **ordinary integer** `Z`, not a residue class used beyond its exposure depth.

Once 73 dyadic bits expose `Z`, no horizon leakage remains in the statement

\[
Z_{\rm pre}=Z_{\rm tail}.
\]

This does not assert that the internal long bridges can be simulated with a fixed 73-bit Hensel carry quotient. They cannot. The finite address is only a physical boundary anchor.

## 6. DSD state architecture

The hard branch now has the three ordinary nodes

\[
\boxed{
X<2^{72}
\longrightarrow
2^{72}<Z<2^{73}
\longrightarrow
Y<2^{72}
}
\]

and two long structural edges.

For each edge, short boundary addresses expose both endpoint integers exactly, while the long interior is represented by the anchored mechanical/Christoffel language.

Thus the DSD descriptor graph is

\[
\boxed{
\text{finite ordinary boundary}
\to
\text{long ordered structural bridge}
\to
\text{finite ordinary boundary}.
}
\]

The two edges communicate only through equality of the ordinary checkpoint `Z` plus the s=1 ordering interface already audited.

## 7. Next gate

The immediate target is an address-intersection certificate:

1. derive a compact description of the pre-side 73-bit checkpoint address set;
2. derive a compact description of the tail-side 73-bit checkpoint start-address set;
3. prove disjointness, or identify the surviving checkpoint classes;
4. only for survivors, restore the exact physical `Y-X` / reset-gap condition.

Finite scans at boundary depth are admissible as regression or exact finite-address certificates, but they must not be promoted to closure of the long bridge unless coefficient-survival constraints for the whole corresponding edge are retained.

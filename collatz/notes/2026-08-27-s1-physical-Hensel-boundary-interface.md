# s=1 physical Hensel boundary interface and checkpoint compression

Date: 2026-08-27

Status: **SAFE exact boundary theorem + proof-architecture correction.** This note does not prove the Collatz conjecture.

## 1. Purpose

The finite-depth Hensel hierarchy has one formal zero-penalty residue cylinder at every depth.  A positive proof-level Hensel lower bound therefore cannot be obtained by minimizing over an arbitrary boundary carry.

The missing question is not whether an internal Hensel carry can be reconstructed from its own control sequence.  That would be circular.  The correct question is:

> what are the Hensel boundary carries supplied independently by the actual Collatz start and endpoint?

This note fixes that interface exactly.

## 2. Exact affine identity

For a length-`A` accelerated Collatz word with `q` odd positions

\[
0\le a_1<\cdots<a_q<A,
\]

write the start as `X` and endpoint as `Y`.  The exact affine identity is

\[
\boxed{
2^A Y
=
3^q X
+
\sum_{j=1}^q3^{q-j}2^{a_j}.
}
\]

Let the mechanical positions be `b_j` and write

\[
a_j=b_j-d_j.
\]

Traverse the odd ordinals from right to left.  For

\[
i=0,\ldots,q-1,
\]

put

\[
e_i:=b_{q-i}-A.
\]

Then the normalized Hensel term is

\[
2^{e_i-d_{q-i}}=2^{a_{q-i}-A}\in\mathbb Z_3^\times.
\]

## 3. Physical boundary carry theorem

Define the right boundary carry by

\[
\boxed{K_0=-Y.}
\]

Use the stored zero-target recurrence

\[
\boxed{
K_{i+1}
=
\frac{K_i+2^{a_{q-i}-A}}{3}.
}
\]

Unrolling gives

\[
3^iK_i
=
-Y
+
2^{-A}
\sum_{\ell=0}^{i-1}
3^\ell2^{a_{q-\ell}}.
\]

At full depth `i=q`, the affine identity gives

\[
3^qK_q
=
-Y+2^{-A}R
=
-3^q2^{-A}X.
\]

Hence

\[
\boxed{
K_q=-2^{-A}X.
}
\]

Therefore the complete physical two-boundary Hensel problem has externally supplied carries

\[
\boxed{
K_{\rm right}=-Y,
\qquad
K_{\rm left}=-2^{-A}X.
}
\]

Both are independent of the defect cost.  The factor `2^{-A}` is a 3-adic unit and is well-defined.

This also reconciles the earlier terminal notation

\[
c_m=(Y_m-Y)/3^m:
\]
`c_m` is exactly the Hensel carry after the final `m` odd ordinals have been traversed.

## 4. Why the internal checkpoint carry is not an external datum

For an internal split after `m` terminal odd ordinals,

\[
\boxed{
K_m
=
\frac{Y_m-Y}{3^m}.
}
\]

This depends on the terminal displacement controls used to form `Y_m`.

Therefore it is **not** legitimate to define an allegedly independent set of checkpoint carries by using

\[
K_0\equiv-
\sum_{i=0}^{h-1}3^iu_i(d_i)
\pmod{3^h}
\]

and then test the same controls for Hensel compatibility.  That is an internal compatibility identity, not an external boundary theorem.

The safe architecture is instead:

\[
(X,Y)
\longrightarrow
(K_{\rm left},K_{\rm right})
\longrightarrow
\text{two-boundary Hensel path}.
\]

The internal carry is optimized over only inside that boundary-preserving path.

## 5. Exact s=1 checkpoint geometry

At the tenth-J0 checkpoint

\[
t_0=10J_0,
\qquad
j_0=10R_0+1.
\]

For the first-resonance rational mechanical word,

\[
n_j
=
\left\lfloor\frac{(j-1)A_0}{Q_0}\right\rfloor+1.
\]

Exact integer arithmetic gives

\[
\boxed{
n_{j_0}=t_0,}
\]

and

\[
\boxed{
n_{j_0+1}=t_0+2.}
\]

Also

\[
\boxed{
Q_0-j_0=P-1=6,189,245,290.
}
\]

The hard low-surplus condition is

\[
s=1
\iff
\tau_{j_0}\le t_0<\tau_{j_0+1}.
\]

Since

\[
\tau_{j_0+1}=n_{j_0+1}-d_{j_0+1}
=t_0+2-d_{j_0+1},
\]

the strict right-hand inequality gives

\[
\boxed{
d_{j_0+1}\in\{0,1\}.}
\]

Thus, in the right-to-left two-block composition, the ordering-memory component at the tenth-J0 interface satisfies

\[
\boxed{p_{\rm int}\in\{0,1\}.}
\]

This is an exact two-state interface compression obtained from `s=1` alone.  It uses neither Hensel cost nor the near-root defect budget.

The carry component `K_int` is not similarly fixed by `s=1`; it must be transmitted by the terminal block from the physical right boundary.

## 6. Physical terminal boundary excludes the zero-cost cylinder by depth 45

For the first global resonance the independent endpoint theorem gives

\[
2^{71}<Y,
\qquad
3Y<4\cdot2^{71}+3\cdot2^{33},
\qquad
Y\equiv3\pmod4.
\]

Let `Y_m(0)` be the terminal mechanical residue with zero displacements in the last `m` odd ordinals.

Exact modular calculation gives at depth 44

\[
Y_{44}(0)
\equiv
760020657836519755297
\pmod{3^{44}},
\]

and there is still one endpoint in the allowed channel:

\[
\boxed{
Y=2729562462203742221059.
}
\]

At depth 45,

\[
Y_{45}(0)
\equiv
1744791560020130988178
\pmod{3^{45}},
\]

but **no** integer in the allowed endpoint channel has this residue.

Therefore

\[
\boxed{
\text{the physical right boundary misses the terminal zero-displacement cylinder by depth }45.
}
\]

Equivalently, every physical first-resonance path has at least one nonmechanical displacement among the final 45 odd ordinals.

At depth 46 the mechanical residue becomes the complete ordinary mechanical endpoint

\[
Y_{46}(0)=4699104266570964686821,
\]

which is above the allowed endpoint ceiling.  This agrees with the existing two-ended exposure theorem and the stronger terminal support ladder.

The finite-depth statement is only a boundary mismatch theorem.  It does not by itself supply a global defect large enough to close the resonance.

## 7. Correct s=1 two-boundary target

The earlier tentative target

\[
\mathcal K_{s=1,h}\cap[\Theta_h]_{3^h}
\]

is incomplete if `K_{s=1,h}` is meant to be an independently prescribed **internal** carry set.  `s=1` does not provide such a set.

The corrected object is the full physical two-boundary minimum:

\[
\boxed{
\inf_{
\substack{
X,Y\text{ in the physical start/end channels},\\
\text{s=1 Hensel/ordering paths}
}}
D.
}
\]

The external carry data are

\[
K_R=-Y,
\qquad
K_L=-2^{-A_0}X,
\]

and the tenth-J0 interface is minimized over

\[
\boxed{(K_{\rm int},p_{\rm int}),\qquad p_{\rm int}\in\{0,1\}.}
\]

Thus the no-transport decomposition is now more precise:

\[
\boxed{
\text{physical right boundary}
\to
\text{tail transfer}
\to
(K,0)\text{ or }(K,1)
\to
\text{pre transfer}
\to
\text{physical left boundary}.
}
\]

This is the boundary-preserving object that should be compressed through the `10 J0 + U` / Christoffel hierarchy.

## 8. Circularity audit

### SAFE direction

\[
\text{exact Collatz affine identity}
\to
(K_R,K_L)
\to
\text{Hensel admissibility}
\to
\text{two-boundary lower cost}
\to
\text{only then compare with near-root budget}.
\]

Separately,

\[
s=1
\to
\text{checkpoint count}
\to
p_{\rm int}\in\{0,1\}.
\]

### REJECTED direction

Do not use

\[
3^hK_h=K_0+\sum3^iu_i(d_i)
\]

to manufacture an “external” checkpoint carry set and then reuse it to certify the same `d_i` controls.

Do not use the numerical defect budget to choose or prune boundary carry residues.

Do not interpret finite-depth endpoint compatibility as existence of an infinite positive-integer Collatz trajectory.

## 9. Status and next gate

### SAFE

- physical right boundary carry `K_R=-Y`;
- physical left boundary carry `K_L=-2^{-A}X`;
- internal carry formula `K_m=(Y_m-Y)/3^m`;
- `s=1` interface compression `p_int in {0,1}`;
- terminal mechanical zero-cost cylinder survives through depth 44 but is excluded at depth 45 by the independent endpoint channel.

### OPEN

- an efficient lower certificate for the full two-boundary transfer between the physical endpoint/start boundary sets;
- propagation through the huge tail/pre blocks while retaining the two interface classes `p=0,1`;
- an amortized Hensel/alignment-cost theorem strong enough to approach the independent `D<0.981G` reset budget in the repeated-A0 branch.

The immediate algorithmic target is no longer to invent an internal `K` set.  It is to construct a **boundary-set transfer operator** whose right and left carry sets come from actual endpoint/start channels and whose tenth-J0 interface has only the two ordering states `p=0,1`.

Companion certificate:

`collatz/src/s1_physical_hensel_boundary_interface_certificate.py`

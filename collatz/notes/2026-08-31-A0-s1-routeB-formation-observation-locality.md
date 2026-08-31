# A0 s=1 Route-B formation observation locality

Date: 2026-08-31

Status: **exact projective theorem / G4-FR reduction**.

This note follows the bounded-drop formation-run theorem.  It isolates what
increasing ternary observation depth can and cannot change.

No global Collatz conclusion is claimed.

---

## 1. Sparse source residue

For a fixed weakly decreasing formation path of total depth `K`, let strict
rank drops occur at transition positions

\[
p_1<\cdots<p_s
\]

with rank levels

\[
b_{i-1}\to b_i.
\]

The sparse correction identity gives

\[
D_K
=
\sum_{i=1}^{s}
2^{K-p_i}3^{p_i}
\left(2^{b_{i-1}}-2^{b_i}\right).
\]

The unique source residue is

\[
\rho_K\equiv-2^{-K}D_K\pmod{3^K}.
\]

The powers of 2 cancel termwise:

\[
\boxed{
\rho_K
\equiv
-
\sum_{i=1}^{s}
3^{p_i}2^{-p_i}
\left(2^{b_{i-1}}-2^{b_i}\right)
\pmod{3^K}.
}
\]

Here every `2^{-p_i}` is interpreted in the corresponding ring modulo a power
of 3.

---

## 2. Formation Observation Locality Theorem

Let `m<=K`, and let `rho_m` be the source residue of the first `m` formation
transitions of the same path.

Reducing the previous formula modulo `3^m`, every strict drop with

\[
p_i\ge m
\]

vanishes identically because its term contains `3^m`.

The remaining terms are exactly the sparse formula for the length-`m` prefix.
Therefore

\[
\boxed{
\rho_K\equiv\rho_m\pmod{3^m}.
}
\]

Equivalently:

> The source residue visible at ternary depth `m` depends only on strict rank
> drops occurring before position `m`.  No later formation event and no choice
> of total future depth can alter already exposed ternary digits.

This is an exact theorem, not a finite stabilization observation.

---

## 3. Exact cylinder nesting

Since both residues are chosen canonically,

\[
0\le\rho_K<3^K,
\qquad
0\le\rho_m<3^m,
\]

there is a unique

\[
0\le\nu_{m,K}<3^{K-m}
\]

with

\[
\boxed{
\rho_K=\rho_m+3^m\nu_{m,K}.
}
\]

Hence a member of the deeper source family

\[
c_0=\rho_K+3^K n
\]

can be rewritten as

\[
\boxed{
c_0
=
\rho_m
+3^m
\left(
\nu_{m,K}+3^{K-m}n
\right).
}
\]

Thus every deeper formation cylinder is literally an arithmetic sub-cylinder
of the prefix cylinder.

Increasing observation depth therefore performs exact refinement:

\[
\boxed{
\mathcal C_K\subseteq\mathcal C_m.
}
\]

No previously admitted ternary digit is revised.

---

## 4. Structural versus arithmetic refinement

The bounded-drop theorem already showed that at fixed initial rank `k` there
are at most `k` strict rank drops.

The locality theorem now separates refinement into two mechanisms.

### Structural refinement

A new strict drop occurs.

This can happen at most `k` times and strictly decreases the well-founded rank

\[
R_{\rm form}=a.
\]

### Arithmetic refinement

Observation depth grows while the strict-drop skeleton does not change.

Then no new structural branch is introduced.  The already fixed sparse terms
are merely evaluated to one additional ternary digit, and a same-rank run is
advanced by its exact jump

\[
3^{\ell}n\mapsto2^{\ell}n.
\]

Therefore an unbounded ternary observation depth is not by itself an infinite
semantic branching obstruction on the formation side.

It may represent unbounded **precision**, but not unbounded **structural rank
choice**.

---

## 5. Projective signature

For a path `w` of depth at least `m`, define

\[
\boxed{
\pi_m(w)=\rho(w)\bmod3^m.
}
\]

Then for every deeper prefix depth `K>=m`,

\[
\boxed{
\pi_m(w_{\le K})
=
\pi_m(w_{\le m}).
}
\]

Consequently the family

\[
(\pi_1,\pi_2,\ldots)
\]

is projectively compatible:

\[
\pi_{m+1}\equiv\pi_m\pmod{3^m}.
\]

The formation source cylinders therefore define a coherent 3-adic refinement
chain whenever a rank/run path is prolonged.

### Important limitation

The scalar residue `rho_m` is **not** claimed to be a complete future
right-congruence state.

Future block composition also depends on the current boundary rank and on the
outgoing carry coordinate `gamma_m`.  The exact compositional macrostate
remains

\[
(m,a_m,\rho_m,\gamma_m)
\]

or an equivalent run-compressed representation.

The locality theorem concerns the nested source-residue projection, not all
future semantics.

---

## 6. Consequence for G4-FR

The variable-target / formation-run intersection problem no longer has to
worry that deeper formation analysis might invalidate earlier source-residue
information.

At depth `m`, the formation side supplies a finite union of exact residues

\[
\mathcal T_{k,m}\subseteq\mathbb Z/3^m\mathbb Z.
\]

Going to `m+1` only splits members of those existing residue cylinders; it does
not create a residue whose reduction modulo `3^m` was previously excluded.

Thus the remaining question lies on the **physical target side**:

> Does the physical/Route-B target family admit a compatible projective
> description modulo `3^m`, or at least a controlled renewal rule, as the cut
> increases?

If the physical target has compatible projections

\[
t_{m+1}\equiv t_m\pmod{3^m},
\]

then target-versus-formation matching can be audited incrementally with no
retroactive formation ambiguity.

If it does not, the exact failure term can be isolated on the target side
rather than attributed to the formation automaton.

---

## 7. DSD audit

✅ old ternary information is stable under deeper formation observation;

✅ later strict drops are invisible below their 3-adic position;

✅ deep source cylinders are exact sub-cylinders of prefix cylinders;

✅ structural refinement is bounded by the initial rank;

✅ arithmetic precision growth between structural changes is deterministic;

✅ projective formation signatures are exact;

⚠️ `rho_m` alone is not a complete future semantic state;

⚠️ the physical variable target has not yet been proved projectively
compatible;

⚠️ no uniform bound on required target observation depth is proved here;

❌ no Route-B global closure or Collatz conclusion is claimed.

## Revised immediate target

The next calculation is now sharply localized:

\[
\boxed{
\textbf{G4-FR2: physical-target projective compatibility / defect law.}
}
\]

We should derive the target residue at consecutive ternary observation depths
and determine whether it

1. projects exactly;
2. projects after a known affine normalization; or
3. has an explicit defect term whose size/valuation can be controlled.

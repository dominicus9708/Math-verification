# Global future reachability cutoff for the directed `P_min` gate

Status: **EXACT theorem / finite jump-8 partition certified separately**

## Purpose

The current exact prefix defect is already carried by

\[
\eta_q=\frac{N_q}{3^q}.
\]

A future one-event of global rank `r` at actual position `a_{r-1}` contributes

\[
\epsilon_r
=\frac{2^{t_{r-1}}-2^{a_{r-1}}}{3^r}\ge0.
\]

The directed physical gate, after dividing its integer score by `3^q`, is

\[
M_{lo}\,\eta+\Delta_{lo}X>B,
\]

where `M_lo`, `Delta_lo`, and `B=L_MAX*QFP+cW_hi` are the already-certified directed constants.

This note gives a source-value cutoff below which **no possible future continuation can ever make this gate fire**.

---

## 1. Total target correction in normalized defect coordinates

Let the full Route-B target have total length `t0` and odd count `j0`, with target one-positions

\[
t_0<t_1<\cdots<t_{j_0-1}.
\]

Its correction is

\[
C_T=\sum_{r=1}^{j_0}3^{j_0-r}2^{t_{r-1}}.
\]

Hence

\[
\boxed{
\frac{C_T}{3^{j_0}}
=\sum_{r=1}^{j_0}\frac{2^{t_{r-1}}}{3^r}.
}
\]

The Christoffel real-envelope certificate supplies outward fixed-point bounds

\[
\frac{C_T}{2^{t_0}}\le \frac{cW_{hi}}{QFP},
\qquad
\frac{3^{j_0}}{2^{t_0}}\ge \frac{mW_{lo}}{QFP}>0.
\]

Therefore

\[
\boxed{
\frac{C_T}{3^{j_0}}
\le
U_T:=\frac{cW_{hi}}{mW_{lo}}.
}
\]

No floating-point approximation is used in this inequality.

---

## 2. Future-defect absolute upper bound

At a current prefix with odd count `q`, define the exact target-prefix sum

\[
A_q:=\sum_{r=1}^{q}\frac{2^{t_{r-1}}}{3^r}.
\]

Every future displacement atom satisfies

\[
0\le\epsilon_r
<\frac{2^{t_{r-1}}}{3^r}.
\]

Consequently every completion through the fixed total odd count `j0` satisfies

\[
\boxed{
\eta_{future}
< U_q:=U_T-A_q.
}
\]

`U_q` is source-independent once `q` is fixed.  It is an absolute ceiling: it assumes the actual future one-position contribution can be discarded completely, so no legal continuation can exceed it.

---

## 3. `P_min`-unreachable source values

For a current exact source state with defect `eta_q=N_q/3^q`, define

\[
\boxed{
X_{noP}(q,N_q)
:=
\frac{B-M_{lo}(\eta_q+U_q)}{\Delta_{lo}}.
}
\]

Because `Delta_lo>0`, every ordinary source value satisfying

\[
X\le X_{noP}
\]

obeys, for every future completion,

\[
M_{lo}(\eta_q+\eta_{future})+\Delta_{lo}X
<
M_{lo}(\eta_q+U_q)+\Delta_{lo}X
\le B.
\]

Hence

\[
\boxed{
X\le X_{noP}
\Longrightarrow
\text{the directed }P_{min}\text{ gate can never reject this }X
\text{ at any future depth.}
}
\]

This is not a survivor proof.  It only proves that this particular directed physical predicate is permanently unavailable on that source-value region.

---

## 4. Exact partition of an affine source cylinder

For

\[
X=r+2^h m,
\qquad m\in[m_{lo},m_{hi}],
\]

let

\[
m_{noP}
=
\left\lfloor
\frac{X_{noP}-r}{2^h}
\right\rfloor.
\]

Then the live interval splits exactly into

\[
[m_{lo},\min(m_{hi},m_{noP})]
\]

where future `P_min` rejection is impossible, and the remaining upper interval where future `P_min` may still become active.

No parity refinement is required for this split; both pieces retain the same current affine channel.

---

## 5. Non-independence with first-75 tightening

The first-75 tail-defect tightening and this reachability cutoff both use the same directed physical envelope.

Therefore their population effects must be intersected on the exact source intervals.  They must not be added as independent pruning fractions.

The jump-8 certificate performs this intersection explicitly.

---

## 6. DSD classification

### EXACT / CLOSED

- total target correction identity;
- conversion of the existing fixed-point Christoffel envelope into `U_T`;
- absolute future-defect upper bound `U_q`;
- source-value cutoff `X_noP`;
- exact affine interval split.

### Important interpretation

The lower interval is **not closed as a Collatz candidate family**.  It is only closed to future use of the directed `P_min` predicate.

### Consequence for search strategy

Future-defect lower-bound work intended solely to trigger `P_min` should be restricted to the upper `P`-reachable source region.  The lower region requires a different independent predicate or membership obstruction.

## Dependencies

- `../src/A0_s1_radius7_defect_christoffel_real_envelope_certificate.py`
- `../src/A0_s1_14root_8jump_tail_defect_tightening_certificate.py`
- `../src/A0_s1_14root_8jump_Pmin_recheck_certificate.py`
- `TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`

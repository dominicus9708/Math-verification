# Gate C: terminal barrier and valid closure criteria

Date: 2026-09-06

Status: **SAFE LOGICAL BARRIER + ZERO-TAIL LAW CLOSED + DIRECT ORIENTATION ROUTE REJECTED.**

This note records the current terminal status after the exact Beatty-parity / signed-skew coordinate audit.

The central warning remains:

\[
\boxed{
\text{normalized candidate-mass decay alone does not exclude one fixed integer path.}
}
\]

The earlier tentative idea of contradicting eventual canonical lift blocks `t_q=0` with the Beatty one-child appended bit `1` is now rejected: the two bits belong to different coordinate systems.

---

## 1. `C_form` — canonical integer condition is closed

The exact canonical lift is

\[
\boxed{
\rho_{q+1}=\rho_q+t_q2^{A_q+1},
\qquad
0\le t_q<2^{v_q}.
}
\]

The `v_q` binary digits of `t_q` occupy the starting-residue bit interval

\[
A_q+1,\ldots,A_{q+1}.
\]

The established formation theorem gives

\[
\boxed{
N\in\mathbb N_{>0}
\iff
(t_q)\text{ has finite support}.
}
\]

Thus a fixed positive integer has a support endpoint `q_0` such that

\[
\boxed{t_q=0\quad(q\ge q_0).}
\]

Status: **CLOSED / SAFE.**

---

## 2. `C_tail` — zero-tail dynamics is closed

The exact canonical carry law is

\[
\boxed{
2^{v_q}y_{q+1}
=3y_q+1+2t_q3^{q+1}.
}
\]

The factor `2` in the injection term is essential.

The exact digit theorem gives

\[
\boxed{t_q=0\iff v_q=v_2(3y_q+1).}
\]

Hence after the support endpoint,

\[
\boxed{
y_{q+1}
=\frac{3y_q+1}{2^{v_2(3y_q+1)}}.}
\]

So the eventually-zero canonical tail is exactly the accelerated Collatz orbit.

With

\[
A_q=\lfloor q\log_2 3\rfloor-s_q
\]

and

\[
r_q
=\lfloor(q+1)\log_2 3\rfloor
-\lfloor q\log_2 3\rfloor,
\]

we also have

\[
\boxed{
s_{q+1}=s_q+r_q-v_2(3y_q+1)}
\]

on the zero tail.

Status: **CLOSED / SAFE.**

This is not a simplification of Collatz itself; it is an exact coordinate description of the hard terminal case.

---

## 3. Exact meaning of the Beatty binary child

The Beatty coefficient-survivor word is the parity word of the half-step map

\[
U(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

It is **not** the canonical lift-digit word.

An accelerated valuation block `v_q` expands exactly as

\[
\boxed{1\,0^{v_q-1}}
\]

in this parity word.

Thus at accelerated binary time

\[
A_q=\sum_{i<q}v_i,
\]

the next parity bit is always `1` because the state `y_q` is odd.

At a Beatty rise with boundary slack zero, the one-child DP also accepts only appended parity bit `1`.

Therefore an accelerated checkpoint lying on that boundary is **consistent**, not contradictory, with an actual Collatz orbit.

Status: **CLOSED COORDINATE FACT.**

---

## 4. Direct `t_q=0` versus Beatty-`1` contradiction is rejected

The canonical lift block `t_q` and the Beatty appended bit encode different objects:

- `t_q`: starting-residue lift bits required to extend a prescribed accelerated valuation code;
- Beatty appended bit: parity of one half-step orbit state.

Consequently

\[
\boxed{
t_q=0
\not\Rightarrow
\text{Beatty append bit }0.}
\]

In fact, at every completed accelerated odd-event checkpoint, the next Beatty parity bit is `1` independently of `t_q`.

Thus the earlier tentative gates `C_orient` and the associated `C_recur -> orientation conflict` route are removed as a valid proof architecture.

Status: **DSD CORRECTION / REJECTED BRANCH.**

---

## 5. Exact coefficient-survivor / signed-skew identification

The coordinate audit gives the useful positive result

\[
\boxed{
q_L\ge b_L\quad\forall L
\iff
s_q\ge0\quad\forall q,
}
\]

where

\[
b_L=\lceil L\log_3 2\rceil.
\]

At accelerated checkpoints,

\[
q_{A_q}=q,
\]

and

\[
q\ge b_{A_q}
\iff
3^q\ge2^{A_q}
\iff
A_q\le\lfloor q\log_2 3\rfloor
\iff
s_q\ge0.
\]

Intermediate half-step depths add no stronger constraint because `b_L` is nondecreasing and the parity word between checkpoints has the exact block form `1 0^(v_q-1)`.

Status: **CLOSED / SAFE.**

Therefore the symbolic Beatty survivor population is exactly the nonnegative signed-skew coefficient-survival population in accelerated coordinates.

---

## 6. Why mass decay still does not give emptiness

Let `S_L` be surviving candidate cylinders and `w_L(C)>0` their normalized weights:

\[
\mu_L=\sum_{C\in S_L}w_L(C).
\]

One nested path

\[
C_1\supset C_2\supset\cdots
\]

may survive while

\[
\mu_L\to0
\]

if its individual cylinder weight also tends to zero.

For the integer-compatible subfamily `I_L`, define

\[
w_L^{\rm int}:=
\inf_{C\in I_L}w_L(C).
\]

Then the valid transfer criterion is

\[
\boxed{
\mu_L<w_L^{\rm int}
\Longrightarrow
I_L=\varnothing,
}
\]

or asymptotically

\[
\boxed{
\mu_L/w_L^{\rm int}\to0.
}
\]

A polynomial mass bound cannot beat an exponentially small individual cylinder scale.

Even the stronger constant-boundary Gate-S route, if it yields exponential normalized mass decay, still needs a quantitative comparison with `w_L^int` before emptiness follows.

Status: **SAFE LOGICAL BARRIER.**

---

## 7. Current valid Gate-C routes

After rejecting the false orientation branch, three legitimate terminal routes remain.

### Route C1 — finite-support lift-digit exclusion

Prove directly that no infinite admissible nonnegative signed-skew hard-core path can have

\[
\boxed{t_q=0\text{ eventually}.}
\]

This is the exact canonical naturalness obstruction already identified by the formation theorem.

Status: **OPEN.**

### Route C2 — absolute integer-compatible survivor count

Let

\[
M_L
=\#\{\text{surviving depth-}L\text{ cylinders compatible with eventual-zero lift}\}.
\]

Any exact estimate

\[
\boxed{M_L<1}
\]

forces `M_L=0`.

This may be obtained from weighted mass only if an absolute weight/count transfer is strong enough.

Status: **OPEN.**

### Route C3 — cross-base rigidity

Prove a deterministic arithmetic incompatibility between

1. the nonnegative signed-skew / coefficient-survivor hierarchy, and
2. eventual stabilization of the dyadic canonical starting residue.

Unlike the rejected orientation shortcut, this theorem must act on complete residue/fibre structure rather than identify unrelated individual bits.

Status: **OPEN.**

---

## 8. Interaction with the strong Beatty-selector route

The aggregate branch is now

\[
\boxed{
F_{\rm map}+F_{\rm unif}
\longrightarrow
\text{selector transfer}
\longrightarrow
\text{strong Gate S contraction}
\longrightarrow
\mu_L\to0.
}
\]

The strong symbolic Beatty theorem supplies a constant boundary fraction `c_*>0`, so under selector ratio `rho_L` the rise loss is

\[
\boxed{
\frac{c_*}{4}(3\rho_L-1)_+.
}
\]

This is much stronger than the elementary harmonic fallback, but it remains an aggregate mass statement.

The terminal branch is

\[
\boxed{
C_{\rm form}\;(\text{closed})
\longrightarrow
C_{\rm tail}\;(\text{closed})
\longrightarrow
\{C1,C2,C3\}\;(\text{open}).
}
\]

A complete proof must connect the aggregate branch to one of these legitimate terminal routes without using `mass zero => empty`.

---

## 9. DSD audit

### CLOSED / SAFE

1. positive integer iff canonical lift blocks have finite support;
2. eventual zero lift follows the accelerated Collatz map exactly;
3. Beatty bits are half-step parity bits, not canonical lift bits;
4. full coefficient survival iff `s_q>=0` at all accelerated checkpoints;
5. constant symbolic Beatty-boundary fraction survives external-theorem audit;
6. normalized mass decay alone does not imply absence of a fixed integer path.

### REJECTED

\[
\boxed{
\text{eventual }t_q=0
\Rightarrow
\text{Beatty append-0}
}
\]

and any direct `0 versus 1` orientation contradiction based on it.

### OPEN

1. `F_map`: exact cross-base selector-to-parity-fibre transfer;
2. `F_unif`: growing-Q compatibility where required;
3. Gate S: enough positive selector margin on exact fibres;
4. Gate C1/C2/C3 terminal closure.

### PROHIBITED UPGRADES

1. Do not infer a fixed path hits the aggregate Beatty boundary from positive boundary density.
2. Do not identify starting-residue lift bits with orbit parity bits.
3. Do not infer set emptiness from normalized density or mass decay.
4. Do not treat the zero-tail accelerated map as already solved; it is the original arithmetic orbit problem in odd-state coordinates.

---

## 10. Next terminal target

The highest-value next target is no longer a bit-orientation lemma.

It is to exploit the exact identity

\[
\boxed{
\text{coefficient survivor}\iff s_q\ge0
}
\]

together with the canonical formation output `t_q` and the existing hard-core restrictions to search for a genuine theorem of the form

\[
\boxed{
\text{admissible nonnegative signed-skew hard core}
\Longrightarrow
\text{infinitely many nonzero }t_q,
}
\]

or an equivalent absolute-count/cross-base rigidity statement.

That is the corrected Gate-C direction.
# Two-ended triangular factorization of dyadic start address and 3-adic correction

Date: 2026-08-14

Status: **exact algebraic factorization theorem + current-resonance scale reduction**.  It separates the low dyadic start address from the low 3-adic correction by opposite ends of a parity word.  It does not prove Collatz.

## 1. Affine correction by odd positions

For a binary parity word `w` of time length `L`, let

\[
0\le p_1<p_2<\cdots<p_q<L
\]

be its odd positions.  Its accelerated affine iterate is

\[
T_w^L(N)=\frac{3^qN+R_w}{2^L},
\]

with

\[
\boxed{
R_w
=\sum_{j=1}^{q}3^{q-j}2^{p_j}.
}
\]

This single sum is triangular in opposite directions in bases two and three.

## 2. Low dyadic address depends only on the early prefix

Fix a binary resolution `B<=L` and split

\[
w=UV,
\qquad |U|=B.
\]

Let `q_U,q_V` and `R_U,R_V` be the corresponding odd counts and corrections.  Concatenation gives

\[
\boxed{
R_{UV}=3^{q_V}R_U+2^B R_V.
}
\]

Modulo `2^B`,

\[
R_{UV}\equiv3^{q_V}R_U\pmod{2^B}.
\]

The canonical start coordinate modulo `2^B` is

\[
r_B(w):=[-3^{-(q_U+q_V)}R_{UV}]_{2^B}.
\]

Therefore

\[
\boxed{
r_B(w)=[-3^{-q_U}R_U]_{2^B}.}
\]

Thus the low `B` bits of the canonical start address depend **only** on the first `B` parity symbols.  All later parity decisions and all later defects cancel out of the formula.

This is the formation/address form of no-retroactive-repair.

## 3. Low 3-adic correction depends only on the late suffix

Now split

\[
w=US
\]

where the suffix `S` has odd count `q_S>=J`.  Concatenation gives

\[
R_w=3^{q_S}R_U+2^{|U|}R_S.
\]

Modulo `3^J`, the prefix term vanishes:

\[
\boxed{
R_w
\equiv
2^{|U|}R_S
\pmod{3^J}.
}
\]

Since `2` is a unit modulo every power of three, the low `J` ternary digits of the correction are determined completely by the suffix orientation, up to a fixed invertible scaling.

Equivalently, in the odd-position sum only the last `J` odd events can survive modulo `3^J`.

## 4. Three-block split

For a decomposition

\[
w=PMS
\]

with

\[
|P|\ge B,
\qquad q_S\ge J,
\]

we therefore have the exact separation

\[
\boxed{
\begin{array}{c|c}
\text{channel}&\text{data required}\\\hline
\text{canonical start mod }2^B&\text{early prefix }P\text{ only}\\
\text{correction mod }3^J&\text{late suffix }S\text{ only}\\
\text{coefficient survival / slack transfer}&\text{middle state }(\Sigma,M)\text{ and counts}
\end{array}
}
\]

The middle may be arbitrarily long without entering either low-resolution arithmetic channel directly.

This is an exact two-ended triangular factorization, not an independence assumption.

## 5. Exact 2-adic concatenation law

It is useful to retain the full 2-adic canonical coordinate

\[
\rho(w):=-3^{-q_w}R_w\in\mathbb Z_2.
\]

For `w=UV`,

\[
\begin{aligned}
\rho(UV)
&=-3^{-(q_U+q_V)}
\left(3^{q_V}R_U+2^{L_U}R_V\right)\\
&=\rho(U)+2^{L_U}3^{-q_U}\rho(V).
\end{aligned}
\]

Hence

\[
\boxed{
\rho(UV)
=\rho(U)+2^{L_U}3^{-q_U}\rho(V).
}
\]

The low `L_U` bits are those of `rho(U)`.  The second term begins only at bit `L_U`; it controls the newly exposed high block after an odd-unit twist.

This is the precise form of the late-lift/direct-sum channel.

## 6. Zero-lift fibre for an ordinary start

Suppose the realized ordinary start satisfies

\[
0<N<2^B
\]

and an early prefix `P` of length `B` has canonical residue

\[
[-3^{-q_P}R_P]_{2^B}=N.
\]

Write the 2-adic high tail of the prefix coordinate as

\[
\Lambda_B(P)
:=
\frac{ho(P)-N}{2^B}
\in\mathbb Z_2.
\]

For any continuation `V`,

\[
\rho(PV)
=N+2^B
\left(
\Lambda_B(P)+3^{-q_P}\rho(V)
\right).
\]

Therefore extension to the same ordinary integer `N` through a deeper target resolution is equivalent to the **zero-lift fibre condition**

\[
\boxed{
\Lambda_B(P)+3^{-q_P}\rho(V)
\equiv0
\pmod{2^{K-B}}
}
\]

at every deeper resolution `K` under consideration.

Thus an ordinary start does not merely require the first `B` bits to match.  The suffix must cancel the entire high 2-adic tail of the already-fixed prefix coordinate.

## 7. Current `m=44` / isolated-resonance scale

Every member of the remaining `m=44` Cantor core obeys

\[
N\le6\cdot3^{44}+1
=5,908,625,413,101,667,397,287
<2^{73}.
\]

Hence for the current isolated R1 resonance it is sufficient to choose

\[
\boxed{B=73.}
\]

The first 73 parity bits determine the ordinary start itself, not merely a residue class:

\[
\boxed{r_{73}=N.}
\]

No later defect can alter those bits.

On the opposite end, the gate-suffix certificate proves full unit correction-residue freedom through

\[
\boxed{J=12}
\]

inside neutral and one-slack gate fibres using only a 57-bit suffix.

Consequently the huge first-crossing word may be cut exactly into

\[
\boxed{
73\text{-bit early dyadic boundary}
\;\times\;
\text{middle survival transport}
\;\times\;
12\text{-trit late Hensel boundary}.
}
\]

The middle length may be on the order of the full resonance without changing these two low-resolution boundary coordinates.

## 8. Relation to the primitive `k=7` gate state

The current isolated R1 pair has already been identified as the `k=7` primitive-collapse subgate inside a partial-quotient-13 level of the same induced Euclidean hierarchy.

Thus its renormalized arithmetic state can be organized as

\[
\boxed{
(k=7\text{ gate phase},\
\text{early }73\text{-bit address},\
(\Sigma,M)\text{ middle state},\
\text{late }3^{12}\text{ correction state}).
}
\]

This is substantially smaller than the original representation by `H=137,528,045,312` individual odd events.

## 9. Limitation and next target

The theorem does not imply statistical independence between the early and late boundaries.  A single parity word must realize both while its middle remains coefficient-admissible.

The remaining target is therefore an exact **boundary compatibility theorem**:

> classify the finite early dyadic boundary states and late Hensel boundary states that can be connected through an admissible Euclidean middle path at the primitive `k=7` gate state, and intersect the early boundary with the remaining ternary-Cantor starts.

The important reduction is that the enormous middle no longer needs to be retained at bit resolution; only its renormalized survival/phase transport is relevant.

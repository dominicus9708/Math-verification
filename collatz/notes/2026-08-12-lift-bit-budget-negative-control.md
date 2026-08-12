# Lift-bit budget and the dynamic-reset negative control

Date: 2026-08-12

Status: **exact formation budget + negative control on a tempting proof route**. The finite start really contains only finitely many nonzero formation lift bits, but deep valuation events after formation stabilization do not necessarily consume any new start bit.

## 1. Binary formation budget

From the canonical lift-digit theorem,

\[
\frac{N-1}{2}=\sum_{q\ge0} t_q2^{A_q},
\]

where the `v_q` binary digits of `t_q` occupy the disjoint bit block

\[
A_q,\ldots,A_{q+1}-1.
\]

Therefore

\[
\boxed{
\sum_q \operatorname{popcount}(t_q)
=
\operatorname{popcount}\!\left(\frac{N-1}{2}\right).
}
\]

In particular,

\[
\boxed{
\#\{q:t_q\ne0\}
\le
\operatorname{popcount}\!\left(\frac{N-1}{2}\right).
}
\]

Each nonzero formation lift uses at least one previously unused ordinary binary digit of the fixed start.

This is a genuine finite information budget.

## 2. But a dynamic reset need not consume a lift bit

The tempting inference

\[
\text{large }v_q\text{ or a deep signed-skew reset}
\Longrightarrow t_q\ne0
\]

is false.

Once the canonical formation floor has stabilized at the actual positive start `N`, the current canonical endpoint is the actual odd orbit state. Hence every subsequent actual valuation is realized with

\[
\boxed{t_q=0}
\]

regardless of how large the valuation is.

The equivalence

\[
t_q=0\iff v_2(3y_q+1)=v_q
\]

makes this explicit: after stabilization, `y_q` is the actual state and the right-hand side is true by definition of the actual valuation code.

## 3. Exact finite examples

The phenomenon occurs before any asymptotic issue.

### Start N=63

The ordinary bit length is `6`. The canonical formation floor stabilizes by the fifth odd-event extension. At odd-event index `q=5`, the actual odd state is

\[
\boxed{y_5=485,}
\]

and

\[
\boxed{v_5=v_2(3\cdot485+1)=4.}
\]

Nevertheless the canonical lift digit is

\[
\boxed{t_5=0.}
\]

Thus a valuation-4 deep halving event occurs with no new start-side formation bit.

### Start N=703

The same phenomenon occurs later in the odd-event trajectory: after the formation floor is already stabilized, a valuation-4 event occurs with zero lift output.

These examples can be reproduced with

`collatz/src/canonical_lift_digit_audit.py`.

## 4. Consequence for bit-budget proofs

The finite budget

\[
\operatorname{popcount}((N-1)/2)
\]

counts **formation changes of the least compatible starting residue**. It does not count future dynamical excursions of the already formed integer.

Therefore a proof strategy of the form

> every deep excursion/reset consumes a fresh initial bit, so infinitely many excursions exhaust the finite start

is invalid unless an additional theorem independently proves that the selected excursions force `t_q\ne0`.

No such implication follows from the valuation size, signed-skew depth, macroblock type, or coefficient crossing alone.

## 5. Proper role of the lift-digit theorem

The exact role is narrower and cleaner:

- infinitely many nonzero `t_q` exclude ordinary-integer naturalness immediately;
- eventual zero `t_q` is exactly the difficult positive-integer branch;
- after eventual zero output, the transducer has already formed one fixed integer and all later complexity is genuine orbit dynamics, not further formation cost.

Thus any successful use of the lift-bit budget must identify a **specific infinite family of orbit events that provably forces new formation lifts before stabilization**, or replace the bit-budget idea with a different transported invariant after stabilization.

This negative control prevents double-counting dynamic resets as formation information consumption.

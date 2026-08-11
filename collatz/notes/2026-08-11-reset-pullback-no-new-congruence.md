# Reset pullback gives no independent congruence

Date: 2026-08-11

Status: **exact redundancy lemma / proof-route pruning**. This note shows that pulling a large reset valuation back to the initial integer merely reproduces the next exponent-code formation condition. Therefore deeper reset congruences alone cannot be treated as an independent exclusion filter.

## 1. Event-prefix identity

For the odd-event code through event `i`, write

\[
\boxed{
2^{A_i}x_i=3^i n+B_i,
}
\]

where

\[
B_{i+1}=3B_i+2^{A_i}.
\]

Suppose the next valuation is

\[
\boxed{v_i=t.}
\]

Then

\[
A_{i+1}=A_i+t.
\]

---

## 2. Exact reset residue at the current state

The valuation `v_i=t` is equivalent to

\[
3x_i+1=2^t u
\]

with `u` odd, hence

\[
\boxed{
3x_i+1
\equiv
2^t
\pmod{2^{t+1}}.
}
\]

This gives the exact current-state residue

\[
x_i\equiv3^{-1}(2^t-1)\pmod{2^{t+1}}.
\]

---

## 3. Pullback to the fixed initial integer

Substitute

\[
x_i=\frac{3^i n+B_i}{2^{A_i}}
\]

into the valuation congruence and multiply by `2^{A_i}`. We obtain

\[
3^{i+1}n+3B_i+2^{A_i}
\equiv
2^{A_i+t}
\pmod{2^{A_i+t+1}}.
\]

Using

\[
B_{i+1}=3B_i+2^{A_i}
\]

and

\[
A_{i+1}=A_i+t,
\]

this becomes

\[
\boxed{
3^{i+1}n+B_{i+1}
\equiv
2^{A_{i+1}}
\pmod{2^{A_{i+1}+1}}.
}
\]

But this is exactly the completed exponent-code formation condition for the next odd endpoint.

---

## 4. Redundancy conclusion

Therefore:

\[
\boxed{
\text{current reset valuation residue}
\xrightarrow{\text{pullback}}
\text{next exponent-code formation bit}.
}
\]

It does **not** provide a second independent congruence on the fixed initial integer.

Consequently, a proof strategy that repeatedly discovers large valuations and then treats their pulled-back congruences as accumulating independent modular restrictions is circular: it is only reading more digits of the same exact parity/exponent code.

---

## 5. What remains genuinely new in the reset theorem

The reset theorem still contributes nonredundant Archimedean information. A return from a deep multiplicative deficit to a fixed critical strip forces:

1. logarithmically large `v_i`;
2. a polynomial lower bound on the current orbit state `x_i`;
3. sparsity of such reset arrivals.

These are consequences of the no-first-descent and harmonic-correction conditions, not tautological restatements of exponent-code formation.

Future filters must combine those real/order constraints with finite-natural 2-adic stabilization in a way that is not equivalent to merely extending the parity code by additional bits.

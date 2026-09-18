# MATH-204 — normalized carry quotient and address-memory erasure

Date: 2026-09-18

Status: \`EXACT STRUCTURAL LEMMA / SINGLETON ADDRESS MEMORY REDUCTION / GLOBAL CLOSURE OPEN\`

## 1. Purpose

MATH-203 reduces a potentially dangerous multi-paid singleton transition to an exact low-bit resonance

\[
X\equiv\eta_e(Q)\pmod{2^z},
\]

with

\[
z\ge z_{\min}(r).
\]

MATH-092 already gives the normalized shift-add address transition.

Combining them shows that a dangerous overshoot does not merely *test* \`z\` address bits: it **consumes and removes** those bits from the future state.

This note identifies the exact quotient carry that remains after this memory erasure.

No paid layer or first-cell closure is claimed.

## 2. Singleton normalized discrepancy

At the beginning of the overshoot, MATH-203 has

\[
R=0,\qquad M=1.
\]

Let

\[
X=3^{-Q}B
\]

be the current normalized address and

\[
\eta_e(Q)=3^{-Q}A_e
\]

the normalized canonical source constant of the next exact factor.

Define

\[
\boxed{
\Delta_X:=X-\eta_e(Q).
}
\]

Compatibility through a \`z\`-bit overshoot is exactly

\[
\boxed{
\Delta_X\equiv0\pmod{2^z}.
}
\]

Hence there is a unique 2-adic quotient

\[
\boxed{
\delta:=\frac{\Delta_X}{2^z}\in\mathbb Z_2.
}
\]

## 3. Exact child address

MATH-092 gives

\[
X'
=
\frac{X-\eta_e(Q)}{2^z}
+
\beta_e(Q)
\]

in the singleton case.

Therefore

\[
\boxed{
X'=\delta+\beta_e(Q).
}
\]

All \`z\` forced zero bits have disappeared.

The parent address influences the child only through the quotient \`delta\`.

## 4. Relation to the ordinary MATH-091 carry

MATH-091 has ordinary carry

\[
d=\frac{B-A_e}{2^z}
\]

for the singleton residue \`r=0\`.

Since

\[
\Delta_X
=
3^{-Q}(B-A_e),
\]

we obtain

\[
\boxed{
\delta=3^{-Q}d.
}
\]

Thus the ordinary transported carry and the normalized quotient carry are the same information in two coordinate systems.

The child intercept identity

\[
B'=B_e+3^{q_e}d
\]

normalizes exactly to

\[
X'=\beta_e(Q)+\delta.
\]

## 5. r=10 erases at least 13 address bits

MATH-202/203 give

\[
r=10\text{ danger}\Longrightarrow z\ge13.
\]

Therefore every potentially dangerous \`r=10\` singleton transition has the form

\[
\boxed{
X
=
\eta_e(Q)+2^{13}\xi
}
\]

for some \`\xi\in\mathbb Z_2\`, and after the full compatible overshoot

\[
\boxed{
X'=\beta_e(Q)+\delta.
}
\]

At least 13 low address bits of the discrepancy are consumed before any dangerous child can exist.

This is an exact radix-2 memory reduction, not a heuristic mixing statement.

## 6. Zero-carry resonance is a canonical reset

If

\[
\delta=0,
\]

then

\[
X=\eta_e(Q).
\]

Because both are multiplied by the same odd unit \`3^Q\`,

\[
\boxed{B=A_e}
\]

as ordinary integers.

MATH-091 then has

\[
d=0
\]

and

\[
\boxed{
B'=B_e.
}
\]

Therefore a zero-carry resonance erases all parent-specific address displacement:

\[
\boxed{
\text{zero carry}
\Longrightarrow
\text{exact canonical target reset}.
}
\]

The future address begins at the canonical target state of the selected factor.

## 7. Nonzero carry retains only the quotient

If

\[
\delta\ne0,
\]

the state does not retain the original discrepancy \`B-A_e\`.

It retains only

\[
\boxed{
d=\frac{B-A_e}{2^z}
}
\]

or equivalently \`\delta=3^{-Q}d\`.

If

\[
v_2(B-A_e)=z+w
\]

with finite \`w>=0\`, then

\[
\boxed{
v_2(d)=w
}
\]

and likewise

\[
v_2(\delta)=w.
\]

Thus the overshoot strips exactly \`z\` forced zero bits from the discrepancy and exposes its residual 2-adic valuation.

## 8. Exact maximum-resonance depth for one edge

For a nonzero discrepancy define

\[
\boxed{
z^*:=v_2(B-A_e)
=
v_2(X-\eta_e(Q)).
}
\]

Then

\[
X\equiv\eta_e(Q)\pmod{2^z}
\]

holds exactly for

\[
0\le z\le z^*.
\]

Therefore an \`r\`-paid dangerous transition can use this edge only if

\[
\boxed{
z^*\ge z_{\min}(r).
}
\]

For \`r=10\`:

\[
\boxed{
z^*\ge13.
}
\]

So the remaining \`r=10\` address problem is equivalently an exact search for legal singleton states whose current normalized address lies in a 2-adic ball of radius

\[
2^{-13}
\]

around a canonical source address.

No metric/probabilistic interpretation is required; this is simply the congruence modulo \`2^13\`.

## 9. Consequence for the next proof state

The singleton address state should no longer be viewed as one arbitrary large intercept.

At a dangerous transition it factors as

\[
\boxed{
(\text{canonical edge},\ z,\ \delta)
}
\]

with

\[
z\ge z_{\min}(r).
\]

The exact child then depends on

\[
\boxed{
\beta_e(Q)+\delta,
}
\]

not on the discarded low \`z\` bits.

This suggests the next finite-state target:

1. canonical edge/source type;
2. paid-count threshold class;
3. quotient carry \`\delta\` at the finite precision needed for the next danger test;
4. Hensel legality and terminal integer defect.

The raw frozen AP-source index is not a proof-state coordinate.

## 10. Zero/nonzero split for the remaining r=10 theorem

The \`r=10\` singleton kernel now has two exact branches.

### A. Zero-carry branch

\[
\boxed{\delta=0}
\]

gives exact canonical reset.

The next task is to audit whether an infinite or sufficiently long sequence of dangerous zero-carry resets is possible without entering the already-closed periodic/ordinary-descent structures.

### B. Nonzero-carry branch

\[
\boxed{\delta\ne0}
\]

retains only the quotient carry.

The next task is to find a well-founded quantity or finite quotient for repeated updates

\[
X'=\beta_e(Q)+\delta
\]

under the next resonance constraint.

## 11. Claim boundary

Established:

- exact quotient carry \`\delta=(X-\eta)/2^z\`;
- exact child normalized address \`X'=\beta+\delta\`;
- equivalence with the MATH-091 ordinary carry;
- at least 13 low discrepancy bits are erased in every potentially dangerous \`r=10\` singleton transition;
- zero carry is an exact canonical reset;
- nonzero carry retains only the shifted quotient;
- one-edge resonance depth is exactly \`v2(B-A_e)\`.

Not established:

- closure of all zero-carry reset chains;
- contraction/finite-state closure of all nonzero quotient-carry chains;
- closure of \`r=10\`;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

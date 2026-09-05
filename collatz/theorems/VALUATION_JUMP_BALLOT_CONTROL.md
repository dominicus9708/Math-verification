# Ballot control across a valuation-cylinder jump

Status: **EXACT / CLOSED for pure-ballot control**

## Threshold count

Let

\[
Q(n)=\lceil n\log_3 2\rceil,
\]

implemented equivalently as the least integer `q` such that

\[
3^q>2^n.
\]

Pure ballot requires the candidate one-count `q(n)` to satisfy

\[
q(n)\ge Q(n)
\]

at every prefix.

At absolute depth `h`, define incoming surplus

\[
S=q(h)-Q(h)\ge0.
\]

## Forced valuation block

Suppose the affine valuation-cylinder transition forces the next block

\[
0^a1.
\]

During the first `a` zero steps the candidate one-count is unchanged, while `Q` is nondecreasing. Therefore all zero-run prefix inequalities are equivalent to the last one:

\[
\boxed{
S\ge Q(h+a)-Q(h).
}
\]

At the final forced 1, the exact condition is

\[
\boxed{
S+1\ge Q(h+a+1)-Q(h).
}
\]

If both inequalities hold, the outgoing surplus is

\[
\boxed{
S'=S+1-\bigl(Q(h+a+1)-Q(h)\bigr)\ge0.
}
\]

Hence the complete pure-ballot effect of `0^a1` is computable in constant state without expanding its individual zero bits.

## Composition

After the jump, replace

\[
(h,S)
\]

by

\[
(h+a+1,S').
\]

The same two inequalities apply to the next valuation jump. Thus pure-ballot control is exactly composable with the affine valuation-cylinder source transducer.

## S10 consequence

A valuation-cylinder child can now carry and update:

- exact affine source state;
- absolute depth;
- remaining one-count/length;
- pure-ballot surplus;

without reverting to bitwise parity expansion.

This closes the first formation coordinate required by the updated S10 transducer target.

## Scope

The result does not establish preservation of H/L hierarchy, C4F, checkpoint/debit, tail, renewal, or physical predicates. Those controls remain separate coordinates until separately proved reducible.

## Certificate

- `../src/A0_s1_valuation_jump_ballot_control_certificate.py`

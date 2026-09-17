# MATH-189 — forward Hensel bridge for the synchronized joint recurrence

Date: 2026-09-18

Status: `EXACT STATE-SPACE BRIDGE / FORWARD HENSEL RECURRENCE / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-188 gives a one-step same-integer recurrence in the natural forward parity direction. MATH-051, however, evaluates fixed-d Hensel dominance by processing cumulative odd-gap levels from high to low using the carry recurrence

\[
h_{r-1}=\frac{2(h_r+\Delta a_r)}3.
\]

That reverse processing order cannot simply be attached to MATH-188 one parity step at a time.

The purpose of MATH-189 is to rewrite the same exact Hensel signature difference as a **forward integer recurrence** whose gap blocks are generated online by the actual parity word.

No new Hensel depth, paid layer, first-cell, or Collatz closure is claimed.

## 2. Online gap blocks

Let a parity word have even positions

\[
e_0<e_1<\cdots<e_{d-1}
\]

and define the MATH-051 cumulative odd-gap coordinate

\[
G_j=e_j-j.
\]

Because among the first `e_j` positions exactly `j` are even, `G_j` is exactly the number of odd positions occurring before the `j`-th even position.

Hence if

\[
a_r:=\#\{j:G_j=r\},
\]

then `a_r` is simply

> the number of even steps occurring after exactly `r` odd steps and before the next odd step.

Thus the gap-block sequence is produced online by the same parity stream used by MATH-188.

Let

\[
p_r:=\sum_{t<r}a_t.
\]

The rank indices belonging to level `r` are

\[
p_r,\ldots,p_r+a_r-1,
\]

so their power-of-two sum is

\[
\boxed{
A_r=2^{p_r}(2^{a_r}-1).
}
\]

Therefore the MATH-051 signature has the grouped form

\[
\boxed{
\Sigma_A
=\sum_{r=0}^{q}A_r\left(\frac23\right)^r.
}
\]

The last level `r=q` allows even steps after the final odd step.

## 3. Competitor blocks

Let a competitor word in the same fixed `(k,d)` comparison have block counts `b_r`, cumulative assigned even ranks

\[
s_r:=\sum_{t<r}b_t,
\]

and block power sum

\[
\boxed{
B_r=2^{s_r}(2^{b_r}-1).
}
\]

Then

\[
\Sigma_B-\Sigma_A
=
\sum_{r=0}^{q}(B_r-A_r)\left(\frac23\right)^r.
\]

## 4. Forward denominator-free recurrence

Define the partial signature difference through level `r`

\[
D_r
:=
\sum_{t=0}^{r}(B_t-A_t)\left(\frac23\right)^t
\]

and the integer-scaled quantity

\[
\boxed{
W_r:=3^rD_r.
}
\]

Then

\[
\begin{aligned}
W_r
&=3^rD_{r-1}+2^r(B_r-A_r)\\
&=3W_{r-1}+2^r(B_r-A_r).
\end{aligned}
\]

Thus

\[
\boxed{
W_r=3W_{r-1}+2^r(B_r-A_r),
\qquad W_{-1}=0.
}
\]

This recurrence is entirely integral and runs from low gap levels to high gap levels, i.e. in the same direction in which the parity stream generates completed gap blocks.

At the terminal odd count `q`,

\[
\boxed{
W_q=3^q(\Sigma_B-\Sigma_A).
}
\]

## 5. Exact Hensel terminal test

MATH-051 uses the fact that two fixed-(k,d) words are in the same exact Hensel class iff

\[
\Sigma_B-\Sigma_A\in\mathbb Z,
\]

and the competitor dominates the candidate iff this integer is positive.

By the identity above, these conditions are exactly

\[
\boxed{
3^q\mid W_q
}
\]

and

\[
\boxed{
W_q>0.
}
\]

Therefore a competitor is a positive exact Hensel witness iff

\[
\boxed{
W_q\in3^q\mathbb Z_{>0}.
}
\]

No floating point or approximate root test occurs.

## 6. Forward witness frontier

For one candidate prefix, define a competitor frontier after completed gap levels `<r` by

\[
\boxed{
\mathcal V_r
\subseteq
\{(s,W):0\le s\le15,\ W\in\mathbb Z\},
}
\]

where

- `s` is the number of competitor even ranks assigned so far;
- `W` is the forward scaled signature difference after the completed levels.

The `15` cap is the audited MATH-051 fixed-d scope for the complete depth-41 coefficient-valid frontier.

Suppose candidate level `r` closes with block size `a`, and the candidate has already assigned `p` even ranks. Then

\[
A=2^p(2^a-1).
\]

For each frontier state `(s,W)` and each legal competitor block length `b`, define

\[
B=2^s(2^b-1),
\]

and update

\[
\boxed{
(s,W)
\longmapsto
\left(s+b,\ 3W+2^r(B-A)\right).
}
\]

Duplicate output pairs are merged exactly.

This is a finite witness-state update, not ordinary-start enumeration.

## 7. Coupling to MATH-188

In the synchronized MATH-188 state

\[
\mathscr U
=(k,q,\Sigma;c,\mathcal P;A,B,M;\mathcal H),
\]

the candidate's current gap block is simply the number of even parity steps taken since the last odd step.

Introduce one additional small integer

\[
\boxed{a_{\rm cur}}
\]

for this unfinished block.

- On an even parity step `b=0`, increment `a_cur`.
- On an odd parity step `b=1`, finalize level `r=q` using the forward Hensel update, then set `a_cur=0` before advancing to odd count `q+1`.
- At a requested terminal depth, finalize the current level `r=q` once more for the terminal Hensel test.

Thus the candidate parity recurrence and the Hensel witness recurrence use the same actual parity stream and need no reconstructed parity history.

A proof-facing product state may therefore be written

\[
\boxed{
\mathscr U^+
=(k,q,\Sigma,c,\mathcal P,A,B,M;
 a_{\rm cur},\mathcal V),
}
\]

with MATH-051 viability pruning later attached to the finite witness frontier `V`.

## 8. Why the bridge is exact

The reverse carry automaton of MATH-051 and the forward `W` recurrence encode the same rational signature difference.

The reverse form is efficient for fixed terminal `(k,d)` because the terminal number of ranks is known in advance.

The forward form is efficient for the joint MATH-188 executor because the parity stream arrives in chronological order.

The two representations should therefore be treated as two coordinate systems for the same exact Hensel-difference relation, not as independent filters.

This also prevents DSD double counting: a candidate must not receive separate credit for passing both representations.

## 9. Terminal depth-2..41 use

At every requested terminal depth `k<=41`, let

\[
d=k-q.
\]

After finalizing the current gap block, retain competitor frontier states with exactly

\[
s=d.
\]

The candidate is terminally Hensel-dominated iff at least one retained state satisfies

\[
W>0,
\qquad
W\equiv0\pmod{3^q}.
\]

This reproduces the exact fixed-d Hensel criterion while allowing all depths `2..41` to be observed from one chronological recurrence.

## 10. Remaining compression target

The raw forward frontier is finite in the audited depth-41 range but may still contain unnecessary competitor witnesses.

The next step is to translate the MATH-051 exact viability predicate into the forward coordinates and delete `(s,W)` states that cannot possibly finish at any requested `(k,d)` terminal with positive divisible credit.

That is a witness-state compression problem, not a source-address enumeration problem.

## 11. Claim boundary

Established:

- online interpretation of MATH-051 gap blocks from the actual parity stream;
- exact grouped signature formula;
- exact denominator-free forward Hensel recurrence;
- terminal positive-class criterion `W_q in 3^q Z_{>0}`;
- a direct state-space bridge from MATH-188 to a finite Hensel witness frontier.

Not established:

- that the unpruned forward frontier is uniformly small at all audited depths;
- forward-coordinate viability pruning equivalent to the optimized MATH-051 solver;
- any new paid-count or Hensel depth closure;
- singleton terminal closure;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

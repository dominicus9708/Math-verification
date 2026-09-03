# Four-displacement horizon pruning on the current A0 s=1 Route-B frontier

Status: **EXACT finite current-frontier theorem / not a universal Route-B theorem**

## 1. Bounded-displacement horizon

For one exact source state `s`, let `H_c(s)` be the maximum number of future one-events reachable by a nonempty exact source descendant while using at most `c` target-displaced ranks.

The exact sparse recursion is

\[
H_0(s)=L_0(s),
\]

\[
H_c(s)=\max\left\{
L_0(s),
\max_{0\le k\le L_0(s),\ d>0}
\bigl(k+1+H_{c-1}(\chi_d(z_k))\bigr)
\right\}.
\]

Here `z_k` is the `k`-th state on the unique zero-displacement chain and `chi_d` is the exact source-residue child with target displacement `d`.

For the 14,224 source intervals surviving the previous `eta_future>1/4` cut, the exact 16-shard execution returned

\[
(45,46,45,48,45,45,45,45,46,46,45,45,45,45,45,45)
\]

as the shard maxima of `H_3`.

Therefore

\[
\boxed{\max_s H_3(s)=48.}
\]

Hence no source member can survive 49 future one-events with at most three displaced target ranks:

\[
\boxed{
\text{horizon }49\Longrightarrow N_{disp}^{future}\ge4.
}
\]

This is a finite exact statement about the current canonical source family.  No linear extrapolation in `c` is used.

## 2. Mechanical defect per displaced rank

For a target rank `r` with target one-position `t_r`, a displacement by at least one position contributes normalized defect

\[
3^{-r}\bigl(2^{t_r}-2^{a_r}\bigr),
\qquad a_r<t_r.
\]

The established mechanical phase bound implies every nonzero displacement contributes strictly more than

\[
\frac1{12}.
\]

Therefore four forced displaced ranks give

\[
\boxed{
\eta_{future}>\frac4{12}=\frac13.
}
\]

For integer endpoint pruning we may weaken this strictly safely to

\[
\eta_{future}\ge\frac13.
\]

## 3. Composition with the physical source cut

Let the already-realized normalized prefix defect of a current source interval be `eta`.

The directed physical envelope gives an upper source bound of the form

\[
X\le
\frac{
B-M_{lo}(\eta+\eta_{future})
}{\delta_{lo}},
\]

with the same certified constants used by the first-75 and `P_min` audits.

The previous cumulative frontier used the safe floor

\[
\eta_{future}\ge\frac14.
\]

The new result **replaces** that floor by

\[
\eta_{future}\ge\frac13.
\]

It is forbidden to add `1/4+1/3`, since both are lower bounds on the same unresolved future defect.

## 4. Exact finite pruning result

On the first-75-tightened jump-8 source family:

\[
26{,}859{,}837{,}368{,}588{,}270{,}254,
\]

the `1/4` floor gave

\[
26{,}859{,}837{,}368{,}531{,}301{,}450.
\]

Replacing it with the certified `1/3` floor gives

\[
\boxed{
26{,}859{,}837{,}368{,}506{,}133{,}665.
}
\]

Thus the strengthening removes an additional

\[
\boxed{25{,}167{,}785}
\]

ordinary source integers from 6,310 interval upper tails.

No whole source interval is eliminated; all 14,224 interval labels remain nonempty.

## 5. Scope

### EXACT / CLOSED

- source-preserving definition of bounded-displacement reachability;
- sparse first-displacement recursion;
- 16-shard current-frontier execution for `c=3`;
- global maximum `H_3=48`;
- horizon-49 minimum of four displaced ranks;
- resulting `eta_future>1/3` floor;
- exact endpoint pruning count on the current source family.

### OPEN

- `H_4` and higher budgets;
- any horizon-independent density or asymptotic displacement theorem;
- closure of any whole current source cylinder by this gate;
- the lower source sector where the directed `P_min` family is permanently inactive;
- full A0 s=1 Route-B membership.

## Canonical certificate

- `../src/A0_s1_8jump_four_displacement_eta_pruning_certificate.py`
- `../src/A0_s1_8jump_c3_displacement_horizon_shard.py`
- `SPARSE_FIRST_DISPLACEMENT_REACHABILITY_RECURSION.md`

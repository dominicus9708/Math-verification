# A0 checkpoint surplus tax and DSD structural audit

Date: 2026-08-27

Status: **SAFE STRUCTURAL LEMMA + DSD AUDIT CORRECTION.** This note does not prove the Collatz conjecture.

## 1. Three parallel tracks

This stage is maintained simultaneously as:

1. **standard proof chain** — exact Collatz/continued-fraction inequalities;
2. **DSD structural chain** — formation, transport, and discharge of the checkpoint surplus;
3. **structural audit** — explicit checks for local/global, finite/infinite, and additive/multiplicative category errors.

The three tracks are required to agree before an edge is marked SAFE.

## 2. Audit correction: the naive recovery-correction gate is invalid

For an A0 first crossing split at the tenth J0 checkpoint, write

\[
(A_0,Q_0)=10(J_0,R_0)+(U,P).
\]

Let

\[
C_{\rm pre}=\frac{3^{10R_0+s}}{2^{10J_0}},
\qquad
C_{\rm tail}=\frac{3^{P-s}}{2^U}.
\]

Then the transported surplus cancels exactly:

\[
\boxed{C_{\rm pre}C_{\rm tail}=C_A:=3^{Q_0}/2^{A_0}<1.}
\]

If normalized corrections of the two subblocks are `S_pre` and `S_tail`, then

\[
X_*=C_{\rm pre}(X+S_{\rm pre}),
\]

\[
X'=C_{\rm tail}(X_*+S_{\rm tail})
=C_A\left(X+S_{\rm pre}+\frac{S_{\rm tail}}{C_{\rm pre}}\right).
\]

Therefore the full normalized correction is

\[
\boxed{
S_{\rm tot}=S_{\rm pre}+\frac{S_{\rm tail}}{C_{\rm pre}}.
}
\]

The earlier proposed target — compare a supposedly huge affine correction required to return from the `>2.99 X` internal excursion to the near-root endpoint — is structurally wrong.  The multiplicative tail coefficient already cancels the multiplicative prefix excursion.  The affine correction is not responsible for undoing a factor of approximately three.

This edge is therefore marked:

\[
\boxed{\text{REJECTED GATE: large excursion }\Rightarrow\text{ huge required affine recovery}.}
\]

The correct quantity to audit is how the checkpoint surplus changes the **available full A0 correction budget**.

## 3. Ordered odd positions and the mechanical envelope

For a first crossing at `(A0,Q0)`, let

\[
\tau_j
\]

be the one-indexed step of the `j`-th odd event.

The mechanical first-crossing envelope has

\[
\boxed{
n_j=\left\lfloor\frac{j-1}{\alpha}\right\rfloor+1,
\qquad \alpha=\log_3 2.
}
\]

Every admissible first-crossing word satisfies

\[
\boxed{\tau_j\le n_j}
\]

for every odd ordinal `j`; this is the ordered-position form of mechanical remainder maximality.

The normalized correction is

\[
S=\sum_{j=1}^{Q_0}\frac{2^{\tau_j-1}}{3^j}.
\]

Hence moving any odd ordinal to an earlier step strictly decreases `S`.

## 4. Surplus at the tenth J0 checkpoint

Put

\[
t_0=10J_0,
\qquad
j_0=10R_0+1.
\]

Exact logarithmic inequalities give

\[
\boxed{\lceil\alpha t_0\rceil=j_0.}
\]

They also give the local phase fact

\[
\boxed{
\lceil\alpha(t_0+1)\rceil=j_0,
\qquad
\lceil\alpha(t_0+2)\rceil=j_0+1.
}
\]

Thus the mechanical `(j0+1)`-st odd event lies exactly at step `t0+2`.

Suppose an actual A0 first-crossing word has checkpoint surplus

\[
s=q_{t_0}-10R_0\ge1.
\]

The mechanical word has `s=1` there.  Therefore

\[
r:=s-1
\]

odd ordinals that mechanically lie to the right of the checkpoint have been transported to its left whenever `r>=1`.

## 5. A universal surplus tax on normalized correction

For the mechanical position of odd ordinal `j`,

\[
n_j-1>\frac{j-1}{\alpha}-1.
\]

Since `ln 2 / alpha = ln 3`, this implies

\[
\boxed{
\frac{2^{n_j-1}}{3^j}>\frac16.
}
\]

For the first transported ordinal `j0+1`, the exact local phase gives

\[
n_{j_0+1}=t_0+2.
\]

Its transported position is at most `t0`, so its correction loss alone is strictly larger than `1/6`.

For the remaining transported ordinals, all transported positions are at most `t0`.  Using

\[
3^{j_0}>2^{t_0}
\]

and the geometric tail beginning at ordinal `j0+2`, their total possible new contribution is less than `1/12`.

All their original mechanical contributions are individually greater than `1/6`.

Consequently, for every

\[
r=s-1\ge1,
\]

the full normalized correction deficit relative to the mechanical A0 envelope obeys

\[
\boxed{
S_{\rm mech}-S
>
\frac r6-\frac1{12}.
}
\]

This is the **checkpoint surplus tax**.

It is deterministic and requires no probabilistic parity assumption.

## 6. Endpoint consequence

The previous exact A0 first-crossing audit gives the unrestricted mechanical gap-credit ceiling

\[
a_A/G\approx0.50220738937,
\qquad G=2^{33}.
\]

Let

\[
\delta_A=A_0\ln2-Q_0\ln3>0,
\qquad C_A=e^{-\delta_A}.
\]

Since the correction deficit is multiplied by `C_A` at the endpoint, an A0 crossing with checkpoint surplus `s>=2` satisfies the strengthened gap-credit bound

\[
\boxed{
(d'-d)
<
a_A
-C_A\left(\frac{s-1}{6}-\frac1{12}\right).
}
\]

Thus extra surplus is not free.  It consumes a provable amount of the near-return budget.

At the arithmetically largest possible surplus `s=P`, the tax is greater than

\[
0.120G,
\]

and the worst-case A0 credit falls below

\[
\boxed{0.383G.}
\]

The companion exact-rational certificate verifies these constants.

## 7. DSD structural chain

The corrected DSD chain is

\[
\boxed{
\text{checkpoint survival}
\to
\text{surplus }s
\to
\text{leftward transport of }s-1\text{ odd ordinals}
\to
\text{correction-budget tax}
\to
\text{terminal deficit }-s
\to
\text{A0 endpoint}.
}
\]

The state variable is no longer only

\[
(\text{gap},\text{active resonance scale}),
\]

but may be refined to

\[
\boxed{
(\text{gap},\text{resonance scale},\text{transported surplus class}).
}
\]

This is a genuine structural refinement because the surplus class changes the allowed additive budget even though it cancels out of the total multiplicative coefficient.

## 8. Structural audit table

### SAFE

- `C_pre*C_tail=C_A` and exact surplus cancellation;
- composition identity for normalized corrections;
- rejection of the naive huge-affine-recovery argument;
- ordered odd-position domination by the mechanical first-crossing word;
- tenth-checkpoint baseline surplus `s=1` for the mechanical envelope;
- surplus tax `S_mech-S > (s-1)/6-1/12` for `s>=2`;
- strengthened A0 endpoint credit as a function of `s`.

### CONDITIONAL

- none of the statements above use the ternary-selector/Ansari entry;
- no repeated local Hensel pullback is used.

### OPEN

- the surplus tax by itself does not make every A0 block gap-decreasing;
- even maximal `s` leaves a positive coarse credit ceiling (<0.383G);
- the next task is to combine the surplus tax with the **activation ladder** and with the shifted-phase tail first-crossing constraint, instead of treating the U tail as an unconstrained recovery block.

## 9. Next Gate

For fixed surplus `s`, the tail prefix counts satisfy the shifted survival wall

\[
r_\ell
\ge
\left\lceil\theta+\alpha\ell\right\rceil-s,
\qquad
\theta=\alpha(10J_0)-10R_0,
\qquad 0\le\ell<U,
\]

while at `ell=U` the tail is exactly one below the shifted wall.

This is a phase-shifted first-crossing problem.  The next exact target is therefore:

> construct the shifted mechanical envelope for the `(U,P-s)` tail, compress it in `s`, and combine its correction loss with the A0/J0 activation thresholds.

Companion certificate:

`collatz/src/A0_checkpoint_surplus_tax_certificate.py`

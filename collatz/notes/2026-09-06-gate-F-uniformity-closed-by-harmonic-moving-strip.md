# Gate `F_unif` closed for logarithmically growing inverse depth by the harmonic moving-strip bound

Date: 2026-09-06

## Status

- **SAFE IDENTIFICATION:** the height `h_i` used in the fixed-Q backtrace/fibre-compatibility theorem is exactly the mechanical height controlled by the harmonic correction theorem.
- **SAFE LEMMA:** the harmonic theorem gives the explicit moving-height estimate
  \[
  N_q(H)<2^{H+1}C_Nq^{1/9}
  \]
  uniformly in every finite integer `H`.
- **SAFE THEOREM / `F_unif` CLOSED:** if
  \[
  Q(q)=\lfloor c\log_2q\rfloor,
  \qquad
  0<c<\frac{8}{9\log_2(3/2)},
  \]
  then the contaminated plateau-site fraction tends to zero.
- **OPEN:** `F_map`, the exact selector-to-canonical-Beatty-fibre identification, remains open.

No Collatz proof is claimed.

---

## 1. The coordinate audit

The fixed-Q zero-entropy/backtrace theorem defines

\[
\gamma:=\log_2 3,
\qquad
B_i:=\lfloor i\gamma\rfloor,
\qquad
A_i:=\sum_{j<i}v_j,
\]

and

\[
\boxed{h_i:=B_i-A_i.}
\]

Writing

\[
\theta_i:=\{i\gamma\},
\]

the harmonic weight is exactly

\[
\boxed{
\lambda_i
:=\frac{2^{A_i}}{3^i}
=2^{-h_i-\theta_i}.
}
\]

This is the same `h_i` that appears in the fixed-Q fibre-compatibility localization theorem and hence in the later Gate-F reduction

\[
N_q(H)
:=\#\{0\le i<q:h_i\le H\}.
\]

There is no coordinate change or hidden comparison constant.

Status: **SAFE IDENTIFICATION**.

Repository sources already proving these definitions:

- `collatz/notes/2026-08-25-fixed-q-backtrace-zero-entropy-barrier.md`;
- `collatz/notes/2026-08-26-q-fixed-plateau-swap-healing-and-fibre-compatibility.md`.

---

## 2. The height dependence was already explicit

For a hypothetical fixed positive integer `N` whose odd-event orbit is nonperiodic and never descends below `N`, the harmonic correction theorem gives

\[
\boxed{
\sum_{i<q}\lambda_i
\le C_Nq^{1/9}
}
\]

for all sufficiently large `q`.

If `h_i<=H`, then because `0<=theta_i<1`,

\[
\lambda_i
=2^{-h_i-\theta_i}
>2^{-(H+1)}.
\]

Therefore

\[
2^{-(H+1)}N_q(H)
<
\sum_{i<q}\lambda_i
\le C_Nq^{1/9},
\]

so

\[
\boxed{
N_q(H)
<2^{H+1}C_Nq^{1/9}.
}
\]

This holds simultaneously for every finite `H`; the constant `C_N` is independent of `H`.

Status: **SAFE LEMMA**.

This corrects the overly weak bookkeeping statement in the earlier Gate-F note, which retained only

\[
N_q(H_0)=O_{N,H_0}(q^{1/9})
\]

for fixed `H_0`.  The original harmonic proof had already exposed the dependence explicitly as exponential `2^H`.

---

## 3. Insert the active growing-Q height

The exact fixed-Q headroom barrier confines a depth-Q root-backtrace witness to

\[
0\le h_i\le H_Q,
\qquad
H_Q:=\left\lfloor Q\log_2\frac32\right\rfloor.
\]

The plateau-swap compatibility bookkeeping uses `H_Q+1` to absorb the one-step local height perturbation.  Hence

\[
N_q(H_Q+1)
<2^{H_Q+2}C_Nq^{1/9}.
\]

Since

\[
H_Q\le Q\log_2\frac32,
\]

we have

\[
2^{H_Q}
\le
\left(\frac32\right)^Q.
\]

Therefore

\[
\boxed{
N_q(H_Q+1)
<4C_N\left(\frac32\right)^Qq^{1/9}.
}
\]

---

## 4. Growing-Q contamination bound

The already proved local healing/localization estimate is

\[
\boxed{
\#\operatorname{Bad}(q,Q)
\le
(Q+2)N_q(H_Q+1).
}
\]

Combining with Section 3 gives

\[
\boxed{
\#\operatorname{Bad}(q,Q)
<
4C_N(Q+2)
\left(\frac32\right)^Q
q^{1/9}.
}
\]

Consequently

\[
\boxed{
\frac{\#\operatorname{Bad}(q,Q)}q
<
4C_N(Q+2)
\left(\frac32\right)^Q
q^{-8/9}.
}
\]

This is the explicit growing-Q compatibility estimate that the previous Gate-F audit left open.

---

## 5. Logarithmically growing Q

Choose

\[
Q(q)=\lfloor c\log_2q\rfloor.
\]

Then

\[
\left(\frac32\right)^{Q(q)}
\le
q^{c\log_2(3/2)}.
\]

Hence

\[
\frac{\#\operatorname{Bad}(q,Q(q))}{q}
=
O_N\!\left(
(\log q)
q^{-8/9+c\log_2(3/2)}
\right).
\]

Thus the contaminated fraction tends to zero whenever

\[
-\frac89+c\log_2\frac32<0,
\]

i.e.

\[
\boxed{
0<c<
\frac{8}{9\log_2(3/2)}
=1.519565592312404\ldots
}
\]

Therefore

\[
\boxed{
(Q(q)+2)N_q(H_{Q(q)}+1)=o(q)
}
\]

for every such logarithmic growth law.

Status: **SAFE THEOREM / `F_unif` CLOSED on this growth regime**.

---

## 6. Two explicit choices

### Simple choice

Take

\[
\boxed{Q(q)=\lfloor\log_2q\rfloor.}
\]

Then the unnormalized bad-count power is

\[
\frac19+\log_2\frac32
=0.696073611832267\ldots<1,
\]

so

\[
\frac{\#\operatorname{Bad}}q
=
O_N\!\left((\log q)q^{-0.303926388167733\ldots}\right)
\to0.
\]

### Near-critical choice

Even

\[
\boxed{Q(q)=\left\lfloor\frac32\log_2q\right\rfloor}
\]

is admissible:

\[
\frac19+\frac32\log_2\frac32
=0.988554862192846\ldots<1.
\]

The margin is small but positive:

\[
\frac{\#\operatorname{Bad}}q
=
O_N\!\left((\log q)q^{-0.0114451378071545\ldots}\right)
\to0.
\]

The critical coefficient `1.51956559...` agrees with the scale already identified in the fixed-Q zero-entropy audit as the minimum logarithmic growth needed for the backtrace height ceiling to reach the density-one harmonic strip.  At the exact critical coefficient this particular contamination estimate has no negative power margin, so no conclusion is claimed there.

---

## 7. Important scope distinction

Closing `F_unif` does **not** prove that a growing-Q backtrace filter kills a positive fraction of actual candidates.

It proves only the compatibility statement required by Gate F:

> choosing a logarithmically growing finite inverse depth does not contaminate more than `o(q)` of the late plateau-swap coordinates used by the fibre argument.

The following remain distinct:

1. `F_heal`: exact defect healing modulo `3^Q` after at most `Q` common odd events — **CLOSED**;
2. `F_unif`: total contaminated fraction for a chosen growing `Q(q)` tends to zero — **CLOSED for every logarithmic coefficient below `1.51956559...`**;
3. `F_map`: selector multiplicity is exactly the counting weight on the same canonical Beatty fibre — **OPEN**;
4. effectiveness of the growing-Q reverse/minimality filter itself — separate from Gate-F compatibility and still subject to the reverse-potential rarity barrier.

This distinction prevents the new uniformity theorem from being overinterpreted as a terminal Collatz result.

---

## 8. DSD audit of the correction

### Previously retained statement

The earlier Gate-F note said the fixed-height theorem had unknown `H` dependence and therefore could not be instantiated at `H=H_Q` with growing `Q`.

### Audit result

That statement was too weak because it referred to a compressed corollary instead of the original harmonic identity.  The original proof gives

\[
\lambda_i=2^{-h_i-\theta_i}
\]

and hence the explicit uniform factor `2^(H+1)` immediately.

### Corrected status

\[
\boxed{
F_{\rm heal}=\text{CLOSED},
\qquad
F_{\rm unif}=\text{CLOSED for }Q(q)=O(\log q)
\text{ below the explicit threshold},
\qquad
F_{\rm map}=\text{OPEN}.
}
\]

This is a genuine reduction of the remaining Gate-F obligations from two open subgates to one.

---

## 9. Reproducibility

Algebra/regression certificate:

`collatz/src/gateF_logarithmic_Q_harmonic_uniformity_certificate.py`

Expected terminal line:

```text
PASS
```

The script verifies the critical coefficient and the exponents for the explicit choices `c=1` and `c=3/2`.  The asymptotic theorem itself follows from the exact inequalities above, not from the finite regression loop.

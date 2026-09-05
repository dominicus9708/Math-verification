# Exact coordinate identification: Beatty parity survivor and signed skew

Date: 2026-09-06

Status: **SAFE EXACT IDENTIFICATION + TERMINAL ORIENTATION CORRECTION.**

This note resolves a coordinate ambiguity exposed by the Gate-C audit.

The binary word used by the Beatty coefficient-survivor language is **not** the canonical lift-digit word `t_q`.  It is the ordinary parity word of the half-step Collatz map

\[
U(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

This distinction removes a tempting but invalid terminal contradiction between `t_q=0` and the Beatty one-child orientation.

At the same time, it yields an exact and useful theorem:

\[
\boxed{
\text{full coefficient-survival of the parity word}
\iff
s_q\ge0\text{ at every accelerated odd-event checkpoint}.
}
\]

Thus the Beatty symbolic survivor and the nonnegative signed-skew condition are two coordinate descriptions of the same coefficient constraint.

---

## 1. Half-step parity word and accelerated valuation blocks

Let an odd-state accelerated orbit be

\[
y_{q+1}
=
\frac{3y_q+1}{2^{v_q}},
\qquad
v_q=v_2(3y_q+1)\ge1,
\]

and define cumulative binary time

\[
\boxed{
A_q:=\sum_{i<q}v_i.
}
\]

Under the half-step map `U`, the `q`th accelerated odd event occupies exactly the parity block

\[
\boxed{
1\,0^{v_q-1}.
}
\]

Indeed, at binary time `A_q` the state is the odd number `y_q`, so the first half-step is odd; the remaining `v_q-1` half-steps divide out the rest of the factor `2^{v_q}` before the next odd state `y_{q+1}` appears at time `A_{q+1}`.

Therefore, if `epsilon_k` denotes the parity of `U^k(N)`,

\[
\boxed{
\varepsilon_{A_q}=1,
\qquad
\varepsilon_{A_q+r}=0
\quad(1\le r<v_q).
}
\]

This is an exact deterministic expansion of the accelerated valuation code.

---

## 2. Prefix odd-count function

Let

\[
q_L:=\sum_{k=0}^{L-1}\varepsilon_k
\]

be the number of odd entries among the first `L` half-step states, exactly as in the coefficient-survivor definition.

The block structure immediately gives

\[
\boxed{q_{A_q}=q.}
\]

For an intermediate depth

\[
A_q<L\le A_{q+1},
\]

the odd event at time `A_q` has already been included and no further odd event occurs, so

\[
\boxed{q_L=q+1.}
\]

Status: **SAFE EXACT IDENTITY.**

---

## 3. Beatty coefficient barrier

Put

\[
\alpha=\log_3 2,
\qquad
\gamma=\log_2 3=\alpha^{-1},
\]

and

\[
\boxed{
b_L=\lceil\alpha L\rceil
=\min\{r:3^r\ge2^L\}.}
\]

The coefficient-survivor condition is

\[
\boxed{
q_L\ge b_L
\quad\text{for every }L\ge1.
}
\]

At an accelerated checkpoint `L=A_q`, this becomes

\[
\boxed{q\ge b_{A_q}.}
\]

---

## 4. Checkpoints are sufficient

Suppose

\[
q\ge b_{A_q}
\]

for every accelerated checkpoint.

For any

\[
A_q<L\le A_{q+1},
\]

we have `q_L=q+1`.  Since `b_L` is nondecreasing,

\[
b_L\le b_{A_{q+1}}\le q+1.
\]

Hence

\[
q_L\ge b_L.
\]

Conversely, full prefix survival obviously implies survival at every checkpoint.

Therefore

\[
\boxed{
q_L\ge b_L\ \forall L
\iff
q\ge b_{A_q}\ \forall q.
}
\]

Status: **SAFE EXACT LEMMA.**

---

## 5. Exact identification with signed skew

The signed-skew coordinate is

\[
\boxed{
A_q=\lfloor q\gamma\rfloor-s_q.
}
\]

For `q>0`, `q gamma` is irrational because `gamma=log_2 3` is irrational.

Now

\[
q\ge b_{A_q}
\iff
3^q\ge2^{A_q}
\iff
q\gamma\ge A_q.
\]

Since `A_q` is an integer,

\[
q\gamma\ge A_q
\iff
\lfloor q\gamma\rfloor\ge A_q.
\]

Using the definition of `s_q`,

\[
\lfloor q\gamma\rfloor-A_q=s_q.
\]

Thus

\[
\boxed{
q\ge b_{A_q}
\iff
s_q\ge0.
}
\]

Combining with the checkpoint lemma,

\[
\boxed{
\text{coefficient-surviving parity word}
\iff
s_q\ge0\quad\forall q.
}
\]

Status: **SAFE EXACT IDENTIFICATION.**

This is a coordinate identity, not a Collatz proof.

---

## 6. Exact checkpoint slack formula

Define the Beatty slack at an accelerated checkpoint by

\[
\boxed{
\sigma_q:=q-b_{A_q}.}
\]

Let

\[
\theta_q:=\{q\gamma\}\in(0,1).
\]

Since

\[
A_q=q\gamma-\theta_q-s_q,
\]

we have

\[
b_{A_q}
=
\left\lceil\frac{A_q}{\gamma}\right\rceil
=
q-\left\lfloor\frac{s_q+\theta_q}{\gamma}\right\rfloor.
\]

Therefore

\[
\boxed{
\sigma_q
=
\left\lfloor
\frac{s_q+\theta_q}{\gamma}
\right\rfloor.
}
\]

This gives an exact conversion between signed skew and the Beatty DP slack at completed odd-event checkpoints.

Status: **SAFE EXACT IDENTITY.**

---

## 7. Checkpoint boundary characterization

The checkpoint lies on the Beatty boundary exactly when

\[
\sigma_q=0.
\]

Equivalently,

\[
\boxed{
0\le s_q+\theta_q<\gamma.
}
\]

For a coefficient survivor `s_q>=0`, and because `s_q` is an integer while `0<theta_q<1` and `1<gamma<2`, this reduces to:

1. `s_q=0`: **always** a checkpoint boundary;
2. `s_q=1`: a checkpoint boundary exactly when
   \[
   \theta_q<\gamma-1;
   \]
3. `s_q>=2`: **never** a checkpoint boundary.

The same criterion can be written without real-number rounding:

\[
\boxed{
\sigma_q=0
\iff
3^{q-1}<2^{A_q}\le3^q.
}
\]

This integer-power form is preferred for exact certificates.

---

## 8. Meaning of the Beatty one-child orientation

At a Beatty rise

\[
b_{L+1}=b_L+1
\]

with boundary parent

\[
q_L=b_L,
\]

the symbolic DP says:

- append parity bit `1`: survives;
- append parity bit `0`: is killed.

The present coordinate identification shows exactly what that means dynamically:

\[
\boxed{
\text{if a surviving orbit reaches zero Beatty slack immediately before a rise,}
\text{ its next half-step state must be odd.}
}
\]

At an accelerated checkpoint `L=A_q`, the next parity bit is **always** `1`, because the state `y_q` is odd.

Thus a checkpoint boundary does not contradict an actual Collatz orbit; the forced one-child orientation is automatically the correct parity orientation there.

If zero slack occurs during the interior zero-run of a valuation block, a subsequent Beatty rise would force an odd bit too early and the coefficient-survivor condition would fail.  This is precisely the scheduling constraint already encoded by the next checkpoint inequality `s_{q+1}>=0`.

---

## 9. DSD correction to the previous Gate-C orientation idea

The earlier tentative terminal route considered comparing

\[
t_q=0\text{ eventually}
\]

with the Beatty boundary's forced appended bit `1`.

That comparison is invalid because the two coordinates encode different objects:

- `t_q`: a variable-length block of **starting-residue lift bits** in the canonical formation code;
- Beatty append bit: the **orbit parity** at one half-step time.

Moreover, at every accelerated odd-event checkpoint the Beatty parity bit is necessarily `1`, regardless of whether the canonical formation lift block `t_q` is zero.

Therefore

\[
\boxed{
\text{eventual }t_q=0
\not\Rightarrow
\text{eventual Beatty append-0}.
}
\]

The proposed direct zero-vs-one orientation contradiction is rejected.

Status: **DSD CORRECTION / CLOSED NEGATIVE RESULT.**

---

## 10. What this closes and what it does not

### Closed

1. exact meaning of the Beatty binary word: half-step parity word;
2. exact conversion from accelerated valuation blocks to parity blocks `1 0^(v_q-1)`;
3. exact checkpoint identity `q_{A_q}=q`;
4. full coefficient survival iff checkpoint coefficient survival;
5. checkpoint coefficient survival iff `s_q>=0`;
6. exact signed-skew/Beatty-slack formula;
7. direct canonical-lift-bit/Beatty-parity-bit contradiction is invalid.

### Still open

1. `F_map` in the **cross-base counting sense**: selector multiplicity must still be identified with/transported to the same dyadic parity-survivor fibre;
2. `F_unif`: growing-Q moving-strip control where required;
3. Gate S: selector-weighted transfer/flatness on the exact fibre;
4. terminal finite-support lift-digit exclusion for the surviving signed-skew hard core.

The exact symbolic coordinate map significantly reduces ambiguity, but it does not turn aggregate boundary exposure into a pathwise contradiction.

---

## 11. Revised terminal target

The correct terminal arithmetic target returns to the canonical formation theorem:

\[
\boxed{
\text{exclude an infinite admissible signed-skew path }s_q\ge0
\text{ whose canonical lift output }t_q\text{ is eventually zero.}
}
\]

The Beatty result contributes by describing and contracting the **population** of nonnegative-skew parity addresses after selector weighting; it does not by itself force a fixed eventually-zero canonical lift to choose the killed parity child.

Any final Gate-C closure must therefore use one of:

1. a genuine cross-base rigidity theorem linking canonical lift support to survivor placement;
2. an absolute integer-compatible survivor count below one;
3. or a deterministic theorem ruling out eventual-zero canonical output within the remaining signed-skew hard core.

---

## 12. Reproducibility target

An exact certificate should use only integer powers for the critical comparisons:

\[
3^q\ge2^{A_q}
\iff s_q\ge0,
\]

and

\[
3^{q-1}<2^{A_q}\le3^q
\iff\sigma_q=0.
\]

This avoids floating-point decisions involving `log_2 3` or `log_3 2`.

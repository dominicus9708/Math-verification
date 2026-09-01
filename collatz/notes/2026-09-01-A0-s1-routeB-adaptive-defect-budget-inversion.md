# A0 s=1 Route-B — adaptive defect-budget inversion

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Purpose

The projective-cylinder theorem gives exact local lower bounds on the monotone
normalized defect \(\eta\).  To turn such a bound into an efficient family
rejection rule, the opposite question is needed:

> For a source interval beginning at \(X_{lo}\), how much certified defect is
> sufficient to reject the *entire* interval by the existing real envelope?

The upstream oracle already gives

\[
\eta\ge E
\quad\Longrightarrow\quad
X\le X_{\max}(E).
\]

Hence a source family with lower endpoint \(X_{lo}\) is closed whenever

\[
X_{\max}(E)<X_{lo}.
\]

This note records the exact inverse threshold on the same 256-bit fixed-point
grid used by the existing certificate.

Source:

`collatz/src/A0_s1_routeB_defect_budget_inverse_certificate.py`

---

## 2. Exact inversion

Let `QFP = 2^256` be the upstream fixed-point scale.  Write a candidate defect
floor as

\[
\eta=\frac{E}{QFP},
\qquad E\in\mathbf Z_{\ge0}.
\]

The certified real-envelope implementation has the form

\[
X_{\max}(E)
=
\left\lfloor
\frac{
L_{\max}QFP+c_{W,hi}
-\left\lfloor m_{W,lo}E/QFP\right\rfloor
}{\delta_{lo}}
\right\rfloor.
\]

Therefore

\[
X_{\max}(E)<X_{lo}
\]

is exactly equivalent to

\[
\left\lfloor\frac{m_{W,lo}E}{QFP}\right\rfloor
>
L_{\max}QFP+c_{W,hi}-X_{lo}\delta_{lo}.
\]

Put

\[
R(X_{lo})
=
L_{\max}QFP+c_{W,hi}-X_{lo}\delta_{lo}.
\]

If \(R<0\), no positive defect is required.  Otherwise the exact smallest
fixed-point numerator is

\[
\boxed{
E_{close}(X_{lo})
=
\left\lceil
\frac{(R(X_{lo})+1)QFP}{m_{W,lo}}
\right\rceil.
}
\]

Thus

\[
\boxed{
\eta_{close}(X_{lo})
=
\frac{E_{close}(X_{lo})}{QFP}
}
\]

is the smallest value on the certified fixed-point grid that rejects the whole
source interval beginning at \(X_{lo}\).

The certificate checks minimality by verifying

\[
X_{\max}(E_{close})<X_{lo}
\]

and, whenever \(E_{close}>0\),

\[
X_{\max}(E_{close}-1)\ge X_{lo}.
\]

---

## 3. Monotonicity

Because \(R(X_{lo})\) decreases as \(X_{lo}\) increases,

\[
\boxed{
X_1\le X_2
\Longrightarrow
\eta_{close}(X_1)\ge\eta_{close}(X_2).
}
\]

This is important for the exact source-refinement forest.

A large root interval may require a large accumulated defect before it can be
rejected as a whole.  After exact dyadic refinement raises the lower endpoint
of a descendant interval, the required closure budget can only decrease.

Thus the correct adaptive comparison at every family node is

\[
\boxed{
\underline\eta(\text{grammar/projective state})
\stackrel{?}{\ge}
\eta_{close}(X_{lo}(\text{source interval})).
}
\]

If yes, the entire node closes.  If not, the result is simply unresolved; no
negative conclusion is drawn.

---

## 4. Scale audit on the current 14 roots

An independent high-precision diagnostic calculation, using the already
certified threshold brackets but not the repository's exact 256-bit directed
rounding path, gives the following approximate whole-root closure scale:

| first defect `f` | approximate `eta_close` at root lower endpoint |
|---:|---:|
| 2 | `4.9141799710e9` |
| 5 | `4.9141799710e9` |
| 8 | `4.9141799710e9` |
| 10 | `4.9141799710e9` |
| 13 | `4.9141799710e9` |
| 16 | `4.9141799710e9` |
| 18 | `4.9141799710e9` |
| 21 | `4.9141799710e9` |
| 24 | `4.9141799710e9` |
| 27 | `4.9141799710e9` |
| 29 | `4.9141799710e9` |
| 32 | `4.9141799710e9` |
| 35 | `4.9141799709e9` |
| 37 | `4.9141799707e9` |

These decimal values are **diagnostic only** until the new repository
certificate is executed in an environment with its upstream imports.  The
exact theorem and exact fixed-point computation are encoded in the certificate.

The qualitative conclusion is already robust: a single local gap such as
\(1/12\) or \(1/8\) is many orders of magnitude too small to close an entire
14-root interval from its lowest ordinary source.

This does **not** make the local gap useless.  It means the gap is an atomic
contribution that must be accumulated through the long grammar, or paired with
source refinement until \(\eta_{close}\) falls sufficiently.

---

## 5. DSD interpretation

The current state now has a clean dual budget.

### Structural side

The H/L, slack, projective-carry, and displacement machinery produces a safe
lower bound

\[
\underline\eta.
\]

### Physical side

The source interval lower endpoint produces an exact decision threshold

\[
\eta_{close}(X_{lo}).
\]

### Decision

Only the comparison

\[
\underline\eta\ge\eta_{close}(X_{lo})
\]

permits whole-family physical rejection through this route.

This avoids two previous failure modes:

1. interpreting a local adic mismatch as rejection without a physical bridge;
2. interpreting a positive but tiny defect as automatically sufficient for a
   gigantic source family.

---

## 6. Consequence for the proof architecture

The next useful theorem should not seek merely another positive local gap.
Instead it should control **accumulation**.

The normalized-defect semiring already gives

\[
\eta(UV)
=
\eta(U)+\mu(U)\eta(V),
\qquad
\mu(U)=\frac{2^{|U|}}{3^{q(U)}}>0.
\]

The projective-cylinder theorem gives exact atomic floors inside factors.
Therefore the next target is a compositional lower-bound DP of the form

\[
\boxed{
\text{H/L grammar state}
\times
\text{projective cylinder state}
\longrightarrow
\underline\eta_{block}
}
\]

with min-plus composition over grammar products.

The key question becomes whether the lower bound grows fast enough along the
actual 14-root descendants to overtake the decreasing physical threshold
\(\eta_{close}(X_{lo})\) before singleton expansion.

---

## 7. DSD audit

### EXACT / CLOSED

- the fixed-point real-envelope pruning map has an exact algebraic inverse on
  its own `QFP` grid;
- `eta_close(X_lo)` is minimal on that grid;
- raising a source interval's lower endpoint cannot increase its required
  closure defect;
- the comparison between a structural defect floor and a physical decision
  threshold is now explicit.

### DIAGNOSTIC ONLY

- the displayed `~4.914e9` root-scale values are independent high-precision
  orientation calculations, not yet connector-executed certificate output.

### NOT INFERRED

- the long H/L grammar is not yet proved to accumulate the required defect;
- a local `1/12` or `1/8` floor is not shell closure;
- no 14-root family is declared eliminated by this note;
- Route-B global membership and the Collatz conjecture remain open.

---

## 8. Updated bottleneck

The two sides of the physical pruning inequality are now explicit:

\[
\boxed{
\underline\eta_{grammar/projective}
\quad\text{vs}\quad
\eta_{close}(X_{lo}).
}
\]

The next calculation should build the **min-plus defect accumulator on the exact
H/L product grammar**, using projective cylinders as the local admissibility
state and the source interval as the decreasing physical budget.

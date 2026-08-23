# Unconditional safe-horizon exclusion budget

Date: 2026-08-24

Status: **quantitative proof-program audit.**  This identifies what the new general-m root-maximality safe horizon does and does not buy asymptotically.  It is not an independence theorem and not a proof of Collatz.

## 1. Constants

Put

\[
\alpha:=\log_3 2
\]

and let the exact coefficient-survivor language entropy be

\[
H_2(\alpha).
\]

The unconditional formation/coefficient exclusion rate is

\[
\boxed{
\delta_{\rm form}:=1-H_2(\alpha)
\approx0.05004447281166946.
}
\]

The general-m whole-prefix root-maximality safe horizon has asymptotic slope

\[
\boxed{
\rho:=\frac{\log_2 3}{1-\log_3 2}
\approx4.29447379207261,
}
\]

so

\[
H_{\rm safe}(m)=\rho m+O(1).
\]

## 2. What formation exclusion can remove inside the safe horizon

The recursively sufficient ternary selector core has one free binary selector digit per depth m, hence raw selector entropy m bits up to lower-order endpoint conventions.

If one credits only the currently unconditional formation exclusion rate, then by the root-safe terminal horizon the available exclusion budget is asymptotically

\[
\delta_{\rm form}H_{\rm safe}(m)
=\delta_{\rm form}\rho m+o(m).
\]

Numerically,

\[
\boxed{
\delta_{\rm form}\rho
\approx0.21491467692780478.
}
\]

Thus raw entropy bookkeeping leaves

\[
\boxed{
1-\delta_{\rm form}\rho
\approx0.7850853230721953
}
\]

selector bits per ternary depth m unaccounted for.

This is a budget statement only: it does not assume selector/dyadic independence.  Its purpose is to show that even perfect use of the known formation rate inside the current automatic root-credit interval is not, by itself, enough to overwhelm the one-bit-per-m selector family.

## 3. Formation-only horizon scale

To repay one selector bit per m using only \(\delta_{\rm form}\), the required binary horizon would be

\[
\boxed{
\frac{H}{m}>\frac1{\delta_{\rm form}}
\approx19.982226683919.
}
\]

Compared with the automatic root-safe slope,

\[
\boxed{
\frac{1/\delta_{\rm form}}{\rho}
\approx4.65300934443.
}
\]

So a proof based only on formation entropy would require root-valid control roughly 4.65 times farther than the currently automatic whole-prefix range.

## 4. Strategic consequence

This rules out one overly optimistic route:

> generalizing the m=45 depth-200 root-credit theorem to \(H_{\rm safe}(m)\sim4.294m\) does **not** by itself close the selector family by raw counting.

At least one additional ingredient is necessary:

1. extend valid smaller-root control substantially beyond \(H_{\rm safe}(m)\), for example via a subexponential nearest-credit theorem;
2. prove an additional positive exclusion rate from terminal maximality / endpoint transfer / high-Hensel syndrome;
3. prove a direct same-address correlation theorem showing that the ternary selector assigns much less mass to the coefficient-surviving terminal language than raw entropy permits; or
4. exploit the recursive m-to-m' structure so that the one-bit-per-m selector entropy is not repaid in one flat horizon.

The current unconditional endpoint fibre bound \(O(H)\), first-crossing buffered core \(O(\log H)\), and phase-adjusted scalar-credit bound all have zero exponential rate.  They remove possible repair channels but do not supply the missing positive exclusion rate themselves.

## 5. Updated core obstruction

The remaining exponential question is therefore sharpened to

\[
\boxed{
\text{selector entropy}
\quad\text{versus}\quad
\text{same-address terminal/renewal exclusion beyond the }0.2149m\text{ safe budget}.
}
\]

This is a more precise target than the earlier generic phrase “close the deterministic tail.”

Certificate:

`collatz/src/general_m_safe_horizon_exclusion_budget_certificate.py`.

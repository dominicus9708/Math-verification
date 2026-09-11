# MATH-064 — superseded r=22 audit

Date: 2026-09-11
Status: `SUPERSEDED BY MATH-065 / ORIGINAL SINGLETON GAP IDENTIFIED / r=22 CLOSURE REPAIRED`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- Canonical repaired certificate: `2026-09-11-math065-paid-count-18plus-closure.md`.

## 1. Correction

The original MATH-064 calculation separated the `r=22` phase/address cells into

\[
433\text{ cost-safe}
+752\text{ singleton-only}
+7\text{ multi-source-critical}
=1192.
\]

The seven multi-source-critical cells were audited correctly: they reduced to 18 ordinary target occurrences and all 18 descended to the frozen floor.

However, the original certificate then treated the 752 singleton-only cells as if removal from the **symbolic multi-source graph** were enough for full layer closure.

That implication is invalid:

\[
\boxed{
\text{singleton cylinder}
\not\Longrightarrow
\text{closed ordinary-integer branch}.
}
\]

A singleton must still be either cost-safe or continued as the corresponding ordinary integer.

Therefore the historical MATH-064 implementation was incomplete as a proof of full `r=22` closure.

## 2. Repaired result

MATH-065 applies one exact dyadic branch-and-bound algorithm to both singleton and multi-source cells.

For `r=22` it obtains

\[
\boxed{
\begin{array}{lr}
\text{phase/address cells} &1192\\
\text{cost-safe cells} &433\\
\text{singleton-only cells} &752\\
\text{multi-source critical cells} &7\\
\text{negative-candidate cylinders} &2184\\
\text{ordinary target occurrences} &2188\\
\text{unique targets} &1338\\
\text{maximum descent steps} &123.
\end{array}
}
\]

Every one of the 1338 unique targets reaches

\[
\le2^{71}.
\]

Hence

\[
\boxed{r=22\text{ is closed, but only through the repaired MATH-065 certificate}.}
\]

The original 18-target result remains valid as a calculation on the seven multi-source-critical cells; it was simply not the whole `r=22` workload.

## 3. Frontier correction

The original MATH-064 note also misstated the MATH-063 cutoff.

MATH-063 proves

\[
\boxed{
r=23\text{ is still below the automatic multi-source bound},
\qquad
r=24\text{ is the first automatic multi-source-safe count}.
}
\]

Therefore the old phrase `23<=r<=64 multi-source automatically safe` was incorrect.

MATH-065 subsequently audits `r=23` directly and closes it, so this transcription error no longer creates an open upper-layer gap, but it must remain recorded as an audit correction.

## 4. DSD lesson

This correction is exactly the information-loss distinction the DSD audit is intended to preserve:

1. **resolution collapse** to one ordinary source is not the same statement as
2. **ordinary-source descent/closure**.

The repaired pipeline is

\[
\text{symbolic cylinder}
\to
\text{singleton handoff}
\to
\text{exact ordinary target}
\to
\text{direct descent or cost closure}.
\]

No future paid-count layer may discard the last two arrows.

## 5. Reproducibility

Historical filename now delegates to the repaired implementation:

`collatz/src/2026_09_11_math064_r22_exact_closure_certificate.py`

Canonical implementation:

`collatz/src/2026_09_11_math065_paid_count_18plus_closure_certificate.py`

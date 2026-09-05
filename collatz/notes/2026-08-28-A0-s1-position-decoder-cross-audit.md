# A0 s=1: position-decoder cross-audit

Date: 2026-08-28

Status: **AUDIT NOTE — distinguishes new structural reduction from reproduced cardinality.**

## 1. Purpose

The position-form ballot certificate and target-aware modular prefix decoder were added after the ten-block Christoffel compression.  A repository-wide comparison was then made against the pre-existing

`collatz/src/A0_s1_72_73bit_ballot_address_cardinality_certificate.py`.

The purpose of this note is to prevent a reproduced numerical count from being misclassified as an additional independent pruning theorem.

## 2. Existing result reproduced exactly

The new position-form dynamic count gives

\[
N_{72}=4\,650\,657\,914\,809\,371\,340.
\]

The pre-existing `72_73bit_ballot_address_cardinality` certificate already proves exactly the same depth-72 count.

Therefore:

- the value `N_72` is **not a new pruning result**;
- its reproduction is retained as an **independent cross-check** of the new position-form representation;
- the agreement strengthens audit confidence but must not be counted twice in any progress or survival estimate.

The pre-existing certificate also contains the depth-73 count, which is not superseded by the new certificate.

## 3. New structural reduction retained

The genuinely new reduction introduced by the position certificate is

\[
Q(n)\ge\lceil\alpha n\rceil\ \forall n
\iff
a_r\le\left\lfloor\frac{r-1}{\alpha}\right\rfloor\ \forall r
\iff
2^{a_r}\le3^{r-1}\ \forall r,
\]

with the corresponding terminal-count condition.

This converts a full prefix-ballot scan into a check on the uniquely decoded odd positions.

At fixed `(t,j)`, correction injectivity therefore changes the target-membership workflow from

\[
\text{enumerate correction language}
\]

to

\[
C_{\rm req}
\to
\text{unique valuation decode}
\to
\{a_r\}
\to
\text{ballot and C4F predicates}.
\]

## 4. New target-aware local decoder retained

For every shallow depth `h <= t0`,

\[
C_{\rm req}\equiv-3^{j_0}X\pmod{2^h}.
\]

Hence all decoded positions below `h` are recoverable from `X mod 2^h` alone.  The endpoint `Z` and the enormous full integer `C_req` are unnecessary for this local check.

An immediate certified consequence is

\[
X\equiv3\pmod4.
\]

## 5. DSD accounting rule

### SAFE to count as new structural progress

- prefix-ballot / ordered-position equivalence;
- power inequality `2^{a_r} <= 3^{r-1}`;
- target-aware shallow modular decoder from `X` alone;
- elimination of full correction-language enumeration for a single fixed target;
- reduction of the next problem to a long-range exact valuation/block-jump decoder.

### CROSS-CHECK ONLY

- the depth-72 cardinality `N_72`, because it was already certified elsewhere in the branch.

### FORBIDDEN

- adding the same depth-72 pruning percentage twice;
- multiplying cardinality and interval survival percentages without an independence theorem;
- upgrading a pure-ballot pass to full `C4F` admissibility;
- treating any of these necessary conditions as same-orbit closure.

## 6. Next gate

The next genuinely open computational object is an exact **block-jump valuation decoder**.  It must preserve:

1. the current decoded rank `r`;
2. the exact 2-adic valuation information needed for the next odd position;
3. the target residue induced by `X`;
4. every predicate needed later for `C4F`;
5. distinguishability whenever two states can answer a future correction-membership query differently.

The Christoffel/Stern-Brocot DAG remains useful as a threshold-boundary transfer skeleton, but injectivity means that an all-deviation correction DAG is no longer required merely to test one fixed target.

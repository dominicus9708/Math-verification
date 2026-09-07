# DSD-native 61+11 computation pilot

Date: 2026-09-08
Status: `CONFIRMED WITHIN FINITE 61+11 SCOPE / REPRESENTATION ERROR BLOCKED / NO NEW GLOBAL PRUNING`

## Purpose

This experiment moves part of DSD from a post-hoc audit layer into the calculation state itself.

The exact Collatz arithmetic is unchanged. DSD metadata is attached to the state so that resolution, representation stage, exclusion reason, transition legality, and evidence norm are carried through the computation rather than reconstructed only after the scan.

## Exact arithmetic retained

Write

\[
N=a2^{61}+x,
\qquad
1024\le a\le1363,
\]

and let

\[
y=T^{61}(x),\qquad q=q_{61}(x).
\]

Then

\[
T^{61}(N)=y+a3^q,
\]

so the final 11 parity bits depend on the lifted phase

\[
r=(y+a3^q)\bmod 2048.
\]

## DSD-native state

The pilot explicitly distinguishes

- `BASE_ENDPOINT`: `y mod 2048`, before the top-address contribution is applied;
- `ADDRESS_LIFTED`: `(y+a3^q) mod 2048`, after the contribution is applied once.

The transition gate accepts only

\[
\texttt{BASE\_ENDPOINT}\to\texttt{ADDRESS\_LIFTED}.
\]

Attempting to apply the address lift to an already lifted phase raises an error.

This is not cosmetic bookkeeping. It blocks a real representation mistake found during the proposed MATH-010 refinement: MATH-006 already included `a3^q` internally. Feeding `y+a3^q` back into the MATH-006 predicate as though it were another base endpoint would have applied the same address information twice.

Therefore the earlier proposed expression

\[
S(q,y+3^qa,a)
\]

must not be interpreted as an additional coupled filter when `S` denotes the existing MATH-006 predicate. In that predicate the correct input is the base endpoint `y`; the address lift is already part of `S`.

## Regression result

The DSD-native implementation reproduces the exact MATH-006 min/max 340-label counts:

| q61 | min labels | max labels |
|---:|---:|---:|
| 39 | 36 | 47 |
| 40 | 124 | 141 |
| 41 | 221 | 235 |
| 42 | 288 | 303 |
| 43 | 320 | 333 |
| 44 | 336 | 340 |
| 45 | 339 | 340 |
| 46–61 | 340 | 340 |

Thus DSD-native representation does not alter the established exact arithmetic.

## New diagnostic retained by the calculation

For each lifted residue the state now records

- first coefficient-survival failure depth;
- minimum coefficient margin over depths 62..72;
- survive/excluded outcome;
- exact resolution and transition stage.

For q61=39 the 2048 lifted residues decompose exactly as follows:

| first failure depth | residue count |
|---:|---:|
| 62 | 1024 |
| 64 | 256 |
| 65 | 256 |
| 67 | 96 |
| 69 | 56 |
| 70 | 76 |
| 72 | 37 |
| survives to 72 | 247 |

Every q61=39 survivor has minimum coefficient margin 0. Thus the strongest low-surplus case is not merely sparse; every surviving tail touches the coefficient boundary somewhere in depths 62..72.

For q61=40..45 the exact first-failure and survivor-margin histograms are stored in the certificate. These are finite exact residue counts, not probability or density statements.

## DSD audit tuple carried in-state

The calculation attaches the following fields to each lifted tail state:

\[
\mathcal A=(D,R,S,E,T,C,N,O).
\]

- `D`: exact phase/parity descriptor;
- `R`: `61 root bits + 11 tail bits`;
- `S`: coefficient-survival selection status;
- `E`: first exclusion depth or none;
- `T`: single affine address lift verified;
- `C`: same-integer address stage preserved;
- `N`: `ESTABLISHED_WITHIN_SCOPE`;
- `O`: `SURVIVE` or `EXCLUDED`.

## What changed and what did not

Changed:

1. representation stages are explicit;
2. duplicate import of address information is automatically rejected;
3. failure depth and margin are retained as first-class calculation data.

Not changed:

1. the shortcut map;
2. MATH-006 exact survivor counts;
3. MATH-008 phase-reachability result;
4. the global proof status.

## Outcome

The proposed new affine-coupling pruning branch is **not** an independent MATH-006 refinement: MATH-006 already performs that coupling.

The useful new result is methodological and diagnostic:

\[
\boxed{\text{DSD stage tracking prevents a concrete double-lift transition error.}}
\]

and the calculation now exposes exact first-failure/margin structure for later coupling attempts.

No new candidate window is eliminated by this pilot alone.

\[
\boxed{\text{Collatz remains OPEN.}}
\]

## Reproducibility

Certificate:

`collatz/src/2026_09_08_dsd_native_61plus11_computation_certificate.py`

Upstream exact certificate:

`collatz/src/first_cell_block_label_11bit_transducer_certificate.py`

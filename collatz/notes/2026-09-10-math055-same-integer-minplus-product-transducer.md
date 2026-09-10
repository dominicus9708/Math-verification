# MATH-055 — same-integer min-plus product transducer

Date: 2026-09-10
Status: `EXACT ADDRESS LIFT / PRODUCT-STATE FORMULATION / UNIVERSAL VALUE-BOUND OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note reformulates the next computation; it does not close the first cell.

## 1. Canonical address lift

For a length-k parity prefix with odd count q and correction C, define its canonical dyadic start residue

\[
N_k\equiv-C3^{-q}\pmod{2^k}
\]

and its exact endpoint quotient

\[
e_k=\frac{3^qN_k+C}{2^k}.
\]

Every lift to modulus `2^(k+1)` has the form

\[
\boxed{N_{k+1}=N_k+t_k2^k},\qquad t_k\in\{0,1\}.
\]

The next parity bit is not independent. Since `3^q` is odd,

\[
\boxed{b_k\equiv e_k+t_k\pmod2}.
\]

The endpoint update is

\[
\boxed{b_k=0:\quad e_{k+1}=\frac{e_k+3^qt_k}{2},\quad q_{k+1}=q_k,}
\]

\[
\boxed{b_k=1:\quad e_{k+1}=\frac{3e_k+3^{q_k+1}t_k+1}{2},\quad q_{k+1}=q_k+1.}
\]

Thus ordinary-start address bits can be used as the input alphabet of the parity transducer.

## 2. Exact relation to the existing 61+11 calculation

Write

\[
N=a2^{61}+x,
\qquad1024\le a\le1363.
\]

The low 61 bits determine `x` and the base endpoint

\[
e_{61}=T^{61}(x).
\]

The eleven bits of `a`, read least-significant first, are exactly the lift bits

\[
t_{61},\ldots,t_{71}.
\]

Therefore the 11-step tail parity is generated deterministically by the endpoint/address lift recurrence. The address and tail parity are not separate choices.

This is the bitwise version of the existing MATH-006 affine relation

\[
T^{61}(N)=y+a3^q.
\]

The new certificate regresses this bitwise lift against direct parity-prefix reconstruction and against the seven MATH-054 budget-5 first-cell starts.

## 3. Product state with MATH-052/MATH-053

The next exact state should combine only non-redundant channels. A proof-facing state may be written schematically as

\[
\boxed{\Xi=(q,u,\mathcal H,e,\mathcal A)}.
\]

Here

- `q` determines the shared Beatty/Sturmian phase and `Omega_q`;
- `u=m(q)-d` is coefficient-boundary slack;
- `H` is the exact normalized Hensel competitor/frontier state from MATH-052;
- `e` is the endpoint state at the resolution needed for future address lifting;
- `A` is the finite address-window automaton state.

`Omega_q` is not an independent state variable because it is determined by q.

At each address-lift bit `t`:

1. compute `b = (e+t) mod 2`;
2. update endpoint and q exactly;
3. update slack `u` by the MATH-053 rule;
4. update the Hensel state using the resulting parity transition;
5. update the address-window automaton;
6. discard states violating coefficient, Hensel, or same-integer address constraints.

## 4. Min-plus weight

The MATH-053 slack penalty at an odd event is

\[
\boxed{p(q,u)=\frac{(1-2^{-u})\Omega_q}{3}}.
\]

Assign zero cost to even events and this cost to odd events. The product transducer then carries a min-plus value

\[
V(\Xi)=\text{minimum accumulated penalty among exact bad-path prefixes reaching }\Xi.
\]

Equivalent max-plus reward formulation:

\[
r(q,u)=\frac{\Omega_q}{3\,2^u}.
\]

The important point is that no path counts are needed. When two histories reach the same exact future state, retain only the smaller penalty (or larger correction reward). This is a DSD-safe quotient because the discarded history can never produce a better proof-facing objective under identical continuation behavior.

## 5. Desired Bellman form

For an exact transition `Xi --t--> Xi'`,

\[
\boxed{V_{j+1}(\Xi')=\min_{\Xi,t:\,\Xi\to\Xi'}\left(V_j(\Xi)+p(\Xi,t)\right).}
\]

The proof-facing target is not the total number of survivors. It is a lower bound on

\[
\boxed{V_{\rm bad}(K)}
\]

over every same-integer state still capable of reaching the first-crossing bad endpoint.

If this lower bound exceeds the correction-only surplus available to the mechanical upper envelope, the corresponding bad state is excluded.

## 6. Why this is stronger than continuing slack-budget enumeration

MATH-054 showed that budget enumeration can force at least five positive-slack events in the first 72 steps for any first-cell start that remains coefficient-valid through depth 195. But increasing the event budget by hand would recreate another enumeration ladder.

The min-plus product transducer instead stores the exact minimum penalty per future-equivalent state. It therefore targets the needed scalar inequality directly, without counting all words or iterating a separate slack budget.

## 7. DSD audit boundary

Established:

- canonical start lifting is one-bit exact;
- parity is determined by endpoint plus address lift bit;
- the existing 61+11 address channel can be integrated into the same transition rather than applied as post-hoc metadata;
- a min-plus objective is continuation-compatible once the exact future state is preserved.

Open:

- a sufficiently small complete quotient for `(H,e,A)` at arbitrary depth;
- a universal lower bound on the min-plus value;
- first-cell emptiness;
- later-strip coverage;
- Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_10_same_integer_address_lift_transducer_certificate.py`

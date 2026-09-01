# Active frontier — A0 `s=1` Route-B

Status: **ACTIVE**

This is the canonical resume point for current computation.

## Input family

Exact retained roots:

`{2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Primary input certificate:

- `../src/A0_s1_14root_long_membership_forest_certificate.py`

Each root is an exact source cylinder `X=r+2^h m` with a finite integer parameter interval and exact bit refinement.

## Forward front

Carry

`source future control × exact interval payload × P_min`

for the directed physical gate, with

\[
P=m_{W,lo}N+\delta_{lo}3^qX_{lo}.
\]

Whole-family rejection occurs when

\[
P>(L_{max}QFP+c_{W,hi})3^q.
\]

Do not restore separate `(r,N)` coordinates unless a later active predicate queries them.

## Backward right front

The current critical-cut right H factor has

\[
h_R=630{,}138{,}897,\qquad q_R=397{,}573{,}380.
\]

Terminal precisions `L=24,28,47` are right-local.

Current closed projective tools include:

- one-step carry bijection and displacement isometry;
- projective interval payload `Pi3_k` for one fixed displacement family;
- backward exponential carry chart;
- prescribed-cylinder right-H singleton threshold `m>=18`;
- max-slack formation quotient under its stated fixed-carry scope.

The remaining right-H task is only the compressed export of distinct carry/cylinder states that can actually participate in the synchronized join. Do not enumerate a flat `3^28` carry space.

## Closed checkpoint seam

The previous checkpoint-exposure blocker is now CLOSED.

Independent pre-defect inputs imply

\[
Z_{min}=7{,}083{,}549{,}723{,}342{,}395{,}146{,}241,
\]

\[
Z_{max}=9{,}444{,}732{,}965{,}107{,}363{,}299{,}196.
\]

For the right H factor

\[
z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}},
\]

while the dyadic checkpoint channel supplies

\[
Z\equiv z_2\pmod{2^{27}}.
\]

The joint CRT modulus is

\[
2^{27}3^{28}=3{,}070{,}471{,}107{,}232{,}407{,}748{,}608,
\]

larger than the entire certified `Z` corridor span. Therefore every coherent pair `(z2,z_H)` supplies at most one ordinary checkpoint `Z`.

Use:

- `../theorems/SYNCHRONIZED_CHECKPOINT_CRT_SINGLETON.md`;
- `../src/A0_s1_routeB_synchronized_checkpoint_CRT_singleton_certificate.py`.

This is synchronized arithmetic on one `Z`, not an independence/density argument.

## Immediate computation target — synchronized 14-root join

For each of the 14 roots:

1. execute/refine the exact forward source state with `P_min`;
2. export only unresolved forward boundary states;
3. generate the compatible compressed right-H observation/export states;
4. form the coherent pair `(z2,z_H)` only when both sides refer to the same boundary/checkpoint coordinates;
5. reconstruct the unique candidate `Z` when the CRT corridor admits one;
6. test exact source/checkpoint/debit compatibility;
7. close a family if the physical score or a certified membership predicate rejects the whole family;
8. retain only unresolved exact families for the next pre-bridge/tail gate.

## Merge rules

Allowed:

- one `P_min` per exact future-control + payload state for the directed physical gate;
- one-dimensional `Pi3_k` quotient under its finite-horizon carry-cylinder scope;
- max-slack merge only for the certified formation-existence predicate at fixed carry.

Not allowed:

- merge histories with different future controls;
- discard carry base solely because interval payloads match;
- infer whole-path injectivity from one-step injectivity;
- treat prescribed-cylinder singleton as unique carry path;
- multiply dyadic and ternary marginal survival ratios;
- use later refined bounds retroactively.

## Success criterion for the next milestone

Produce a reproducible 14-root table containing, per root and explored exact state depth:

- forward states created/merged/physically closed;
- right-H export states queried;
- synchronized CRT pairs with zero or one corridor checkpoint;
- exact joined survivors;
- reason for every whole-family closure;
- unresolved families and the next predicate each requires.

Finite counts are evidence about that execution only, not a universal theorem unless separately proved.

## Remaining global warning

Even closure of all 14 current Route-B roots would not prove Collatz. Route-A, `s>=2`, the remaining formation sectors, and global branch completeness remain separate obligations.

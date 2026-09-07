# Root-Hensel correction ordering vs endpoint ordering — redundancy audit

Date: 2026-09-08
Status: `CONFIRMED / REDUNDANT / NO NEW PRUNING`
Scope: fixed-depth, fixed-endpoint, fixed-odd-count candidate fibers in the current first universal cell.

## Claim

For two candidates at the same depth `k`, with the same endpoint `E` and the same odd count `q`,

\[
2^kE=3^qN_i+R_i\qquad(i=1,2).
\]

Subtracting gives

\[
R_1-R_2=3^q(N_2-N_1).
\]

Hence

\[
N_1<N_2\iff R_1>R_2.
\]

Therefore the ordering called "root-Hensel correction maximality" and the ordinary-start ordering inside the same `(k,q,E)` endpoint fiber are not independent constraints. They are the same affine ordering written in opposite coordinates.

## Consequence

It is prohibited to count

1. endpoint/minimum-start ordering, and
2. correction-maximum ordering

as two independent pruning filters inside the same locked fiber.

Doing so would double-count one exact relation and create spurious pruning.

This does **not** remove the separate value of the root-Hensel depth-195 result as a same-integer extension/eligibility statement. Only the attempted use of the two orderings as independent selectors is closed.

## DSD classification

- `D` — the objects `(N,E,q,R,k)` are explicit.
- `R` — the comparison is locked to the same depth, endpoint and odd count.
- `S/E` — no candidate may be excluded twice by the same affine ordering under two names.
- `T` — subtraction of the two exact affine endpoint identities is valid.
- `C` — consistent with the earlier endpoint q-lock result.
- `N` — local exact identity only; no global Collatz upgrade.
- `O` — `REDUNDANT / NO NEW PRUNING`.

## Prohibited upgrades

\[
\text{redundancy of two local orderings}
\not\Rightarrow
\text{root-Hensel information is globally useless}.
\]

\[
\text{local exact identity}
\not\Rightarrow
\text{first universal cell closed}.
\]

Collatz remains `OPEN`.

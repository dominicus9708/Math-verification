# Right-offset lifespan bootstrap to 10^7 — MATH-022

Date: 2026-09-08

Status: `CONFIRMED / FINITE EXACT BOOTSTRAP / INTERNAL-BOUNDARY ENDPOINT EXCLUSION THROUGH DEPTH 30,000,003`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## 1. Input from MATH-021

MATH-021 reduced any internal adjacent-block same-endpoint candidate collision at depth `k` to the exact displacement condition

\[
0<d<Q/3\le k/3.
\]

For

\[
N_L=b2^{61}-\ell,
\qquad
N_R=b2^{61}+r,
\]

we have

\[
d=\ell+r.
\]

Therefore a right offset `r` can participate in a collision only after it enters the linear halo:

\[
\boxed{k\ge 3r+1.}
\]

This gives a new computational comparison for each right offset:

\[
\boxed{
\text{candidate lifespan }L(b,r)
\quad\text{versus}\quad
\text{halo-entry depth }3r+1.
}
\]

If

\[
L(b,r)<3r+1
\]

for every internal boundary `b`, then that ordinary start loses candidate status before it can possibly participate in a same-endpoint cross-boundary collision.

## 2. Exhaustive right-offset domain

The certificate exhausts

\[
0\le r\le10^7.
\]

For the first 61 steps, the candidate prefix depends only on `r`, because

\[
b2^{61}+r\equiv r\pmod{2^{61}}.
\]

Exact filtering leaves

\[
\boxed{17,745}
\]

right offsets that satisfy every coefficient-survival prefix through depth 61.

The first and last such offsets in the audited interval are

\[
703,
\qquad
9,999,823.
\]

All other offsets in `[0,10^7]` are permanently excluded from the candidate language by or before depth 61.

## 3. Exact continuation through all internal boundaries

For each surviving lower-61 offset and every

\[
b=1025,\ldots,1363,
\]

the calculation uses the exact affine lower-prefix identity

\[
T^{61}(b2^{61}+r)
=
T^{61}(r)+b3^{q_{61}(r)}.
\]

The resulting state is then continued with the shortcut map while enforcing the coefficient-survival gate at every prefix.

The published-floor threshold

\[
\left(3+2^{-71}\right)^q>2^k
\]

is checked by exact integer arithmetic to have the same minimum integer `q` as `3^q>=2^k` for every depth `1..512` used by this computation.

## 4. Lifespan result

None of the

\[
17,745\times339
\]

continued right states survives through depth 512.

The largest candidate lifespan found is exactly

\[
\boxed{429}.
\]

The first lexicographic witness attaining this maximum is

\[
\boxed{r=276,199,\qquad b=1177.}
\]

By comparison, the **smallest** halo-entry depth in the entire audited right-offset domain is already

\[
3\cdot703+1=2110.
\]

Therefore every audited right state satisfies

\[
\boxed{L(b,r)<3r+1}.
\]

No audited offset ever becomes collision-relevant while it is still a candidate.

## 5. Depth interval obtained without scanning every depth

For any

\[
61\le k\le3\cdot10^7+3
=30,000,003,
\]

MATH-021 forces every possible collision right offset to satisfy

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor\le10^7.
\]

Every such offset has been exhaustively classified:

- it either fails by depth 61; or
- it survives depth 61 but then dies before its own halo-entry depth `3r+1` on every internal boundary.

Hence

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate pair exists for}
\quad61\le k\le30,000,003.
}
\]

This is a finite bootstrap theorem built from an exact linear-halo reduction and an exhaustive finite right-offset calculation.  It is not a universal Collatz proof.

## 6. Why this supersedes naive depth stepping

Before MATH-021, the calculation proceeded depth by depth:

\[
72,73,\ldots,81.
\]

MATH-021 changed the relevant coordinate from depth to **ordinary displacement**.  MATH-022 then audits a block of 10,000,001 right offsets once and obtains a depth interval of about thirty million steps.

The computational architecture has therefore changed from

\[
\text{deeper endpoint scan}
\]

to

\[
\boxed{
\text{offset prefix filter}
\to
\text{lifespan}
\to
\text{halo-entry comparison}.
}
\]

This is the preferred DSD-native direction because the gate is both exact and much earlier than endpoint equality testing.

## 7. DSD cause classification

For the audited internal boundary problem, the gates now order as follows:

1. **right prefix survival** — removes almost every small offset immediately;
2. **lifespan vs halo-entry** — removes every remaining offset through `10^7` before endpoint comparison is legal/relevant;
3. final-`Q` support — unnecessary in this range;
4. normalized endpoint interval order — unnecessary in this range;
5. endpoint equality — never reached.

Thus the MATH-019/MATH-020 endpoint-order phenomenon remains correct, but MATH-022 finds an earlier exclusion gate for the actual collision-complete region.

## 8. Prohibited upgrades

Do not infer:

- no internal endpoint coupling through depth 30,000,003 `=>` no candidate integers;
- audited `r<=10^7` behavior `=>` all right offsets;
- internal-boundary independence `=>` first-cell emptiness;
- this endpoint result `=>` arbitrary full-Hensel or terminal-correction closure;
- finite bootstrap `=>` arbitrary-depth theorem.

The first universal cell and the Collatz conjecture remain open.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_right_offset_lifespan_bootstrap_10m_certificate.cpp`

Certificate commit:

`02b5095c8e54d04175f094cf057d31040d774c0c`

Expected key output:

```text
PASS
RMAX=10000000
depth61 surviving right offsets in [0,RMAX]=17745
first survivor=703 last survivor=9999823
max candidate lifespan=429 at r=276199 boundary=1177
states surviving through depth512=0
states reaching their halo-entry depth 3r+1=0
internal adjacent-block endpoint collision excluded through depth=30000003
COLLATZ STATUS=OPEN
```

## Next target

The next brute-force extension would be `r>10^7`, but DSD route selection says not to scale it blindly.

First analyze the 17,745 audited survivor offsets and their lifespans for a structural inequality or finite-state descriptor that can certify

\[
L(b,r)<3r+1
\]

without enumerating every `r` individually.

If no such descriptor appears, extend the finite bootstrap in bounded chunks while preserving the same exact certificate structure.

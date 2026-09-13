# MATH-123 — linear AP resolution/value lexicographic rank

Status: `MAINLINE EXACT LEMMA / STRONGER THAN MATH-122 / NO NEW LAYER CLOSURE CLAIM`

Date: 2026-09-14

## Setup

For one exact unmerged AP branch

```text
P(a,b,m) = {a+bk : 0<=k<m},
```

with odd `b>0`, multiplicity `m>=2`, and current maximum

```text
N = a+b(m-1),
```

MATH-122 showed that every parity child satisfies

```text
m' <= ceil(m/2) < m.
```

## Stronger linear value-resolution quantity

Define

```text
W = (N+1)m.
```

### Odd child

For every odd member,

```text
T(n)+1 = 3(n+1)/2.
```

Therefore

```text
N'+1 <= 3(N+1)/2,
m' <= ceil(m/2),
```

and hence

```text
W' <= (3/2)(N+1) ceil(m/2).
```

For every integer `m>=2`,

```text
3 ceil(m/2) <= 2m.
```

Thus

```text
W' <= W.
```

The coefficient inequality is strict except when `m=3`. Even in the equality case, `m'<m`.

### Even child

For an even child,

```text
N'+1 < N+1,
m'<m,
```

so

```text
W'<W.
```

## Exact well-founded rank

Use the lexicographic pair

```text
R = (W,m).
```

On every non-singleton exact AP refinement:

- either `W'<W`; or
- `W'=W` can occur only in the exceptional coefficient-equality case, where `m'<m`.

Therefore

```text
(W',m') <_lex (W,m)
```

strictly on every branch step.

Because `W,m` are positive integers, this is a well-founded branch-local rank.

## Stronger singleton growth bound

When an exact branch is fully resolved to `m=1`, repeated monotonicity gives

```text
N_singleton + 1 <= (N_source + 1) m_source.
```

This improves the quadratic bound supplied by the simpler MATH-122 scalar rank.

The bound is still not a frozen-floor closure theorem: the right-hand side can be much larger than `2^71`.

## Why this matters

MATH-123 proves simultaneously that:

1. AP resolution cannot continue indefinitely;
2. value growth incurred while consuming AP multiplicity is linearly compensated by the loss of unresolved multiplicity;
3. a branch cannot obtain arbitrary value growth for free while retaining a large unresolved source family.

This is precisely the structural coupling missing from a rank based only on the MATH-120 floor deficit.

## Remaining obstruction

At `m=1`, the rank becomes

```text
W=N+1.
```

An odd singleton shortcut may increase `W`. Therefore a second-stage address/macro rank is still required after full source resolution, or a floor gate must fire before that point.

MATH-123 does not close any new paid-count layer by itself.

## Claim boundary

The certified multi-paid frontier remains `r>=12 CLOSED`; `r=11` remains under MATH-116 execution and `r<=10` remain open. First-cell and Collatz status are unchanged.

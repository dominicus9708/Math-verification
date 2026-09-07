# External audit — Denjoy–Koksma / Ostrowski rotation-sum input

Date: 2026-09-07

Status: **A — POSITIVE PRIOR ART / SAFE WITHIN STATED SCOPE.**

## 1. External sources audited

Primary usable references:

- Jean-Pierre Conze, Stefano Isola, Stéphane Le Borgne, *Diffusive behavior of ergodic sums over rotations*, Stochastics and Dynamics 19(02), 1950016 (2019), DOI `10.1142/S0219493719500163`.
- Lorenz Frühwirth, Manuel Hauke, *On the metric upper density of Birkhoff sums for irrational rotations*, Nonlinearity 36 (2023), 7065–7104, DOI `10.1088/1361-6544/ad086f`.

The first source explicitly records the standard Denjoy–Koksma bound at convergent denominators and the Ostrowski decomposition of an arbitrary time `N`, yielding

\[
\left|\sum_{j=0}^{N-1}\phi(x+j\alpha)-N\int_0^1\phi\right|
\le \operatorname{Var}(\phi)\sum_i b_i
\]

when

\[
N=\sum_i b_i q_i
\]

is the Ostrowski expansion relative to the convergent denominators `q_i` of the irrational rotation angle `alpha`.

The second source independently uses the same classical Denjoy–Koksma/Ostrowski framework and records the arbitrary-`N` bound in terms of the continued-fraction/Ostrowski digits.

## 2. DSD claim-unit audit

### DK-1 — convergent-time Denjoy–Koksma inequality

For irrational rotation by `alpha`, a 1-periodic bounded-variation observable `phi`, every phase `x`, and every continued-fraction denominator `q_n`,

\[
\left|\sum_{j=0}^{q_n-1}\phi(x+j\alpha)-q_n\int_0^1\phi\right|
\le \operatorname{Var}(\phi).
\]

Verdict: **A / SAFE EXTERNAL THEOREM.**

### DK-2 — arbitrary-time Ostrowski decomposition

If

\[
N=\sum_i b_iq_i
\]

is the Ostrowski expansion, split the orbit segment into `b_i` translated blocks of length `q_i`. Applying DK-1 to every translated block and using the triangle inequality gives

\[
\boxed{
\left|S_N-N\int\phi\right|
\le \operatorname{Var}(\phi)\sum_i b_i.
}
\]

Verdict: **A / SAFE DERIVED USE.** No probabilistic independence or asymptotic equidistribution is required.

## 3. Application interface for the Collatz first-cell rotation sum

Use

\[
\theta=\log_2(3/2).
\]

This is irrational: if `theta=p/q` were rational, then

\[
3^q=2^{p+q},
\]

contradicting unique prime factorization.

Define the periodic observable

\[
f(x)=2^{-\{x\}}.
\]

On the circle it decreases from `1` to `1/2` and has a jump of size `1/2` back to `1`, so

\[
\boxed{\operatorname{Var}(f)=1.}
\]

Also

\[
\boxed{
\int_0^1 f(x)\,dx
=\frac1{2\ln2}.
}
\]

Therefore for every `N` with Ostrowski digits `b_i`,

\[
\boxed{
\left|
\sum_{n=0}^{N-1}2^{-\{x+n\theta\}}
-\frac{N}{2\ln2}
\right|
\le \sum_i b_i.
}
\]

## 4. Exact arithmetic coincidence at the first universal cell

The exact continued-fraction prefix of `theta` needed here is

```text
[0; 1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2]
```

with consecutive denominators

\[
q_{21}=6,586,818,670,
\]

\[
q_{22}=65,470,613,321,
\]

\[
q_{23}=137,528,045,312.
\]

The first universal Collatz cell has

\[
Q_0=72,057,431,991
=q_{22}+q_{21}.
\]

Since the next partial quotient is `a_23=2`, this is the valid Ostrowski expansion

\[
\boxed{Q_0=q_{22}+q_{21}}
\]

with digit sum

\[
\boxed{\sum_i b_i=2.}
\]

The accompanying certificate verifies the continued-fraction cylinder using rigorous rational intervals for `ln 2` and `ln 3`; no floating-point continued-fraction decision is used.

Thus

\[
\boxed{
\left|
\sum_{n=0}^{Q_0-1}2^{-\{x+n\theta\}}
-\frac{Q_0}{2\ln2}
\right|
\le2
\quad\text{for every phase }x.
}
\]

## 5. Permitted citation role

This theorem may be cited positively to replace the earlier 1024-block uniform rotation cap by an essentially exact global mean-plus-constant bound.

It is a theorem about a deterministic irrational rotation sum. It does **not** by itself establish any of the following:

- that the mechanical word has an ordinary positive start in the surviving Collatz interval;
- that a large correction and the required dyadic start address occur for the same word;
- that the first universal cell is empty;
- that Collatz is proved.

## 6. Prohibited upgrades

1. `small discrepancy` does not imply same-integer compatibility.
2. `rotation average` does not imply stochastic independence of parity bits.
3. Denjoy–Koksma controls the scalar correction envelope only; it does not solve the joint dyadic-address/correction gate.
4. The external theorem must be used with the exact observable variation and exact Ostrowski digits, not with a guessed asymptotic `O(log N)` constant.

## 7. DSD verdict

\[
\boxed{
\text{Denjoy–Koksma + Ostrowski arbitrary-time BV bound: A / SAFE.}
}
\]

The imported theorem is stronger than required here because the first-cell time has digit sum exactly `2`. This is a positive literature absorption, not a conditional input.

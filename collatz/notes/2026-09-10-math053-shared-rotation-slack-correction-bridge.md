# MATH-053 — shared rotation and slack-correction bridge

Date: 2026-09-10
Status: `EXACT ALGEBRAIC BRIDGE / FINITE REGRESSION PASS / HENSEL-TO-SLACK LOWER BOUND OPEN`

Collatz conjecture: `OPEN`.

## 1. Shared irrational rotation

Let

\[
\theta=\log_2(3/2).
\]

The coefficient boundary in the universal `(q,d)` lattice is

\[
m(q)=\lfloor q\theta\rfloor.
\]

The mechanical first-crossing odd-position formula used earlier is

\[
p_r=\lfloor(r-1)\log_2 3\rfloor.
\]

Since `log_2 3 = 1+theta`,

\[
\boxed{p_r=(r-1)+m(r-1)}.
\]

Thus the root-Hensel coefficient boundary and the earlier mechanical first-crossing word are driven by the same irrational rotation.

## 2. Boundary slack

For a coefficient-valid prefix with q odd and d even shortcut steps, define

\[
\boxed{u=m(q)-d}.
\]

Because `q theta` is irrational for q>0,

\[
3^q>2^{q+d}\iff d\le m(q)\iff u\ge0.
\]

Let

\[
\varepsilon_{q+1}=m(q+1)-m(q)\in\{0,1\}.
\]

Then the exact forward slack transitions are

\[
\boxed{E:u\mapsto u-1},
\qquad
\boxed{O:u\mapsto u+\varepsilon_{q+1}}.
\]

Hence first coefficient failure is exactly an even transition from `u=0` to `u=-1`.

## 3. Mechanical phase variable

Define

\[
\boxed{\Omega_q=\frac{2^{q+m(q)}}{3^q}=2^{-\{q\log_2 3\}}}.
\]

Then `1/2 < Omega_q <= 1` and, because the equality threshold never occurs,

\[
\boxed{
\Omega_{q+1}=\begin{cases}
\frac23\Omega_q,&\Omega_q>\frac34,\\
\frac43\Omega_q,&\Omega_q<\frac34.
\end{cases}}
\]

This is an exact piecewise-rational realization of the same irrational rotation.

## 4. Exact normalized correction decomposition

For the shortcut-map correction `C` and current odd count q, put

\[
S=C/3^q.
\]

At an odd step taken from a state with q odd steps already accumulated and boundary slack u,

\[
\Delta S=\frac{2^{q+d}}{3^{q+1}}
=\boxed{\frac{\Omega_q}{3\,2^u}}.
\]

Therefore, if `u_n` is the slack immediately before the `(n+1)`-st odd step,

\[
\boxed{S(w)=\frac13\sum_{n=0}^{q-1}2^{-u_n}\Omega_n}.
\]

The boundary/mechanical word has `u_n=0` at every odd event, so

\[
\boxed{S_*=\frac13\sum_{n=0}^{q-1}\Omega_n}.
\]

For any coefficient-valid word,

\[
\boxed{S_*-S(w)=\frac13\sum_{n=0}^{q-1}(1-2^{-u_n})\Omega_n\ge0}.
\]

Thus positive boundary slack has an exact additive correction cost.

## 5. Why this is the next proof bridge

The earlier correction-only route showed that the mechanical maximum `S_*` is too large to close the first universal cell by a scalar upper bound alone. The current root-Hensel work gives an exact finite-state characterization of class-maximality. The remaining bridge is therefore:

\[
\boxed{\text{nested Hensel maximality + same-integer lineage}\Longrightarrow\text{a universal lower bound on }\sum (1-2^{-u_n})\Omega_n.}
\]

If the lower bound exceeds the correction-only surplus required by the first-cell endpoint inequality, the same-integer first-cell branch is excluded.

## 6. Audit boundary

Established here: shared rotation identity, exact slack transitions, exact Omega recurrence, exact correction decomposition.

Not established here: any positive asymptotic density of `u_n>0`, any arbitrary-depth Hensel-to-slack lower bound, emptiness of the first universal cell, or the Collatz conjecture.

# MATH-053 — boundary phase, integer slack, and normalized-correction bridge

Date: 2026-09-10
Status: `EXACT ALGEBRAIC BRIDGE / FINITE REGRESSION PASS / SAME-INTEGER LOWER BOUND OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note changes the representation of the coefficient/correction calculation; it does not close the same-integer bridge.

## 1. Shared coefficient-boundary phase

Put

\[
\theta=\log_2(3/2),\qquad m(q)=\lfloor q\theta\rfloor.
\]

For a prefix with `q` odd shortcut steps and `d` even shortcut steps,

\[
3^q>2^{q+d}
\]

is exactly equivalent to

\[
\boxed{d\le m(q)}.
\]

Define the integer distance from the coefficient boundary

\[
\boxed{u=m(q)-d.}
\]

Then coefficient admissibility is simply `u>=0`.

Let

\[
\varepsilon_{q+1}=m(q+1)-m(q)\in\{0,1\}.
\]

The forward parity transitions are

\[
\boxed{E:u\mapsto u-1},
\]

\[
\boxed{O:u\mapsto u+\varepsilon_{q+1}}.
\]

Hence a first coefficient failure is exactly the local transition

\[
\boxed{u=0\xrightarrow{E}-1}.
\]

This makes the moving coefficient line a one-dimensional integer slack process driven by the mechanical word `epsilon_q`.

## 2. Exact phase weight

Define

\[
\boxed{\Omega_q=\frac{2^{q+m(q)}}{3^q}}.
\]

Since

\[
\log_2 3=1+\theta,
\]

we also have algebraically

\[
\Omega_q=2^{-\{q\theta\}}=2^{-\{q\log_2 3\}}.
\]

The exact rational update is

\[
\boxed{
\Omega_{q+1}=\begin{cases}
\frac23\Omega_q,&\varepsilon_{q+1}=0,\\[1mm]
\frac43\Omega_q,&\varepsilon_{q+1}=1.
\end{cases}}
\]

Equivalently, for positive q,

\[
\Omega_q>\frac34\Rightarrow\varepsilon_{q+1}=0,
\qquad
\Omega_q<\frac34\Rightarrow\varepsilon_{q+1}=1.
\]

The phase therefore needs no floating-point logarithm in exact computation.

## 3. Normalized correction as a weighted slack sum

For the shortcut map write

\[
T^k(N)=\frac{3^qN+C}{2^k},
\qquad
S=\frac{C}{3^q}.
\]

Immediately before an odd shortcut step, let the current odd/even counts be `(q,d)` and let

\[
u=m(q)-d.
\]

The correction recurrence adds `2^(q+d)` to the unnormalized correction before division by the new power of 3. Therefore the exact contribution to `S` is

\[
\frac{2^{q+d}}{3^{q+1}}
=\frac{2^{q+m(q)-u}}{3^{q+1}}
=\boxed{\frac{\Omega_q}{3\,2^u}}.
\]

If `u_n` is the slack immediately before the `(n+1)`-st odd step, then every coefficient-surviving parity word satisfies

\[
\boxed{
S(w)=\frac13\sum_{n=0}^{q-1}2^{-u_n}\Omega_n.
}
\]

This identity has been regressed by exact rational arithmetic against the original correction recurrence for exhaustive small parity words in the accompanying certificate.

## 4. Boundary-envelope decomposition

Define the formal coefficient-boundary envelope

\[
\boxed{
S_{\partial}(q)=\frac13\sum_{n=0}^{q-1}\Omega_n.
}
\]

For any coefficient-surviving word,

\[
\boxed{
S_{\partial}(q)-S(w)
=\frac13\sum_{n=0}^{q-1}
\left(1-2^{-u_n}\right)\Omega_n.
}
\]

Thus every positive unit of integer slack has an explicit correction cost.  This is the correct bridge quantity to carry into a same-integer optimization.

Important scope rule: `S_partial` is a boundary envelope defined by the slack representation.  It must not be silently identified with any historically named mechanical correction extremizer until the orientation/index convention of that older construction is checked explicitly.

## 5. Relation to MATH-052

MATH-052 compressed exact Hensel dominance into the universal `(q,d)` credit transducer and introduced the coefficient-boundary slack coordinate.  MATH-053 shows that the same slack coordinate also controls the normalized correction multiplicatively through `2^{-u}`.

Therefore Hensel state and correction budget can be coupled without restoring the original parity word, provided the exact same-integer dyadic-address lineage is carried separately.

The desired future implication is not

\[
\text{Hensel maximality}\Rightarrow u>0.
\]

Finite targeted tests already show that this implication is false as a standalone principle: coefficient-boundary/extremal candidates can remain Hensel class-max over substantial audited ranges.

The required bridge is instead

\[
\boxed{
\text{Hensel maximality + same-integer address + first-cell/endpoint constraints}
\Rightarrow
\text{a quantitative lower bound on the weighted slack penalty}.
}
\]

## 6. Exact same-integer address equation

For a fixed length-k parity word `(q,C)`, integrality of the endpoint gives

\[
3^qN+C\equiv0\pmod{2^k}.
\]

Since 3 is invertible modulo powers of 2,

\[
\boxed{
N(w)\equiv-C(w)\,3^{-q}\pmod{2^k}.
}
\]

At a root-safe depth `k` exceeding the known first-cell start bit-length, the canonical residue is the ordinary start itself.  This is the exact coupling to be added next; address and correction are not independent filters.

## 7. DSD audit result

The current information hierarchy is

\[
(q,d)\to(q,u)\to(q,\Omega,u,S),
\]

where `Omega` is determined by q and `S` is an additive functional of the slack history.  The parity word itself is unnecessary for this correction functional.

However the ordinary starting residue is not determined by the terminal `(q,u,S)` alone.  The dyadic address remains necessary lineage information and cannot be quotiented away without a separate exact equivalence proof.

## 8. Reproducibility

Certificate:

`collatz/src/2026_09_10_boundary_phase_slack_correction_certificate.py`

The certificate checks:

1. exact integer evaluation of `m(q)`;
2. equivalence of the coefficient inequality and `u>=0`;
3. the exact `Omega` recurrence;
4. even/odd slack transitions;
5. the first-failure transition `0 -> -1` under an even step;
6. the normalized-correction weighted-sum identity against the original correction recurrence.

## 9. Open bridge

Do not continue increasing finite depth merely to accumulate more counts.  The next target is the product state that simultaneously preserves

- coefficient slack / shared mechanical phase;
- Hensel maximality state;
- the same ordinary integer's dyadic root address;
- endpoint/correction budget.

The proof-facing question is whether this exact product system admits an infinite bad path, not how many finite prefixes survive at each depth.

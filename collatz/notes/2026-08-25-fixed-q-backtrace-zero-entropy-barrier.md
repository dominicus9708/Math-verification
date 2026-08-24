# Fixed-Q root-backtrace filters have zero asymptotic entropy rate on the harmonic hard core

Date: 2026-08-25

Status: **exact proof-strategy barrier.**  The root-globalized backtrace/headroom filters remain valid minimal-counterexample propositions and are useful for finite correction bounds.  This note proves that keeping the inverse depth `Q` fixed cannot by itself provide a positive linear entropy gap on a hypothetical nonperiodic no-first-descent hard orbit.  The conclusion is a limitation on the current fixed-Q route, not a Collatz result.

## 1. Mechanical-height coordinate

Let

\[
\gamma:=\log_2 3,
\qquad
B_i:=\lfloor i\gamma\rfloor,
\]

and let

\[
A_i=\sum_{j<i}v_j
\]

be the accumulated actual halving count at odd-event time `i`.

The coefficient-survival/mechanical height is

\[
\boxed{h_i:=B_i-A_i\ge0.}
\]

Writing

\[
\theta_i:=\{i\gamma\},
\]

the harmonic weight is exactly

\[
\lambda_i:=\frac{2^{A_i}}{3^i}
=2^{A_i-i\gamma}
=
\boxed{2^{-h_i-\theta_i}}.
\]

Hence for every fixed integer `H0>=0`,

\[
h_i\le H_0
\quad\Longrightarrow\quad
\boxed{\lambda_i>2^{-(H_0+1)}}.
\]

For a hypothetical nonperiodic no-first-descent orbit, the harmonic theorem gives

\[
\boxed{
\sum_{i<q}\lambda_i\le C_Nq^{1/9}.
}
\]

Therefore

\[
\boxed{
\#\{i<q:h_i\le H_0\}
<2^{H_0+1}C_Nq^{1/9}.
}
\]

Every fixed mechanical-height strip is visited only `O_N(q^(1/9))` times.

## 2. A fixed inverse depth can only act in a bounded height strip

Consider a root-globalized inverse/backtrace witness with

- reverse odd depth `1<=q<=Q`;
- total inverse halving count `K>=q`;
- current mechanical height `h>=0`;
- phase factor `2^theta>=1`.

The exact headroom inequality used by the phase-adaptive certificates has the form

\[
2^{K+h}2^\theta(3V+H)<3^{q+1}V.
\]

A necessary condition for this inequality is obtained from

\[
2^\theta\ge1,
\qquad
3V+H>3V:
\]

\[
3\,2^{K+h}V<3^{q+1}V,
\]

so

\[
\boxed{2^{K+h}<3^q.}
\]

Since `K>=q`,

\[
2^{q+h}<3^q,
\]

hence

\[
\boxed{
h<q\log_2(3/2)\le Q\log_2(3/2).
}
\]

Thus every fixed-`Q` root-backtrace filter is automatically confined to the bounded strip

\[
\boxed{
0\le h\le H_Q:=\lfloor Q\log_2(3/2)\rfloor.
}
\]

The exact current `Q=8` phase-adaptive certificate is even tighter: after exact phase suprema are included, the nonempty forbidden tables occur only through `h=3`.

## 3. Harmonic sparsity of all fixed-Q filter opportunities

Combining Sections 1 and 2,

\[
\#\{i<q:\text{a fixed-Q root-backtrace witness can fire at }i\}
\le
\#\{i<q:h_i\le H_Q\}
\]

and therefore

\[
\boxed{
\#\{\text{fixed-Q opportunities before }q\}
=O_{N,Q}(q^{1/9}).
}
\]

So the valid repeated-backtrace proposition acts at zero-density event times on the harmonic hard core.

## 4. Zero entropy-rate consequence

For fixed `Q`, the inverse residue state lies in a finite set (for example modulo `3^Q`) and each firing event can impose only `O_Q(1)` bits of local finite-state information.

Since there are only `O_{N,Q}(q^(1/9))` firing opportunities up to odd-event time `q`, the total amount of exclusion information that a fixed-Q local automaton can accumulate is at most

\[
\boxed{O_{N,Q}(q^{1/9})=o(q)}.
\]

Equivalently, any language-size improvement obtainable solely by attaching a fixed-Q finite-state root-backtrace filter to the harmonic hard core is at most a subexponential factor

\[
\boxed{2^{o(q)}}.
\]

It cannot create a new positive linear entropy gap.

This explains why the exact `Q=8` calculations can substantially improve finite correction budgets while failing to resolve the asymptotic ternary/dyadic dimension mismatch.

## 5. Required growth of inverse depth

The harmonic area-deficit theorem says that for every `epsilon>0`, density-one many large odd-event times satisfy roughly

\[
h_i\ge\left(\frac89-\epsilon\right)\log_2 i.
\]

For an inverse-depth filter to reach this typical strip, its maximal possible active height

\[
H_Q\sim Q\log_2(3/2)
\]

must grow comparably.  Thus a necessary scale for a fixed-form backtrace strategy to interact with density-one hard-core times is

\[
\boxed{
Q(i)\gtrsim
\frac{8}{9\log_2(3/2)}\log_2 i
=1.51956559\ldots\log_2 i.
}
\]

This is only a necessary scale, not a sufficient theorem.

## 6. Consequence for the proof program

The next backtrace target should therefore not be a larger but still fixed table such as `Q=9`, `Q=10`, or `Q=12` merely to improve a finite percentage.

A terminal root-minimality route would need a **growing-depth backtrace theorem** in which

\[
Q=Q(i)\to\infty
\]

at least logarithmically with the event scale, while retaining:

1. exact root-globalization (`m<N`);
2. controllable residue/state complexity;
3. compatibility with the same fixed ordinary integer / ternary selector address.

The current `Q<=8` phase-adaptive certificates are retained as exact finite calibrations and correction-budget tools, but fixed-Q entropy refinement is pruned as a terminal strategy.

# Lazy ternary observation theorem

Status: **EXACT / CLOSED within stated predicate scope**

Executable regression guard:

- `../src/A0_s1_routeB_lazy_ternary_observation_bellman_certificate.py`

## Statement

Fix a target-dominance prefix with current one-count `q` and integer normalized-defect numerator

\[
N_q=3^q\eta_q=C_q^*-C(W_q)\ge0.
\]

Fix a prescribed final one-count `J` and suppose a downstream predicate queries only the final defect/correction residue

\[
N_J\pmod{3^L}.
\]

Let

\[
s=J-q
\]

be the number of future one-events.

Every fixed future suffix has

\[
N_J=3^sN_q+A_{\rm suffix},
\]

where `A_suffix` depends only on that future suffix.

Therefore the smallest generally sufficient present ternary precision is

\[
\boxed{m(q)=\max\{0,L-(J-q)\}.}
\]

The exact forward observation coordinate is

\[
\boxed{R_q=N_q\bmod 3^{m(q)}}
\]

with the unique trivial state `R_q=0` when `m(q)=0`.

## Dormancy theorem

If

\[
J-q\ge L,
\]

then

\[
3^{J-q}N_q\equiv0\pmod{3^L}.
\]

Hence the present prefix defect residue is completely invisible to the final `L`-trit observation.

The ternary coordinate is therefore dormant until the last `L` future one-events.

For the current A0 `s=1` target

\[
J=j_0=65,868,186,701.
\]

For a 28-trit final correction/defect observation,

\[
R_q\text{ is unnecessary for }q\le j_0-28
=65,868,186,673.
\]

It first becomes nontrivial at

\[
q=65,868,186,674.
\]

For a 24-trit observation it is dormant through

\[
q\le65,868,186,677.
\]

These statements concern a final defect/correction congruence only. They do not assert that every checkpoint predicate has already been reduced to that form.

## Minimality

Assume `m(q)>0` and try to store only `N_q mod 3^(m(q)-1)`.

Take two admissible abstract prefix numerators differing by

\[
\Delta N=3^{m(q)-1}.
\]

They are indistinguishable at the proposed lower precision.

Under the same future suffix their final difference is

\[
3^{J-q}\Delta N
=3^{J-q+m(q)-1}
=3^{L-1},
\]

which is nonzero modulo `3^L`.

Thus, for an arbitrary fixed future suffix, one fewer trit is not sufficient in general.

The precision schedule `m(q)` is therefore not merely sufficient; it is the minimal generic observation resolution.

## Forward transition

If the next emitted parity bit is `0`, then

\[
q'=q,
\qquad N'=N,
\]

so

\[
R'=R.
\]

If the next emitted bit is the new ranked one at absolute position `h`, with target ranked-one position `a_(q+1)`, put

\[
d=2^{a_{q+1}}-2^h\ge0.
\]

Then

\[
N'=3N+d.
\]

Once the ternary coordinate is active, every such one-event raises the required precision by exactly one trit:

\[
m'=m+1,
\]

and

\[
\boxed{R'=3R+d\pmod{3^{m+1}}.}
\]

Before activation, the state remains the unique trivial residue.

## Backward singleton transition

For a fixed one-event and prescribed successor residue `R' mod 3^(m+1)`, a predecessor exists exactly when

\[
R'\equiv d\pmod3.
\]

When this holds the predecessor residue is unique:

\[
\boxed{R=(R'-d)/3\pmod{3^m}.}
\]

Hence a fixed final ternary residue propagates backward through a fixed parity suffix as either:

- an impossible branch; or
- one unique predecessor residue cylinder.

The projective residue is therefore a **filter/control coordinate**, not a defect cost.

## Bellman compatibility with the physical danger score

The directed physical gate already has the exact scalar score

\[
P=m_{lo}N+\delta_{lo}3^qX_{lo}
\]

with closure test

\[
P>B3^q.
\]

For the source/ballot/interval predicates, common child transitions map `P` by an increasing affine map `P -> P+c` or `P -> 3P+c`.

After the final ternary residue predicate is activated, use the exact key

\[
\boxed{(Y,q,\text{interval payload},R_q)}
\]

and retain only

\[
\boxed{P_{min}}
\]

for that key.

Histories sharing the augmented key and one next parameter bit have:

- the same emitted parity;
- the same child interval payload;
- the same next `q`;
- the same projective-residue transition;
- the same increasing affine transformation of `P`.

Therefore the minimum `P` label remains exact after the ternary observation is added.

No separate `(r,N)` Pareto frontier is restored by this predicate.

## DSD analysis

The state separates three logically different roles:

1. **transition control** — source future-control state `(Y,q)` and interval payload;
2. **observation resolution** — lazy projective residue `R_q`;
3. **decision cost** — physical danger label `P_min`.

The previous local-carry greedy counterexample remains respected: this theorem does not choose the future carry/cylinder sequence greedily. It only states the exact information required once the forward or backward branch is specified.

## Audit classification

### EXACT / CLOSED

- suffix identity `N_J=3^(J-q)N_q+A_suffix`;
- minimal generic precision `m(q)=max(0,L-(J-q))`;
- dormancy before the last `L` one-events;
- one-trit forward activation law;
- unique-or-empty backward one-event predecessor;
- compatibility of the augmented residue key with one `P_min` Bellman label.

### REGRESSION ONLY

The executable certificate compares raw source histories against the augmented quotient on small first-defect shapes and finite parameter intervals. Those finite comparisons guard implementation only.

### NOT INFERRED

- that checkpoint, debit, C4F, or tail predicates all reduce to `N_J mod 3^L`;
- closure of any current 14-root family;
- full Route-B membership/nonmembership;
- the Collatz conjecture.

## Strategic consequence

A forward terminal-ternary coordinate is mathematically cheap for almost the entire long bridge because it is dormant, but for the same reason it cannot supply early pruning there.

To exploit a terminal ternary condition before the last `L` one-events, the useful direction is a **backward singleton-residue filter through the compressed right-side H/projective grammar**, followed by a join with the forward source/physical Bellman state.

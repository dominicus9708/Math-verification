# Collatz terminal-gate execution checklist

Date: 2026-08-25

This is the operational companion to `2026-08-25-dsd-terminal-proof-chain-roadmap.md`.

## Gate A — candidate-language tail tightness

Status: **OPEN / highest priority**

Already safe:

- coefficient ratio `Theta_q = 3^q / 2^A_q`;
- signed skew and Beatty surplus are logarithmic projections of `Theta`;
- Beatty macrocycles are `A=PR`, `B=PRR`, with `AA` forbidden;
- weighted dyadic surplus contraction factor at most `3125/3456` per macrocycle pair;
- fixed-Q and uniform adaptive-Q reverse-density closure are unavailable.

Required next:

- [ ] condition the weighted Beatty transfer on the actual canonical / ternary-selector candidate language;
- [ ] measure whether the conditioned factor remains `<1` on exact finite horizons;
- [ ] identify the static comparison quantity responsible for any preserved contraction;
- [ ] prove a horizon-independent tail inequality;
- [ ] state the final Gate-A theorem with all conditioning explicit.

Failure criterion:

If selector conditioning makes the weighted factor approach or exceed `1`, do not force the Lyapunov route.  Record the failure and move to arithmetic correlation/min-plus alternatives.

## Gate B — low-strip finite-state loss

Status: **OPEN, but deferred until Gate A has a viable transfer theorem**

Already safe / certified:

- exact `(d,z)` local transfer after endpoint decoupling;
- exact reverse-potential DP;
- multiple finite Q7/H24-H25 cross-place pruning certificates;
- root-global minimality filters;
- fixed-Q ceiling identifies why only a bounded strip can be handled this way.

Required after Gate A:

- [ ] choose a strip height `D` justified by the Gate-A tail bound;
- [ ] choose ternary resolution `Q` and block length `r`;
- [ ] construct the exact finite killed transition matrix / automaton;
- [ ] certify a substochastic spectral radius or block loss `<1`;
- [ ] independently reproduce the gap with a second implementation if feasible.

Do not optimize survivor counts before `D,Q,r` are justified by Gate A.

## Gate C — minimal-counterexample closure

Status: **OPEN / terminal globalization**

Already safe:

- canonical formation classes and lift digits;
- positive ordinary integer naturalness iff lift digits are eventually zero;
- root-level Hensel/minimality implications that have survived pullback audit.

Required:

- [ ] formulate a hypothetical minimal counterexample as an infinite nested sequence of canonical candidate cylinders;
- [ ] combine Gate-A recurrence/tightness with Gate-B recurrent loss;
- [ ] show this recurrent loss is incompatible with eventual stabilization `rho_q=N` / eventual zero lift digits;
- [ ] ensure no step replaces `measure -> 0` by `set = empty` without an additional discrete/minimality argument;
- [ ] audit every later-block statement for root globalization.

## Auxiliary arithmetic-correlation route

Status: **secondary / only pursue on concrete forcing evidence**

Target:

`eventual-zero lift + minimality` forces endpoint residues into exponentially rare strong-reverse classes at a rate far above generic density.

Do not pursue generic-density versions: universal reverse rarity already rules them out.

## Closed/demoted routes

- [x] fixed-Q reverse elimination over unbounded surplus: closed;
- [x] adaptive Q for uniform positive strong-reverse density: closed;
- [x] bounded pathwise return time to Beatty boundary: false;
- [x] stopped-tree coefficient-only energy closure: dimension barrier;
- [x] arbitrary later-block Hensel maximality: withdrawn;
- [x] finite m=44 elimination percentage as global proof progress: prohibited interpretation.

## Immediate execution order

1. Gate A conditioned Lyapunov diagnostic.
2. Gate A static comparison / mixing inequality.
3. Gate A theorem attempt.
4. Only then Gate B finite-state spectral certificate.
5. Gate C nested-cylinder/minimality contradiction.

Current bottleneck:

`Beatty high-surplus drift -> actual canonical candidate language`.

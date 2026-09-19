# MATH-246 — local-origin audit and restoration of the r=10 mainline

Date: 2026-09-19

Status: CRITICAL SCOPE CORRECTION / MATH-235--245 CLOSURE UPGRADES WITHDRAWN / MAINLINE RESTORED TO MATH-225/229/231

## 1. Origin audit

MATH-057 defines a u=0 boundary anchor as an orbit endpoint

Y=T^k(N),

where N is the original first-cell ordinary start.

MATH-058 then enumerates paid-exit boundary-anchor sources

Y=R+2^L t,

and MATH-061 explicitly calls the canonical macro source Y, not the original first-cell source N.

MATH-206 imports exactly these local boundary-to-boundary factors:

Y=A+2^H s -> Y'=B+3^Q s.

Therefore the MATH-206 A,B,H,Q coordinates are local macro-origin coordinates unless an explicit MATH-188 rebasing to the original ordinary source has been carried out.

## 2. Why local self-descent is not global closure

For an imported local factor, the identity

J_local=2^H(Y'-Y)

is exact.

But J_local<0, equivalently Y'<Y, does not imply Y'<N.

A later orbit anchor may satisfy Y>N, and a decrease below Y can still remain above the original hypothetical minimal source N.

Thus minimal-counterexample closure cannot be inferred from local self-descent alone.

MATH-188 already states the governing rule: terminal/self-descent comparisons must use a common synchronized ordinary-source origin, or else local and global exponents/intercepts must remain distinct.

## 3. Scope corrections

The following numerical/algebraic observations remain exact as local diagnostics:

- MATH-235's split of frozen local factors by the sign of 2^H-3^Q;
- MATH-238's local affine-orientation coherence;
- MATH-239's universal theorem that for an arbitrary source Y>2^71, coefficient sign controls T^H(Y)-Y through depth 183;
- MATH-237's phase-product bound inside its explicitly defined post-J diagnostic subset.

The following proof-facing upgrades are WITHDRAWN:

- MATH-235: local J<0 implies r=10 branch CLOSED;
- MATH-236: treating the MATH-235 local-J survivor subset as the global r=10 mainline;
- MATH-243: treating the first later local coefficient contraction as the original source's first coefficient failure;
- MATH-244: closed-or-synchronized-singleton within 38 bits based on MATH-243;
- MATH-240/241/245: any PASS based on pruning a local coefficient contraction as if it closed the original first-cell candidate.

The MATH-241/245 workflows are therefore diagnostic/support experiments only until rebased to a true MATH-188 synchronized original-source state.

## 4. Valid r=10 restoration point

### MATH-225

Every frozen r=10 output cylinder has local source-resolution R<=40.

MATH-197 gives nonnegative resolution-adjusted Bellman increment while M>=2. Hence any future Bellman deficit is delayed to singletonization/overshoot.

### MATH-229

Arbitrary SAFE-prefix cylinder/phase/address composition is exact, provided the Bellman scalar is inherited from a synchronized global origin and the global 89-step allowance is not restarted locally.

### MATH-231

The r=10 layer is correctly treated as a relative-debt problem:

D0=lambda H-P_10.

Later relative reduced-cost increments may repay this debt without any local minimality assumption.

### Direct-floor closures

MATH-201/221/224/226 remain usable where they close an exact ordinary endpoint by reaching the frozen floor or by a separately synchronized argument. Their individual premises must remain unchanged.

## 5. Correct remaining target

initial local r=10 debt -> SAFE* -> first unpaid dangerous singleton handoff.

At the first dangerous handoff, the MATH-192/193/202 selector fixes at most one local source parameter per exact phase/address word.

The remaining task is to attach enough synchronized original-source information to that selected local singleton to decide one of:

- debt repaid;
- endpoint reaches <=2^71;
- globally synchronized terminal defect J_sync<0;
- valid Hensel equal-endpoint domination.

## 6. Claim boundary

This note is a scope repair, not a new closure.

r=10 remains OPEN.
First-cell emptiness remains OPEN.
The Collatz conjecture remains OPEN.
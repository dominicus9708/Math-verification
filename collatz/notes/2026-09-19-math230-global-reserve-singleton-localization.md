# MATH-230 — global Bellman reserve cannot fail before ordinary-source singletonization

Date: 2026-09-19

Status: EXACT GLOBAL LOCALIZATION / ANY RESERVE-THREATENING LOW-PAID EDGE IS ALREADY SINGLETON / r=10 OPEN

## 1. Global adjusted reserve

Let lambda=19/503.

At any coefficient-valid composed state measured from the current first-cell boundary source, let

H = accumulated shortcut depth,
R = ceil(log2 M) for the surviving ordinary-source family,
P = accumulated correction penalty.

Define

boxed: V = P - lambda(H-89) - lambda R.

Every penalty atom is nonnegative, so universally

boxed: V >= lambda(89-H-R).

This bound requires no assumption that earlier macro edges were individually Bellman-safe.

## 2. One potentially negative low-paid edge

Suppose the next completed paid first-return factor emits r in {2,...,10}.

Let its zero-cost prefix have length L and let

z = L-R

be the overshoot beyond unresolved source resolution.

MATH-202 gives

Delta V >= underline_epsilon_r - lambda z.

Let

z_min(r) = ceil(underline_epsilon_r/lambda).

Since

underline_epsilon_r/lambda > z_min(r)-1,

we have the strict lower bound

boxed: Delta V > lambda(z_min(r)-1-z).

## 3. Reserve exhaustion forces at least 89+z_min(r) source bits

Assume this edge could make the global adjusted reserve nonpositive:

V_after <= 0.

Using the two lower bounds above, this is possible only if

0 > lambda(89-H-R) + lambda(z_min(r)-1-z).

All quantities inside the parentheses are integers except for the strict inequality already absorbed above. Therefore

boxed: z >= 89-H-R+z_min(r).

The zero-cost prefix ends at accumulated source-address depth

H+L = H+R+z.

Hence

boxed: H+L >= 89+z_min(r).

For every r=2..10, z_min(r)>=1. Therefore

boxed: H+L >= 90.

## 4. 73-bit ordinary-source ceiling

MATH-057 proves every relevant first-cell boundary source anchor is strictly below 2^73.

A parity/source cylinder of depth at least 73 fixes at most one such ordinary integer.

Since every reserve-threatening edge requires at least 90 accumulated source bits before its paid cluster even begins,

boxed: global Bellman reserve cannot become nonpositive while the ordinary-source family is multi-source.

Any genuine global Bellman obstruction is already an exact singleton ordinary source.

## 5. r=10 specialization

For r=10, z_min(10)=13.

Thus any r=10 edge capable of exhausting the global MATH-060 reserve must satisfy

boxed: H+L >= 102.

This is 29 bits beyond the 73-bit source-saturation threshold.

So the symbolic AP/multiplicity channel is provably irrelevant to the final r=10 Bellman obstruction.

## 6. Relation to MATH-227 and MATH-229

MATH-227 showed that every frozen r=10 output enters its continuation with at least 16 lambda of conservative reserve.

MATH-229 showed how arbitrary safe prefixes compose exactly.

MATH-230 is stronger in one respect: even without assuming every earlier edge is individually safe, nonnegative accumulated penalty plus the resolution potential imply that a global reserve failure cannot occur until after exact source saturation.

Therefore the multi-source part of the safe-prefix transducer needs only preserve exact state until singletonization; it cannot itself be the final obstruction.

## 7. New mainline target

The r=10 proof obligation is now purely singleton:

1. start from an exact ordinary boundary source;
2. propagate the deterministic common recurrence;
3. retain exact global reserve and terminal defect J;
4. use MATH-220/221/224/226 address gates where applicable;
5. prove that no singleton path reaches the first universal crossing with negative reserve and J>=0.

## Claim boundary

Established:
- exact global adjusted reserve lower bound;
- any reserve-threatening r=2..10 edge requires accumulated source depth >=89+z_min(r);
- every global low-paid Bellman obstruction is already an ordinary-source singleton;
- r=10 reserve threat requires at least 102 accumulated source bits.

Not established:
- closure of every exact singleton tail;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.
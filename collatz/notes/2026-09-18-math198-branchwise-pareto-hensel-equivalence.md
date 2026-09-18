# MATH-198 — branchwise Pareto monotonicity and Hensel-extremal equivalence

Date: 2026-09-18

Status: `EXACT STRUCTURAL LEMMA / PARETO-TRANSFER COMPATIBILITY / HENSEL-EXTREMAL IDENTIFICATION / FIRST-CELL OPEN`

## 1. Purpose

MATH-197 localizes every possible coefficient-valid Bellman deficit to the singleton regime and introduces the terminal risk order

\[
N\text{ smaller},\qquad C\text{ larger}.
\]

This note proves that the order is preserved by every common parity branch and identifies positive one-sided Hensel credit with the same extremal direction inside an equal-endpoint fiber.

The result supplies the exact compatibility needed to combine the MATH-051 Hensel automaton with a Pareto-pruned singleton transfer.

No first-cell or Collatz closure is claimed.

## 2. Risk order at fixed outer state

Fix one outer state \((k,q)\). For singleton states define

\[
(N_1,C_1)\succeq_{\rm risk}(N_2,C_2)
\]

when

\[
\boxed{N_1\le N_2,\qquad C_1\ge C_2.}
\]

At a terminal crossing with

\[
\Delta_{k,q}=2^k-3^q>0,
\]

MATH-197 gives

\[
J_i=C_i-N_i\Delta_{k,q}.
\]

Hence

\[
(N_1,C_1)\succeq_{\rm risk}(N_2,C_2)
\Longrightarrow
\boxed{J_1\ge J_2}.
\]

Also, at fixed \(q\),

\[
\mathcal P_i=S_\partial(q)-\frac{C_i}{3^q},
\]

so

\[
\boxed{\mathcal P_1\le\mathcal P_2.}
\]

Thus the same order is adverse for both terminal descent and Bellman penalty accumulation.

## 3. Common-branch transition preserves the order

Suppose two states at the same \((k,q)\) take the same next shortcut parity bit

\[
b\in\{0,1\}.
\]

MATH-190 gives

\[
C'=3^bC+b2^k.
\]

The ordinary source \(N\) is unchanged by advancing the prefix.

Therefore

\[
N_1\le N_2
\Longrightarrow
N_1'\le N_2',
\]

and

\[
C_1\ge C_2
\Longrightarrow
3^bC_1+b2^k
\ge
3^bC_2+b2^k.
\]

Hence

\[
\boxed{
(N_1,C_1)\succeq_{\rm risk}(N_2,C_2)
\Longrightarrow
(N_1',C_1')\succeq_{\rm risk}(N_2',C_2')
}
\]

on every common parity branch.

The step penalty atom

\[
p_b=\frac b3(\Omega-\rho)
\]

depends only on the common outer coordinates and the common branch bit. Therefore the branch adds the same Bellman increment to both states, so their Bellman ordering cannot reverse either.

## 4. Required partition before Pareto pruning

The preceding theorem does **not** permit comparison of states that take different next parity bits.

Therefore a future-complete transfer must first partition states by enough exact address information to determine the legal branch.

This is precisely why MATH-095 rejected phase/resolution-only quotients and why MATH-096 retained finite dyadic address precision.

Pareto pruning is valid only inside a common exact branch / future-equivalence cell.

## 5. Equal-endpoint fibers are totally ordered in the risk direction

Take two fixed-\((k,q)\) states with the same endpoint \(Y\):

\[
2^kY=3^qN_1+C_1=3^qN_2+C_2.
\]

Then

\[
\boxed{
C_1-C_2=3^q(N_2-N_1).
}
\]

Therefore

\[
\boxed{
N_1<N_2
\iff
C_1>C_2.
}
\]

So every equal-endpoint fiber is totally ordered by the MATH-197 risk order.

The smallest ordinary start in the fiber has the largest correction and is simultaneously

- the most dangerous for terminal non-descent;
- the least favorable for accumulated penalty.

## 6. Positive Hensel credit is exactly the same order

MATH-189 identifies a positive one-sided Hensel credit \(t\) by

\[
C_*=C+t3^q,
\qquad t>0.
\]

The exact start translation is

\[
\boxed{N_*=N-t.}
\]

Thus

\[
N_*<N,
\qquad
C_*>C.
\]

Hence

\[
\boxed{
(N_*,C_*)\succ_{\rm risk}(N,C).
}
\]

So a positive Hensel competitor is not merely a different exclusion mechanism: it is exactly a more dangerous Pareto representative of the same equal-endpoint translation fiber.

This agrees with the earlier endpoint/Hensel ordering-redundancy result and gives it a direct Bellman/terminal interpretation.

## 7. Consequence for MATH-051 integration

MATH-051 asks whether a candidate parity word is dominated by a positive-credit competitor in its exact fixed-\(d\) Hensel class.

MATH-198 shows that whenever such a competitor exists, it lies in the same adverse Pareto direction.

Therefore the combined executor may safely organize its logic as

1. exact future/address partition;
2. exact Hensel viability / domination;
3. within each surviving common-branch cell, retain only undominated risk representatives;
4. use MATH-197 integer defect \(J\) at terminal crossings.

No unique-sink or local-gradient hypothesis is used.

## 8. Branchwise transfer theorem

Let \(\mathcal F\) be any exact state cell whose members share

- the same \((k,q)\);
- the same legal next parity bit;
- the same proof-legality predicates required for the transition.

Let \(\operatorname{Max}_{\rm risk}(\mathcal F)\) denote its undominated subset under

\[
N\text{ smaller},\quad C\text{ larger}.
\]

Then after the common parity transition,

\[
\boxed{
T_b(\operatorname{Max}_{\rm risk}(\mathcal F))
}
\]

contains every possible risk-maximal child; a dominated parent cannot become an undominated child on that same branch.

Thus Pareto pruning commutes with the exact common-branch transition.

## 9. Relation to the 338 MATH-179 outer states

MATH-179 records 338 coefficient-valid \((k,q)\) outer states for global depths

\[
2\le k\le41.
\]

The present theorem says that an implementation need not preserve every ordinary singleton representative inside each outer state.

It may instead preserve, separately for each exact future/address/Hensel branch cell, only the undominated \((N,C)\) frontier.

The remaining implementation question is quantitative:

> how large can this exact frontier become over the 338 audited outer states once MATH-051 viability and MATH-096 address precision are imposed?

That is now an engineering/combinatorial measurement problem rather than an unresolved semantic compatibility problem.

## 10. Claim boundary

Established:

- exact branchwise invariance of the MATH-197 risk order;
- exact Bellman-order invariance on a common parity branch;
- total risk ordering of equal-endpoint fibers;
- positive Hensel credit equals movement toward the Pareto-risk extremum;
- exact compatibility of Hensel pruning and Pareto pruning;
- Pareto pruning commutes with a common exact branch transition.

Not established:

- a uniform bound on the size of the future-complete Pareto frontier;
- closure of all MATH-193 singleton danger states;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

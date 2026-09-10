# MATH-052 — universal q-d credit transducer and relation to the final proof target

Date: 2026-09-10

Status: `EXACT REPARAMETRIZATION / MATH-051 REGRESSION PASS / ARBITRARY-d FINITE CLOSURE OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-051 remains the latest completed full finite depth (`k=41`).
- MATH-052 does **not** advance the depth frontier. It changes the representation of the Hensel calculation so that the former fixed-d solvers become slices of one universal recurrence.

## 1. Why this checkpoint exists

MATH-051 replaced a huge parity-word enumeration by exact fixed-d finite-state propagation. The next DSD question is whether the remaining dependence on d is genuine mathematical information or only a representation artifact.

The answer is partly positive: the fixed-d deadline arrays and the old block-sum carry are removable. The exact Hensel-dominance calculation can be written as one recurrence in `(q,d)` with a universal coefficient staircase and a universal credit transition.

What remains open is whether the normalized state space admits a **uniform finite quotient independent of d**.

## 2. Universal coefficient deadline

Let a length-k parity word have d even steps and q=k-d odd steps. Number the even positions

\[
e_0<e_1<\cdots<e_{d-1}
\]

and define cumulative odd-gap coordinates

\[
G_j=e_j-j.
\]

At the prefix ending at the j-th even step, the number of odd steps is exactly `G_j` and the prefix length is `G_j+j+1`. Therefore coefficient admissibility at that prefix is

\[
3^{G_j}>2^{G_j+j+1}.
\]

Equivalently,

\[
\left(\frac32\right)^{G_j}>2^{j+1}.
\]

Since no positive powers of 3 and 2 are equal, `log_{3/2}2` is irrational. Hence the least allowed gap is exactly

\[
\boxed{
\ell_j=\left\lceil (j+1)\log_{3/2}2\right\rceil.
}
\]

Thus the full all-prefix coefficient condition is

\[
\boxed{G_j\ge\ell_j\quad(0\le j<d).}
\]

The sequence `ell_j` is universal; a fixed d calculation merely takes its first d entries.

## 3. Exact inverse capacity / mechanical boundary

Define

\[
\gamma:=\log_2\frac32\approx0.5849625007211562.
\]

At reverse gap level r, the maximum number of candidate even ranks that can still remain is

\[
\boxed{
m(r)=\left\lfloor\gamma r\right\rfloor.
}
\]

Indeed `a` remaining ranks can fit at gap at most r exactly when

\[
3^r>2^{r+a},
\]

which is equivalent to `a<gamma r`; `gamma r` is nonintegral for positive integer r.

Consequently

\[
\ell_{a-1}\le r
\iff
\boxed{a\le m(r)}.
\]

The boundary increment

\[
\boxed{
\varepsilon_r=m(r)-m(r-1)\in\{0,1\}
}
\]

is the lower mechanical/Beatty (Sturmian) word of slope `gamma`. This terminology is standard; no novelty claim is attached to the existence of mechanical/Sturmian coding itself.

### DSD consequence

The old `L[j]` array is not a separate d-dependent object. Coefficient admissibility in the reverse gap computation needs only the single universal staircase `m(r)`.

## 4. Remove the block-sum carry

In MATH-051 let

- `a` = remaining candidate even ranks,
- `b` = remaining arbitrary-competitor even ranks,
- `h` = old high-gap carry.

If the current gap level consumes blocks leaving `a'` and `b'`, the old block contributions are

\[
A=2^a-2^{a'},\qquad B=2^b-2^{b'}
\]

and

\[
h'=\frac{2(h+B-A)}3.
\]

Define the exact credit coordinate

\[
\boxed{\chi=h+2^b-2^a.}
\]

Then

\[
\begin{aligned}
\chi'
&=h'+2^{b'}-2^{a'}\\
&=\boxed{\frac{2\chi+2^{b'}-2^{a'}}3}.
\end{aligned}
\]

Thus the old `blocksum` terms disappear completely.

Initial state:

\[
\boxed{(a,b,\chi)=(d,d,0).}
\]

At remaining depth zero, coefficient validity forces `a=0` and the exact Hensel translation credit is simply

\[
\boxed{\chi.}
\]

A terminal competitor dominates exactly when

\[
\boxed{\chi>0.}
\]

## 5. Universal viability recurrence

Let

\[
V(r,a,b,\chi)
\]

mean that there exists at least one completion through the remaining r gap levels whose candidate stays coefficient-valid, whose competitor is an arbitrary same-d word, whose exact carry divisibilities all hold, and whose final translation credit is positive.

Then for `r>0`, provided `a<=m(r)`,

\[
\boxed{
V(r,a,b,\chi)
=
\bigvee_{
\substack{
0\le a'\le\min(a,m(r-1))\\
0\le b'\le b
}
}
\left[
3\mid(2\chi+2^{b'}-2^{a'})
\;\wedge\;
V\!\left(r-1,a',b',
\frac{2\chi+2^{b'}-2^{a'}}3
\right)
\right].
}
\]

Base condition:

\[
\boxed{
V(0,a,b,\chi)\iff (a=0\ \wedge\ \chi>0).
}
\]

This recurrence contains **no original fixed-d parameter**.

The pair `(q,d)` enters only through

- starting level `r=q`,
- initial state `(a,b,chi)=(d,d,0)`.

Therefore the MATH-051 fixed-d solvers are finite slices of one universal `(q,d)` transducer.

## 6. Regression against MATH-051

Certificate:

`collatz/src/2026_09_10_universal_qd_credit_transducer_certificate.cpp`

Regression ledger:

`collatz/results/2026-09-10-universal-qd-credit-transducer-regression.tsv`

The universal recurrence reproduced the MATH-051 terminal-dominated counts exactly:

| q | d | D(q,d) |
|---:|---:|---:|
| 30 | 10 | 54,028,926 |
| 29 | 11 | 124,678,824 |
| 29 | 12 | 361,499,293 |
| 28 | 13 | 586,723,760 |
| 27 | 14 | 703,863,494 |
| 26 | 15 | 355,002,462 |

No mismatch occurred.

This is a regression of the representation change against finite exact MATH-051. It is not evidence that arbitrary d has already been finitely closed.

## 7. Exact rank-shift conjugacy and 2-adic factor

The chi transition has an exact simultaneous-rank shift symmetry. For any `s>=0`,

\[
(a,b,\chi,a',b')
\mapsto
(a+s,b+s,2^s\chi,a'+s,b'+s)
\]

commutes with the transition because

\[
\frac{2(2^s\chi)+2^{b'+s}-2^{a'+s}}3
=2^s\frac{2\chi+2^{b'}-2^{a'}}3.
\]

Starting from `chi=0`, every reachable state therefore satisfies the exact divisibility invariant

\[
\boxed{2^{\min(a,b)}\mid\chi.}
\]

Define

\[
v=b-a,
\qquad
c=\frac{\chi}{2^{\min(a,b)}}\in\mathbb Z.
\]

This removes the common absolute rank scale from the arithmetic state.

The identity is regression-checked in

`collatz/src/2026_09_10_rank_normalized_bulk_recurrence_certificate.py`.

## 8. Boundary slack and normalized local recurrence

Let

\[
u=m(r)-a\ge0,
\qquad
p(v)=\min(0,v),
\]

and define

\[
\Delta(v)=2^{\max(v,0)}-2^{\max(-v,0)}.
\]

The initial normalized state is

\[
\boxed{
(u,v,c)=\bigl(m(q)-d,0,0\bigr).
}
\]

Thus d first appears only as the distance from the fixed-q coefficient boundary.

Suppose the candidate consumes

\[
t=a-a'
\]

ranks at the current gap level and the new excess is

\[
v'=b'-a'.
\]

Since

\[
u'=m(r-1)-a',
\]

we have

\[
\boxed{t=u'-u+\varepsilon_r.}
\]

The normalized credit update is

\[
\boxed{
c'
=
\frac{
2^{1+t+p(v)-p(v')}c+\Delta(v')
}{3}.
}
\]

Equivalently, substituting the slack update,

\[
\boxed{
c'
=
\frac{
2^{1+u'-u+\varepsilon_r+p(v)-p(v')}c+\Delta(v')
}{3}.
}
\]

The finite-r geometric bounds are

\[
0\le u'\le m(r-1),
\]

\[
u'\ge u-\varepsilon_r,
\]

and

\[
\boxed{
u'-m(r-1)\le v'\le v+u'-u+\varepsilon_r.}
\]

The arithmetic update itself depends only on

\[
(u,v,c),\quad(u',v'),\quad\varepsilon_r,
\]

not on the absolute ranks a,b or on d.

### Interpretation

Away from the finite rank-zero boundary, the local arithmetic core is driven only by the two symbols

\[
\varepsilon_r=0\quad\text{or}\quad1.
\]

This suggests a two-operator Sturmian-driven transducer as the next exact target. It does **not** yet prove that the reachable normalized state set is finite.

## 9. Exact carry-residue dominance quotient

At r remaining levels, replace chi by

\[
\chi+m3^r.
\]

For any fixed future sequence of candidate/competitor rank choices, every divisibility condition is unchanged, and after r steps the final credit is shifted by

\[
\boxed{m2^r.}
\]

Therefore, for fixed `(r,a,b)` and one residue class `chi mod 3^r`, a larger chi dominates a smaller chi for all identical future choices.

This gives an exact frontier quotient: lower chi values in the same `(b, chi mod 3^r)` class need not be retained when a larger representative is present.

A stronger cross-b Pareto quotient is also safe when the larger representative has both `b` and `chi` no smaller and the same `chi mod 3^r`, because the larger b state can imitate every future competitor rank choice available to the smaller one.

These quotients are correctness-preserving. In the depth-41 regression range they do not, by themselves, collapse the whole normalized state set to a d-independent finite set.

## 10. Correction to the earlier generating-function target

A previous planning note suggested that a fixed finite matrix M might immediately yield a rational generating function. MATH-052 refines that target.

The exact coefficient boundary is driven by the nonperiodic mechanical sequence

\[
\varepsilon_r
=
\lfloor\gamma r\rfloor-
\lfloor\gamma(r-1)\rfloor.
\]

Therefore one must **not** assume a single constant transition matrix or a rational generating function before proving an additional finite phase quotient.

The more natural intermediate target is a two-operator cocycle

\[
\boxed{
M_{\varepsilon_q}M_{\varepsilon_{q-1}}\cdots M_{\varepsilon_1},
}
\]

provided the normalized state space can be proved to admit a uniform finite quotient.

If such a quotient does not exist, the alternative target is a well-founded/ranking argument on the normalized state space.

## 11. Counting is no longer the final objective

MATH-051 computed

\[
D(q,d)=\#\{\text{coefficient-valid candidates terminally dominated in their exact Hensel class}\}.
\]

That was necessary to validate the quotient against the enumerated finite data. But a universal Collatz argument ultimately needs an **emptiness / path-existence statement**, not only counts.

For a candidate prefix, let `F` be its exact frontier of still-possible dominating competitors. Candidate choice determines the next candidate rank count; competitor responses generate the next frontier.

This defines a safety game:

- candidate chooses a coefficient-valid continuation;
- the frontier propagates every exact arbitrary-word Hensel competitor;
- a terminal state is Hensel-safe when no competitor has positive translation credit.

A finite-horizon survival predicate may be written schematically as

\[
W(r,a,F)
=
\bigvee_{a'}
W\bigl(r-1,a',\Phi_{r,a'}(F)\bigr),
\]

with terminal safety meaning no positive-credit competitor remains.

For an infinite proof architecture the object of interest becomes a greatest fixed point / infinite safe-path set rather than the numerical count D.

### Audit warning

Root-Hensel maximality alone is not expected to make this safe set empty. For example, trivial/high-q branches can remain Hensel-maximal. The final proof state must preserve the other obligations of the proof architecture.

## 12. Relation to the current full-proof target

The current proof-architecture authority requires a **same-integer** intersection, not an independent multiplication of filters.

For the first universal cell the unresolved target includes:

1. the surviving ordinary dyadic root address;
2. all-prefix coefficient survival;
3. nested root-Hensel maximality;
4. extension to the first-crossing cell;
5. terminal correction/end-point sufficiency.

Therefore the eventual bad-path state must be a lineage-preserving product, schematically

\[
\boxed{
\mathcal S_{\rm bad}
=
\mathcal S_{\rm Hensel}
\times
\mathcal S_{\rm dyadic\ address}
\times
\mathcal S_{\rm crossing}
\times
\mathcal S_{\rm endpoint/correction},
}
\]

with only mathematically justified quotients applied.

The final type of theorem sought is not

\[
\frac{\#\text{survivors}}{\#\text{candidates}}\to0,
\]

but rather

\[
\boxed{\text{no infinite / terminally valid bad path exists}.}
\]

On a genuine uniform finite quotient this could be expressed by emptiness of the greatest safe fixed point or, in a stronger acyclic case, nilpotence of the bad-state transition graph. Without a finite quotient, a well-founded ranking function is the alternative.

Eliminating the first Farey cell would still not by itself eliminate all later strip cells; a uniform strip-coverage bridge remains a separate global obligation.

## 13. DSD analysis verdict

The calculation compression chain is now

\[
\boxed{
\text{parity words}
\to
(e_j)
\to
(G_j)
\to
\Sigma_d
\to
h
\to
\chi
\to
(u,v,c;\varepsilon_r).
}
\]

The first five arrows have already removed enormous finite enumeration. MATH-052 shows that the apparent family of d-specific solvers also collapses to one universal arithmetic recurrence.

The remaining unresolved information is concentrated in:

- unbounded normalized-state coordinates as d grows;
- the nonperiodic mechanical boundary drive `epsilon_r`;
- the same-integer dyadic/crossing/endpoint lineage that Hensel compression intentionally does not contain.

These are the next DSD targets. More finite-depth counting is now secondary to proving a complete quotient or a well-founded path obstruction.

## 14. Audit boundaries

Do not promote any of the following:

- universal recurrence `=>` uniform finite automaton;
- finite MATH-051 regression `=>` arbitrary-d closure;
- Sturmian two-symbol drive `=>` periodic matrix power;
- Hensel-safe-path elimination in one component `=>` same-integer proof;
- first-cell closure `=>` all later Farey cells;
- density/count decay `=>` emptiness;
- Git provenance `=>` mathematical novelty priority.

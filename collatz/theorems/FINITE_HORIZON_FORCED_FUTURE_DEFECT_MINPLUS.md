# Finite-horizon source-sensitive forced-future-defect min-plus recursion

Status: **EXACT finite-horizon theorem / execution result not universal**

## Purpose

At an active S10 source cylinder, the current exact defect numerator

\[
N_q=C_T(q)-C_W(q)
\]

contains every target displacement already realized in the prefix.

To strengthen the physical gate without double counting, one needs a defect contribution that is forced by the unresolved future.

This note defines the exact finite-horizon quantity

\[
\boxed{F_r^{min}}
\]

that measures the minimum **new** correction defect accumulated over `r` future one-events among all nonempty source-preserving pure-ballot descendants.

Branches that violate pure ballot before the requested horizon are treated as already closed, not as zero-defect survivors.

---

## 1. One-step future atom

Let a current state have depth `h`, odd count `q`, and exact defect `N`.

A legal next valuation jump `0^a1` realizes the next one-event at

\[
u=h+a.
\]

Let its target position be

\[
t_q.
\]

Pure ballot gives

\[
u\le t_q.
\]

The child defect is

\[
N'=3N+2^{t_q}-2^u.
\]

Define the new one-step atom

\[
\boxed{
\Delta(s\to s'):=N'-3N=2^{t_q}-2^u\ge0.
}
\]

This atom contains no already-realized prefix defect.

It is zero exactly when the next one-event occurs at its target position.

---

## 2. Path transport

Consider a legal path of `r` future one-events

\[
s_0\to s_1\to\cdots\to s_r.
\]

Let

\[
\Delta_k:=\Delta(s_k\to s_{k+1}).
\]

Repeated use of

\[
N_{k+1}=3N_k+\Delta_k
\]

gives

\[
\boxed{
N(s_r)=3^rN(s_0)+F_r(s_0\rightsquigarrow s_r),
}
\]

where

\[
\boxed{
F_r
=\sum_{k=0}^{r-1}3^{r-1-k}\Delta_k.
}
\]

Equivalently,

\[
F_0=0,
\qquad
F_{k+1}=3F_k+\Delta_k.
\]

Thus `F_r` is the exact future defect transported to the `q+r` odd-count normalization.

---

## 3. Exact source-sensitive minimum

For a source state `s`, let

\[
\mathcal D_r(s)
\]

be the set of nonempty exact source-preserving descendants reachable after exactly `r` legal valuation jumps while satisfying pure ballot throughout.

If

\[
\mathcal D_r(s)\ne\varnothing,
\]

define

\[
\boxed{
F_r^{min}(s)
:=
\min_{d\in\mathcal D_r(s)}
\left(N(d)-3^rN(s)\right).
}
\]

Because each source transition is an exact residue-class intersection, this minimum ranges over actual nonempty source subcylinders, not abstract control words.

Therefore

\[
\boxed{
F_r^{min}(s)>0
}
\]

means:

> every source member that remains pure-ballot for `r` more one-events must accumulate at least that much genuinely new defect by that horizon.

If instead

\[
\mathcal D_r(s)=\varnothing,
\]

then every member of the parent source cylinder violates pure ballot before `r` future one-events.  This is a stronger outcome: finite-horizon ballot closure.  It must be recorded separately rather than encoded as `F_r^{min}=+\infty` or `0` in proof-facing state.

---

## 4. Min-plus recursion

For `r>=1`, let `Ch(s)` be the nonempty legal exact valuation children of `s`.

For a child `c`, define

\[
\Delta(s,c)=N(c)-3N(s).
\]

A child contributes to an `r`-step survivor only when

\[
\mathcal D_{r-1}(c)\ne\varnothing.
\]

For every contributing child,

\[
N(d)-3^rN(s)
=
3^{r-1}\Delta(s,c)
+
\left(N(d)-3^{r-1}N(c)\right).
\]

Hence

\[
\boxed{
F_r^{min}(s)
=
\min_{\substack{c\in Ch(s)\\\mathcal D_{r-1}(c)\ne\varnothing}}
\left(
3^{r-1}\Delta(s,c)+F_{r-1}^{min}(c)
\right).
}
\]

Base case:

\[
F_0^{min}(s)=0.
\]

This is an exact min-plus Bellman recursion on the source-preserving valuation tree.

No merging of distinct source payloads is required for correctness.

---

## 5. Zero-floor criterion

Because all future atoms are nonnegative,

\[
F_r^{min}(s)=0
\]

if and only if at least one nonempty legal `r`-jump descendant path has

\[
\Delta_0=\cdots=\Delta_{r-1}=0.
\]

Equivalently, along at least one surviving source subcylinder, every one-event for the next `r` ranks lands exactly at its target position.

Thus a positive floor has a particularly strong interpretation:

\[
\boxed{
F_r^{min}(s)>0
\iff
\text{no exact source descendant can follow the target one-positions for all next }r\text{ ranks.}
}
\]

This is source-sensitive: the abstract ballot-control language may admit the zero-displacement path while the parent source residue interval fails to intersect its required dyadic parameter class.

---

## 6. Direct dyadic test for the zero path

For fixed horizon `r`, the all-zero-defect continuation prescribes the exact future one-positions

\[
t_q,t_{q+1},\ldots,t_{q+r-1}.
\]

Equivalently, it prescribes a finite parity block from the current depth to the final target position.

By the certified multibit/source transducer, that block has one exact parameter residue class modulo a power of two.

Therefore `F_r^{min}>0` can sometimes be certified without expanding every positive-defect child: it is enough to prove that the live parent parameter interval has empty intersection with the exact all-zero-displacement residue class, while at least one legal `r`-jump descendant remains.

This gives a high-value shortcut:

\[
\boxed{
\text{exclude the unique zero-defect future cylinder first.}
}
\]

If it is absent, positivity follows; the full min-plus recursion is then needed only to compute the numerical floor.

---

## 7. Composition with the existing physical score

At horizon `r`, every surviving descendant `d` satisfies

\[
N(d)\ge3^rN(s)+F_r^{min}(s).
\]

However a physical whole-parent rejection must also handle the source `X` lower endpoint and any other descendant-dependent terms at the same horizon.

A safe route is either:

1. enumerate exact horizon-`r` descendants and verify the physical rejection predicate on every survivor, with early ballot-dead branches already closed; or
2. derive a parent-level lower bound for every other positive coefficient in the physical score and combine it with the transported defect floor.

One must not insert `F_r^{min}` directly into the current-depth `N` normalization.

---

## 8. Exactness versus finite execution

The recursion and transport identity are algebraic and exact for every state in their domain.

A computation to a chosen horizon `r` on the current 14,224 jump-8 cylinders is finite evidence only.  It may prove closure for any specific cylinder whose complete finite descendant partition is exhausted, but it does not establish a horizon-independent global theorem.

---

## 9. DSD classification

### EXACT / CLOSED

- one-step future atom;
- path transport;
- source-sensitive descendant definition;
- min-plus recursion;
- separate treatment of early ballot death;
- zero-floor equivalence;
- all-zero-defect residue exclusion as a positivity certificate.

### SAFE finite use

For a fixed source cylinder and fixed horizon, exhaustive exact source-child recursion can certify `F_r^{min}`, ballot closure, or physical closure of that finite partition.

### OPEN

- whether a small fixed horizon yields positive floors for a useful fraction of the 14,224 current cylinders;
- whether those floors produce any whole-parent physical closures;
- whether a horizon-independent analytic lower bound exists;
- whether a finite right-congruence can compress the min-plus state without losing source-sensitive predicates.

## Next certificate

`../src/A0_s1_8jump_forced_future_defect_minplus_certificate.py` should evaluate small horizons from the exact jump-8 states and report separately:

- parents with no surviving depth-`r` descendant;
- parents with `F_r^{min}=0`;
- parents with `F_r^{min}>0`;
- whole-parent closure when every exact surviving descendant is physically rejected.

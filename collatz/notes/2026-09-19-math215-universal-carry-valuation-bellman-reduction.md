# MATH-215 — universal carry-valuation Bellman reduction for every emitted paid count

Date: 2026-09-19

Status: EXACT VARIABLE-r POTENTIAL REDUCTION / OVERSHOOT DEPTH ELIMINATED / GLOBAL CLOSURE OPEN

## 1. Purpose

MATH-186/202 localize every potentially nonpositive multi-paid transfer to a singleton overshoot.

For an emitted paid count \(r\), write its exact phase-dependent local surplus as

\[
\epsilon_r(x)=\mathcal P_r(x)-\lambda h_r(x),
\qquad
\lambda=\frac{19}{503}.
\]

The singleton transfer bound is

\[
\boxed{\Delta\mathcal B\ge\epsilon_r(x)-\lambda z},
\]

where \(z>0\) is the overshoot length after source resolution has been exhausted.

This note adds one universal carry potential and removes \(z\) from the theorem-facing transition law for every paid count \(r\). No assumption of consecutive equal-\(r\) clusters is made.

## 2. Nonzero carry

Let
\[
d\ne0,\qquad c=B-A_{\rm next},
\]
so
\[
\boxed{d'=\frac{3^Qd+c}{2^z}}.
\]

Assume \(d'\ne0\), and put
\[
v=\nu_2(d),\qquad v'=\nu_2(d').
\]

Define
\[
\boxed{\gamma=\nu_2(3^Qd+c)-\nu_2(d)}.
\]

MATH-213 gives
\[
\boxed{z=v-v'+\gamma}.
\]

## 3. Universal carry potential

Define
\[
\boxed{\Psi(d)=-\lambda\nu_2(d)\qquad(d\ne0)}.
\]

Then
\[
\Delta\Psi=\lambda(v-v').
\]

Therefore
\[
\begin{aligned}
\Delta\mathcal B+\Delta\Psi
&\ge\epsilon_r(x)-\lambda z+\lambda(v-v')\\
&=\boxed{\epsilon_r(x)-\lambda\gamma}.
\end{aligned}
\]

The raw overshoot depth and the stored carry valuation have disappeared. Only newly regenerated cancellation bits remain.

## 4. Paid-count threshold becomes a regeneration threshold

MATH-202 proves
\[
\epsilon_r(x)\ge\underline\epsilon_r>0
\]
and
\[
\boxed{z_{\min}(r)=\left\lceil\frac{\underline\epsilon_r}{\lambda}\right\rceil}.
\]

Hence
\[
\gamma<z_{\min}(r)
\Longrightarrow
\Delta\mathcal B+\Delta\Psi>0.
\]

Therefore every potentially nonpositive nonzero-carry transfer satisfies
\[
\boxed{\gamma\ge z_{\min}(r)}.
\]

The MATH-202 overshoot threshold has become an exact regeneration threshold, valid for arbitrary mixtures of paid counts.

## 5. Exact odd-part resonance

If \(c\ne0\), let \(s=\nu_2(c)\).

If
\[
s\ne\nu_2(d),
\]
then
\[
\nu_2(3^Qd+c)=\min(s,\nu_2(d))
\]
and therefore \(\gamma\le0\).

Thus danger requires
\[
\boxed{\nu_2(c)=\nu_2(d)=s}.
\]

Write
\[
d=2^su,\qquad c=2^sa,
\]
with \(u,a\) odd. Then
\[
\boxed{\gamma=\nu_2(3^Qu+a)}.
\]

Consequently
\[
\boxed{
\gamma\ge z_{\min}(r)
\iff
3^Qu+a\equiv0\pmod{2^{z_{\min}(r)}}.
}
\]

Equivalently,
\[
\boxed{
u\equiv-a3^{-Q}\pmod{2^{z_{\min}(r)}}.
}
\]

Thus an unbounded integer carry reduces to one finite odd-part residue.

## 6. Zero incoming carry

Set
\[
\boxed{\Psi(0)=0}.
\]

If \(d=0\) and \(c\ne0\), let \(s=\nu_2(c)\). Compatibility gives
\[
d'=\frac{c}{2^z},\qquad \nu_2(d')=s-z.
\]

Hence
\[
\boxed{
\Delta\mathcal B+\Delta\Psi
\ge
\epsilon_r(x)-\lambda s.
}
\]

Therefore danger requires
\[
\boxed{\nu_2(c)\ge z_{\min}(r)}.
\]

Again the explicit overshoot depth disappears.

## 7. Exact reset branch

If
\[
d=0,\qquad c=0,
\]
then \(d'=0\).

No finite carry valuation pays for the overshoot, so this exact-reset branch remains separate.

MATH-206 proves that the frozen initial \(r=10\) full-factor catalogue has no zero-carry compatible next factor and therefore no reset there. A universal regenerated reset theorem remains a separate obligation.

## 8. Threshold table

For \(2\le r\le21\),
\[
z_{\min}(r)
=
(1,2,3,6,7,8,10,11,13,14,16,18,19,21,22,25,25,26,28,29).
\]

MATH-215 reinterprets the same table as the minimum number of newly generated cancellation bits needed after stored carry valuation is paid by \(\Psi\).

For the current frontier,
\[
\boxed{r=10\text{ potential danger}\Longrightarrow\gamma\ge13}.
\]

Thus the whole \(r=10\) layer, even with arbitrary intervening paid counts, reduces on the nonzero-carry branch to a 13-bit regeneration resonance.

## 9. Relation to MATH-214

MATH-214 was later scope-corrected: its four-phase calculation is a synthetic direct-paid-cluster experiment and is not used on the proof-facing full-boundary chain.

The universal proof-facing threshold remains 13 bits for \(r=10\).

## 10. DSD consequence

The paid/address state now factors into:

1. emitted paid count \(r\);
2. common phase state;
3. Hensel/Pareto extremality;
4. exact-reset flag;
5. finite regeneration residue.

The raw overshoot depth and unbounded carry magnitude are no longer theorem-state axes.

## 11. Claim boundary

Established:
- one carry potential valid for arbitrary mixtures of emitted paid counts;
- exact elimination of overshoot depth from nonzero-carry Bellman accounting;
- exact regeneration threshold \(\gamma\ge z_{\min}(r)\);
- exact finite odd-part congruence for every dangerous nonzero carry;
- zero-to-nonzero branch reduced to \(\nu_2(c)\ge z_{\min}(r)\).

Not established:
- emptiness of the reachable regeneration quotient;
- universal exact-reset exclusion;
- closure of \(r=10\);
- closure of the first universal Farey cell;
- the Collatz conjecture.

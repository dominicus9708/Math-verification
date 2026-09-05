# Neutral Beatty tail: single-class Hensel recurrence and Sturmian critical audit

Date: 2026-09-06

## Status

- **SAFE LEMMA:** exact single-class full-Hensel count/max recurrence.
- **FINITE CERTIFICATE:** the canonical neutral tail audited here has a singleton full-Hensel class through depth 95.
- **SAFE IDENTIFICATION:** after a finite initial prefix, the neutral tail is an upper mechanical/Sturmian word of slope `alpha=log_3 2`.
- **LITERATURE BARRIER / OPEN GATE:** proving that this critical Sturmian parity tail cannot be the parity vector of a rational 2-adic integer sits at the known critical boundary of the 3x+1 periodicity/conjugacy problem.

No Collatz proof is claimed.

---

## 1. Neutral Beatty tail

Put

\[
b(k)=\min\{q:3^q\ge2^k\}=\lceil k\log_3 2\rceil,
\qquad
\delta_k=b(k+1)-b(k).
\]

Take the parity word whose first six symbols are `1` and whose later symbols are

\[
e_k=\delta_k\qquad(k\ge6).
\]

Since `b(6)=4`, its odd count at every depth `k>=6` is exactly

\[
q_k=6+b(k)-b(6)=b(k)+2.
\]

Therefore its Beatty surplus is permanently

\[
\boxed{d_k=q_k-b(k)=2.}
\]

This is the neutral boundary-following language isolated in the preceding Gate-B audit.

---

## 2. Full-Hensel correction class

For a length-`k` parity word with `q` odd symbols write

\[
T^k(N)=\frac{3^qN+R}{2^k}.
\]

The full-Hensel class used by the root-minimality theorem is

\[
(q,R\bmod3^q).
\]

For a state `(k,q,r)` define

\[
C_k(q,r)
=
\#\{w:|w|=k,\ |w|_1=q,\ R(w)\equiv r\pmod{3^q}\},
\]

and

\[
M_k(q,r)
=
\max\{R(w):|w|=k,\ |w|_1=q,\ R(w)\equiv r\pmod{3^q}\}.
\]

Invalid states have count zero and no maximum.

---

## 3. Exact single-class recurrence

If the last parity symbol is zero, then

\[
R'=R,
\qquad q'=q.
\]

If it is one at position `k-1`, then

\[
R'=3R+2^{k-1},
\qquad q'=q+1.
\]

Hence for the one-child inverse branch we require

\[
r\equiv2^{k-1}\pmod3,
\]

and its unique parent Hensel residue is

\[
r_-=rac{r-2^{k-1}}3\pmod{3^{q-1}}.
\]

Therefore

\[
\boxed{
M_k(q,r)=
\max\left\{
M_{k-1}(q,r),
\ 3M_{k-1}(q-1,r_-)+2^{k-1}
\right\},
}
\]

with nonexistent branches omitted.

The class counts satisfy

\[
\boxed{
C_k(q,r)=
C_{k-1}(q,r)
+
C_{k-1}(q-1,r_-)
}
\]

under the same branch condition.

This is an exact parameter-universal algebraic recurrence.  It evaluates only the Hensel classes actually required by a target word and therefore avoids constructing the complete class table.

Status: **SAFE LEMMA**.

---

## 4. A forced-zero simplification along the neutral tail

Suppose the target's last bit at depth `k` is zero.

The Beatty word has no consecutive plateaus, so the preceding target bit is one.  Thus the target correction modulo 3 is

\[
R\equiv2^{k-2}\pmod3.
\]

A competitor ending in one would instead require

\[
R\equiv2^{k-1}\pmod3.
\]

But consecutive powers of two have opposite nonzero residues modulo 3.  Hence these congruences are incompatible.

Therefore at every neutral-tail plateau,

\[
\boxed{
\text{every word in the same full-Hensel class is forced to end in }0.
}
\]

All new Hensel branching occurs only at Beatty rises.

Status: **SAFE LEMMA**.

This explains why the target-specific recursion is much smaller than the complete root-Hensel table.

---

## 5. Exact singleton audit

The accompanying exact integer certificate evaluates the target class recursively and independently brute-checks the recurrence at small depths.

For every audited depth

\[
1\le k\le95,
\]

it finds

\[
\boxed{
C_k(q_k,R_k\bmod3^{q_k})=1.
}
\]

Consequently the target is trivially the correction maximum of its class:

\[
\boxed{
M_k(q_k,R_k\bmod3^{q_k})=R_k
\qquad(k\le95).
}
\]

In particular this strengthens the earlier depth-22 observation.  Through depth 95 the root-Hensel filter does not merely fail to find a larger-correction competitor; there is no second parity word in the target's full-Hensel class at all.

Status: **FINITE CERTIFICATE ONLY**.

It is not legitimate to extrapolate class uniqueness to all depths from this computation.

Reproducer:

`collatz/src/neutral_tail_single_class_hensel_audit.py`

The conservative default is depth 75.  The recorded depth-95 audit is reproduced with

```text
python neutral_tail_single_class_hensel_audit.py --max-k 95
```

The depth-95 memo table is substantially larger than the default run.

---

## 6. Mechanical/Sturmian identification

Let

\[
\alpha=\log_3 2.
\]

Then

\[
\delta_k
=
\lceil\alpha(k+1)\rceil-
\lceil\alpha k\rceil.
\]

Because `alpha` is irrational, this is an upper mechanical word and hence a Sturmian word.  Changing the first finitely many symbols does not change its asymptotic slope.

Thus the neutral tail has exact limiting odd density

\[
\boxed{
\lim_{k\to\infty}\frac{q_k}{k}=\alpha=\frac{\log2}{\log3}.
}
\]

This is precisely the coefficient-neutral density.

Status: **SAFE IDENTIFICATION**.

---

## 7. External literature audit: this is a known critical boundary

López and Stoll studied the 3x+1 conjugacy map over Sturmian/mechanical words directly:

- J. López and P. Stoll, *The 3x + 1 Conjugacy Map over a Sturmian Word*, Integers 9 (2009), 141--162, DOI `10.1515/INTEG.2009.014`.

Their framework associates every parity word `v in Z_2` with the unique 2-adic starting value `Phi(v)`.  The paper treats irrational mechanical words but does not establish a general theorem that their 3x+1 conjugacy images cannot be rational/eventually periodic.

A later López--Stoll preprint,

- J. López and P. Stoll, *The 3x+1 Periodicity Conjeture in R*, arXiv:2101.12747 (2021),

proves aperiodicity of the conjugacy image under the strict density condition

\[
\liminf_{k\to\infty}\frac{q_k}{k}
>
\frac{\log2}{\log3}.
\]

It also identifies equality with the critical density as the only possible asymptotic density for a rational 2-adic integer with a non-cyclic trajectory.

Our neutral tail has exactly

\[
\lim q_k/k=\log_3 2,
\]

so it lies on the equality boundary rather than inside the strict theorem's domain.

Therefore the proposed terminal shortcut

> prove directly that the neutral Sturmian parity word cannot come from an ordinary positive integer

must not be treated as an easy consequence of known Sturmian conjugacy theory.  In its unrestricted form it overlaps the known critical periodicity boundary of the 3x+1 problem.

Status: **LITERATURE BARRIER / OPEN GATE**.

---

## 8. DSD consequence

The current terminal decomposition should therefore remain

\[
\boxed{
\text{contracting bulk}
+
\text{controlled high-surplus tail}
+
\text{critical neutral Sturmian exceptional channel}.
}
\]

The third channel cannot presently be removed by any of the following alone:

1. fixed-Q7 reverse potential -- blocked by the exact boundary-following Q7 barrier;
2. root-Hensel maximality -- target class is singleton through depth 95;
3. the known strict-density Sturmian conjugacy theorem -- the neutral word sits at equality.

A genuinely new terminal theorem therefore has to use additional arithmetic information not present in the bare critical parity word, for example the same-integer ternary selector / recursively sufficient `F_m` structure, canonical finite-support lift constraints, or a cross-base correlation with those channels.

This prevents the proof program from silently replacing Collatz by a known equivalent/near-equivalent critical periodicity problem.

---

## 9. Revised next target

The highest-value next question is no longer whether the critical Sturmian word itself is impossible in `Z_2`.

It is the narrower same-integer question:

\[
\boxed{
\text{critical neutral Sturmian parity tail}
+
\text{actual }F_m\text{ ternary-selector membership}
+
\text{canonical finite-support lift}
\Longrightarrow ?
}
\]

Any contradiction obtained from this conjunction would be stronger than the bare Sturmian periodicity problem and would use information specific to the current DSD/Ansari core architecture.

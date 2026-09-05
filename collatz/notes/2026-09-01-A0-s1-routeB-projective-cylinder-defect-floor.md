# A0 s=1 Route-B — projective carry cylinder to normalized-defect floor

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Purpose

The current audited proof interface is

\[
\text{projective adic constraints}
\to
\text{forced displacement/slack cylinders}
\to
\underline\eta
\to
\text{physical }X\text{ pruning}.
\]

The previous work closed the first local ingredient: at remaining ternary
precision \(m\), a legal one-step carry transition is a bijection between one
parity class of exponent residues modulo

\[
\lambda_m=\operatorname{ord}_{3^m}(2)=2\cdot3^{m-1}
\]

and the successor carry residues modulo \(3^{m-1}\).

This note closes the next interface.  Once a successor projective carry is
fixed, the candidate one-position lies in one arithmetic cylinder.  Intersecting
that cylinder with the exact order/dominance interval gives either an empty
family or an exact minimum normalized correction defect.

This is a membership-relevant lower-bound theorem.  It is **not** a rule that
an adic target mismatch is automatically a membership rejection.

---

## 2. One-step projective cylinder

Fix

\[
m\ge1,
\qquad M=3^m,
\qquad \lambda_m=2\cdot3^{m-1}.
\]

Let

- \(z\in\mathbf Z/M\mathbf Z\) be the incoming carry;
- \(a\) be the target ranked-one position;
- \(b\) be the candidate ranked-one position.

The next ternary digit passes when

\[
z+2^a-2^b\equiv0\pmod3,
\]

and the outgoing projective carry is

\[
z'\equiv\frac{z+2^a-2^b}{3}\pmod{3^{m-1}}.
\]

If

\[
z+2^a\equiv0\pmod3,
\]

then there is no legal \(b\), because \(2^b\) is a unit modulo 3.

Otherwise the existing carry-bijection theorem gives, for every prescribed
successor residue \(z'\), exactly one

\[
\boxed{\beta\pmod{\lambda_m}}
\]

such that

\[
\boxed{b\equiv\beta\pmod{\lambda_m}}.
\]

Thus a successor carry state is exactly an exponent cylinder, not merely a
loose parity restriction.

---

## 3. Exact interval intersection

Suppose formation/order information gives

\[
\ell\le b\le u,
\qquad b\le a.
\]

Put

\[
U=\min(u,a).
\]

The admissible set is

\[
\mathcal B
=
[\ell,U]\cap(\beta+\lambda_m\mathbf Z).
\]

If \(\mathcal B=\varnothing\), the entire projective cylinder is impossible.

Otherwise its largest member is

\[
\boxed{
b_{\max}
=
U-((U-\beta)\bmod\lambda_m).
}
\]

provided this value is at least \(\ell\).

Every other legal member is

\[
b_{\max}-k\lambda_m,
\qquad k\ge0,
\]

while it remains in the interval.

Equivalently the displacement

\[
\delta=a-b
\]

lies in one residue class modulo \(\lambda_m\), and

\[
\boxed{\delta_{\min}=a-b_{\max}.}
\]

This is the exact smallest displacement allowed by the projective carry state
and the formation interval together.

---

## 4. Exact normalized-defect floor

At global ranked-one index \(r\), the dominance defect atom is

\[
D_r(a,b)
=
\frac{2^a-2^b}{3^r}.
\]

For fixed \(a,r\), this is strictly decreasing in \(b\).  Therefore, whenever
\(\mathcal B\ne\varnothing\),

\[
\boxed{
\min_{b\in\mathcal B}D_r(a,b)
=
\frac{2^a-2^{b_{\max}}}{3^r}.
}
\]

Equivalently, with \(w_r=2^a/3^r\),

\[
\boxed{
D_{r,\min}
=w_r\left(1-2^{-\delta_{\min}}\right).
}
\]

The bound is attained, so it is an exact cylinder minimum rather than a coarse
inequality.

Two cases must remain distinct.

### Zero-defect cylinder

If

\[
b_{\max}=a,
\]

then the current projective state permits the target position itself and this
rank alone forces no positive defect.

### Positive-defect cylinder

If

\[
b_{\max}<a,
\]

then

\[
\delta_{\min}\ge1
\]

and the cylinder forces a strict positive defect.

For a strict-high characteristic target, the already proved weight inequality

\[
\frac16\le w_r<\frac12
\]

immediately gives

\[
\boxed{D_{r,\min}\ge\frac1{12}}
\]

whenever the projective cylinder excludes \(b=a\).

If an additional gate forces \(\delta_{\min}\ge2\), the same calculation gives

\[
D_{r,\min}\ge\frac18,
\]

recovering the earlier first-nontrivial-ternary-collider gap as a special case.

---

## 5. Composition with the global defect

For the target-dominance language,

\[
\eta
=
\sum_r D_r(a_r,b_r),
\]

and every atom is nonnegative.

Hence any projective cylinder floor is irreversible:

\[
\boxed{\eta\ge D_{r,\min}.}
\]

If a disjoint prefix has already certified a defect floor \(\eta_0\), then

\[
\boxed{\eta\ge\eta_0+D_{r,\min}.}
\]

At a block product

\[
T=UV,
\qquad W=U'V',
\]

the same statement can be transported through the exact semiring law

\[
\eta(T,W)
=
\eta(U,U')+
\frac{2^{|U|}}{3^{q(U)}}\eta(V,V').
\]

Thus a local cylinder floor inside \(V\) contributes globally with the positive
multiplier

\[
\mu(U)=\frac{2^{|U|}}{3^{q(U)}}.
\]

This is the correct bridge from projective state compression to the physical
real-envelope pruning oracle.

---

## 6. Why this does not repeat the rejected collision argument

The theorem does **not** use

\[
C(W)\not\equiv C_{th}\pmod{2^K}
\Rightarrow
\text{reject}.
\]

Instead it uses a projective state only to identify which ordinary positions
are possible.  Those positions imply an ordinary positive correction loss, and
that loss is converted to the already defined monotone functional \(\eta\).

Therefore the logical chain is

\[
\boxed{
\text{adic state}
\to
\text{position cylinder}
\to
\text{ordinary defect atom}
\to
\underline\eta
}
\]

before any physical rejection is attempted.

This preserves the target-collision vs membership distinction from the latest
scope audit.

---

## 7. Regression certificate

Source:

`collatz/src/A0_s1_routeB_projective_cylinder_defect_floor_certificate.py`

An independent local execution of the same arithmetic recurrence during this
analysis checked:

- interval/cylinder comparisons: `1,853,392`;
- empty-gate states: `688`;
- successor-bijection residue states: `29,384`;
- displacement-minimum comparisons: `2,100`.

All checks agreed.

These finite checks are implementation regression only.  The theorem itself is
the algebraic order/congruence argument above.

---

## 8. DSD analysis

### Structure separation

The state now has three explicitly different roles.

1. **Observation state** — \((m,z,z')\) in the projective ternary channel.
2. **Formation state** — the legal position interval/order constraints.
3. **Membership functional** — the monotone normalized defect \(\eta\).

No one of these is silently substituted for another.

### Resolution dependence

The arithmetic-cylinder period is

\[
2\cdot3^{m-1}.
\]

This grows with requested precision, so this theorem does not establish a
horizon-independent finite quotient.

However the growing modulus now has a concrete semantic role: it increases the
spacing between allowed candidate positions, which can only increase a forced
displacement when the target position is excluded from the selected cylinder.

This converts a former state-growth obstruction into a potential defect-growth
resource, but no global growth theorem is inferred yet.

---

## 9. DSD audit

### EXACT / CLOSED

- a prescribed successor projective carry selects one exponent residue modulo
  \(2\cdot3^{m-1}\);
- intersecting it with an ordinary order interval gives an exact arithmetic
  cylinder or the empty set;
- the largest legal exponent is the exact minimum-displacement member;
- that member gives the exact minimum normalized defect atom;
- positive defect floors compose monotonically and through the existing
  normalized-defect semiring.

### REGRESSION ONLY

- the finite counts listed above check implementation conventions for
  \(m\le4\) and small position intervals.

### NOT INFERRED

- an arbitrary target-collision mismatch is not a membership rejection;
- every surviving 14-root family is not yet known to enter a positive-defect
  projective cylinder at a specified gate;
- the \(1/12\) or \(1/8\) local gap is not automatically additional to an
  already counted defect unless the supports/ranks are certified disjoint;
- no current physical shell is declared closed by this theorem alone;
- Route-B global membership and the Collatz conjecture remain open.

---

## 10. Updated bottleneck

The local interface

\[
\boxed{
\text{projective carry}
\to
\text{displacement cylinder}
\to
\eta\text{ floor}
}
\]

is now closed.

The next exact target is to feed the **actual 14-root source/channel families**
into this cylinder rule and determine, gate by gate, whether the physical
endpoint constraints force

1. an empty projective cylinder, or
2. a cylinder excluding the target position and therefore carrying a positive
   \(\eta\) floor.

Only after that floor is known should it be compared with the certified
real-envelope \(X\) bound for shell closure.

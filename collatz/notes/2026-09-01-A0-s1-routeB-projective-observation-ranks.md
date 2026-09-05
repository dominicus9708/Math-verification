# A0 s=1 Route-B projective observation ranks

## Purpose

Replace giant absolute observation moduli by recursively consumed precision
ranks on the already certified target-relative / H-L hierarchy.

This note does **not** claim a polynomial-time global decoder.  It closes only
the well-foundedness of hierarchical observation refinement.

---

## 1. Left dyadic precision rank

Inside either equal-count target-relative dominance factor, the existing exact
valuation theorem gives

\[
C(W)\equiv C(T)\pmod{2^K}
\iff
W_{[0,K)}=T_{[0,K)}.
\]

Suppose a certified target hierarchy split is

\[
T=A B,
\qquad |A|=a.
\]

For a dominance candidate `W`:

### Case D1: \(K\le a\)

Only the first `K` target bits matter, hence the task descends into the target
left block `A`.  The precision `K` is unchanged but the target horizon becomes
strictly smaller.

### Case D2: \(K>a\)

Passing the dyadic gate forces the whole first block to match:

\[
W_A=A.
\]

Because the prefix surplus is then exactly zero at the cut, the remaining
suffix is again a dominance problem relative to `B`, and the remaining
precision is

\[
\boxed{K'=K-a}.
\]

Thus the lexicographic rank

\[
\boxed{\mathcal R_2=(K,h)}
\]

strictly decreases on every recursive call: either `K` decreases or `K` stays
fixed and `h` decreases.

For the current characteristic target, the already certified H/L--Stern-Brocot
alignment supplies hierarchy cuts whose remainders remain characteristic, so
this recursion can use run/continued-fraction blocks rather than literal bits.

---

## 2. Right ternary precision rank

For a corresponding equal-count grammar split

\[
T=A B,
\qquad W=A' B',
\qquad q(B)=q(B')=q_B,
\]

let `z` be the carry imported from material already processed to the right and
set

\[
G_B(z)=\Delta_B+2^{|B|}z,
\qquad
\Delta_B=C(B)-C(B').
\]

The block carry theorem gives:

### Case T1: \(L\le q_B\)

The requested ternary precision is contained entirely in the right block.  The
task descends into `B`; `L` is unchanged and the word horizon decreases.

### Case T2: \(L>q_B\)

The right block must first pass

\[
3^{q_B}\mid G_B(z).
\]

Then

\[
z'=G_B(z)/3^{q_B}
\]

is passed to the left child only modulo

\[
3^{L-q_B},
\]

and the remaining precision is

\[
\boxed{L'=L-q_B}.
\]

If a degenerate child has `q_B=0`, precision does not decrease, but the child
horizon still does.

Hence the lexicographic rank

\[
\boxed{\mathcal R_3=(L,h)}
\]

strictly decreases on every recursive call.

---

## 3. Ternary local state is symbolic displacement, not raw carry

At each one-position suffix gate the incoming carry either rejects immediately
or fixes one candidate parity.  Writing

\[
b=a-\epsilon-2d,
\]

the outgoing carry map

\[
\Phi(d)=\frac{z+2^a-2^{a-\epsilon-2d}}3
\]

satisfies

\[
\boxed{
v_3(\Phi(d)-\Phi(e))=v_3(d-e).
}
\]

Thus the correct projective coordinate is a displacement cylinder

\[
d\pmod{3^r}
\]

plus its ordinary interval/order bounds, not an enumerated list of raw carries.

The root-scale first-step no-go certificate shows why this distinction is
necessary: at `L=28` the first right-factor gate already has 116,282,759
distinct raw carry residues.

---

## 4. Combined well-foundedness

The root critical product splits the current collision problem into two
independent tasks:

\[
\text{LEFT dyadic dominance/prefix task}
\times
\text{RIGHT ternary dominance/carry task}.
\]

Each side now has an explicit decreasing observation rank.  Therefore no branch
can refine observation precision forever merely because `K` or `L` is large.
Large absolute precisions are consumed by hierarchy block length / one-count.

This closes **observation-refinement termination**.

It does not close **state-width complexity**: on the ternary side, many symbolic
displacement cylinders may coexist because successive one-position ordering
constraints couple the free displacement variables.

---

## 5. DSD audit

✅ dyadic precision interpreted as a consumable prefix-equality rank;

✅ ternary precision interpreted as a consumable suffix-carry rank;

✅ every recursive observation call strictly decreases `(precision,horizon)`;

✅ raw-carry and symbolic-displacement state are kept distinct;

✅ no arbitrary candidate is assumed to share the target Christoffel hierarchy;

❌ no polynomial bound on the number of ternary displacement cylinders yet;

❌ no Route-B global closure or Collatz conclusion claimed.

## Next gate

The remaining family-level problem is now:

\[
\boxed{
\textbf{G4-PC: projective cylinder composition}
}
\]

Prove that the ordered displacement cylinders produced by successive ternary
suffix gates admit a recursively bounded representation (preferably through
H/L grammar or Ostrowski/continued-fraction coordinates) without enumerating
all admissible exponent positions.

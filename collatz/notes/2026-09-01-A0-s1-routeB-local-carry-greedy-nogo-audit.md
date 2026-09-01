# A0 s=1 Route-B — local carry greedy no-go audit

Date: 2026-09-01  
Branch: `collatz-stage4-window-threshold`

## 1. Rejected shortcut

A tempting shortcut after the projective-cylinder theorem is:

> while processing the ternary suffix from right to left, at each gate choose
> the largest currently legal candidate position \(b_r\).

This would minimize the current defect atom, but it is not globally valid
because the chosen \(b_r\) also changes the successor carry and therefore the
arithmetic cylinder seen by earlier ranks.

The rule is now explicitly **REJECTED**.

Source:

`collatz/src/A0_s1_routeB_local_carry_greedy_nogo_certificate.py`

---

## 2. Exact counterexample

Take target ranked-one positions

\[
a=(0,1,3,4,6)
\]

and require

\[
C(a)-C(b)
\equiv27\pmod{3^4}.
\]

The candidate

\[
\boxed{b=(0,1,2,3,4)}
\]

is ordered and target-dominant.

Its corrections are

\[
C(a)=319,
\qquad
C(b)=211,
\]

so

\[
C(a)-C(b)=108
\equiv27\pmod{81}.
\]

Its normalized defect is

\[
\boxed{
\eta=\frac{108}{3^5}=\frac49.
}
\]

Thus the prescribed ternary residue family is nonempty.

---

## 3. Failure of myopic largest-position selection

Initialize the target-relative carry by

\[
z_0=-27\pmod{81}=54.
\]

Choosing the largest position allowed at each successive gate produces the
right-to-left choices

\[
6,4,3,0.
\]

At that point the remaining earlier rank would need a position below zero, so
the local greedy route declares failure.

But the explicit feasible candidate above exists.

Therefore

\[
\boxed{
\text{locally largest }b_r
\not\Rightarrow
\text{globally minimum defect or even global feasibility}.
}
\]

---

## 4. Why the ordered-cylinder greedy theorem survives

There is no contradiction with the separately proved ordered-cylinder theorem.

That theorem assumes the full arithmetic cylinder at every rank has already
been fixed:

\[
b_r\equiv\beta_r\pmod{\lambda_r}.
\]

Once those cylinders are fixed, the right-to-left componentwise-largest vector
is indeed the exact minimum-defect vector.

The invalid rule instead tries to choose \(b_r\) **before** the future
successor-carry/cylinder sequence is fixed.

Thus the two operations are distinct:

1. choose/resolve a carry-state path;
2. minimize positions inside the resulting fixed cylinder path.

Only step 2 is greedy.

---

## 5. DSD audit

### EXACT

- the displayed candidate is a valid dominance candidate;
- its required ternary residue is exactly `27 mod 81`;
- the myopic largest-position path fails;
- therefore local carry-state choice cannot be greedily collapsed.

### PRESERVED

- fixed-cylinder ordered greedy minimum;
- one-step projective carry/exponent bijection;
- source and H/L min-plus Bellman quotients.

### REJECTED

- `largest current b` as a rule for choosing the successor carry state.

### OPEN

The successor-carry choices need a genuine DP, quotient, or family-level
isometry argument before the ordered-cylinder minimum can be applied.

# Whole-prefix maximal endpoint fibres are polynomial

Date: 2026-08-23

Status: **unconditional algebraic theorem about the whole-prefix maximum-correction language.**  Its use as a minimal-counterexample pruning rule at a horizon `H` additionally requires the corresponding root predecessor credit to be smaller than the hypothetical minimal root.  This note does not prove Collatz.

## 1. Setup

For a length-`H` parity word `w`, let

\[
q=q(w),\qquad R=R(w),
\]

so that

\[
T^H(N)=\frac{3^qN+R}{2^H}.
\]

For fixed `H,q` and a residue class `a mod 3^q`, call `w` **whole-prefix maximal** when

\[
R(w)=\max\{R(u): |u|=H,\ q(u)=q,\ R(u)\equiv a\pmod{3^q}\}.
\]

Let `r(w)` be the canonical start residue in `[0,2^H)` and

\[
y(w)=\frac{3^q r(w)+R(w)}{2^H}
\]

its canonical `H`-step endpoint.

## 2. Fixed-(endpoint,q) uniqueness theorem

Fix `H`, an endpoint `y`, and an odd count `q`.

Suppose two whole-prefix maximal words `u,w` satisfy

\[
y(u)=y(w)=y,\qquad q(u)=q(w)=q.
\]

Then

\[
3^q r(u)+R(u)=2^Hy=3^q r(w)+R(w),
\]

so

\[
R(u)-R(w)=3^q\bigl(r(w)-r(u)\bigr).
\]

Hence

\[
R(u)\equiv R(w)\pmod{3^q}.
\]

They therefore belong to the same complete Hensel correction class.  Since both are maximum-correction representatives of that class,

\[
R(u)=R(w).
\]

The endpoint identity then gives

\[
r(u)=r(w).
\]

The length-`H` parity-vector map is a bijection on residues modulo `2^H`, so the two words are identical.

Therefore

\[
\boxed{\text{for fixed }(H,y,q),\text{ at most one whole-prefix maximal word exists}.}
\]

This statement does not use coefficient survival, probability, selector mixing, or any local-block maximality argument.

## 3. Polynomial endpoint fibre under coefficient survival

Terminal coefficient survival requires

\[
3^q\ge2^H.
\]

Put

\[
q_{\min}(H):=\min\{q:3^q\ge2^H\}=\lceil H\log_3 2\rceil.
\]

Thus a coefficient-surviving whole-prefix maximum reaching a fixed endpoint can have only

\[
q\in\{q_{\min}(H),\ldots,H\}.
\]

By the fixed-`q` uniqueness theorem,

\[
\boxed{
\#\{\text{whole-prefix maximal coefficient survivors reaching }y\}
\le H-q_{\min}(H)+1.
}
\]

In particular,

\[
H-q_{\min}(H)+1
=(1-\log_3 2)H+O(1)=O(H).
\]

Hence the endpoint-fibre information cost is at most

\[
\boxed{
\log_2(H-q_{\min}(H)+1)=O(\log H)=o(H).
}
\]

So exact endpoint injectivity, although observed through the current finite range, is stronger than is needed to rule out an independent positive exponential endpoint-multiplicity channel.

## 4. Minimal-counterexample applicability and the root-credit condition

If a coefficient-surviving word `w` is not whole-prefix maximal and

\[
R_{\max}=R(w)+3^q d,
\qquad d>0,
\]

then the smaller root `N-d` reaches the same `H`-step endpoint.  To contradict minimality one needs

\[
0<d<N.
\]

Therefore define the finite root-credit diameter

\[
D_H:=\max_{w\text{ coefficient surviving, nonmaximal}}
\frac{R_{\max}(w)-R(w)}{3^{q(w)}}.
\]

Whenever a hypothetical minimal counterexample satisfies `N>D_H`, its length-`H` prefix belongs to the whole-prefix maximal language and the polynomial endpoint-fibre theorem applies to it.

The exact current calculations give

\[
\boxed{
D_{28}=29,\quad
D_{29}=47,\quad
D_{30}=59,\quad
D_{31}=71,\quad
D_{32}=71.
}
\]

At `H=32` the exact per-`q` values for `q=21,...,32` are

\[
\boxed{(71,47,15,7,7,3,1,1,1,1,0,0).}
\]

Thus for the current enormous `m=45` representative range, root positivity is not remotely close to being an obstruction through depth 32.

These finite values are evidence only for the growth of `D_H`; no all-`H` polynomial or subexponential bound is asserted here.

## 5. Stronger finite injectivity remains diagnostic

Exact targeted collision audits show the stronger property that no endpoint contains two whole-prefix maximal coefficient survivors through the tested range.

New extensions are:

- `H=30`: 12,771,274 coefficient survivors, 758,572 collision groups before maximality, and zero groups containing two maximal survivors;
- `H=31`: 23,642,078 coefficient survivors, 1,401,286 collision groups before maximality, and zero groups containing two maximal survivors.

Moreover, whenever a collision group contains one maximal survivor, that survivor is always the largest-`q` member in these exact audits.

This supports an eventual endpoint-injectivity theorem candidate, but the polynomial fibre theorem above already gives the asymptotically sufficient multiplicity conclusion without requiring that stronger statement.

## 6. New proof-program split

The unconditional endpoint branch is now separated into two questions.

1. **Multiplicity:** closed at exponential scale once whole-prefix maximality is legitimate, because every endpoint fibre is `O(H)`.
2. **Root-credit applicability:** prove a sufficiently weak growth theorem for `D_H`, ideally

\[
D_H=2^{o(H)}.
\]

Such a subexponential root-credit theorem would make whole-prefix maximality compatible with the exponentially large representative roots in the proof scaling regime, while contributing only `O(log H)` endpoint multiplicity.

The remaining genuinely cross-base problem would then be endpoint/selector transport itself, rather than an uncontrolled multiplicity of binary histories above one endpoint.

# Source terminal-descriptor endpoint lattice

Status: **EXACT / CLOSED source-first endpoint theorem**

## Scope

This theorem specializes the exact valuation/macroblock source transition to the
late `q=j_0-28` activation seam.

It shows that once one **validated exact terminal suffix descriptor** is supplied
to one exact source activation channel, the source integer and ordinary
checkpoint lie on one common one-parameter affine lattice.  Because the current
physical source corridor is vastly shorter than the lattice spacing, each such
terminal descriptor has at most one physical source realization.

This does **not** solve the hard problem of generating the admissible terminal
descriptor language compactly.

## 1. Late source activation channel

Let an exact source-preserving activation channel be

\[
X=r+2^h k,
\qquad
Y=T^h(X)=y+3^q k,
\qquad
k\in[k_{lo},k_{hi}],
\]

with

\[
q=j_0-28.
\]

Let a validated terminal parity suffix `B` satisfy

\[
|B|=n,
\qquad
q(B)=28,
\qquad
C_B=C(B),
\]

and terminate at the fixed checkpoint depth

\[
\boxed{h+n=t_0.}
\]

Its affine endpoint equation is

\[
2^n Z=3^{28}Y+C_B.
\]

Substituting the activation channel gives

\[
2^n Z
=3^{28}y+C_B+3^{q+28}k.
\]

Since

\[
q+28=j_0,
\]

we have

\[
\boxed{
2^n Z=3^{28}y+C_B+3^{j_0}k.
}
\]

## 2. Exact terminal-block source residue

Because `3^{j_0}` is odd, it is invertible modulo `2^n`.
Therefore the supplied suffix `B` is realized only on the unique source-parameter
residue

\[
\boxed{
\kappa_B
\equiv
-\left(3^{28}y+C_B\right)
\left(3^{j_0}\right)^{-1}
\pmod{2^n}.
}
\]

This is exactly the fixed-macroblock residue from
`VALUATION_MACROBLOCK_COMPILATION.md`, specialized to `d=28`.

Write every compatible parameter as

\[
\boxed{k=\kappa_B+2^n t},
\qquad t\in\mathbb Z.
\]

The actual allowed `t` interval is obtained exactly from the parent parameter
interval:

\[
\boxed{
\left\lceil\frac{k_{lo}-\kappa_B}{2^n}\right\rceil
\le t\le
\left\lfloor\frac{k_{hi}-\kappa_B}{2^n}\right\rfloor.
}
\]

## 3. Joint source/checkpoint endpoint lattice

Substitute the refined parameter into the source coordinate:

\[
\begin{aligned}
X
&=r+2^h(\kappa_B+2^nt)\\
&=(r+2^h\kappa_B)+2^{h+n}t.
\end{aligned}
\]

Using `h+n=t_0`, define

\[
R_B:=r+2^h\kappa_B.
\]

Then

\[
\boxed{X=R_B+2^{t_0}t.}
\]

Likewise the checkpoint equation becomes

\[
\begin{aligned}
Z
&=
\frac{3^{28}y+C_B+3^{j_0}\kappa_B}{2^n}
+3^{j_0}t.
\end{aligned}
\]

The first term is an integer by the definition of `\kappa_B`.  Define

\[
Z_B:=
\frac{3^{28}y+C_B+3^{j_0}\kappa_B}{2^n}.
\]

Therefore

\[
\boxed{Z=Z_B+3^{j_0}t.}
\]

Combining the two coordinates,

\[
\boxed{
(X,Z)
=
(R_B,Z_B)
+t\,(2^{t_0},3^{j_0}).
}
\]

This is the exact source/checkpoint endpoint lattice associated with one
activation channel and one validated terminal descriptor.

## 4. Current physical-source singleton consequence

The independently certified source corridor satisfies

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33}.
\]

Its upper endpoint is strictly below `2^72`, because

\[
\frac{\frac43 2^{71}+0.478\,2^{33}}{2^{72}}
=
\frac23+0.478\,2^{-39}<1.
\]

Hence the entire physical source set lies inside an interval of width less than

\[
2^{72}.
\]

But

\[
t_0=104{,}398{,}605{,}910>72,
\]

so

\[
2^{t_0}>2^{72}.
\]

Two different lattice parameters `t_1!=t_2` would give source integers separated
by at least `2^{t_0}`, which is larger than the complete physical source
corridor.

Therefore

\[
\boxed{
\text{for a fixed activation channel and validated }(n,C_B),
\text{ there is at most one physical source }X.
}
\]

When it exists, the same unique `t` immediately determines the ordinary
checkpoint

\[
\boxed{Z=Z_B+3^{j_0}t.}
\]

Thus a source-derived terminal descriptor exposes a **provenanced ordinary
checkpoint directly**; CRT is not required to manufacture that checkpoint.

## 5. Relation to the existing checkpoint interfaces

This theorem supplies a source-first route:

```text
exact activation channel
    -> validated terminal descriptor (n,C_B)
    -> unique dyadic refinement k = kappa_B + 2^n t
    -> at most one physical source X
    -> directly determined checkpoint Z
    -> derive z_H, z_2 and the actual post-checkpoint parity prefix from Z
    -> test any remaining right-H / post-checkpoint formation predicates.
```

The existing synchronized CRT theorem remains correct and useful when the
checkpoint is approached from separately supplied synchronized boundary
observations.

The existing source-activation/checkpoint provenance join also remains correct
and useful for a checkpoint `Z` generated from another interface.

The present theorem shows that **when the terminal suffix itself is generated
with source provenance**, neither of those interfaces is needed to create
source provenance after the fact: it is already built into the refined endpoint
lattice.

## 6. DSD state consequence

Once `(activation channel, n, C_B)` is fixed and validated:

- `\kappa_B` is derived;
- the child source lattice is derived;
- the child checkpoint lattice is derived;
- the physical source corridor leaves at most one lattice point;
- if that point exists, `X` and `Z` are derived;
- `F_28` is derived from `(n,C_B)` and the fixed target;
- `z_H` is derived from `F_28` (equivalently from `Z`);
- `z_2=Z mod 2^27` is derived;
- the actual 27-bit post-checkpoint prefix is deterministic from `Z`.

Therefore the principal unsolved object is narrowed again to the compact,
source-preserving generation and validation of terminal descriptors rather than
the later arithmetic exposure of their endpoints.

## 7. DSD audit

### EXACT / CLOSED

- unique `k mod 2^n` terminal-block realization residue;
- exact compatible `t` interval;
- joint endpoint lattice
  \[
  (X,Z)=(R_B,Z_B)+t(2^{t_0},3^{j_0});
  \]
- current physical source corridor width `<2^72<2^{t_0}`;
- at most one physical source/checkpoint pair per fixed activation channel and
  validated terminal descriptor.

### SAFE / inherited

- the numerical physical source corridor is inherited from the independently
  certified pre-defect corridor chain;
- `(n,C_B)` may stand for the raw terminal word only after fixed-`(n,28)`
  correction-language validity/injectivity is discharged.

### REJECTED

- treating a terminal descriptor that is not source-refined as already
  provenanced;
- using integrality of an arbitrary correction integer not known to belong to
  the valid 28-one correction language;
- claiming that one descriptor covers multiple source histories after the
  physical singleton step;
- treating CRT compatibility or right-H residue agreement as a substitute for
  terminal-word/source realization.

### OPEN / principal

- compact generation of all admissible `(n,C_B)` descriptors from the current
  14,224 source cylinders without raw middle-word expansion;
- efficient intersection of that descriptor language with right-H
  formation/boundary predicates;
- post-checkpoint membership checks on the directly exposed `Z`;
- `A0,s=1,Route-B` and global Collatz closure.

## Certificate

- `../src/A0_s1_source_terminal_descriptor_endpoint_lattice_certificate.py`

# Gate C: terminal barrier and valid closure criteria

Date: 2026-09-06

Status: **SAFE LOGICAL BARRIER + TERMINAL TARGET REFINEMENT.**

This note audits the last step of the current Collatz proof program after the new Beatty one-child / selector-repair route.

The central conclusion is negative but important:

\[
\boxed{
\text{polynomial normalized candidate-mass decay alone cannot exclude one integer path.}
}
\]

Therefore Gate C must contain an additional arithmetic/canonical-tail theorem.  It is not merely a formal consequence of Gate S.

---

## 1. Canonical integer condition

The established canonical formation condition is

\[
\boxed{
N\in\mathbb N_{>0}
\iff
(t_q)\text{ has finite support}.
}
\]

Hence a fixed positive integer has some support endpoint `q_0` such that

\[
\boxed{
t_q=0\qquad(q\ge q_0).
}
\]

A hypothetical minimal Collatz counterexample must therefore determine an infinite surviving candidate path whose canonical lift is eventually zero.

Status: **SAFE LEMMA already present in the terminal roadmap.**

---

## 2. Why `mu_L -> 0` is insufficient

Let `S_L` be the finite family of surviving depth-`L` candidate cylinders and let `w_L(C)>0` be the normalized weight of cylinder `C`.

Then

\[
\mu_L
=
\sum_{C\in S_L}w_L(C).
\]

Suppose one exceptional nested path

\[
C_1\supset C_2\supset\cdots
\]

survives for all `L`.

There is no contradiction with

\[
\mu_L\to0,
\]

because its own cylinder weight may also satisfy

\[
w_L(C_L)\to0.
\]

For example, under a dyadic-type normalization a single depth-`L` cylinder can have weight of order

\[
2^{-L},
\]

while the total candidate mass may decay only polynomially:

\[
\mu_L\asymp L^{-\gamma}.
\]

Then

\[
2^{-L}\ll L^{-\gamma},
\]

so the total mass bound is compatible with many surviving cylinders, and certainly with one.

Status: **SAFE LOGICAL BARRIER.**

---

## 3. General mass-to-emptiness transfer lemma

Let `I_L subset S_L` be the cylinders that can still represent the finite prefix of an eventually-zero canonical lift.

Define

\[
w_L^{\rm int}
:=
\inf_{C\in I_L}w_L(C)
\]

when `I_L` is nonempty.

If `I_L` contains at least one survivor, then trivially

\[
\mu_L\ge w_L^{\rm int}.
\]

Therefore

\[
\boxed{
\mu_L<w_L^{\rm int}
\quad\Longrightarrow\quad
I_L=\varnothing.
}
\]

More generally, if

\[
\boxed{
\frac{\mu_L}{w_L^{\rm int}}\to0,
}
\]

then eventually no integer-compatible cylinder can remain.

Status: **SAFE LEMMA.**

This gives a valid measure-to-emptiness route, but it requires a sufficiently strong lower bound on the weight of every integer-compatible survivor.

---

## 4. Why the current polynomial decay does not close this lemma

The Beatty one-child harmonic route presently gives, conditionally,

\[
\mu_L\le C L^{-\gamma}
\]

for some `gamma>0` once Gates F and S are closed.

If the best available lower bound on a single compatible cylinder is exponential,

\[
w_L^{\rm int}\ge cB^{-L},
\qquad B>1,
\]

then

\[
\frac{\mu_L}{w_L^{\rm int}}
\le
\frac Cc B^L L^{-\gamma},
\]

which does **not** tend to zero.

Thus the current polynomial contraction cannot be promoted to emptiness by a naive atom-weight comparison.

Even geometric mass decay would need its rate compared quantitatively with the compatible-cylinder weight scale.

Status: **SAFE BARRIER.**

---

## 5. Gate C must therefore split

The terminal gate should now be decomposed as

\[
\boxed{
C_{\rm form}
+ C_{\rm tail}
+ C_{\rm hit}
}
\]

or replaced by an absolute-counting theorem.

### `C_form` — canonical integer characterization

\[
N\in\mathbb N_{>0}
\iff
(t_q)\text{ has finite support}.
\]

Status: **CLOSED / SAFE.**

### `C_tail` — zero-tail state law

After a support endpoint `q_0`, derive the exact state evolution forced by

\[
t_q=0
\quad(q\ge q_0)
\]

in the same variables used by the Beatty/selector proof: coefficient-surplus, selector residue, parent fibre, and any minimal-counterexample state required by the root-global filter.

The important point is that this must be a **pathwise** law, not an average-measure statement.

Status: **OPEN.**

### `C_hit` — deterministic forbidden-hit theorem

Prove that every infinite zero-tail state trajectory allowed by `C_tail` must eventually enter a configuration eliminated by an exact canonical/minimal-counterexample rule.

A target form is

\[
\boxed{
\forall s_0\in\mathcal S_{\rm integer},
\quad
\exists r<\infty:
T_0^r(s_0)\in\mathcal K,
}
\]

where

- `T_0` is the exact eventually-zero tail transition;
- `S_integer` is the set of states that can occur at a support endpoint of a positive integer candidate;
- `K` is an exactly forbidden/killed state set.

Status: **OPEN.**

If proved, this directly excludes a fixed positive integer counterexample and avoids any density-zero/emptiness inference.

---

## 6. Alternative Gate-C route: absolute integer-compatible count

Instead of a deterministic tail-hit theorem, one could prove an absolute counting estimate.

Let

\[
M_L
:=
\#\{\text{surviving depth-}L\text{ cylinders compatible with an eventually-zero integer tail}\}.
\]

If an exact argument yields

\[
\boxed{
M_L<1
}
\]

for some sufficiently large `L`, then necessarily

\[
M_L=0.
\]

This is a valid terminal closure because `M_L` is an integer.

A mass estimate can imply this only if it is converted into an **absolute** count with enough strength, for example

\[
M_L
\le
\frac{\mu_L}{w_L^{\rm int}}
<1.
\]

The current polynomial mass decay does not provide such a bound under exponentially small cylinder weights.

Status: **VALID ALTERNATIVE TARGET / OPEN.**

---

## 7. Interaction with the new Gate-S block theorem

The new Gate-S target

\[
\sum_{L\text{ rise}}
\frac{(3\rho_L-1)_+}{L}
=\infty
\]

is sufficient to prove

\[
\mu_L\to0
\]

once Gate F is closed.

It is **not** sufficient to prove `C_hit`.

Therefore the current dependency chain must be written as

\[
\boxed{
F_{\rm map}+F_{\rm unif}
\longrightarrow
\text{Gate S harmonic contraction}
\longrightarrow
\mu_L\to0
}
\]

and separately

\[
\boxed{
C_{\rm form}
\longrightarrow
C_{\rm tail}
\longrightarrow
C_{\rm hit}.
}
\]

A final proof requires the two chains to meet through a genuine pathwise or absolute-counting bridge.

This prevents the phrase “candidate mass tends to zero” from hiding the terminal logical gap.

---

## 8. Minimal-counterexample information

The minimal-counterexample assumption remains potentially useful because it can create exact forbidden states: any canonical/reverse configuration that certifies descent below the hypothetical minimal counterexample is incompatible with that counterexample.

However, a positive *density* of such forbidden states among all residues is not enough.

Gate C needs one of the following stronger statements:

1. every eventually-zero tail is **forced** to hit such a state;
2. the set of zero-tail states avoiding it is exactly empty;
3. the number/weight of avoiding zero-tail states has an absolute bound strong enough to be `<1`.

Status: **OPEN ARITHMETIC FORCING PROBLEM.**

---

## 9. DSD audit

### SAFE

1. A positive integer gives an eventually-zero canonical lift.
2. Normalized mass tending to zero does not imply emptiness.
3. The ratio criterion `mu_L/w_L^int -> 0` is a valid sufficient transfer.
4. Polynomial mass decay cannot beat an exponential single-cylinder scale.
5. A deterministic zero-tail forbidden-hit theorem would close the singleton-path problem without a measure argument.

### OPEN

- exact zero-tail transition in the final proof state variables;
- deterministic forbidden-hit theorem;
- or a strong absolute integer-compatible count theorem.

### PROHIBITED UPGRADES

1. Never write `mu_L -> 0 => no counterexample` without an additional transfer theorem.
2. Never use normalized survivor percentages as an absolute survivor count.
3. Never assume eventual-zero digits force bounded surplus; the repository already contains a negative finite control against that shortcut.
4. Never replace pathwise minimality by generic residue-density elimination.

---

## 10. Next terminal calculation

The next Gate-C calculation should explicitly construct the state transition induced by

\[
t_q=0\quad\text{for all future }q
\]

and ask a deterministic question:

\[
\boxed{
\text{Can an eventually-zero canonical tail remain forever inside the exact survivor automaton?}
}
\]

If the answer can be reduced to a finite or monotone state problem, Gate C may become independently tractable.

If not, then the proof architecture must seek a quantitative lower bound `w_L^int` or an absolute-counting mechanism strong enough to connect Gate-S mass decay to integer nonexistence.

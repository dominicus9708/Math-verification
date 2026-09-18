# MATH-210 — equal-endpoint extremal reduction of Hensel, Pareto risk, and terminal defect

Date: 2026-09-19

Status: `EXACT STATE REDUCTION / TERMINAL CHANNEL MERGE / r=10 OPEN`

## 1. Purpose

MATH-189 identifies positive Hensel credit with an ordinary-start translation.
MATH-197 defines the terminal defect
[
J=C-N(2^k-3^q).
]
MATH-198 shows that positive Hensel credit moves in the adverse Pareto direction.

The three descriptions can be collapsed exactly.

## 2. Equal-endpoint translation

Fix one outer state ((k,q)) and endpoint (Y):
[
2^kY=3^qN+C.
]

A positive Hensel translation of credit (t>0) is
[
oxed{
N_t=N-t,qquad C_t=C+t3^q.
}
]

Then
[
3^qN_t+C_t=3^qN+C,
]
so the endpoint is unchanged.

## 3. Exact defect translation

Put
[
Delta=2^k-3^q.
]

Then
[
egin{aligned}
J_t
&=C_t-N_tDelta\
&=C+t3^q-(N-t)(2^k-3^q)\
&=J+t2^k.
end{aligned}
]

Hence
[
oxed{
J_t=J+t2^k.
}
]

Therefore positive Hensel translation strictly increases terminal defect.

At the same time
[
N_t<N,qquad C_t>C.
]

Thus the following directions are identical inside an equal-endpoint fiber:

[
oxed{
	ext{positive Hensel credit}
=
	ext{smaller source}
=
	ext{larger correction}
=
	ext{larger terminal defect}.
}
]

## 4. Consequence for terminal state representation

A proof-facing terminal cell that already preserves exact future/address legality does not need three independent order coordinates:

- Hensel-credit order;
- Pareto ((N,C)) order;
- defect (J) order.

They are one ordered fiber.

Within one equal-endpoint / future-equivalent fiber, retain only the Hensel/Pareto extremal representative required by the proof orientation.

All other representatives have defect obtained by an exact multiple of (2^k).

## 5. Congruence invariant

The defect translation also gives
[
oxed{
J_tequiv Jpmod{2^k}.
}
]

Since
[
J=2^k(Y-N),
]
indeed every equal-endpoint representative lies in the same trivial (2^k)-multiple class, and the quotient
[
oxed{
j:=J/2^k=Y-N
}
]
transforms simply as
[
oxed{
j_t=j+t.
}
]

Thus the terminal defect quotient is literally the ordinary endpoint gap.

## 6. Interaction with minimal-counterexample logic

If a candidate belongs to a positive-credit equal-endpoint Hensel fiber, the translated representative has a smaller ordinary start and the same endpoint.

Therefore the Hensel test should be applied before storing multiple terminal Pareto representatives from that fiber.

This is exactly the MATH-198 ordering, now with the explicit defect identity.

No extra 'J filter' credit may be counted for eliminating a state already removed by the same Hensel/Pareto extremality relation.

## 7. r=10 consequence

The current (r=10) terminal danger predicate was written schematically as

[
mathsf{HenselLegal}
wedge
(Jge0)
wedge
mathsf{Res}_{13}.
]

MATH-210 reduces the first two channels to

[
oxed{
	ext{Hensel-extremal future/address fiber}
wedge
(jge0)
}
]

with
[
j=Y-N.
]

The remaining genuinely independent obstruction is the next-address/carry resonance.

So the (r=10) quotient no longer needs separate Hensel-order, Pareto-order, and integer-defect coordinates.

## 8. Claim boundary

Established:

- exact defect translation (J_t=J+t2^k);
- exact endpoint-gap translation (j_t=j+t);
- Hensel, Pareto-risk, and terminal-defect orders coincide on an equal-endpoint fiber;
- terminal product state may merge these order channels after exact future/address partition.

Not established:

- emptiness of every Hensel-extremal (r=10) 13-bit resonance cell;
- arbitrary-depth singleton closure;
- (r=10) closure;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

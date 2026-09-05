# Position-dependent repair branching wedge

Date: 2026-08-26

Status: **exact structural corollary** for the repaired first resonance.  It refines the long-credit uniqueness theorem spatially along the odd-ordinal axis.

## 1. Local displacement cap

At odd ordinal `j`,

\[
d_j\le\left\lfloor\frac{(j-1)P}{Q}\right\rfloor,
\qquad
P=42150895613,
\quad
Q=72057431991.
\]

An `L`-trit alignment repair belongs to one residue class modulo

\[
M_L=2\cdot3^L.
\]

Two different ordinary representatives of that repair class can exist only if the local displacement interval is at least one full modulus wide.  Thus multiple representatives require

\[
\left\lfloor\frac{(j-1)P}{Q}\right\rfloor\ge M_L.
\]

The first possible odd ordinal is therefore

\[
\boxed{
j_L=1+\left\lceil\frac{M_LQ}{P}\right\rceil.}
\]

Before `j_L`, the ordinary repair representative is unique whenever it exists.

## 2. Exact first branching locations

\[
\begin{array}{c|r|r}
L&M_L=2\cdot3^L&j_L\\\hline
15&28697814&49059239\\
16&86093442&147177713\\
17&258280326&441533135\\
18&774840978&1324599402\\
19&2324522934&3973798204\\
20&6973568802&11921394610
\end{array}
\]

Thus, for example, every 20-trit repair occurring among the first

\[
\boxed{11921394609}
\]

odd ordinals has at most one ordinary displacement representative.

## 3. Global closure at 21 trits

The ordering-debt budget theorem gives

\[
d_j\le19106028518
\]

for every surviving first-resonance path.  Since

\[
2\cdot3^{21}=20920706406>19106028518,
\]

we have the global statement

\[
\boxed{
L\ge21
\Longrightarrow
\text{at most one ordinary repair representative at every ordinal}.}
\]

## 4. DSD/Bellman interpretation

The repair-control space has a wedge shape rather than a uniform branching factor:

- near the start boundary, even moderately long alignment purchases are deterministic;
- farther into the bridge, shorter repairs may acquire several ordinary representatives;
- 21-trit or longer repairs are deterministic everywhere under the global defect budget.

Therefore a future Bellman implementation should not allocate a uniform action set to all positions.  The exact local cap can be attached to each Christoffel macro block, so impossible repair representatives are removed before Hensel-state expansion.

Companion certificate:

`collatz/src/first_resonance_position_dependent_repair_branching_certificate.py`.

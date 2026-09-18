# MATH-221 — complete closure of the r=10 zero-carry singleton branch

Date: 2026-09-19

Status: EXACT BRANCH CLOSURE / r=10 ZERO CARRY CLOSED / NONZERO CARRY OPEN

## 1. Zero carry forces L=72

At singleton resolution R=0, an exact zero-cost prefix source is Y=A+2^L t with 0<=A<2^L, and the transported carry is d=t=(Y-A)/2^L.

If d=0 then Y=A<2^L. Every unresolved first-cell boundary anchor has Y>2^71, while MATH-058 gives L<=72. Therefore d=0 forces L=72.

Thus arbitrary regenerated zero carry does not require an audit over L=13..72; only L=72 is possible.

## 2. Complete L=72 paid-exit catalogue

Replaying the unchanged MATH-058R exact generator gives four phase intervals. Every row has q_prefix=46 and t_min=t_max=0.

The four phase rows collapse to exactly two ordinary boundary anchors:

Y1 = 2,923,998,483,521,551,607,675
Y2 = 3,684,363,727,262,161,628,267

These are the complete first-cell paid-exit candidates with L=72 and zero carry.

## 3. Exact descent

Direct exact shortcut iteration gives:

- Y1 reaches 1,736,361,812,508,308,967,506 <= 2^71 after 80 steps.
- Y2 reaches 1,458,593,661,034,558,542,377 <= 2^71 after 79 steps.

The actual shortcut orbit is deterministic, so no enumeration of r=10 paid-cluster realizations is needed once the exact boundary anchor is fixed.

## 4. Conclusion

singleton r=10 zero incoming carry => descent to <=2^71.

Therefore the r=10 zero-carry branch is CLOSED in the current first-cell scope.

This strengthens MATH-206: the result is not restricted to the frozen initial factor catalogue. Zero carry itself forces the universal L=72 paid-exit catalogue.

## 5. Remaining branch

Every unresolved r=10 path now has d != 0. At R=0, d=floor(Y/2^L), 13<=L<=71, and because Y<2^73:

1 <= d < 2^(73-L) <= 2^60.

The remaining target is the bounded nonzero carry combined with the nine MATH-220 low-address/phase cells and the exact Hensel/Pareto/global-defect state.

Claim boundary: zero carry CLOSED; nonzero carry and full r=10 remain OPEN.
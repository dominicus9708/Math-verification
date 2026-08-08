# Math-verification

수학적 추측·정리 후보를 **증명 / 계산검증 / 반례탐색 / 문헌기반 파생결과**로 분리하여 기록하는 저장소입니다.

## 현재 작업

- `collatz/`: Collatz 추측의 accelerated map에 대한 구조적 검증
- 목표는 계산 결과를 증명으로 오인하지 않고, 기존 정리(Terras, Bernstein–Lagarias, Rozier–Terracol, Winkler 등)와 새로 도출한 보조정리 후보를 분리하는 것입니다.

## 상태 표기

- **THEOREM (external)**: 외부 문헌에서 증명된 결과
- **DERIVED LEMMA**: 외부 정리와 명시적 계산식으로부터 이번 작업에서 도출한 결과
- **COMPUTATIONAL CHECK**: 유한 범위 exact-integer 검증
- **CONJECTURE / TARGET**: 아직 증명이 필요한 명제
- **FAILED ROUTE**: 반례 또는 포화로 인해 전역 증명 경로로 부적절함이 확인된 접근

# SmartThings AI 루틴 어시스턴트 데모

자연어 한 문장으로 If/Then 자동화 루틴을 만드는 시나리오를, Figma 설계 그대로 터치하며 진행하는 인터랙티브 데모입니다.

| 파일 | 용도 |
|---|---|
| `index.html` | **iPhone 16 Pro 세로 풀스크린** (GitHub Pages 기본 주소) |
| `desktop.html` | PC 발표용 (폰 목업 + 단계 설명 패널) |
| `versions/` | 지난 버전 보관 (V1, V2, V3) |

## 아이폰에서 실행
1. Safari에서 `https://manggoo71.github.io/routine-demo/` 열기
2. 공유 → **홈 화면에 추가** → 홈 화면 아이콘으로 실행하면 주소창 없는 전체 화면
3. 파란 링이 보이는 곳을 터치해 진행, **두 손가락 탭**으로 데모 메뉴(이전/다음/처음부터)

## 수정·빌드
- 화면과 동작은 `src/demo.iphone.src.html`, `src/demo.desktop.src.html`에서 수정합니다.
- `python3 tools/build.py` 로 폰트(One UI Sans)와 아이콘을 넣어 `index.html`, `desktop.html`을 다시 만듭니다.

## 버전 기록
| 버전 | 내용 |
|---|---|
| V1 | 영상·Figma 주석 기반 11단계 터치 진행 데모 |
| V2 | Figma 원본 라운드 값 적용, 루틴 스크롤 포커스, 조건 개선·동작 제안 다이얼로그 |
| V3 | 보내기 시 추천 루틴 제거, 완료 메시지 3·2·1 자동 닫힘, 트랙패드 스크롤 보강 + iPhone 16 Pro 풀스크린 버전 |

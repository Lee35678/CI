# CI

pytest(fixture·caplog·mocker)와 GitHub Actions로 테스트 자동화를 연습한 저장소.

## 개요

간단한 장바구니(`Cart`)와 결제 호출(`charge`) 코드를 두고, pytest 테스트를 작성한 뒤
`main` 브랜치에 push / PR이 올라올 때마다 GitHub Actions에서 테스트가 자동으로 실행되도록 구성했다.

## 주요 내용

- `src/cart.py` — `Cart.add(name, price, qty)`(음수 가격이면 `ValueError`), `Cart.total()`(빈 장바구니면 `EmptyCartError`)
- `src/payment.py` — `requests.post`로 결제 API(`https://api.example.com/pay`, 예시 주소)를 호출하는 `charge(amount)`
- `tests/conftest.py` — 테스트마다 새 `Cart`를 만들고 끝나면 비우는 `cart` fixture (yield 방식 준비/정리)
- `tests/test_cart.py` — 빈 장바구니 결제 시 예외가 ERROR 로그로 남는지 `caplog`로 확인
- `tests/test_payment.py` — `pytest-mock`으로 `requests.post`를 가짜로 바꿔, 실제 네트워크 없이 호출 횟수와 전달된 금액을 검증
- `.github/workflows/test.yml` — Ubuntu + Python 3.12에서 `pip install -r requirements.txt` 후 `pytest -v` 실행 (pip 캐시 사용)

## 기술 스택

Python 3.12, pytest, pytest-mock, pytest-cov, requests, GitHub Actions

## 실행 방법

```bash
pip install -r requirements.txt
pytest -v
```

`pyproject.toml`에서 `pythonpath = ["."]`를 설정해 두었으므로 저장소 루트에서 실행하면 `from src.cart import Cart`가 동작한다.

커버리지 확인(`pytest-cov` 설치됨):

```bash
pytest --cov=src --cov-report=term-missing
```

## 폴더 구조

```
CI/
├── .github/workflows/test.yml   # GitHub Actions 테스트 워크플로
├── src/
│   ├── cart.py                  # 장바구니
│   └── payment.py               # 결제 API 호출
├── tests/
│   ├── conftest.py              # cart fixture
│   ├── test_cart.py
│   └── test_payment.py
├── pyproject.toml               # pytest 설정 (pythonpath)
└── requirements.txt
```

## 참고

- 연습용 코드라 테스트는 2개뿐이다. `Cart.add`의 음수 가격 검증이나 `total()` 합계 계산 자체를 확인하는 테스트는 아직 없다.
- `payment.py`의 결제 주소는 예시 도메인이며 실제 결제 연동이 아니다. 타임아웃·HTTP 오류 처리도 없다.
- 워크플로는 `main` 브랜치 대상 push / pull request에서만 실행된다.

import pytest
from src.cart import Cart

@pytest.fixture(scope="function")
def cart():
    print("\n [준비] 새 장바구니")
    c = Cart()
    yield c
    print(" [정리] 장바구니 비움")
    c.items.clear()


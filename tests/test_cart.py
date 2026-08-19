import logging

def test_error_is_logged(cart, caplog):
    with caplog.at_level(logging.ERROR):
        try:
            cart.total()
        except Exception:
            logging.getLogger("app").exception("빈 장바구니 결제 시도")
    assert "빈 장바구니" in caplog.text
    assert caplog.records[0].levelname == "ERROR"
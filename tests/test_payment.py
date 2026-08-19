def test_charge_called_with_amount(mocker):
    fake = mocker.patch("src.payment.requests.post")
    fake.return_value.json.return_value = {"status": "ok"}
    
    from src.payment import charge
    assert charge(12000) == {"status": "ok"}
    assert fake.call_count == 1
    assert fake.call_args.kwargs["json"]["amount"] == 12000
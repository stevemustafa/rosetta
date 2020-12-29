import functions.stock_checker

@pytest.mark.skip(reason="to be deprecated")
def test_stock_checker():
    pass
    """
    stock_price = 25
    input_payload = {"stock_price": stock_price}

    data = app.lambda_handler(input_payload, "")

    assert "id" in data
    assert "price" in data
    assert "type" in data
    assert "timestamp" in data
    assert "qty" in data

    assert data["type"] == "sell"
    assert data["price"] == str(stock_price)
    """
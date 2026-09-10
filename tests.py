from unittest.mock import Mock, patch

from price_tracker import Object

PRICE_HTML = '<div id="corePrice_feature_div"><span class="a-price-whole">1,299.</span></div>'


def fake_response(html):
    return Mock(status_code=200, text=html)


@patch("price_tracker.requests.get")
def test_reached_when_price_below_target(mock_get):
    mock_get.return_value = fake_response(PRICE_HTML)
    assert Object("Headphones", 1500, "https://example.com").check_if_reached_target() is True


@patch("price_tracker.requests.get")
def test_not_reached_when_price_above_target(mock_get):
    mock_get.return_value = fake_response(PRICE_HTML)
    assert Object("Headphones", 1000, "https://example.com").check_if_reached_target() is False


@patch("price_tracker.requests.get")
def test_missing_price_element(mock_get):
    mock_get.return_value = fake_response("<html>Enter the characters you see below</html>")
    assert Object("Headphones", 1000, "https://example.com").check_if_reached_target() is False
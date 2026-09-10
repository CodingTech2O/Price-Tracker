import pytest
from price_tracker import Object


def test_price_target():
    url = "https://www.amazon.com/gp/product/B08P2D215V/ref=ewc_pr_img_1?smid=ATVPDKIKX0DER&th=1"

    assert Object("LED strips", 28236, url).check_if_reached_target() is False
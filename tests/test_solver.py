import rooftop_puzzle as rp


def test_check():
    expected = False
    obtained = rp.check()
    assert expected == obtained

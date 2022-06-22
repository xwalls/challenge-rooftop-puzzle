import rooftop_puzzle as rp


def test_check():
    expected = True
    obtained = rp.check()
    assert expected == obtained

from score import level


def test_boundary_score():
    assert level(59) == "fail"
    assert level(60) == "pass"

    
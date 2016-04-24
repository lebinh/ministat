from ministat.ministat import lookup_t_value, pooled_s_value, compare

iguana = [50, 200, 150, 400, 750, 400, 150]
chameleon = [150, 400, 720, 500, 930]


def is_close_enough(v1, v2, epsilon=0.001):
    return v1 - v2 < epsilon


def test_lookup_t_value():
    assert is_close_enough(lookup_t_value(iguana, chameleon), 2.228)


def test_pooled_s_value():
    assert is_close_enough(pooled_s_value(iguana, chameleon), 154.676)


def test_compare():
    is_different, _, _, _ = compare(iguana, chameleon)
    assert not is_different


def test_compare_at_lower_confidence():
    is_different, _, _, _ = compare(iguana, chameleon, confidence_level=80)
    assert is_different

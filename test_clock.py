import pytest

from clock import calculate_angle


def test_calculate_angle():

    # simple wrapper to show debug output
    def c(t):
        res = calculate_angle(t)
        print t, res
        return res

    assert c('0:00') == 0
    assert c('2:00') == 60
    assert c('3:00') == 90
    assert c('12:00') == 0
    assert c('18:00') == 180
    assert c('21:00') == 90
    assert c('22:00') == 60

    assert c('12:01') < 360 / 60
    assert c('23:59') < 360 / 60

    assert c('13:03') < 360 / 60 * 3
    assert c('13:04') < 360 / 60 * 3
    assert c('13:05') < 360 / 60 * 3
    assert c('13:08') < 360 / 60 * 3

    assert c('21:48') < 360 / 60 * 2

    assert c('17:28') < 360 / 60 * 3

    with pytest.raises(Exception):
        c('invalid')

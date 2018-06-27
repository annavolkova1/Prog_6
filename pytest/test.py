import pytest
from hypothesis import given
import hypothesis.strategies as strat


list1 = list('123456')
list2 = list('abcd')


def dictionaryFromKeys(k, v):
    try:
        res = dict.fromkeys(k, None)
        res.update(zip(k, v))
    except TypeError:
        res = 'TypeError'
    return res


result = dictionaryFromKeys(list1, list2)
print(result)


def assert_dictionaryFromKeys():
    assert dictionaryFromKeys([1, 2, 3, 4], [2, 3, 4, 5]) == {1: 2, 2: 3, 3: 4, 4: 5}, ('False')
    assert dictionaryFromKeys([6, 7, 8, 9, 10], [1, 2, 3, 4]) == {6: 1, 7: 2, 8: 3, 9: 4, 10: None}, ('Wrong!')


@pytest.mark.parametrize("a,b,expected", [
    ([1, 2, 3], ['a', 'b', 'c', 'd'], {1: 'a', 2: 'b', 3: 'c'}),
    ([1, 2, 3], 3, None),
    (3, ['a', 'b', 'c'], None),
    ([], ['a', 'b', 'c'], {})
    ])


def test_parametr(a, b, expected):
    assert dictionaryFromKeys(a, b) == expected
    assert dictionaryFromKeys([1, 2, 3], 3) == None
    assert dictionaryFromKeys(3,['a', 'b', 'c']) == None
    assert dictionaryFromKeys([], ['a', 'b', 'c']) == {}


@given(strat.lists(), strat.lists())
def test_dictionaryFromKeys(a, b):
    assert type(dictionaryFromKeys(a, b)) == dict
    assert len(dictionaryFromKeys(a, b)) == len(a)



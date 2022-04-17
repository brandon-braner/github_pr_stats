import pytest

from py_github.utils.url_utils import get_query_string, get_query_string_value


def test_get_query_string():
    url = 'https://example.com?last=5&next=2'
    query_string = get_query_string(url)
    assert query_string == {'last': ['5'], 'next': ['2']}


def test_get_query_string_value():
    url = 'https://example.com?last=5&next=2'
    query_string_value = get_query_string_value(url, 'last')
    query_string_value_not_first = get_query_string_value(url, 'last', False)

    assert query_string_value == '5'
    assert query_string_value_not_first == ['5']



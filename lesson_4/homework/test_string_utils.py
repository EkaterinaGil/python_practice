import pytest
from string_utils import StringUtils


@pytest.mark.parametrize('str, result', [
    ('test', 'Test'),
    ('Test', 'Test'),
    (' test', 'Test'),
    ('1test', '1Test'),
    ('&test', '&Test'),
    ('тест', 'Тест'),
    ('', ''),
    (' ', ' ')
])
def test_capitalize(str, result):
    string = StringUtils()
    res = string.capitilize(str)
    assert res == result


@pytest.mark.parametrize('str, result', [
    (' test', 'test'),
    ('test', 'test'),
    ('  test', 'test'),
    ('                test', 'test'),
    ('test ', 'test '),
    (' ', ''),
    ('', '')
])
def test_trim(str, result):
    string = StringUtils()
    res = string.trim(str)
    assert res == result


@pytest.mark.parametrize('data, delimeter, result', [
    ('s,t,r,i,n,g', ',', ['s', 't', 'r', 'i', 'n', 'g']),
    ('s:t:r:i:n:g', ':', ['s', 't', 'r', 'i', 'n', 'g']),
    ('', '', []),
    ('s,t,r,i,n,g', '-', ['s,t,r,i,n,g']),
    #     ('s,t,r,i,n,g', None, ['s', 't', 'r', 'i', 'n', 'g']),          Здесь я не придумала, как проверить кейсы без указания разделителя.
    #     ([], None, [])                                                  Пробовала подставлять '', None, просто два запятые - не работает.
])
def test_to_list(data, delimeter, result):
    string = StringUtils()
    res = string.to_list(data, delimeter)
    assert res == result


@pytest.mark.parametrize('data, symbol, result', [
    ('строка', 'о', True),
    ('строка', 'v', False),
    ('string', 'i', True),
    ('строка', '10', False),
    ('строка', 'ок', True),
    ('строка', 'та', False),
    ('строка', 'Стр', False),
    ('string', '', True),
    ('', '', True)
])
def test_contains(data, symbol, result):
    string = StringUtils()
    res = string.contains(data, symbol)
    assert res == result


@pytest.mark.parametrize('data, symbol, result', [
    ('строка', 'о', 'стрка'),
    ('сорока', 'о', 'срка'),
    ('string', 'i', 'strng'),
    ('строка', 'стро', 'ка'),
    ('строка', 'строка', ''),
    ('', '', '')
])
def test_delete_symbol(data, symbol, result):
    string = StringUtils()
    res = string.delete_symbol(data, symbol)
    assert res == result


@pytest.mark.parametrize('data, symbol, result', [
    ('строка', 'с', True),
    ('строка', 'стр', True),
    ('string', 'string', True),
    ('string', 'string ', False),
    ('строка', '10', False),
    ('строка', 'ок', False),
    ('строка', 'та', False),
    ('строка', 'C', False),
])
def test_starts_with(data, symbol, result):
    string = StringUtils()
    res = string.starts_with(data, symbol)
    assert res == result


@pytest.mark.parametrize('data, symbol, result', [
    ('строка', 'а', True),
    ('строка', 'ка', True),
    ('string', 'string', True),
    ('string', ' string', False),
    ('строка', '10', False),
    ('строка', 'ок', False),
    ('строка', 'та', False),
    ('строка', 'А', False),
])
def test_end_with(data, symbol, result):
    string = StringUtils()
    res = string.end_with(data, symbol)
    assert res == result


@pytest.mark.parametrize('data, result', [
    ('строка', False),
    ('', True),
    (' ', True),
    ('   ', True),
    (' строка', False),
])
def test_is_empty(data, result):
    string = StringUtils()
    res = string.is_empty(data)
    assert res == result


@pytest.mark.parametrize('data, delimeter, result', [
    ([1, 2, 3, 4], ',', '1,2,3,4'),
    ([1, 2, 3, 4], ', ', '1, 2, 3, 4'),
    (['1', '2', '3', '4'], ', ', '1, 2, 3, 4'),
    ([True, False], ',', 'True,False'),
    ([['dark', 'blue'], 'YELLOW'], ',', "['dark', 'blue'],YELLOW"),
    (['Ekaterina', 'Gil'], ' ', 'Ekaterina Gil'),
    (['dark', 'blue'], '-', 'dark-blue'),
    (['String', 'Utils'], '', 'StringUtils'),
    ([], '', '')
])
def test_list_to_string(data, delimeter, result):
    string = StringUtils()
    res = string.list_to_string(data, delimeter)
    assert res == result

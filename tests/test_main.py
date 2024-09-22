import pytest
from main import check_age
from main import check_auth
from main import get_cost


@pytest.mark.parametrize(
    'a, expected',
    (
        [18, 'Доступ разрешён'],
        [20, 'Доступ разрешён'],
        [15, 'Доступ запрещён'],
    )

)
def test_check_age(a,expected):
    actual = check_age(a)
    assert actual == expected


@pytest.mark.parametrize(
    'login, password, expected',
    (
        ['admin', 'password', 'Добро пожаловать'],
        ['Dima', '1234', 'Доступ ограничен']
    )
)
def test_check_auth(login, password, expected):
    actual = check_auth(login, password)
    assert actual == expected


@pytest.mark.parametrize(
    'a, expected',
    (
        [10, 'Стоимость доставки: 200 руб.'],
        [20, 'Стоимость доставки: 500 руб.'],
    )
)
def test_check_cost(a, expected):
    actual = get_cost(a)
    assert actual == expected
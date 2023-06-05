import pytest

# для каждой сесии

@pytest.fixture
def chrome(browser):
    pass

# для файла
@pytest.fixture(scope="module")
def user_id():
    return 123


def test_auth(chrome, user_id):
        assert user_id == 123
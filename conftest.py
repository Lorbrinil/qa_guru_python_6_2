import pytest

@pytest.fixture(scope="session")
def browser():
    print("Браузер стартует")
    yield
    print("\nБраузер закрывается")
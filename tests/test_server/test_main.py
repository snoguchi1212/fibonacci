from fastapi.testclient import TestClient
from fastapi import status

from app.server.main import app

client = TestClient(app=app)


def test_incorrect_url():
    response = client.get("/fib")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {'detail': [
                                {'loc': ['query', 'n'],
                                 'msg': 'field required',
                                 'type': 'value_error.missing'}]}

def test_index_returns_correct_1():
    response = client.get("/fib?n=1")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"result": 1}


def test_index_returns_correct_2():
    response = client.get("/fib?n=2")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"result": 1}


def test_index_returns_correct_99():
    response = client.get("/fib?n=99")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"result": 218922995834555169026}


def test_index_returns_over_n_10001():
    response = client.get("/fib?n=10001")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {'detail': [{'ctx': {'limit_value': 10000},
                               'loc': ['query', 'n'],
                               'msg': 'ensure this value is less than or equal to 10000',
                               'type': 'value_error.number.not_le'}]}

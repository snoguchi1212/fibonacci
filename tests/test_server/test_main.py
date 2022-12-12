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


def test_index_returns_correct_2():
    response = client.get("/fib?n=2")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 1


def test_index_returns_correct_99():
    response = client.get("/fib?n=99")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 218922995834555169026

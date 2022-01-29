from app import app


def test():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test2():
    response = app.test_client().get("/base")
    assert response.status_code == 200


def test3():
    response = app.test_client().get("/base")
    assert b'Added Task' in response.data
    assert response.status_code == 200

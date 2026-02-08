from app import app


def test_index_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_tei_route():
    client = app.test_client()
    response = client.get("/tei")
    assert response.status_code == 200

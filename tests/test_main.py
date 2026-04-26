from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Teste 1: Rota raiz retorna status 200
def test_root():
    response = client.get("/")
    assert response.status_code == 200


# Teste 2: Rota /status retorna status 200
def test_status():
    response = client.get("/status")
    assert response.status_code == 200


# Teste 3: Rota /teste retorna status 200
def test_teste():
    response = client.get("/teste")
    assert response.status_code == 200


# Teste 4: Rota raiz retorna conteúdo JSON (não vazio)
def test_root_returns_json():
    response = client.get("/")
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() is not None


# Teste 5: Rota /status retorna conteúdo JSON com algum dado
def test_status_returns_json():
    response = client.get("/status")
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() is not None


# Teste 6: Rota inexistente retorna 404
def test_rota_inexistente_retorna_404():
    response = client.get("/rota-que-nao-existe")
    assert response.status_code == 404


# Teste 7: Método POST na rota raiz retorna 405 (método não permitido)
def test_post_na_raiz_retorna_405():
    response = client.post("/")
    assert response.status_code == 405
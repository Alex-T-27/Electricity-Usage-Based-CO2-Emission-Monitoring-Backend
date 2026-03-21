from fastapi.testclient import TestClient
from main import app 
   
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    print(response.json())

def test_registering_new_user():
    response = client.post("/auth/register", json={"username":"Alex217", "password":"ILoveCookies"})
    assert response.status_code == 200
    assert response.json() == {"message" : "User registered successfully"}
    print(response.json())

def test_registering_existing_user():
    response = client.post("/auth/register", json={"username":"Alex", "password":"ILoveCookies"})
    assert response.status_code == 409
    assert response.json() == {"detail" : "Username already taken"}
    print(response.json())


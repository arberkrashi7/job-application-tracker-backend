import pytest

@pytest.mark.anyio
async def test_register_login_create_and_list_applications(client):
    # Register
    r = await client.post("/auth/register", json={"email": "a@example.com", "password": "supersecret1"})
    assert r.status_code == 200, r.text
    user = r.json()
    assert user["email"] == "a@example.com"

    # Login
    r = await client.post("/auth/login", json={"email": "a@example.com", "password": "supersecret1"})
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a few applications
    for company in ["Bloomberg", "Google", "Bloomberg"]:
        r = await client.post(
            "/applications",
            json={"company": company, "role": "Software Engineer", "status": "applied"},
            headers=headers,
        )
        assert r.status_code == 201, r.text

    # List with pagination
    r = await client.get("/applications?limit=2&offset=0", headers=headers)
    assert r.status_code == 200
    apps = r.json()
    assert len(apps) == 2

    # Filter by company
    r = await client.get("/applications?company=Bloomberg", headers=headers)
    assert r.status_code == 200
    apps = r.json()
    assert all("Bloomberg" in a["company"] for a in apps)
    assert len(apps) == 2

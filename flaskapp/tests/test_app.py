from flaskapp.app import app
import json

def test_home():
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    
    # Parse JSON body
    data = json.loads(response.data.decode("utf-8"))
    
    # Now assert the message
    assert data["message"] == "Hello from kenneth DevOps Pipeline this is a clear message from the devops team!"

import os
import tempfile
from app import app


def test_index_get():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200, "GET request to index failed"


def test_index_post():
    tester = app.test_client()

    # Create a mock CSV file for testing
    mock_data = "Content\nI loved the movie\nIt was amazing\nNot great"
    mock_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    mock_file.write(mock_data.encode())
    mock_file.close()

    data = {
        "movie_name": "Mock Movie",
        "budget": "25000000",
        "genre": "Horror",
        "tweets_csv": (open(mock_file.name, "rb"), mock_file.name),
    }
    response = tester.post("/", data=data, content_type="multipart/form-data")
    os.unlink(mock_file.name)

    assert response.status_code == 200, "POST request to index failed"
    assert b"Prediction Result" in response.data, "Result page not rendered correctly"

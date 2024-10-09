from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    
    """
    A simple Flask application that demonstrates a basic web server.

    This application initializes a Flask instance and defines a single route that returns a greeting message. It runs the server in debug mode when executed as the main program.

    """
    return '<h1>Hello from Flask & Docker</h2>'

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("endpoint, expected_status, expected_content", [
    ('/', 200, b'<h1>Hello from Flask & Docker</h2>'),
], ids=["happy_path_root"])
def test_flask_app(client, endpoint, expected_status, expected_content):


    # Act
    response = client.get(endpoint)
    
    # Assert
    assert response.status_code == expected_status
    assert response.data == expected_content

@pytest.mark.parametrize("endpoint, expected_status", [
    ('/nonexistent', 404),
], ids=["error_path_nonexistent"])
def test_flask_app_error_cases(client, endpoint, expected_status):
    
    # Act
    response = client.get(endpoint)
    
    # Assert
    assert response.status_code == expected_status


if __name__ == "__main__":
    app.run(debug=True)

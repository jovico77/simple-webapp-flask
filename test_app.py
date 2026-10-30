from app import app

client = app.test_client()

def test_home_page():
    response = client.get('/')

    assert response.status_code == 200
    assert response.data == b'Welcome!'

def test_how_are_you_page():
    response = client.get('/how-are-you')

    assert response.status_code == 200
    assert response.data == b'I am good, how about you?'

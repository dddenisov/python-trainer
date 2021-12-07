import pytest

def test_ping(client):
    """Start with a blank database."""

    rv = client.get('/ping')
    assert b'Pong' in rv.data

def test_post(client):
    rv = client.post('/post', data=dict(
        data='test text'
    ), follow_redirects=True)

    assert b'test text' in rv.data
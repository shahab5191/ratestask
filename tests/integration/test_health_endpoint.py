def test_server_is_running(client):
    response = client.get('/v1/healthz')
    assert response.status_code == 200
    json_response = response.json
    assert 'status' in json_response
    assert json_response['status'] == 'healthy'

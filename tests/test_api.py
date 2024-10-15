import requests
import pytest
import responses
from config import API_URL
from mock_responses import SUCCESS_RESPONSE, INVALID_FIELDS_RESPONSE


@pytest.fixture(autouse=True)
def enable_vcr():
    responses.start()
    yield
    responses.stop()
    responses.reset()
def make_order(data):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{API_URL}/orders",json = data, headers=headers)
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"status": "error", "message": str(e)}
    

def test_successful_order():
    responses.add(
        responses.POST,
        f"{API_URL}/orders",
        json=SUCCESS_RESPONSE,
        status=200
    )
    
    data = {"product_id":1, "quantity":2}
    result= make_order(data)
    assert result["status"] == "success"
    assert result["message"] == "Order placed successfully."
    
    
def test_invalid_fields():
    responses.add(
        responses.POST,
        f"{API_URL}/orders",
        json=INVALID_FIELDS_RESPONSE,
        status=400
    )
    
    data = {"product_id":1, "quantity":2}
    result= make_order(data)
    assert result["status"] == "error"
    assert result["message"] == "Required fields are missing or incorrect."
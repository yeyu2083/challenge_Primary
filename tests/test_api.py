import requests
import pytest
import responses
import allure

from config import API_URL
from mock_responses import SUCCESS_RESPONSE, INVALID_FIELDS_RESPONSE


@pytest.fixture(autouse=True)
def enable_vcr():
    responses.start()
    yield
    responses.stop()
    responses.reset()
    
@allure.step("Making an order")    
def make_order(data):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{API_URL}/orders",json = data, headers=headers)
        
        allure.attach(str(data), name="Request Data", attachment_type=allure.attachment_type.JSON)
        allure.attach(response.text, name="Response Data", attachment_type=allure.attachment_type.JSON)
      
        return response.json()
    except requests.exceptions.HTTPError as e:
        allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
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
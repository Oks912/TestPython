import pytest
import requests
import json

BASE_URL = 'https://api.restful-api.dev/objects'
product_headers = {
    "content-type": "application/json"
}

product_json = json.dumps({
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})


def test_get_request():
    expected_response = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    response = requests.get(BASE_URL)
    response_data = response.json()  # Parse the JSON response to a dictionary

    print("Response status code:", response.status_code)
    print("Response data:", response_data)

    assert response.status_code == 200

    found_response = None
    for data in response_data:
        if data["name"] == "Apple MacBook Pro 16":
            found_response = data
            break

    assert found_response is not None
    for key, value in expected_response["data"].items():
        assert key in found_response["data"]
        assert found_response["data"][key] == value


def test_post_request():
    response = requests.post(BASE_URL, data=product_json, headers=product_headers)
    response_data = response.json()
    print("Response status code:", response.status_code)
    print("Response data:", response_data)
    assert response.status_code == 200
    assert response_data["name"] == "Apple MacBook Pro 16"
    assert response_data["data"]["year"] == 2019
    assert response_data["data"]["price"] == 1849.99
    assert response_data["data"]["CPU model"] == "Intel Core i9"
    assert response_data["data"]["Hard disk size"] == "1 TB"


def test_put_request():
    # Create a product first
    response = requests.post(BASE_URL, data=product_json, headers=product_headers)
    assert response.status_code == 200

    # Retrieve the created product ID
    product_id = response.json().get('id')

    # Prepare updated product data
    updated_product_json = json.dumps({
        "name": "Updated MacBook Pro",
        "data": {
            "year": 2022,
            "price": 1999.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    })

    # Make the PUT request to update the product
    update_url = f"{BASE_URL}/{product_id}"
    response = requests.put(update_url, data=updated_product_json, headers=product_headers)
    assert response.status_code == 200
    print("PUT response status code:", response.status_code)
    # Verify the updated product data
    updated_product_data = response.json().get('data')
    assert updated_product_data["year"] == 2022
    assert updated_product_data["price"] == 1999.99
    assert updated_product_data["CPU model"] == "Intel Core i9"
    assert updated_product_data["Hard disk size"] == "2 TB"


def test_patch_request():
    # Create a product first
    response = requests.post(BASE_URL, data=product_json, headers=product_headers)
    assert response.status_code == 201

    # Retrieve the created product ID
    product_id = response.json().get('id')

    # Prepare updated product data for PATCH request
    patch_data = {
        "name": "Updated MacBook Pro",
        "data": {
            "year": 2022,
            "price": 1999.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }

    # Make the PATCH request to update the product
    patch_url = f"{BASE_URL}/{product_id}"
    response = requests.patch(patch_url, json=patch_data, headers=product_headers)
    assert response.status_code == 200

    # Verify the updated product data
    updated_product_data = response.json().get('data')
    assert updated_product_data["year"] == 2022
    assert updated_product_data["price"] == 1999.99
    assert updated_product_data["CPU model"] == "Intel Core i9"
    assert updated_product_data["Hard disk size"] == "2 TB"

def test_delete_request():
    # Create a product first
    response = requests.post(BASE_URL, data=product_json, headers=product_headers)
    assert response.status_code == 201

    # Retrieve the created product ID
    product_id = response.json().get('id')

    # Make the DELETE request to delete the product
    delete_url = f"{BASE_URL}/{product_id}"
    response = requests.delete(delete_url)
    assert response.status_code == 204
    print("DELETE response status code:", response.status_code)

    if response.status_code == 204:
        print(f"Product with ID {product_id} successfully deleted")
    else:
        print(f"Failed to delete product with ID {product_id}")
    # Verify that the product has been deleted
    response = requests.get(BASE_URL)
    response_data = response.json()
    assert not any(data["id"] == product_id for data in response_data)
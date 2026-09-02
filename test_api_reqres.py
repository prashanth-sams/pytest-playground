import requests
import pytest
# from pytest_html_reporter import attach_text
from pytest_html_reporter import attach_api, attach_file, attach_json, attach_text

class TestReqresAPI:
    """Test suite for Reqres API endpoints"""
    
    BASE_URL = "https://reqres.in/api"
    
    # def test_get_single_user(self):
    #     """Test GET request for single user with ID 2"""
    #     # Arrange
    #     user_id = 2
    #     endpoint = f"{self.BASE_URL}/users/{user_id}"
        
    #     # Act
    #     response = requests.get(endpoint)
        
    #     # Assert
    #     assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
    #     # Verify response structure
    #     json_data = response.json()
    #     assert "data" in json_data, "Response should contain 'data' key"
    #     assert "support" in json_data, "Response should contain 'support' key"
        
    #     # Verify user data
    #     user_data = json_data["data"]
    #     assert user_data["id"] == user_id, f"Expected user id {user_id}, got {user_data['id']}"
    #     assert "email" in user_data, "User data should contain 'email'"
    #     assert "first_name" in user_data, "User data should contain 'first_name'"
    #     assert "last_name" in user_data, "User data should contain 'last_name'"
    #     assert "avatar" in user_data, "User data should contain 'avatar'"
        
    # def test_get_single_user_response_time(self):
    #     """Test that the API responds within acceptable time"""
    #     endpoint = f"{self.BASE_URL}/users/2"
        
    #     response = requests.get(endpoint)
        
    #     # Assert response time is less than 2 seconds
    #     assert response.elapsed.total_seconds() < 2, "Response time exceeded 2 seconds"
        
    def test_get_single_user_headers(self):
        """Test response headers"""
        endpoint = f"{self.BASE_URL}/users/2"
        
        response = requests.get(endpoint)

        assert response.status_code == 200
        
        # attach_text(response.headers)
        attach_json(requests.get(f"{self.BASE_URL}/users/2").json())
        # attach_json(response.json())
        # attach_api(response)

        # assert "application/json" in response.headers.get("Content-Type", ""), \
        #     "Content-Type should be application/json"
            
    # def test_get_nonexistent_user(self):
    #     """Test GET request for a user that doesn't exist"""
    #     endpoint = f"{self.BASE_URL}/users/999"
        
    #     response = requests.get(endpoint)
        
    #     # Reqres returns 404 for non-existent users
    #     assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

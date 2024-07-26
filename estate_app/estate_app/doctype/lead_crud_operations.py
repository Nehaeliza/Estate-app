
# import requests
# import uuid  # For generating unique IDs

# base_url = 'http://localhost:8000/api/resource/Lead'
# auth = ('c70b9b776f8b2f2', '5dbefb8bf7d231d')

# def create_lead():
#     unique_email = f"john.doe.{uuid.uuid4().hex[:6]}@example.com"
#     data_create = {
#         "first_name": "John",
#         "last_name": "Doe",
#         "email_id": unique_email,
#         "mobile_no": "+1234567890",
#         "company": "eliz",
#         "country": "India"
#     }
#     response_create = requests.post(base_url, json=data_create, auth=auth)
#     print("Create Lead:", response_create.json())
#     lead_name = response_create.json().get('data', {}).get('name')
#     return lead_name

# def read_lead(lead_name):
#     response_read = requests.get(f"{base_url}/{lead_name}", auth=auth)
#     print(f"Read Lead '{lead_name}':", response_read.json())

# def update_lead(lead_name):
#     data_update = {
#         "mobile_no": "+1987654321"
#     }
#     response_update = requests.put(f"{base_url}/{lead_name}", json=data_update, auth=auth)
#     print(f"Update Lead '{lead_name}':", response_update.json())

# def delete_lead(lead_name):
#     response_delete = requests.delete(f"{base_url}/{lead_name}", auth=auth)
#     print(f"Delete Lead '{lead_name}':", response_delete.status_code)

# # Main function to orchestrate the operations
# def main():
#     # Create lead
#     lead_name = create_lead()
#     input("Press Enter to continue...")
    
#     # Read lead
#     read_lead(lead_name)
#     input("Press Enter to continue...")
    
#     # Update lead
#     update_lead(lead_name)
#     input("Press Enter to continue...")
    
#     # Delete lead
#     delete_lead(lead_name)
#     input("Press Enter to exit...")

# if __name__ == "__main__":
#     main()

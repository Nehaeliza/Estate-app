
# import requests

# base_url = 'http://localhost:8000/api/resource/Student'
# auth = ('c70b9b776f8b2f2', '5dbefb8bf7d231d')

# reg_no = "123458"

# # Check if the student already exists
# response = requests.get(f"{base_url}/{reg_no}", auth=auth)
# if response.status_code == 200:
#     print("Student already exists:", response.json())
# else:
#     # Create
#     data = {
#         "reg_no": reg_no,
#         "name1": "Johny Doe",
#         "dob": "2000-01-01",
#         "gender": "Male"
#     }
#     response = requests.post(base_url, json=data, auth=auth)
#     print("Create:", response.json())

# # Read
# response = requests.get(f"{base_url}/{reg_no}", auth=auth)
# print("Read:", response.json())

# # Update
# data = {
#     "dob": "2000-01-02"
# }
# response = requests.put(f"{base_url}/{reg_no}", json=data, auth=auth)
# print("Update:", response.json())

# # Delete
# response = requests.delete(f"{base_url}/{reg_no}", auth=auth)
# print("Delete:", response.status_code)  # 204 indicates success

# import requests

# base_url = 'http://localhost:8000/api/resource/Student'
# auth = ('c70b9b776f8b2f2', '5dbefb8bf7d231d')

# reg_no = "123457"

# def create_student():
#     data = {
#         "reg_no": reg_no,
#         "name1": "Joyana Doe",
#         "dob": "2000-01-01",
#         "gender": "Male"
#     }
#     response = requests.post(base_url, json=data, auth=auth)
#     print("Create:", response.json())

# def read_student():
#     response = requests.get(f"{base_url}/{reg_no}", auth=auth)
#     print("Read:", response.json())

# def update_student():
#     data = {
#         "dob": "2000-01-02"
#     }
#     response = requests.put(f"{base_url}/{reg_no}", json=data, auth=auth)
#     print("Update:", response.json())

# def delete_student():
#     response = requests.delete(f"{base_url}/{reg_no}", auth=auth)
#     print("Delete:", response.status_code)  # 204 indicates success

# # Main function to orchestrate the operations
# def main():
#     input("Press Enter to create student...")
#     create_student()
    
#     input("Press Enter to read student...")
#     read_student()
    
#     input("Press Enter to update student...")
#     update_student()
    
#     input("Press Enter to delete student...")
#     delete_student()

# if __name__ == "__main__":
#     main()

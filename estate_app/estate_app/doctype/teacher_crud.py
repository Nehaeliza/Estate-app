# import requests
# from frappe import _
# import frappe
# # Configuration
# base_url = 'http://localhost:8000/api/resource/Teacher'
# auth = ('c70b9b776f8b2f2', '5dbefb8bf7d231d')
# teacher_name = None  # Variable to store the created teacher's name  /home/neha/projects/test_bench/frappe-bench/apps/estate_app/estate_app/estate_app/doctype/teacher_crud.py
# @frappe.whitelist(allow_guest=True)
# def create_teacher():
#     global teacher_name
#     data = {
#         "title": "Professor",
#         "description": "A professor of Computer Science.",
#         "age": 40,
#         "birth_date": "1983-06-01",
#         "is_active": 1,
#         "status": "Active"
#     }
#     response = requests.post(base_url, json=data, auth=auth)
#     if response.status_code == 200:
#         print("Create:", response.json())
#         teacher_name = response.json().get('data', {}).get('name')
#     else:
#         print("Failed to create teacher:", response.json())

# def read_teacher():
#     if teacher_name:
#         response = requests.get(f"{base_url}/{teacher_name}", auth=auth)
#         print("Read:", response.json())
#     else:
#         print("Teacher name not defined. Create a teacher first.")

# def update_teacher():
#     if teacher_name:
#         data = {
#             "age": 41
#         }
#         response = requests.put(f"{base_url}/{teacher_name}", json=data, auth=auth)
#         print("Update:", response.json())
#     else:
#         print("Teacher name not defined. Create a teacher first.")

# def delete_teacher():
#     if teacher_name:
#         response = requests.delete(f"{base_url}/{teacher_name}", auth=auth)
#         print("Delete:", response.status_code)  # 204 indicates success
#     else:
#         print("Teacher name not defined. Create a teacher first.")

# # Main function to orchestrate the operations
# def main():
#     input("Press Enter to create teacher...")
#     create_teacher()
    
#     input("Press Enter to read teacher...")
#     read_teacher()
    
#     input("Press Enter to update teacher...")
#     update_teacher()
    
#     input("Press Enter to delete teacher...")
#     delete_teacher()

# if __name__ == "__main__":
#     main()

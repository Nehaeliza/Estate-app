import frappe

def create_custom_doctype():
    if not frappe.db.exists("DocType", "CustomDoc"):
        custom_doctype = frappe.get_doc({
            "doctype": "DocType",
            "name": "CustomDoc",
            "module": "Estate App",
            "custom": 1,
            "autoname": "field:field_1",
            "fields": [
                {
                    "fieldname": "field_1",
                    "fieldtype": "Data",
                    "label": "Field 1",
                    "reqd": 1
                },
                {
                    "fieldname": "field_2",
                    "fieldtype": "Int",
                    "label": "Field 2"
                }
                # Add more fields as needed
            ],
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1
                }
                # Define more permissions as required
            ]
        })
        custom_doctype.insert()
        frappe.db.commit()
        print("Custom doctype created successfully.")
    else:
        print("Doctype already exists.")
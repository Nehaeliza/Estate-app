import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_students():
    try:
        # Query to fetch student records from the database
        students = frappe.get_all("Student", fields=["reg_no","name1", "dob", "gender", "email", "phone", "department", "course"])

        # Fetch marks (assuming marks is a child table)
        # for student in students:
        #     student["marks"] = frappe.get_all("Mark", filters={"parent": student.name}, fields=["subject_code", "subject_name"])

        return students

    except Exception as e:
        frappe.throw(_("Failed to fetch students: {0}").format(str(e)))


# Copyright (c) 2024, Neha Joy and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data
# custom_report.py

# custom_report.py

# custom_report.py


'''import frappe

def execute(filters=None):
    columns = [
        {"label": "Registration Number", "fieldname": "reg_no", "fieldtype": "Data"},
        {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
        {"label": "Phone", "fieldname": "phone", "fieldtype": "Data"},
        {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
        {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
        {"label": "Date of Birth", "fieldname": "dob", "fieldtype": "Date"},
        {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
        {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
        {"label": "Mark", "fieldname": "mark", "fieldtype": "Data"},
        {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
        {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
    ]

    data = []

    student_filters = {}
    if filters:
        
        if filters.get("reg_no"):
            student_filters["reg_no"] = filters.get("reg_no")
        if filters.get("name1"):
            student_filters["name1"] = ["like", f"%{filters.get('name1')}%"]
        if filters.get("gender"):
            student_filters["gender"] = filters.get("gender")
        if filters.get("email"):
            student_filters["email"] = ["like", f"%{filters.get('email')}%"]
        if filters.get("phone_number"):
            student_filters["phone"] = filters.get("phone")
        if filters.get("department"):
            student_filters["department"] = ["like", f"%{filters.get('department')}%"]
        if filters.get("course"):
            student_filters["course"] = ["like", f"%{filters.get('course')}%"]
        if filters.get("dob"):
            student_filters["dob"] = filters.get("dob")

    # Check if DOB filter is cleared or all filters are empty
    # if "dob" not in student_filters:
    #     #Fetch all students if no filters are applied or DOB filter is cleared
    #     students = frappe.get_all("Student", fields=["*"])
    # else:
    #     # Fetch students based on filters
    # students = frappe.get_all("Student", filters=student_filters, fields=["*"])

    #     if filters.get("dob"):
    #         student_filters["dob"] = filters.get('dob')


    students = frappe.get_all("Student", filters=student_filters, fields=["*"])

    for student in students:
        marks = frappe.get_all("Marks", filters={"parent": student.name}, fields=["*"])
        if marks:
            for mark in marks:
                row = {
                    "reg_no": student.reg_no,
                    "name1": student.name1,
                    "status": student.status,
                    "gender": student.gender,
                    "email": student.email,
                    "phone": student.phone,
                    "department": student.department,
                    "course": student.course,
                    "dob": student.dob,
                    "subject_code": mark.subject_code,
                    "subject_name": mark.subject_name,
                    "mark": mark.mark,
                    "total_mark": mark.total_mark,
                    "percentage": mark.percentage
                }
                data.append(row)
        else:
            row = {
                "reg_no": student.reg_no,
                "name1": student.name1,
                "status": student.status,
                "gender": student.gender,
                "email": student.email,
                "phone": student.phone,
                "department": student.department,
                "course": student.course,
                "dob": student.dob,
                "subject_code": "",
                "subject_name": "",
                "mark": "",
                "total_mark": "",
                "percentage": ""
            }
            data.append(row)

    # Remove duplicate entries
    unique_data = []
    seen_entries = set()
    for entry in data:
        identifier = (entry['reg_no'], entry['subject_code'])
        if identifier not in seen_entries:
            unique_data.append(entry)
            seen_entries.add(identifier)

    return columns, unique_data''''''






    
# import frappe

# def execute(filters=None):
#     columns = [
#         {"label": "Registration Number", "fieldname": "reg_no", "fieldtype": "Data"},
#         {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
#         {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
#         {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
#         {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
#         {"label": "Phone", "fieldname": "phone", "fieldtype": "Data"},
#         {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
#         {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
#         {"label": "Date of Birth", "fieldname": "dob", "fieldtype": "Date"},
#         {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
#         {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
#         {"label": "Mark", "fieldname": "mark", "fieldtype": "Data"},
#         {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
#         {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
#     ]

#     data = []

#     student_filters = {}
#     if filters:
#         if filters.get("reg_no"):
#             student_filters["reg_no"] = filters.get("reg_no")
#         if filters.get("name1"):
#             student_filters["name1"] = filters.get("name1")
#         if filters.get("gender"):
#             student_filters["gender"] = filters.get("gender")
#         if filters.get("email"):
#             student_filters["email"] = filters.get("email")
#         if filters.get("phone"):
#             student_filters["phone"] = filters.get("phone")
#         if filters.get("department"):
#             student_filters["department"] = filters.get("department")
#         if filters.get("course"):
#             student_filters["course"] = filters.get("course")
#         if filters.get("dob"):
#             student_filters["dob"] = filters.get("dob")

#     students = frappe.get_all("Student", filters=student_filters, fields=["*"])

#     seen_entries = set()
#     for student in students:
#         marks = frappe.get_all("Marks", filters={"parent": student.name}, fields=["*"])
#         if marks:
#             for mark in marks:
#                 identifier = (student.reg_no, mark.subject_code)
#                 if identifier not in seen_entries:
#                     row = {
#                         "reg_no": student.reg_no,
#                         "name1": student.name1,
#                         "status": student.status,
#                         "gender": student.gender,
#                         "email": student.email,
#                         "phone": student.phone,
#                         "department": student.department,
#                         "course": student.course,
#                         "dob": student.dob,
#                         "subject_code": mark.subject_code,
#                         "subject_name": mark.subject_name,
#                         "mark": mark.mark,
#                         "total_mark": mark.total_mark,
#                         "percentage": mark.percentage
#                     }
#                     data.append(row)
#                     seen_entries.add(identifier)
#         else:
#             identifier = (student.reg_no, None)
#             if identifier not in seen_entries:
#                 row = {
#                     "reg_no": student.reg_no,
#                     "name1": student.name1,
#                     "status": student.status,
#                     "gender": student.gender,
#                     "email": student.email,
#                     "phone": student.phone,
#                     "department": student.department,
#                     "course": student.course,
#                     "dob": student.dob,
#                     "subject_code": "",
#                     "subject_name": "",
#                     "mark": "",
#                     "total_mark": "",
#                     "percentage": ""
#                 }
#                 data.append(row)
#                 seen_entries.add(identifier)

#     return columns, data

'''
# import frappe

# def execute(filters=None):
#     columns = [
#         {"label": "Registration Number", "fieldname": "reg_no", "fieldtype": "Data"},
#         {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
#         {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
#         {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
#         {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
#         {"label": "Phone", "fieldname": "phone", "fieldtype": "Data"},
#         {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
#         {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
#         {"label": "Date of Birth", "fieldname": "dob", "fieldtype": "Date"},
#         {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
#         {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
#         {"label": "Mark", "fieldname": "mark", "fieldtype": "Data"},
#         {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
#         {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
#     ]

#     data = []

#     student_filters = {}
#     if filters:
#         if filters.get("reg_no"):
#             student_filters["reg_no"] = filters.get("reg_no")
#         if filters.get("name1"):
#             student_filters["name1"] = filters.get("name1")
#         if filters.get("gender"):
#             student_filters["gender"] = filters.get("gender")
#         if filters.get("email"):
#             student_filters["email"] = filters.get("email")
#         if filters.get("phone"):
#             student_filters["phone"] = filters.get("phone")
#         if filters.get("department"):
#             student_filters["department"] = filters.get("department")
#         if filters.get("course"):
#             student_filters["course"] = filters.get("course")
#         if filters.get("dob"):
#             student_filters["dob"] = filters.get("dob")

#     students = frappe.get_all("Student", filters=student_filters, fields=["*"])

#     for student in students:
#         # Add a row for the student details
#         student_row = {
#             "reg_no": student.reg_no,
#             "name1": student.name1,
#             "status": student.status,
#             "gender": student.gender,
#             "email": student.email,
#             "phone": student.phone,
#             "department": student.department,
#             "course": student.course,
#             "dob": student.dob,
#             "subject_code": "",
#             "subject_name": "",
#             "mark": "",
#             "total_mark": "",
#             "percentage": ""
#         }
#         data.append(student_row)

#         # Add rows for each subject the student has
#         marks = frappe.get_all("Marks", filters={"parent": student.name}, fields=["*"])
#         for mark in marks:
#             subject_row = {
#                 "reg_no": "",
#                 "name1": "",
#                 "status": "",
#                 "gender": "",
#                 "email": "",
#                 "phone": "",
#                 "department": "",
#                 "course": "",
#                 "dob": "",
#                 "subject_code": mark.subject_code,
#                 "subject_name": mark.subject_name,
#                 "mark": mark.mark,
#                 "total_mark": mark.total_mark,
#                 "percentage": mark.percentage
#             }
#             data.append(subject_row)

#         # If no marks, add an empty row to show no subjects
#         if not marks:
#             empty_subject_row = {
#                 "reg_no": "",
#                 "name1": "",
#                 "status": "",
#                 "gender": "",
#                 "email": "",
#                 "phone": "",
#                 "department": "",
#                 "course": "",
#                 "dob": "",
#                 "subject_code": "",
#                 "subject_name": "",
#                 "mark": "",
#                 "total_mark": "",
#                 "percentage": ""
#             }
#             data.append(empty_subject_row)

#     return columns, data
# '''

import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": "Registration Number", "fieldname": "reg_no", "fieldtype": "Data"},
        {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
        {"label": "Phone", "fieldname": "phone", "fieldtype": "Data"},
        {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
        {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
        {"label": "Date of Birth", "fieldname": "dob", "fieldtype": "Date"},
        {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
        {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
        {"label": "Mark", "fieldname": "mark", "fieldtype": "Int"},
        {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Int"},
        {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
    ]

    data = []
    chart_data = {
        "labels": [],
        "datasets": [
            {"name": "Marks", "values": []},
            {"name": "Total Marks", "values": []}
        ]
    }

    student_filters = {}
    if filters:
        if filters.get("reg_no"):
            student_filters["reg_no"] = filters.get("reg_no")
        if filters.get("name1"):
            student_filters["name1"] = ["like", f"%{filters.get('name1')}%"]
        if filters.get("gender"):
            student_filters["gender"] = filters.get("gender")
        if filters.get("email"):
            student_filters["email"] = ["like", f"%{filters.get('email')}%"]
        if filters.get("phone"):
            student_filters["phone"] = filters.get("phone")
        if filters.get("department"):
            student_filters["department"] = ["like", f"%{filters.get('department')}%"]
        if filters.get("course"):
            student_filters["course"] = ["like", f"%{filters.get('course')}%"]
        if filters.get("dob"):
            student_filters["dob"] = filters.get("dob")

    students = frappe.get_all("Student", filters=student_filters, fields=["*"])

    for student in students:
        marks = frappe.get_all("Marks", filters={"parent": student.name}, fields=["*"])
        total_marks = 0
        total_full_marks = 0
        if marks:
            for mark in marks:
                row = {
                    "reg_no": student.reg_no,
                    "name1": student.name1,
                    "status": student.status,
                    "gender": student.gender,
                    "email": student.email,
                    "phone": student.phone,
                    "department": student.department,
                    "course": student.course,
                    "dob": student.dob,
                    "subject_code": mark.subject_code,
                    "subject_name": mark.subject_name,
                    "mark": mark.mark,
                    "total_mark": mark.total_mark,
                    "percentage": mark.percentage
                }
                data.append(row)
                total_marks += int(mark.mark)
                total_full_marks += int(mark.total_mark)
        else:
            row = {
                "reg_no": student.reg_no,
                "name1": student.name1,
                "status": student.status,
                "gender": student.gender,
                "email": student.email,
                "phone": student.phone,
                "department": student.department,
                "course": student.course,
                "dob": student.dob,
                "subject_code": "",
                "subject_name": "",
                "mark": 0,
                "total_mark": 0,
                "percentage": ""
            }
            data.append(row)

        if student.name1 not in chart_data["labels"]:
            chart_data["labels"].append(student.name1)
            chart_data["datasets"][0]["values"].append(total_marks)
            chart_data["datasets"][1]["values"].append(total_full_marks)
        else:
            index = chart_data["labels"].index(student.name1)
            chart_data["datasets"][0]["values"][index] += total_marks
            chart_data["datasets"][1]["values"][index] += total_full_marks

    # Remove duplicate entries
    unique_data = []
    seen_entries = set()
    for entry in data:
        identifier = (entry['reg_no'], entry['subject_code'])
        if identifier not in seen_entries:
            unique_data.append(entry)
            seen_entries.add(identifier)

    # Chart data format
    chart = {
        "data": {
            "labels": chart_data["labels"],
            "datasets": [
                {
                    "name": _("Marks"),
                    "values": chart_data["datasets"][0]["values"]
                },
                {
                    "name": _("Total Marks"),
                    "values": chart_data["datasets"][1]["values"]
                }
            ]
        },
        "type": 'bar'
    }

    return columns, unique_data, None, chart

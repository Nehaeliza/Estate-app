import frappe

def send_weekly_holiday_emails():
    # Get the email template
    # template = frappe.get_doc("Email Template", "Holiday Email Template")
    subject = "Dear Students"
    message = "Wishing You a great week ahead"
    print("inside the function")

    # Get all students
    students = frappe.get_all("Student", fields=["name1", "email"])

    for student in students:
        print("inside for")
        if student.email:
            try:
                # Send email
                frappe.sendmail(
                    recipients=student.email,
                    subject=subject,
                    message=message,
                    reference_doctype="Student",
                    reference_name=student.name1,
                    now=True
                )
                frappe.log_error(title="Email Sent", message=f"Email sent to {student.email}")
            except Exception as e:
                frappe.log_error(title="Email Sending Failed", message=f"Failed to send email to {student.email}: {str(e)}")

# Call the function
send_weekly_holiday_emails()
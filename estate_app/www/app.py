import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_index_html():
    return frappe.render_template("students")
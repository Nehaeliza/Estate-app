// Copyright (c) 2024, Neha Joy and contributors
// For license information, please see license.txt

frappe.query_reports["Student Report"] = {
    "filters": [
        {
            "fieldname": "reg_no",
            "label": __("Reg No."),
            "fieldtype": "Link",
			"options": "Student",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "name1",
            "label": __("Name"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "gender",
            "label": __("Gender"),
            "fieldtype": "Select",
            "options": ["","Female", "Male", "Others"],
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "email",
            "label": __("Email"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "phone",
            "label": __("Phone"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "department",
            "label": __("Department"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "course",
            "label": __("Course"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "dob",
            "label": __("DOB"),
            "fieldtype": "Date",
            "reqd": 0,
            "hidden": 0
        },
       
    ]
};

// frappe.query_reports["Your Report Name"] = {
//     onload: function(report) {
//         frappe.call({
//             method: "path.to.your.execute",
//             callback: function(r) {
//                 if (r.message) {
//                     const columns = r.message[0];
//                     const data = r.message[1];
//                     const chart_data = r.message[2];

//                     // Render your table with columns and data here
//                     // (Assuming you have a table rendering function)

//                     // Prepare data for chart
//                     const labels = chart_data.labels;
//                     const marks = chart_data.datasets[0].values;
//                     const total_marks = chart_data.datasets[1].values;

//                     const chart = new frappe.Chart("#chart", {
//                         data: {
//                             labels: labels,
//                             datasets: [
//                                 {
//                                     name: "Marks",
//                                     values: marks
//                                 },
//                                 {
//                                     name: "Total Marks",
//                                     values: total_marks
//                                 }
//                             ]
//                         },
//                         title: "Student Marks and Total Marks by Status",
//                         type: 'bar',
//                         height: 250,
//                         colors: ['#7cd6fd', '#743ee2']
//                     });
//                 }
//             }
//         });
//     }
// }

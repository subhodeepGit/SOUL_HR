frappe.query_reports["Employee wise Project and Task Report"] = {
    "filters": [
        {
            "fieldname":"employee",
            "label": __("Employee"),
            "fieldtype": "MultiSelectList",
            // "options": "Project",
            // "reqd":1,
            get_data: function(txt) {
				return frappe.db.get_link_options('Employee', txt)
			}
        },
        {
            "fieldname":"project",
            "label": __("Project"),
            "fieldtype": "MultiSelectList",
            // "options": "Project",
            // "reqd":1,
            get_data: function(txt) {
				return frappe.db.get_link_options('Project', txt)
			}
        },
        {
            "fieldname":"task",
            "label": __("Task"),
            "fieldtype": "MultiSelectList",
            "options": "Task",
            // "reqd":1,
            get_data: function(txt) {
				return frappe.db.get_link_options('Task', txt)
			},
            // get_query: function(txt) {
			// 	return {
            //         "filters" : {
            //             "project" : frappe.query_report.get_filter_value('project'),
            //         }
            //     };
			// }
        },

        {
            "fieldname":"start_date",
            "label": __("Start Date"),
            "fieldtype": "Date",
            // "reqd":1,
        },
        {
            "fieldname":"end_date",
            "label": __("End Date"),
            "fieldtype": "Date",
            // "reqd":1,
        },
    ]
}

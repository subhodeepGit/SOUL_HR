# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ProjectandTasksReport(Document):
	def validate(self):
		self.validate_years()
		# self.validate_child_date()

		
	def validate_years(self):
		duplicateForm=frappe.get_all("Project and Tasks Report", filters={
			"employee":self.employee,
			"report_for_week_starting": self.report_for_week_starting,
			"name":("!=",self.name)
		})
		if duplicateForm:
			frappe.throw(("Employee has already filled the form for this Date."))

	

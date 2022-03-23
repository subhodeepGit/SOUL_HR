# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt

class ProjectandTasksReport(Document):
	def validate(self):
		self.validate_years()
		self.calculate_total()
		# self.validate_child_date()

	def calculate_total(self):
		mon=tue=wed=thu=fri=sat=sun=0
		for d in self.get("estimation"):

			mon+=flt(d.mon)
			tue+=flt(d.tue)
			wed+=flt(d.wed)
			thu+=flt(d.thu)
			fri+=flt(d.fri)
			sat+=flt(d.sat)
			sun+=flt(d.sun)
		self.monday=mon
		self.tuesday=tue
		self.wednesday=wed
		self.thursday=thu
		self.friday=fri
		self.saturday=sat
		self.sunday=sun
		self.total=mon + tue + wed + thu + fri + sat + sun

		
	def validate_years(self):
		duplicateForm=frappe.get_all("Project and Tasks Report", filters={
			"employee":self.employee,
			"report_for_week_starting": self.report_for_week_starting,
			"name":("!=",self.name)
		})
		if duplicateForm:
			frappe.throw(("Employee has already filled the form for this Date."))
	

@frappe.whitelist()
def get_employees(user=None):
	if user!="Administrator":
		p = frappe.db.get_all("Employee",filters={"user_id":user})
		p=p[0]
	else:
		p = frappe.db.get_all("Employee")
	return p

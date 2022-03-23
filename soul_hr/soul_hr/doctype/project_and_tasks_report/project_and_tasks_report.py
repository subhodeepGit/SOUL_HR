# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.db_query import get_date_range
from frappe.model.document import Document
from frappe.utils import flt
from frappe.utils.data import getdate


class ProjectandTasksReport(Document):
	def validate(self):
		self.calculate_totals()
		# self.validate_years()
		self.validate_dates()
		duplicate_row_validation(self, "estimation", ['project','tasks'])
	def on_submit(self):
		self.calculate_total()
	def validate_dates(self):
			if self.report_for_week_starting and getdate(self.report_for_week_starting) >= getdate():
				frappe.throw(frappe._("Submission Date cannot be greater than today's date."))

	def calculate_totals(self):
		mon=tue=wed=thu=fri=sat=sun=0
		for d in self.get("estimation"):

			mon+=flt(d.mon)
			tue+=flt(d.tue)
			wed+=flt(d.wed)
			thu+=flt(d.thu)
			fri+=flt(d.fri)
			sat+=flt(d.sat)
			sun+=flt(d.sun)
		error=[]
		self.monday=mon
		if self.monday>24:
			error.append("Monday")
			# frappe.throw("Yor have worked less than 8 hrs on Monday")
		self.tuesday=tue
		if self.tuesday>24:
			error.append("Tuesday")
			# frappe.throw("Yor have worked less than 8 hrs on Tuesday")
		self.wednesday=wed
		if self.wednesday>24:
			error.append("Wednesday")
			# frappe.throw("Yor have worked less than 8 hrs on Wednesday")
		self.thursday=thu
		if self.thursday>24:
			error.append("Thursday")
			# frappe.throw("Yor have worked less than 8 hrs on Thursday")
		self.friday=fri
		if self.friday>24:
			error.append("Friday")
		a=""
		len_of_list=len(error)
		b=1
		for t in error:
			if b==len_of_list and b!=1:
				a=a+" and "+t+"."
			elif b==len_of_list and b==1:
				a=t+" ."
			elif b==1:
				b=b+1
				a=t
			else:
				b=b+1
				a=a+", "+t	
		if len_of_list !=0:
			frappe.throw("Yor have worked more than 24 hrs on "+a)	
		self.saturday=sat
		self.sunday=sun
		self.total=mon + tue + wed + thu + fri + sat + sun
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
		error=[]
		self.monday=mon
		if self.monday<8:
			error.append("Monday")
			# frappe.throw("Yor have worked less than 8 hrs on Monday")
		self.tuesday=tue
		if self.tuesday<8:
			error.append("Tuesday")
			# frappe.throw("Yor have worked less than 8 hrs on Tuesday")
		self.wednesday=wed
		if self.wednesday<8:
			error.append("Wednesday")
			# frappe.throw("Yor have worked less than 8 hrs on Wednesday")
		self.thursday=thu
		if self.thursday<8:
			error.append("Thursday")
			# frappe.throw("Yor have worked less than 8 hrs on Thursday")
		self.friday=fri
		if self.friday<8:
			error.append("Friday")
		# 	frappe.throw("Yor have worked less than 8 hrs on Friday")	
		# error=["Monday","Tuesday","sat"]
		a=""
		len_of_list=len(error)
		b=1
		for t in error:
			if b==len_of_list and b!=1:
				a=a+" and "+t+"."
			elif b==len_of_list and b==1:
				a=t+" ."
			elif b==1:
				b=b+1
				a=t
			else:
				b=b+1
				a=a+", "+t	
		if len_of_list !=0:
			frappe.throw("Yor have worked less than 8 hrs on "+a)	

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

def duplicate_row_validation(doc,table_field_name,comapre_fields):
	print("ok")
	row_names=[]
	for row in doc.get(table_field_name):
		row_names.append(row.name)

	for row in doc.get(table_field_name):
		filters={"parent":row.parent,"idx":("!=",row.idx)}
		for field in comapre_fields:
			filters[field]=row.get(field)
		for duplicate in frappe.get_all(row.doctype,filters,['idx','name']):
			if duplicate.name in row_names:
				frappe.throw("#Row {0} Duplicate values in <b>{1}</b> Not Allowed".format(duplicate.idx, table_field_name))
# @frappe.whitelist()

# def before_save(self):
# 	icr_id = self.tasks
# 	in_doc_info=frappe.db.sql("""select * from `tabProject and Tasks Estimation Table` where  tasks="%s" """%(icr_id))
# 	print("\n\n\n\n\n")
# 	print(in_doc_info)
# 	if len(in_doc_info)!=0:
# 		icr = frappe.get_doc("Project and Tasks Estimation Table",icr_id)
# 		stu_df = pd.DataFrame({
# 			'Al_no':[]
# 		})
# 		for al in icr.student:
# 			s = pd.Series([al.tasks],index = ['Al_no'])
# 			stu_df = stu_df.append(s,ignore_index = True)
# 		if len(stu_df)!=0:
# 			duplicate = stu_df[stu_df.duplicated()].reset_index()
# 			if len(duplicate) == 0:
# 				pass
# 			else:
# 				b=""
# 				for t in range(len(duplicate)):
# 					a="%s  "%(duplicate['Al_no'][t])
# 					b=b+a
# 				frappe.throw("Duplicate Tasks are not allowed "+b)
# 		else:
# 			pass
################################################

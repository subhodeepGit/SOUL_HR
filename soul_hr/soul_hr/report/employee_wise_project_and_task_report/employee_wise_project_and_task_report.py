# Copyright (c) 2023, SOUL and contributors
# For license information, please see license.txt

from dataclasses import field
import frappe
from frappe import _

def execute(filters=None):
    data=get_data(filters)
    get_columns_info=get_columns()
    return  get_columns_info,data

def get_data(filters):
    print("\n\n\n\n")
    employee = filters.get('employee')
    project = filters.get('project')
    task = filters.get('task')
    start_date = filters.get('start_date')
    end_date = filters.get('end_date')

    data = frappe.get_all("Project and Tasks Report", filters=[["employee","in",tuple(employee)], 
                                                               ["report_for_week_starting", "between", [start_date,end_date]],["workflow_state","in", ["Sent for Approval","Approved"]]],
                                                                              fields = ["name", "employee", "employee_name", "report_for_week_starting"])

    final_data=[]
    for t in data:
        flag_dict={}
        child_data = frappe.get_all("Project and Tasks Estimation Table", {"parent":t["name"],"project":project,"tasks":task},
                                    ["parent","project","project_name","tasks","task_name","task_description","total"])
        for j in child_data:
            flag_dict['name']=t['name']
            flag_dict['employee']=t['employee']
            flag_dict['employee_name']=t['employee_name']
            flag_dict['report_for_week_starting']=t['report_for_week_starting']
            flag_dict['parent']=j["parent"]
            flag_dict['project']=j["project"]
            flag_dict['project_name']=j["project_name"]
            flag_dict['tasks']=j["tasks"]
            flag_dict['task_name']=j["task_name"]
            flag_dict['task_description']=j["task_description"]
            flag_dict['total']=j["total"]
            final_data.append(flag_dict)
    return final_data

def get_columns():
    columns = [
        {
            "label": _("Project and Task ID"),
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Project and Tasks Report",
            "width":145
        },
        {
            "label": _("Employee"),
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width":250,
        },
        {
            "label": _("Week Starting Date"),
            "fieldname": "report_for_week_starting",
            "fieldtype": "Date",
            "width":145
        },
        # {
        # 	"label": _("Employee Name"),
        # 	"fieldname": "employee_name",
        # 	"fieldtype": "Link",
        # 	"options": "Employee",
        # 	"width":180
        # },
        {
            "label": _("Project"),
            "fieldname": "project",
            "fieldtype": "Data",
            "width":120
        },
        {
            "label": _("Project Name"),
            "fieldname": "project_name",
            "fieldtype": "Data",
            "width":120
        },
        {
            "label": _("Task"),
            "fieldname": "tasks",
            "fieldtype": "Data",
            "width":120
        },
        {
            "label": _("Task Name"),
            "fieldname": "task_name",
            "fieldtype": "Data",
            "width":120
        },
        {
            "label": _("Task Description"),
            "fieldname": "task_description",
            "fieldtype": "Data",
            "width":500
        },
        {
            "label": _("Total Hours"),
            "fieldname": "total",
            "fieldtype": "Data",
            "width":100
        },
    ]
    return columns
# Copyright (c) 2023, SOUL and contributors
# For license information, please see license.txt

from dataclasses import field
import frappe
from frappe import _
from operator import itemgetter

def execute(filters=None):
    data=get_data(filters)
    get_columns_info=get_columns()
    return  get_columns_info,data

def get_data(filters=None):
    employee = filters.get('employee')
    project = filters.get('project')
    task = filters.get('task')
    start_date = filters.get('start_date')
    end_date = filters.get('end_date')

    filt=[]
    if employee:
        filt.append(["employee","in",tuple(employee)])
    if start_date and end_date:
       filt.append(["report_for_week_starting", "between", [start_date,end_date]])     
    filt.append(["workflow_state","in", ["Sent for Approval","Approved"]])


    data = frappe.get_all("Project and Tasks Report", filters=filt,fields = ["name", "employee", "employee_name", "report_for_week_starting"])


    final_data=[]
    for t in data:
        flag_dict={}
        filter=[]
        filter.append(["parent","=",t["name"]])
        if project:
            filter.append(["project","in",tuple(project)])
        if task:
            filter.append(["tasks","in",tuple(task)])      
        child_data = frappe.get_all("Project and Tasks Estimation Table", filters=filter,
                            fields = ["parent","project","project_name","tasks","task_name","task_description","total"])

        for j in child_data:
            flag_dict['employee']=t['employee']
            flag_dict['employee_name']=t['employee_name']
            flag_dict['report_for_week_starting']=t['report_for_week_starting']
            flag_dict['parent']=j["parent"]
            flag_dict['project']=j["project"]
            flag_dict['project_name']=j["project_name"]
            flag_dict['tasks']=j["tasks"]
            flag_dict['task_name']=j["task_name"]
            flag_dict['total']=j["total"]
            temp = []
            res = dict()
        
            for key, val in flag_dict.items():
            
                if val not in temp:
                    temp.append(val)
                    res[key] = val
            final_data.append(res)

            
    sorted_final_data = (sorted(final_data, key=itemgetter('project', 'tasks')))
    return sorted_final_data

def get_columns():
    columns = [
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
        {
            "label": _("Project"),
            "fieldname": "project",
            "fieldtype": "Data",
            "width":150
        },
        {
            "label": _("Project Name"),
            "fieldname": "project_name",
            "fieldtype": "Data",
            "width":160
        },
        {
            "label": _("Task"),
            "fieldname": "tasks",
            "fieldtype": "Data",
            "width":150
        },
        {
            "label": _("Task Name"),
            "fieldname": "task_name",
            "fieldtype": "Data",
            "width":160
        },
        {
            "label": _("Total Hours"),
            "fieldname": "total",
            "fieldtype": "Data",
            "width":180
        },        # {
        #     "label": _("Task Description"),
        #     "fieldname": "task_description",
        #     "fieldtype": "Data",
        #     "width":500
        # },
    ]
    return columns
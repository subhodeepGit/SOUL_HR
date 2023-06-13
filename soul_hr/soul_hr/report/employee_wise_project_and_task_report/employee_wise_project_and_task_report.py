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
    # print("\n\n\n\n")
    employee = filters.get('employee')
    # print("employee : ",employee)
    project = filters.get('project')
    # print("project : ",project)
    task = filters.get('task')
    # print("task : ",task)
    start_date = filters.get('start_date')
    end_date = filters.get('end_date')

    filt=[]
    if employee == [] and project == [] and task == [] and start_date == [] and end_date == []:
        data = frappe.get_all("Project and Tasks Report", filters=[["workflow_state","in", ["Sent for Approval","Approved"]]],
                                                                             fields = ["name", "employee", "employee_name", "report_for_week_starting"])
    else:

        data = frappe.get_all("Project and Tasks Report", filters=[["employee","in",tuple(employee)], 
                                                               ["report_for_week_starting", "between", [start_date,end_date]],["workflow_state","in", ["Sent for Approval","Approved"]]],
                                                                              fields = ["name", "employee", "employee_name", "report_for_week_starting"])
    # print("parent_data: ",data)

    final_data=[]
    for t in data:
        flag_dict={}
        # child_data = frappe.get_all("Project and Tasks Estimation Table", {"parent":t["name"],"project":project,"tasks":task},
        #                             ["parent","project","project_name","tasks","task_name","task_description","total"])

        # if employee == []:
        #     print("ok")
        #     child_data = frappe.get_all("Project and Tasks Estimation Table", filters=[["project","in",tuple(project)],["tasks","in",tuple(task)]],
        #                     fields = ["parent","project","project_name","tasks","task_name","task_description","total"])
        # else:
        child_data = frappe.get_all("Project and Tasks Estimation Table", filters=[["parent","=",t["name"]],["project","in",tuple(project)],["tasks","in",tuple(task)]],
                            fields = ["parent","project","project_name","tasks","task_name","task_description","total"])
        # child_data = frappe.db.sql("""SELECT `parent`,`project`,`project_name`,`tasks`,`task_name`,`task_description` FROM `tabProject and Tasks Estimation Table` 
        #                             WHERE (`parent` = %s) AND (`project` in %s) AND (`tasks` in %s)"""%(t["name"],str(tuple(project)),str(tuple(task))))
        

        # print("child_data: ", child_data, "\n")

        for j in child_data:
            # flag_dict['name']=t['name']
            flag_dict['employee']=t['employee']
            flag_dict['employee_name']=t['employee_name']
            flag_dict['report_for_week_starting']=t['report_for_week_starting']
            flag_dict['parent']=j["parent"]
            flag_dict['project']=j["project"]
            flag_dict['project_name']=j["project_name"]
            flag_dict['tasks']=j["tasks"]
            flag_dict['task_name']=j["task_name"]
            # flag_dict['task_description']=j["task_description"]
            flag_dict['total']=j["total"]
            temp = []
            res = dict()
        
            for key, val in flag_dict.items():
            
                if val not in temp:
                    temp.append(val)
                    res[key] = val
            final_data.append(res)

            
    sorted_final_data = (sorted(final_data, key=itemgetter('project', 'tasks')))
    # print("final_data: ",sorted_final_data)
    return sorted_final_data

def get_columns():
    columns = [
        # {
        #     "label": _("Project and Task ID"),
        #     "fieldname": "name",
        #     "fieldtype": "Link",
        #     "options": "Project and Tasks Report",
        #     "width":145
        # },
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
            "width":150
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
            "width":150
        },
        # {
        #     "label": _("Task Description"),
        #     "fieldname": "task_description",
        #     "fieldtype": "Data",
        #     "width":500
        # },
        {
            "label": _("Total Hours"),
            "fieldname": "total",
            "fieldtype": "Data",
            "width":100
        },
    ]
    return columns
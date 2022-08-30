from warnings import filters
import frappe
import string
import random
from re import L
from frappe.utils.data import format_date
from frappe.utils import get_url_to_form
from frappe.utils import cint, cstr, parse_addr
from frappe.utils import getdate
from datetime import datetime, timedelta


def all():
    pass

def cron():
    now = datetime.now()
    # monday = now - timedelta(days = now.weekday())
    # monday_date=monday.date()
    last_monday = now - timedelta(days=now.weekday(), weeks=1)
    last_monday_date = last_monday.date()
    project_and_task = frappe.get_all("Project and Tasks Report",{'report_for_week_starting':last_monday_date,'docstatus':1},["employee","employee_name","email"])
    all_employees = frappe.get_all("Employee")

    project_and_task_name=[t["employee"] for t in project_and_task]
    all_employees_name=[t["name"] for t in all_employees]

    l_func = lambda x, y: list((set(x)- set(y)))
    non_match = l_func(all_employees_name, project_and_task_name)
    # print(non_match)
    employee_non_match = frappe.get_all("Employee",filters=[['name',"in",tuple(non_match)]],fields=["prefered_email"])
    email_non_match_email=[t["prefered_email"] for t in employee_non_match]

    msg="""<p>You have not <b>submitted</b> the <b>Project and Tasks Report</b> for last week. Kindly submit the Report as soon as possible.</p><br>"""

    if len(email_non_match_email)!=0:
        send_mail(email_non_match_email,'Reminder to Submit Project and Tasks Report',msg)

    # print("\n\n\n\n")
    # print(email_non_match_email)
    # print("\n\n\n\n")
    # print(last_monday_date)
    # print("\n\n\n\n")
    # print(project_and_task_name)
    # print("\n\n\n\n")
    # print(all_employees_name)
    # print("\n\n\n\n")
    # print(non_match)
    # print("\n\n\n\n")
    


def send_mail(recipients,subject,message):
    if has_default_email_acc():
        frappe.sendmail(recipients=recipients,subject=subject,message=message,with_container=True)

def has_default_email_acc():
    for d in frappe.get_all("Email Account", {"default_outgoing":1}):
        return "true"
    return ""
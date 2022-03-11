from re import L
import frappe
from frappe.utils.data import format_date
from frappe.utils import get_url_to_form
from frappe.utils import cint, cstr, parse_addr


def interview_schedule_cleared(doc):
    msg="""<p>Greetings <b>{0} !!</b> </p>""".format(doc.get('job_applicant'))
    msg+="""<p>You have been selected for the {0}</p>""".format(doc.get('job_opening'))
    
    msg+="""<b>Status:</b> {0}<br>""".format(doc.get('status'))
    msg+="""<p>Further Process will be informed!!</p>"""
    send_mail(frappe.db.get_value("Job Applicant",doc.get('job_applicant'),"email_id"),'Application Status',msg)

def interview_schedule_rejected(doc):
    msg="""<p>Hello <b>{0} !!</b> </p>""".format(doc.get('job_applicant'))
    msg+="""<p>You have not been selected for the further round!!</p>"""
    msg+="""<p>Better Luck Next Time...</p>"""
    
    send_mail(frappe.db.get_value("Job Applicant",doc.get('job_applicant'),"email_id"),'Application Status',msg)  

def interview_schedule_under_review(doc):
    msg="""<p>Greetings <b>{0} !!</b> </p>""".format(doc.get('job_applicant'))
    msg+="""<p>Your Job Application is Currently <b>Under Review!!</b></p>"""
    msg+="""<p>Status will be updated soon.</p>"""
    msg+="""<b>Current Status:</b> {0}<br>""".format(doc.get('status'))
    
    send_mail(frappe.db.get_value("Job Applicant",doc.get('job_applicant'),"email_id"),'Application Status',msg)
def interview_schedule_pending(doc):
    msg="""<p>Greetings <b>{0} !!</b> </p>""".format(doc.get('job_applicant'))
    msg+="""<p>You have been selected for the further round!!</p>"""
    msg+="""<b>---------------------Interview Schedule---------------------</b><br>"""
    msg+="""<b>Interview Round:</b> {0}<br>""".format(doc.get('interview_round'))
    msg+="""<b>Schedule Date:</b> {0}<br>""".format(doc.get('scheduled_on'))
    msg+="""<b>Time:</b> {0}<br>""".format(doc.get('from_time'))
    
    send_mail(frappe.db.get_value("Job Applicant",doc.get('job_applicant'),"email_id"),'Application Status',msg)

def job_offer_awaiting_response(doc):
    sub = "Job Offer for {0}".format(doc.designation)
    msg="""<p>Greetings <b>{0} !!</b> </p>""".format(doc.get('applicant_name'))
    msg+="""<p>We are pleased to inform you that, you are now eligible to join us as a {0} </p>""".format(doc.designation)
    msg+="""<p>We are offering you with a Job Offer</p>"""
    msg+="""<p>Job Offer Terms: </p>"""
    msg += """</u></b></p><table class='table table-bordered'><tr>
        <th>Offer Term</th><th>Value / Description</th>"""
    for d in doc.get("offer_terms"):
        msg += "<tr><td>" + """{0}""".format(str(d.get('offer_term'))) + "</td><td>" + str(d.get('value')) + "</td></tr>" 
    msg += "</table>"
    msg+="""<b>Terms and Conditions:</b> {0}<br>""".format(doc.get('terms'))

    send_mail(frappe.db.get_value("Job Applicant",doc.get('job_applicant'),"email_id"),sub,msg)

def job_offer_accepted(doc):
    sub = "Welcome to {0}".format(doc.company)
    msg="""<p>Congratulation <b>{0} !!</b> </p>""".format(doc.get('applicant_name'))
    msg+="""<p>Now you are a part of our family.. </p>"""
    msg+="""<p>Looking forward for your joining, appointment letter will be shared soon.</p>"""
    msg+="""<p>Thank You</p>"""
     

    send_mail(frappe.db.get_value("Job Applicant",doc.get('job_applicant'),"email_id"),sub,msg)


def employee_creation(doc):
    sub = "Welcome to {0}".format(doc.company)
    msg="""<p>Your Employee Profile is created. </p>"""
    msg+="""<b>---------------------Employee Details---------------------</b><br>"""
    msg+="""<p>Employee Id: <b>{0}</b> </p>""".format(doc.get('employee'))
    msg+="""<p>Email: <b>{0} </b> </p>""".format(doc.get('user_id'))     
    msg+="""<p>Password:<b>demo@123</b></p>"""
    msg+="""<p><b>Note:</b> The Email Id provided is your official mail id and Password given is for one time use, kindly change ASAP.</p>"""
    msg+="""<p>Thank You</p>"""

    send_mail(frappe.db.get_value("Employee",doc.get('employee'),"personal_email"),sub,msg)

def send_mail(recipients,subject,message):
    if has_default_email_acc():
        frappe.sendmail(recipients=recipients,subject=subject,message = message)
    
def has_default_email_acc():
    for d in frappe.get_all("Email Account", {"default_outgoing":1}):
       return "true"
    return ""
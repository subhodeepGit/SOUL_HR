import frappe
from frappe import _
from frappe.utils import (
	add_days,
	cint,
	cstr,
	date_diff,
	flt,
	formatdate,
	get_fullname,
	get_link_to_form,
	getdate,
	nowdate,
)

def on_update(self, method):
	if self.status == "Open" and self.docstatus < 1:
		# notify leave approver about creation
		if frappe.db.get_single_value("HR Settings", "send_leave_notification"):
			notify_leave_approver(self)
			notify_employee_hr(self)

def validate(self,method):
	hr(self)
def on_submit(self, method):
	if frappe.db.get_single_value("HR Settings", "send_leave_notification"):
			notify_employee(self)
			notify_leave_approver_hr(self)

def hr(self):
		email = frappe.db.get_single_value('HR Email Settings', 'hr_email')
		self.set("hr_email",email)

def notify_employee_hr(self):
		parent_doc = frappe.get_doc('Leave Application', self.name)
		args = parent_doc.as_dict()

		template = frappe.db.get_single_value('HR Settings', 'leave_status_notification_template')
		if not template:
			frappe.msgprint(_("Please set default template for Leave Status Notification in HR Settings."))
			return
		email_template = frappe.get_doc("Email Template", template)
		message = frappe.render_template(email_template.response, args)

		self.notify({
			# for post in messages
			"message": message,
			"message_to": self.hr_email,
			# for email
			"subject": email_template.subject,
			"notify": "employee"
		})

def notify_employee(self):
		parent_doc = frappe.get_doc('Leave Application', self.name)
		args = parent_doc.as_dict()

		template = frappe.db.get_single_value('HR Settings', 'leave_status_notification_template')
		if not template:
			frappe.msgprint(_("Please set default template for Leave Status Notification in HR Settings."))
			return
		email_template = frappe.get_doc("Email Template", template)
		message = frappe.render_template(email_template.response, args)

		self.notify({
			# for post in messages
			"message": message,
			"message_to": self.leave_approver,
			# for email
			"subject": email_template.subject,
			"notify": "employee"
		})

def notify_leave_approver_hr(self):
		parent_doc = frappe.get_doc('Leave Application', self.name)
		args = parent_doc.as_dict()

		template = frappe.db.get_single_value('HR Settings', 'leave_approval_notification_template')
		if not template:
			frappe.msgprint(_("Please set default template for Leave Approval Notification in HR Settings."))
			return
		email_template = frappe.get_doc("Email Template", template)
		message = frappe.render_template(email_template.response, args)

		notify(self,{
			# for post in messages
			"message": message,
			"message_to": self.hr_email,
			# for email
			"subject": email_template.subject,
			"notify": "employee"
		})

def notify_leave_approver(self):
		employee = frappe.get_doc("Employee", self.employee)
		if not employee.user_id:
			return

		parent_doc = frappe.get_doc('Leave Application', self.name)
		args = parent_doc.as_dict()

		template = frappe.db.get_single_value('HR Settings', 'leave_approval_notification_template')
		if not template:
			frappe.msgprint(_("Please set default template for Leave Approval Notification in HR Settings."))
			return
		email_template = frappe.get_doc("Email Template", template)
		message = frappe.render_template(email_template.response, args)

		notify(self,{
			# for post in messages
			"message": message,
			"message_to": employee.user_id,
			# for email
			"subject": email_template.subject,
			"notify": "employee"
		})

def notify(self, args):
	args = frappe._dict(args)
	# args -> message, message_to, subject
	if (self.follow_via_email):
		contact = args.message_to
		if not isinstance(contact, list):
			if not args.notify == "employee":
				contact = frappe.get_doc('User', contact).email or contact

		sender      	    = dict()
		sender['email']     = frappe.get_doc('User', frappe.session.user).email
		sender['full_name'] = get_fullname(sender['email'])

		try:
			frappe.sendmail(
				recipients = contact,
				sender = sender['email'],
				subject = args.subject,
				message = args.message,
			)
			frappe.msgprint(_("Email sent to {0}").format(contact))
		except frappe.OutgoingEmailError:
			pass            
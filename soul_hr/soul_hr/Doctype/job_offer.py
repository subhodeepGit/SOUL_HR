import frappe
from soul_hr.soul_hr.notification.custom_notification import job_offer_awaiting_response,job_offer_accepted

def before_save(self):
        if self.status=="Awaiting Response":
                job_offer_awaiting_response(self)
        elif self.status=="Accepted":
            job_offer_accepted(self)
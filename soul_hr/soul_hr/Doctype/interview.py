import frappe
from soul_hr.soul_hr.notification.custom_notification import interview_schedule_cleared,interview_schedule_rejected,interview_schedule_under_review,interview_schedule_pending

def before_save(self,method):
            if self.status=="Pending":
                interview_schedule_pending(self)
            elif self.status=="Under Review":
                interview_schedule_under_review(self)
            elif self.status=="Cleared":
                interview_schedule_cleared(self)
            elif self.status=="Rejected":
                interview_schedule_rejected(self)
            else:
                interview_schedule_rejected(self)
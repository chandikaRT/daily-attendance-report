import frappe
import json

from frappe.utils import nowdate, add_days, today

def sendmail():

	# send previous date
	email = frappe.get_doc("Auto Email Report","Daily Attendance")
	
	filters = json.loads(email.filters)
	
	filters.update({"date":add_days(today(),-1)})

	email.filters = json.dumps(filters)
	email.send()

	# send now date
	filters.update({"date":today()})

	email.filters = json.dumps(filters)
	
	email.save(ignore_permissions=True)
	
	email.send()
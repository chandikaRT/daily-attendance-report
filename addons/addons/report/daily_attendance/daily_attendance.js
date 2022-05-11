// Copyright (c) 2016, DAS and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.query_reports["Daily Attendance"] = {
	"filters": [
		{
			"fieldname":"date",
			"label": __("Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.nowdate()
		}
	]
}
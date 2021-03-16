// Copyright (c) 2016, Ruturaj Patil and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales Invoice datewise report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": "From Date",
			"mandatory": 1,
			"wildcard_filter": 0
		   },
		   {
			"fieldname": "to_date",
			"fieldtype": "Date",
			"label": "To Date",
			"mandatory": 1,
			"wildcard_filter": 0
		   }
	]
};

// Copyright (c) 2016, Ruturaj Patil and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Quotation datewise Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"fieldtype": "Date",
			"lable": "From Date",
			"mandatory": 1,
			"wildcard_filter": 0
		},
		{
			"fieldname": "from_shift",
			"fieldtype": "Select",
			"label": "Shift",
			"mandatory": 1,
			"options": "Morning\nEvening",
			"wildcard_filter": 0
		},
		{
			"fieldname": "to_date",
			"fieldtype": "Date",
			"lable": "To Date",
			"mandatory": 1,
			"wildcard_filter": 0
		},
		{
			"fieldname": "to_shift",
			"fieldtype": "Select",
			"label": "Shift",
			"mandatory": 1,
			"options": "Morning\nEvening",
			"wildcard_filter": 0
		}

	]
};

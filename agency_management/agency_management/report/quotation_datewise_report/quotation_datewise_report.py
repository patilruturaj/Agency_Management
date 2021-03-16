# Copyright (c) 2013, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate

def execute(filters=None):
	print(filters)
	from_date=getdate(filters.from_date).strftime("%d-%m-%Y")
	to_date=getdate(filters.to_date).strftime("%d-%m-%Y")

	get_data=frappe.db.get_all("Quotation", ["quotation_to","customer_name","transaction_date","valid_till","contact_mobile","total","total_taxes_and_charges","grand_total"],filters={"transaction_date":["between",[filters.from_date,filters.to_date]],"docstatus":1})
	print("\n\n\n",get_data,"\n\n\n\n\n")

	print(from_date,to_date)

	columns, data = [], []
	columns = [
		{
		"fieldname": "quotation_to",
		"fieldtype": "Data",
		"label": "Quotation to",
		"width": 0
		},
		{
		"fieldname": "customer_name",
		"fieldtype": "Data",
		"label": "Customer",
		"width": 0
		},
		{
		"fieldname": "transaction_date",
		"fieldtype": "Date",
		"label": "Transaction Date",
		"width": 0
		},
		{
		"fieldname": "vaild_till",
		"fieldtype": "Date",
		"label": "Valid Till",
		"width": 0
		},
		{
		"fieldname": "contact_mobile",
		"fieldtype": "Data",
		"label": "Mobile No",
		"width": 0
		},
		{
		"fieldname": "total",
		"fieldtype": "Currency",
		"label": "Total Item Price",
		"width": 0
		},
		{
		"fieldname": "total_taxes_and_charges",
		"fieldtype": "Currency",
		"label": "Tax",
		"width": 0
		},
		{
		"fieldname": "grand_total",
		"fieldtype": "Currency",
		"label": "Grand Total",
		"width": 0
		}
		]
	data.extend(get_data)
	return columns, data

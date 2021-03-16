# Copyright (c) 2013, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate

def execute(filters=None):
	# print("\n\n\n",filters,"\n\n\n\n")
	# from_date=frappe.utils.getdate(filters.from_date).strftime("%d-%m-%Y")
	# todo_date=frappe.utils.getdate(filters.to_date).strftime("%d-%m-%Y")
	
	# print(from_date)
	# print(todo_date)
	
	get_data=frappe.db.get_all('Sales Invoice', ['customer', 'posting_date','total','total_taxes_and_charges','grand_total'], filters={"posting_date":["between",[filters.from_date,filters.to_date]],"docstatus":1})
	# get_data=frappe.db.sql("SELECT customer,posting_date,total,total_taxes_and_charges,grand_total FROM `tabSales Invoice` WHERE posting_date BETWEEN {} AND {}".format(filters.from_date,filters.to_date))
	print(get_data)
	data = []
	columns=[
		{
		"fieldname": "customer",
		"fieldtype": "Data",
		"label": "Customer",
		"width": 0
		},
		{
		"fieldname": "posting_date",
		"fieldtype": "Date",
		"label": "Posting Date",
		"width": 0
		},
		{
		"fieldname": "total",
		"fieldtype": "Currency",
		"label": "Total",
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
	
	print("\n\n\n\n\n\n\n",columns,data,"\n\n\n\n\n\n")
	return columns,data

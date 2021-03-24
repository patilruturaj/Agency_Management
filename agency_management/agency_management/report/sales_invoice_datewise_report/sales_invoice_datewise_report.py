# Copyright (c) 2013, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate


def execute(filters=None):
	""" The Sales Invoice datewise report is user to create report of sales invoces.
		Using this report we can create report of sales invoice created betwwen date and submitted sales invoices.
	"""
    get_data = frappe.db.get_all('Sales Invoice', ['customer', 'posting_date', 'total', 'total_taxes_and_charges', 'grand_total'], filters={
                                 "posting_date": ["between", [filters.from_date, filters.to_date]], "docstatus": 1})
    print(get_data)
    data = []
    columns = [
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

    print("\n\n\n\n\n\n\n", columns, data, "\n\n\n\n\n\n")
    return columns, data

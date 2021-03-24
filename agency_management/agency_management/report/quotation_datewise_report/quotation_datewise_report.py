# Copyright (c) 2013, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate


def execute(filters=None):
    from_date = getdate(filters.from_date).strftime("%d-%m-%Y")
    to_date = getdate(filters.to_date).strftime("%d-%m-%Y")
    if (filters.from_date == filters.to_date):
        frappe.throw("Both dates must be different")
    elif (filters.from_date > filters.to_date):
        frappe.throw("From date is befor To date, Please try again...")

    """ The following sql query is used to filter data between two dates and and shift"""

    get_data = frappe.db.sql("""SELECT quotation_to, customer_name, transaction_date, shift, valid_till, contact_mobile, total, total_taxes_and_charges, grand_total FROM `tabQuotation`
                                    WHERE transaction_date='{}' AND shift IN('{}','Evening') AND docstatus=1
                            UNION SELECT quotation_to, customer_name, transaction_date, shift, valid_till, contact_mobile, total, total_taxes_and_charges, grand_total FROM `tabQuotation`
                                    WHERE transaction_date>'{}' AND  transaction_date<'{}' AND docstatus=1
                            UNION SELECT quotation_to, customer_name, transaction_date, shift, valid_till, contact_mobile, total, total_taxes_and_charges, grand_total FROM `tabQuotation`
                                    WHERE transaction_date='{}' AND shift IN('Morning','{}') AND docstatus=1
                            """.format(filters.from_date, filters.from_shift, filters.from_date, filters.to_date, filters.to_date, filters.to_shift))

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
            "fieldname": "shift",
            "fieldtype": "Data",
            "label": "Shift",
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

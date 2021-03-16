# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class UserRegistration(Document):
	def on_update(self):
		if self.status=="Opportunity":
			self.create_new_opportunity()
		elif self.status=="Customer":
			self.create_new_customer()
	def before_insert(self):
		lead_info=frappe.db.exists({"doctype":"Lead","email_id":self.email_id})

		print(self.docstatus)
		print("\n\n\n Befor save\n\n\n")
		self.create_new_user()
		print("\n\n\n After User Creation\n\n\n")
		if self.status=="Lead":
			self.create_new_lead()
		elif self.status=="Opportunity":
			self.create_new_opportunity()
		elif self.status=="Customer":
			self.create_new_customer()

	def create_new_user(self):
		validate_mail_id_is_unique(self.email_id)
		user_password=self.first_name+"@123"
		print("\n\n\n"+user_password+"\n\n\n")
		new_user=frappe.get_doc({
			"doctype":"User",
			"email":self.email_id,
			"first_name":self.first_name,
			"send_welcome_email":0,
			"new_password":user_password
		})
		new_user.insert()
		print("\n\n\n User Created \n\n\n")
		send_welcome_email(self.email_id,self.first_name,user_password)
		# frappe.throw("User is created")

	def create_new_lead(self):
		personal_name=self.first_name+" "+self.last_name
		print("\n\n\n"+personal_name+"\n\n\n")
		new_lead=frappe.get_doc({
			"doctype":"Lead",
			"salutation":self.salutation,
			"lead_name":personal_name,
			"status":"Lead",
			"gender":self.gender,
			"email_id":self.email_id,
			"mobile_no":self.mobile_no,
			"address_line1":self.address_line1,
			"address_line2":self.address_line2,
			"city":self.city,
			"state":self.state,
			"county":self.country
		})
		new_lead.insert()
		print("\n\n\n Lead Created \n\n\n")
		# frappe.throw("Lead is created")
	
	def create_new_opportunity(self):
		lead_info=frappe.db.exists({"doctype":"Lead","email_id":self.email_id})
		print(lead_info,type(lead_info))
		if len(lead_info)!=1:
			self.create_new_lead()
		lead_info=frappe.db.exists({"doctype":"Lead","email_id":self.email_id})
		opportunity_info=frappe.db.exists({
			"doctype":"Opportunity",
			"party_name":lead_info[0][0]
		})
		if type(opportunity_info)==None or len(opportunity_info)==0:
			print("creating opportinity for existing lead")
			create_opportunity=frappe.get_doc({
				"doctype":"Opportunity",
				"opportunity_from":"Lead",
				 "party_name":lead_info[0][0]
			})
			create_opportunity.insert()
			frappe.msgprint("Opportunity is created...")



	def create_new_customer(self):
		lead_info=frappe.db.exists({
			"doctype":"Lead"
			,"email_id":self.email_id
		})
		if len(lead_info)!=1:
			self.create_new_lead()
		lead_info=frappe.db.exists({"doctype":"Lead","email_id":self.email_id})
		customer_info=frappe.db.exists({
			"doctype":"Customer",
			"party_name":lead_info[0][0]
		})

		cust_full_name=self.first_name+" "+self.last_name
		print("\n\n\n"+cust_full_name+"\n\n\n")
		if type(customer_info)!=None:
			new_customer=frappe.get_doc({
				"doctype":"Customer",
				"salutation":self.salutation,
				"customer_name":cust_full_name,
				"lead_name":lead_info[0][0],
				"gender":self.gender,
				"customer_type":self.customer_type,
				"customer_group":self.customer_group,
				"territory":self.territories,
			})
			new_customer.insert()
			print("\n\n\n Customer Created\n\n\n")

def validate_mail_id_is_unique(email):
	print("\n\n\n Email Validation \n\n\n")
	if frappe.db.exists("User",email):
		print("\n\n\n email is present \n\n\n")
		frappe.throw("This Email is Already exist in User")
	

# @frappe.whitelist()	
def send_welcome_email(rec_email,rec_name,rec_password):
	"""Sends welcome email with login cardentials and ask to login to system"""
	subject="Welcome to Agency"
	context={
	"user_name":rec_name,
	"login_id":rec_email,
	"login_password":rec_password
	}
	msg=frappe.render_template("agency_management/public/js/email_template/WelcomeEmail.html",context)
	# frappe.sendmail(recipients=rec_email,
	# 				sender=frappe.session.user, 
	# 				subject=subject, 
	# 				message=msg,
	# 				reference_doctype="User",
	# 				reference_name=rec_name
	# )
	frappe.msgprint("Email Sent")






@frappe.whitelist()
def featch_item_name(item_group):

	items=frappe.db.sql("""select item_name from `tabItem` where item_group=%s""",item_group,as_dict=1)
	print(items)
	return items

@frappe.whitelist()
def featch_item_details(item_code):
	data=frappe.db.sql("""select item_name,description,image from `tabItem` where item_code=%s""",item_code,as_dict=1)
	print(data)
	return data
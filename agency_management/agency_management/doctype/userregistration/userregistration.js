// Copyright (c) 2021, Ruturaj Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('UserRegistration', {
	onload:function(frm){
		frm.toggle_reqd("first_name","reqd",1);
		frm.toggle_reqd("email_id","reqd",1);
		frm.toggle_reqd("mobile_no",frm.doc.status==="Lead")
		
	},
	
	status: function(frm){
		frm.trigger("set_mandatory_fields")
	},
	set_mandatory_fields(frm){
		// frm.toggle_reqd("mobile_no",frm.doc.status==="Lead")
	
		frm.toggle_reqd("customer_type",frm.doc.status==="Customer")
		frm.toggle_reqd("customer_group",frm.doc.status==="Customer")
		frm.toggle_reqd("territories",frm.doc.status==="Customer")
	},
	mobile_no: function (frm){
		var mobile_no=frm.doc.mobile_no;
		var test_regex = /^[0]?[789]\d{9}$/;
		if (test_regex.test(mobile_no)){
			console.log("number is valid")
		}
		else{
			console.log("number is not valid")
			msgprint('Mobile no is not valid');
		}
	},
	email_id:function(frm){
		var email_id=frm.doc.email_id;
		var test_regex = /^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$/;
		if (test_regex.test(email_id)){
			console.log("valid Email")
		}
		else{
			console.log("Invalid Email")
			msgprint('Invalid Email');
		}
	},
	car_type: function(frm){
		// var car_names=frappe.model.get_doc("Item",item_group=frm.doc.car_type);
		frm.fields_dict["car_name"].get_query=function(){
			return{
				filters:{
					"item_group":frm.doc.car_type
				}
			}
		}
	},
	car_select:function(frm){
		console.log(frm.doc.car_name);
		frappe.call({
			method:"agency_management.agency_management.doctype.userregistration.userregistration.featch_item_details",
			args:{
				"item_code":frm.doc.car_select
			},
			callback: function(r){
				frm.set_value("car_name",r.message[0].item_name)
				frm.set_value("details",r.message[0].description)
				frm.set_value("car_image",r.message[0].image)
			}
		})
	},
	

});


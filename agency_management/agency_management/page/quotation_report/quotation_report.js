frappe.pages['quotation-report'].on_page_load = function (wrapper) {
	new quotation_report(wrapper);
}

quotation_report = class QuotationReport {
	constructor(wrapper) {
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Quotation Report',
			single_column: true
		});
		this.parent = wrapper;
		this.page = this.parent.page;
		this.add_menu();
		this.add_filters();
	}
	add_menu() {
		const me = this;
		me.page.add_menu_item("PDF", ()=>this.create_pdf())
		me.page.add_menu_item("Export Excel", ()=>this.export_excel())
	}
	add_filters() {
		console.log("Make is called")
		const me = this;
		let start_date = me.page.add_field({
			label: "Start Date",
			fieldtype: "Date",
			fieldname: "start_date",
			reqd: 1,
			change() {
				me.start_date = start_date.get_value();
				me.make_report();
			}
		})
		let start_shift = me.page.add_field({
			label: "Start Shift",
			fieldtype: "Select",
			fieldname: "start_shift",
			reqd: 1,
			options: [
				'Morning',
				'Evening'
			],
			change() {
				me.start_shift = start_shift.get_value();
				me.make_report();
			}
		})
		let end_date = me.page.add_field({
			label: "End Date",
			fieldtype: "Date",
			fieldname: "end_date",
			reqd: 1,
			change() {
				me.end_date = end_date.get_value();
				me.make_report();
			}
		})
		let end_shift = me.page.add_field({
			label: "End Shift",
			fieldtype: "Select",
			fieldname: "end_shift",
			reqd: 1,
			options: [
				'Morning',
				'Evening'
			],
			change() {
				me.end_shift = end_shift.get_value();
				me.make_report();
			}
		})
	}

	make_report() {
		const me = this;
		// console.log(me.end_shift)
		if (me.start_date, me.start_shift, me.end_date, me.end_shift) {
			if (me.start_date < me.end_date) {
				console.log("All clear")
				frappe.call({
					method: "agency_management.agency_management.page.quotation_report.quotation_report.get_report_data",
					args: {
						"from_date": me.start_date,
						"from_shift": me.start_shift,
						"to_date": me.end_date,
						"to_shift": me.end_shift,
					},
					callback: function (r) {
						console.log(r.message)
						me.body = $(r.message).appendTo(me.page.main);
					}
				})
			}
			else {
				frappe.throw("Date are Invalid")
			}
		}
	}

	create_pdf(){
		const me = this;
		console.log("PDF called")
		if (me.start_date, me.start_shift, me.end_date, me.end_shift) {
			if (me.start_date < me.end_date) {
				frappe.call({
					method: "agency_management.agency_management.page.quotation_report.quotation_report.create_pdf",
					args: {
						"from_date": me.start_date,
						"from_shift": me.start_shift,
						"to_date": me.end_date,
						"to_shift": me.end_shift,
					}
				})
			}
			else {
				frappe.throw("Date are Invalid")
			}
		}
	}

	export_excel(){
		console.log("Export to excel called")
		const me = this;
		if (me.start_date, me.start_shift, me.end_date, me.end_shift) {
			if (me.start_date < me.end_date) {
				frappe.call({
					method: "agency_management.agency_management.page.quotation_report.quotation_report.export_excel",
					args: {
						"from_date": me.start_date,
						"from_shift": me.start_shift,
						"to_date": me.end_date,
						"to_shift": me.end_shift,
					}
				})
			}
			else {
				frappe.throw("Date are Invalid")
			}
		}
		frappe.msgprint("Excel is created")
	}


}
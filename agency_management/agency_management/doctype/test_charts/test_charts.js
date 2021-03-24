// Copyright (c) 2021, Ruturaj Patil and contributors
// For license information, please see license.txt
// import { Chart } from "frappe-charts/dist/frappe-charts.min.esm"

frappe.ui.form.on('Test Charts', {
	refresh: function (frm) {
		$.getScript("https://cdn.jsdelivr.net/npm/frappe-charts@1.1.0/dist/frappe-charts.min.iife.js", function () {

			const data = {
				labels: ["12am-3am", "3am-6pm", "6am-9am", "9am-12am",
					"12pm-3pm", "3pm-6pm", "6pm-9pm", "9am-12am"
				],
				datasets: [
					{
						name: "Some Data", type: "bar",
						values: [25, 40, 30, 35, 8, 52, 17, -4]
					},
					{
						name: "Another Set", type: "line",
						values: [25, 50, -10, 15, 18, 32, 27, 14]
					}
				]
			}

			const chart = new frappe.Chart("#chart", {  // or a DOM element,
				// new Chart() in case of ES6 module with above usage
				title: "My Awesome Chart",
				data: data,
				type: 'axis-mixed', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
				height: 250,
				colors: ['#7cd6fd', '#743ee2']
			})
			const data2 = {
				labels: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
				datasets: [
					{ values: [18, 40, 30, 35, 8, 52, 17, -4] }
				]
			}
			const charts = new frappe.Chart("#second", {
				title: "My Awesome Bar Chart",
				data: data2,
				type: 'bar',
				height: 209,
				colors: ['orange']
			});
			var data3= {
				labels: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
				datasets: [
				  { name: "Dataset 1", values: [18, 40, 70, 35, 8, 52, 17, -4] },
				  { name: "Dataset 2", values: [30, 50, -20, 15, 18, 32, 27, 14] }
				]
			}
			var thred=new frappe.Chart("#thred",{
				title:"Line Chart",
				data:data3,
				type:"bar",
				height:300,
				color:["red","pink"]
			})

		})


	}
});

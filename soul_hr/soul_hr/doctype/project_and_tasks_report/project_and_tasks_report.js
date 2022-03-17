// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project and Tasks Report', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on("Project and Tasks Estimation Table", "mon", function(frm, cdt, cdn) {
    var ed_details = frm.doc.estimation;
    for(var i in ed_details) {
        // if (ed_details[i].denominacion && ed_details[i].cantidad) {
        ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
    }
        cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "tue", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "wed", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "thu", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "fri", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "sat", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "sun", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
		





frappe.ui.form.on('Project and Tasks Estimation Table', {
	mon:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d)  { a = a+ d.mon; });
	frm.set_value("monday", a);
	refresh_field("monday");
	},
	estimation_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d) { a += d.mon; });
	frm.set_value("monday", a);
	refresh_field("monday");
		}
	});
frappe.ui.form.on('Project and Tasks Estimation Table', {
	tue:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d)  { a = a+ d.tue; });
	frm.set_value("tuesday", a);
	refresh_field("tuesday");
	},
	estimation_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d) { a += d.tue; });
	frm.set_value("tuesday", a);
	refresh_field("tuesday");
		}
	});
frappe.ui.form.on('Project and Tasks Estimation Table', {
	wed:function(frm, cdt, cdn){
		var d = locals[cdt][cdn];
		var total = 0;
		let a= parseInt(total)
		frm.doc.estimation.forEach(function(d)  { a = a+ d.wed; });
		frm.set_value("wednesday", a);
		refresh_field("wednesday");
		},
		estimation_remove:function(frm, cdt, cdn){
		var d = locals[cdt][cdn];
		var total = 0;
		let a= parseInt(total)
		frm.doc.estimation.forEach(function(d) { a += d.wed; });
		frm.set_value("wednesday", a);
		refresh_field("wednesday");
			}
		});
frappe.ui.form.on('Project and Tasks Estimation Table', {
	thu:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d)  { a = a+ d.thu; });
	frm.set_value("thursday", a);
	refresh_field("thursday");
	},
	estimation_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d) { a += d.thu; });
	frm.set_value("thursday", a);
	refresh_field("thursday");
		}
	});
frappe.ui.form.on('Project and Tasks Estimation Table', {
	fri:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d)  { a = a+ d.fri; });
	frm.set_value("friday", a);
	refresh_field("friday");
	},
	estimation_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d) { a += d.fri; });
	frm.set_value("friday", a);
	refresh_field("friday");
		}
	});
frappe.ui.form.on('Project and Tasks Estimation Table', {
	sat:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d)  { a = a+ d.sat; });
	frm.set_value("saturday", a);
	refresh_field("saturday");
	},
	estimation_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d) { a += d.sat; });
	frm.set_value("saturday", a);
	refresh_field("saturday");
		}
	});
frappe.ui.form.on('Project and Tasks Estimation Table', {
	sun:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d)  { a = a+ d.sun; });
	frm.set_value("monday", a);
	refresh_field("monday");
	},
	estimation_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total = 0;
	let a= parseInt(total)
	frm.doc.estimation.forEach(function(d) { a += d.sun; });
	frm.set_value("sunday", a);
	refresh_field("sunday");
		}
	});
// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project and Tasks Report',{
	before_load: function(frm) {
				frappe.call({
					method: "soul_hr.soul_hr.doctype.project_and_tasks_report.project_and_tasks_report.get_employees",
					
					args: {"user": frappe.session.user },
					callback: function(r) { 
						if(r.message) {
							var d=r.message
							frm.set_value("employee", d['name'])
						}

					}
					
				});
			},
		refresh: function(frm) {	
			frm.set_query("tasks","estimation", function(_doc, cdt, cdn) {
				var d = locals[cdt][cdn];
				return {
					filters: {
						"project":d.project
					}
				};
			});
		},	


				
	// onload: function(frm) {
	// 	frappe.call({
	// 		method: "soul_hr.soul_hr.doctype.project_and_tasks_report.project_and_tasks_report.get_employees",
			
	// 		args: {"user": frappe.session.user },
			
	// 		// args: {
	// 		// 	semester: frm.doc.program,
	// 		// },
	// 		callback: function(r) { 
	// 			if(r.message) {
	// 				var d=r.message
	// 				frm.set_value("employee", d['name'])
	// 			}

	// 		}
			
	// 	});
	// }		
	
	// /opt/bench/frappe-bench/apps/soul_hr/soul_hr/soul_hr/doctype/project_and_tasks_report/project_and_tasks_report.js

});
frappe.ui.form.on("Project and Tasks Estimation Table", "tasks", function(frm, cdt, cdn) {
	var al_no = frm.doc.estimation;
	var arr =[];
	for(var i in al_no){
		arr.push(al_no[i].tasks);
	}
	for (var j=0;j<arr.length-1;j++){
		for(var k=j+1;k<arr.length;k++){
			if(arr[j] == arr[k]){
				// frappe.show_alert('Duplicate Allotment number')
				// frappe.msgprint(arr[k])
				frappe.msgprint("Duplicate entry "+arr[k])
			}
		}
	}
});
frappe.ui.form.on("Project and Tasks Estimation Table", "mon", function(frm, cdt, cdn) {
    var ed_details = frm.doc.estimation;

    for(var i in ed_details) {
		if (ed_details[i].mon<0) {
			ed_details[i].mon=("0");
		}
        // if (ed_details[i].denominacion && ed_details[i].cantidad) {
        ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
    }
        cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "tue", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;

	for(var i in ed_details) {
		if (ed_details[i].tue<0) {
			ed_details[i].tue=("0");
		}
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "wed", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		for(var i in ed_details) {

			if (ed_details[i].wed<0) {
				ed_details[i].wed=("0");
			}
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); }
	});
frappe.ui.form.on("Project and Tasks Estimation Table", "thu", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		for(var i in ed_details) {
			if (ed_details[i].thu<0) {
				ed_details[i].thu=("0");
			}
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation");
 }
 });
frappe.ui.form.on("Project and Tasks Estimation Table", "fri", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		for(var i in ed_details) {
			if (ed_details[i].fri<0) {
				ed_details[i].fri=("0");
			}
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); 
	}
	});

frappe.ui.form.on("Project and Tasks Estimation Table", "sat", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;
	for(var i in ed_details) {
		if (ed_details[i].sat<0) {
			ed_details[i].sat=("0");
		}
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); });
frappe.ui.form.on("Project and Tasks Estimation Table", "sun", function(frm, cdt, cdn) {
	var ed_details = frm.doc.estimation;

	for(var i in ed_details) {
		if (ed_details[i].sun<0) {
			ed_details[i].sun=("0");
		}
		// if (ed_details[i].denominacion && ed_details[i].cantidad) {
		ed_details[i].total=ed_details[i].mon + ed_details[i].tue + ed_details[i].wed + ed_details[i].thu + ed_details[i].fri + ed_details[i].sat + ed_details[i].sun;
	}
		cur_frm.refresh_field ("estimation"); 
	});
		
// frappe.ui.form.on("Project and Tasks Estimation Table", "level", function(frm, cdt, cdn) {

// 	var ed_details = frm.doc.books_chapters_in_books_etc;
// 	//var total = 0;
// 	for(var i in ed_details) {
				
// 	if (ed_details[i].level=="International") {
// 		ed_details[i].level_score=("12");
// 	}
// 	else if (ed_details[i].level=="National") {
// 		ed_details[i].level_score=("10");
// 	}
// 	else {
// 		frappe.throw("Wrong Entry")
// 	}	 
		
// }
// 		cur_frm.refresh_field ("books_chapters_in_books_etc");
	
		
// 		//alert(ed_details[i].percent);
	
// 	});	




// frappe.ui.form.on('Project and Tasks Estimation Table', {
// 	mon:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d)  { a = a+ d.mon; });
// 	frm.set_value("monday", a);
// 	refresh_field("monday");
// 	},
// 	estimation_remove:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d) { a += d.mon; });
// 	frm.set_value("monday", a);
// 	refresh_field("monday");
// 		}
// 	});
// frappe.ui.form.on('Project and Tasks Estimation Table', {
// 	tue:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d)  { a = a+ d.tue; });
// 	frm.set_value("tuesday", a);
// 	refresh_field("tuesday");
// 	},
// 	estimation_remove:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d) { a += d.tue; });
// 	frm.set_value("tuesday", a);
// 	refresh_field("tuesday");
// 		}
// 	});
// frappe.ui.form.on('Project and Tasks Estimation Table', {
// 	wed:function(frm, cdt, cdn){
// 		var d = locals[cdt][cdn];
// 		var total = 0;
// 		let a= parseInt(total)
// 		frm.doc.estimation.forEach(function(d)  { a = a+ d.wed; });
// 		frm.set_value("wednesday", a);
// 		refresh_field("wednesday");
// 		},
// 		estimation_remove:function(frm, cdt, cdn){
// 		var d = locals[cdt][cdn];
// 		var total = 0;
// 		let a= parseInt(total)
// 		frm.doc.estimation.forEach(function(d) { a += d.wed; });
// 		frm.set_value("wednesday", a);
// 		refresh_field("wednesday");
// 			}
// 		});
// frappe.ui.form.on('Project and Tasks Estimation Table', {
// 	thu:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d)  { a = a+ d.thu; });
// 	frm.set_value("thursday", a);
// 	refresh_field("thursday");
// 	},
// 	estimation_remove:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d) { a += d.thu; });
// 	frm.set_value("thursday", a);
// 	refresh_field("thursday");
// 		}
// 	});
// frappe.ui.form.on('Project and Tasks Estimation Table', {
// 	fri:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d)  { a = a+ d.fri; });
// 	frm.set_value("friday", a);
// 	refresh_field("friday");
// 	},
// 	estimation_remove:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d) { a += d.fri; });
// 	frm.set_value("friday", a);
// 	refresh_field("friday");
// 		}
// 	});
// frappe.ui.form.on('Project and Tasks Estimation Table', {
// 	sat:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d)  { a = a+ d.sat; });
// 	frm.set_value("saturday", a);
// 	refresh_field("saturday");
// 	},
// 	estimation_remove:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d) { a += d.sat; });
// 	frm.set_value("saturday", a);
// 	refresh_field("saturday");
// 		}
// 	});
// frappe.ui.form.on('Project and Tasks Estimation Table', {
// 	sun:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d)  { a = a+ d.sun; });
// 	frm.set_value("sunday", a);
// 	refresh_field("sunday");
// 	},
// 	estimation_remove:function(frm, cdt, cdn){
// 	var d = locals[cdt][cdn];
// 	var total = 0;
// 	let a= parseInt(total)
// 	frm.doc.estimation.forEach(function(d) { a += d.sun; });
// 	frm.set_value("sunday", a);
// 	refresh_field("sunday");
// 		}
// 	});









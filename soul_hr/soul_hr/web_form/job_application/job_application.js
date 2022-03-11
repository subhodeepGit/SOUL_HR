frappe.ready(function() {
	frappe.web_form.after_save=()=>{
		alert('Thank you for applying');
		window.location.href="http://soulunileaders.com/career.html"
	}
})
frappe.listview_settings['Employee'] = {
    onload: function(listview) {
        if (frappe.user.has_role(["Employee"]) && !frappe.user.has_role(["Projects Manager"])){    
            $(".filter-selector").hide();    
            if(frappe.route_options){
                frappe.route_options = {
                    "user_id": ["=", frappe.session.user]
                };
            }
        }
        else{

        }
    }
}
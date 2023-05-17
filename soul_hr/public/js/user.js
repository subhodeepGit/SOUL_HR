frappe.ui.form.on('User',{
    refresh: function(frm) {
        if (frappe.user.has_role(["Employee","Expense Approver","Leave Approver","Projects Manager","Chairperson"])){
            frm.set_df_property('api_access', 'hidden', 1);
            frm.remove_custom_button("Create User Email");
        }
        if (frappe.user.has_role(["Employee","Expense Approver","Leave Approver","Projects Manager","Chairperson"]) && !frappe.user.has_role(["System Manager"])){ 
            Object.keys(cur_frm.fields_dict).forEach(field=>{
                if (['new_password','logout_all_sessions','phone','mobile_no','interest','bio','mute_sounds','desk_theme',].includes(field)){
                    frm.set_df_property(field,'read_only',0)
                }
                else{
                    frm.set_df_property(field,'read_only',1)
                }
            })
        }
        
    }
})
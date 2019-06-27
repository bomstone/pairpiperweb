$(function(ready){
    $("#slct").change(function() {
        user = this.value.toLowerCase();
            $("form").each(function() {
            form = this;
               if($(this).find(".userCell input")[0].value.toLowerCase() == user || user == "user"){
                $(form).show();
               }else{
               $(form).hide();
               }
            });
            });
});
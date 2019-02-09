
function toggleColumns(cols, visible){
        for(i=0;i<cols.length;i++){
        if(visible){
            $('#subpositionsTable tr > *:nth-child('+cols[i]+')').show();
            $('#mainTable tr > *:nth-child('+cols[i]+')').show();
            }else{
            $('#subpositionsTable tr > *:nth-child('+cols[i]+')').hide();
            $('#mainTable tr > *:nth-child('+cols[i]+')').hide();
            }
        }
     };
//function addposition(){
$(function(ready){
    $(".setBtn").each(function( index ) {
       this.onclick=(function() {
            var qty = $("#targetExposure").val() / $(".assetOpen")[index].value;
            $(".positionQuantity")[index].value = Math.round(qty);
            });
        });
     $("#id_strategy").change(function(){
        $("#submitPosition").show();
        if(this.value == "standard"){
            $("#mainPosition").show();
            $("#subpositions").hide();
        }else if(this.value == "pairs trade"){
            $("#subpositions").show();
            $("#mainPosition").hide();
        }else{
            $("#subpositions").hide();
            $("#mainPosition").hide();
            $("#submitPosition").hide();
        }

     });

      toggleColumns([5,6],false);
     $('#currency').change(function(){
        console.log(this.checked);
        if(this.checked){
            toggleColumns([5,6],true);
        }else{
        toggleColumns([5,6],false);
        }
     });

     $('#id_product_type').change(function(){
        console.log(this.value);
        if(this.value != 'stock'){
            toggleColumns([7,10,11,12],true);
        }else{
 $('#subpositionsTable tr > *:nth-child(7)').show();
            toggleColumns([7,10,11,12],false);
        }
     });
});
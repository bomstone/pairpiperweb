
function toggleColumns(cols, visible){
        for(i=0;i<cols.length;i++){
        if(visible){
            $('#subPositionsTable tr > *:nth-child('+cols[i]+')').show();
            $('#mainTable tr > *:nth-child('+cols[i]+')').show();
            }else{
            $('#subPositionsTable tr > *:nth-child('+cols[i]+')').hide();
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
            $("#subPositions").hide();
        }else if(this.value == "pairs trade"){
            $("#subPositions").show();
            $("#mainPosition").hide();
        }else{
            $("#subPositions").hide();
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
            toggleColumns([7,10,11,12],true);
        if(this.value == 'stock'){
            toggleColumns([7,10,11,12],false);
        }else if(this.value == 'mini short'){
            toggleColumns([11,12],false);
        }else if(this.value == 'mini long'){
            toggleColumns([11,12],false);
        }
    });
        $('#id_form-0-product_type').change(function(){
        console.log(this.value);
            toggleColumns([7,10,11,12],true);
        if(this.value == 'stock'){
            toggleColumns([7,10,11,12],false);
        }else if(this.value == 'mini short'){
            toggleColumns([11,12],false);
        }else if(this.value == 'mini long'){
            toggleColumns([11,12],false);
        }
    });
});

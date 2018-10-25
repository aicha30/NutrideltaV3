   $(document).ready(function() {

    var tab_alim=["poulet","viande","charcuterie"];
    var tab_alim_id=[1200,1400,1600];
    var cpt=0;

    $("#new_aliment").html("<div class='aliment' id='"+tab_alim_id[cpt]+"'><span class='aliment_text'>"+tab_alim[cpt]+"</span></div>");
    

    $("#new_aliment, #never, #rarely, #sometimes, #often, #always").sortable({
      connectWith: ["#new_aliment, #never, #rarely, #sometimes, #often, #always"],
      receive: function(){ 
        cpt=cpt+1;
        var test= $("#new_aliment").find("div").text();
        if(test==""){
          $("#new_aliment").html("<div class='aliment' id='"+tab_alim_id[cpt]+"'><span class='aliment_text'>"+tab_alim[cpt]+"</span></div>");}
        }
      });


  });


   function algo_nutrition(alim_user){

    var cpt=0;
    var alim_user_rar=[];
    var i = 0;

    $("#rarely").find(".aliment").each( function(index, element){
      alim_user_rar[i]=$(this).text();
      var txt = $("input").val();
      $.get('MyTest', {aliment_name: alim_user_rar[i], frequency: "rarely"}, function(result){
        alert("test");
      });
      
      
    });

    
  }
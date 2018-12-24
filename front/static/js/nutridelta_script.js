// initialisation jquery (javascript simplifié)
$(document).ready(function(){
   
    // si user clique sur un des block objectif
	$(".blockChoiceObjective").unbind('click').bind('click',function(){
        id=this.id;
        var checked=$("#customCheck"+id).prop("checked");
        if (checked==true){
            addObjective(id);
        }
        else{
            deleteObjective(id);
        }
       
       
    });
});

function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

function addObjective(id){
    $("#customCheck"+id).prop("checked", true);
    $.ajax({
        headers: {'Content-Type':'application/json',
        'X-CSRFToken': getCookie('csrftoken')},
        url: "addObjective/"+id,
        type:"POST",
        
        success: function (data) {
            
            
        }
    });
    
}
function deleteObjective(id){
    $("#customCheck"+id).prop("checked", false);
    $.ajax({
        headers: {'Content-Type':'application/json',
        'X-CSRFToken': getCookie('csrftoken')},
        url: "deleteObjective/"+id,
        type:"POST",
        
        success: function (data) {
          
            
        }
    });
    
}

// initialisation jquery (javascript simplifié)
$(document).ready(function () {





    $(".choixSexe").unbind('click').bind('click', function () {
    hideOrShowSpecificDivForWomen(this.id);
    updateSexe(this.id);
    $(".choixSexe").each(function(){
    $(this).removeClass("objectSelected");
    });
    $(this).addClass("objectSelected");
    });


    $(".choixEnceinte").unbind('click').bind('click', function () {
       $(this).toggleClass("objectSelected");
        updateEnceinte(this.id);
    });

    $(".choixAllaitante").unbind('click').bind('click', function () {
       $(this).toggleClass("objectSelected");
        updateAllaitante(this.id);
    });


    $("#addSport").unbind('click').bind('click', function () {
        var sport_id=$('#select_sport option:selected').val();
        var sport_name=$('#select_sport option:selected').text();
        addSportChoice(sport_id, sport_name);
    });



   });



var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});







function hideOrShowSpecificDivForWomen(id){
    if(id=="True"){
       $("#specific-div-for-women").hide(200);
    }else{

        $("#specific-div-for-women").show(200);

    }
}

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






function addSportChoice(id, sport_name){
    $.ajax({
        headers: {'Content-Type':'application/json',
        'X-CSRFToken': getCookie('csrftoken')},
        url: "addSportChoice/"+id,
        type:"POST",

        success: function (data) {
            $('#selectSport') > $('#'+id).remove();

            var html="<div class=\"card-1 div_user_sport\" id=\"div_user_Sport_"+id+"\" style=\"margin-top:1.5em;\">\n" +
                "        <div style=\"width:100%;display:flex;\">\n" +
                "        <div style=\"margin-top:auto;\">"+ sport_name+"</div>\n" +
                "        <div style=\"margin-left:auto;\">\n" +
                "          <button type=\"button\" class=\"btn btn-danger deleteSport\" onclick=\"deleteSportChoice("+id+",'"+sport_name+"')\" id=\""+id+"\" style=\"margin-left:1em;\">X</button>\n" +
                "        </div>\n" +
                "      </div>\n" +
                "        <select class=\"form-control inputstl\" style=\"margin-top:0.2em;\">\n" +
                "          <div>\n" +
                "            <option>30min</option>\n" +
                "            <option>1h</option>\n" +
                "            <option>2h</option>\n" +
                "            <option>3h</option>\n" +
                "            <option>4h</option>\n" +
                "            <option>5h</option>\n" +
                "            <option>Plus de 5h</option>\n" +
                "          </div>\n" +
                "\n" +
                "        </select>\n" +
                "      </div>";

$("#sportUserDiv").append(html);
        }
    });

}


function deleteSportChoice(id, sport_name) {
    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        url: "deleteSportChoice/" + id,
        type: "POST",

        success: function (data) {
      $('#select_sport').append($('<option>', {
    value: id,
    text: ""+sport_name+"",
          id:id
}));
        $("#div_user_Sport_"+id).remove();
        }

    });
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





function updateSexe(sexe) {

    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        url: "updateSexe/" + sexe,
        type: "POST",

        success: function (data) {

        }
    });
}

function updateEnceinte(enceinte) {

    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'csrfmiddlewaretoken': getCookie('csrftoken')
        },
        url: "updateEnceinte/" + enceinte,
        type: "POST",

        success: function (data) {

        }
    });
}
function updateAllaitante(allaitante) {

    $.ajax({
        headers: {
            'Content-Type': 'application/json'
        },
        url: "updateAllaitante/" + allaitante,
        type: "POST",

        success: function (data) {
        }
    });
}


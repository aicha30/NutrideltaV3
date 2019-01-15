// initialisation jquery (javascript simplifié)
$(document).ready(function () {
    // si user clique sur un des block objectif
    $(".choixObjectif").unbind('click').bind('click', function () {
        if (!$(this).hasClass("objectifSelected")) {
            addObjective(this.id);
            $(this).addClass("objectifSelected");

        }
        else {
            deleteObjective(this.id);
            $(this).removeClass("objectifSelected");

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

function addObjective(id) {

    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        url: "addObjective/" + id,
        type: "POST",

        success: function (data) {

        }
    });

}
function deleteObjective(id) {

    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        url: "deleteObjective/" + id,
        type: "POST",

        success: function (data) {


        }
    });

}

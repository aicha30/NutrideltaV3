function updateReponseObjectifQuestion(id, value) {
    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        url: "/questionnaire/updateReponseObjectifQuestion/" + id + "/" + value,
        type: "POST",

        success: function (data) {

            generateNewQuestion();

        }
    });


}


function remplissage(objectif_id, question_id, value) {

    console.log(question_id, value);
    updateReponseObjectifQuestion(question_id, value);

    $(".question" + question_id).each(function () {
        $(this).css('background-color')
        $(this).css('background-color', "white");
        if ($(this).attr('value') == value) {
            var myColor = $(this).css("border-color");
            $(this).css('background-color', myColor);
        }
    });


}

function generateNewQuestion() {
    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        url: "/questionnaire/generateNewQuestion",
        type: "GET",

        success: function (data) {
    console.log(data);
            if (data.newQuestion[0]) {

                    $("#suivantQuestionnaire").addClass("forbiddenButton");
                        afficheQuestion(data.newQuestion[0][0]);




            }else{
                 $("#suivantQuestionnaire").removeClass("forbiddenButton");
                 $("#suivantQuestionnaire").off('click');
            }

        }
    });
}

function afficheQuestion(question) {


    var bonusClass = "bubble";
    var html = "<div id='cadre_question_" + question.id + "' class='cadre_question' style=\"width:100%;  padding:0.5em;margin-top:1.5em;background-color: white;\">\n" +
        "<div class=\"title-question-nutridelta\" style=\"width:100%;text-align:center;\">" + question.name + "</div>\n" +
        "\t<div style=\"margin:auto;\">\n" +
        "\t\t<div class=\"titreQuestion1\" style=\"display:flex;margin:auto;margin-bottom:1em\">\n" +
        "\n" +
        "\t\t</div>\n" +
        "\t\t<div class='magic_flos_responsive " + bonusClass + " ' style=\"display:flex;margin:auto;width:100%;text-align:center;\">\n" +
        "\t\t\t<div  class=\"magic_flos_responsive\" style=\"margin:auto;display:flex;text-align:center;\">\n" +
        "\n" +
        "\n" +
        "\t\t\t\t<div class=\"buttonChoice buttonChoice_wideSize buttonChoice_greenBorder question" + question.id + "\" id='-3'  value=\"-3\"  onclick=\"remplissage(" + question.objectif_id + "," + question.id + ",-3);\">\n" +
        "\t\t\t\t</div>\n" +
        "\t\t\t\t<div class=\"buttonChoice buttonChoice_mediumSize buttonChoice_greenBorder question" + question.id + "\"  id='-2' value=\"-2\" onclick=\"remplissage(" + question.objectif_id + "," + question.id + ",-2);\">\n" +
        "\t\t\t\t</div>\n" +
        "\n" +
        "\t\t\t\t<div class=\"buttonChoice buttonChoice_littleSize buttonChoice_greenBorder question" + question.id + "\" id='-1' value=\"-1\" onclick=\"remplissage(" + question.objectif_id + "," + question.id + ",-1);\">\n" +
        "\t\t\t\t</div>\n" +
        "\t\t\t\t<div class=\"buttonChoice buttonChoice_neutralSize buttonChoice_grayBorder question" + question.id + "\" id='0' value=\"0\"  onclick=\"remplissage(" + question.objectif_id + "," + question.id + ",0);\">\n" +
        "\t\t\t\t</div>\n" +
        "\t\t\t\t<div class=\"buttonChoice buttonChoice_littleSize buttonChoice_redBorder question" + question.id + "\" id='1' value=\"1\"  onclick=\"remplissage(" + question.objectif_id + "," + question.id + ",+1);\">\n" +
        "\t\t\t\t</div>\n" +
        "\t\t\t\t<div class=\"buttonChoice buttonChoice_mediumSize buttonChoice_redBorder question" + question.id + "\" id='2' value=\"2\"  onclick=\"remplissage(" + question.objectif_id + "," + question.id + ",+2);\">\n" +
        "\t\t\t\t</div>\n" +
        "\t\t\t\t<div class=\"buttonChoice buttonChoice_wideSize buttonChoice_redBorder question" + question.id + "\" id='3' value=\"3\"  onclick=\"remplissage(" + question.objectif_id + "," + question.id + ", +3);\">\n" +
        "\t\t\t\t</div>\n" +
        "\n" +
        "\n" +
        "\n" +
        "\t\t\t</div>\n" +
        "\t\t</div>\n" +
        "\t</div>\n" +
        "  </div>";


    $("#cadreQuestionsObjectives").append(html);
    var n = $(document).height();
    var elementY = $("#cadre_question_" + question.id).position().top;
    $('html, body').animate({scrollTop: elementY - 200}, 0);

    if (question.reponse) {


        $(".question" + question.objectif_id + data.id).each(function () {

            $(this).css('background-color', "white");
            if ($(this).attr('value') == data.reponse) {
                var myColor = $(this).css("border-color");
                $(this).css('background-color', myColor);
            }
        });
        $('html, body').animate({scrollTop: 0}, 0);
    }
}

function reponseForThisQuestion(reponses, question_id) {
    var trouve = false;
    $.each(reponses, function () {

        $.each(this, function (k, reponse) {

            if (reponse.question_id == question_id) {
                trouve = true;
                $(".question" + reponse.question_id).each(function () {
                    $(this).css('background-color', "white");
                    if ($(this).attr('value') == reponse.value) {
                        var myColor = $(this).css("border-color");
                        $(this).css('background-color', myColor);
                    }
                });
            }
        });
    });
    return trouve;
}


function giveMeQuestionsAnswered() {
    $("#suivantQuestionnaire").attr('onclick', '');
    $("#suivantQuestionnaire").addClass("forbiddenButton");
    //ajax
    $.ajax({
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        async: false,
        url: "/questionnaire/giveMeQuestionsAnswered",
        type: "GET",

        success: function (data) {

            if (data.questions) {

                $.each(data.questions, function () {

                    $.each(this, function (k, question) {



                            afficheQuestion(question);
                            reponseForThisQuestion(data.reponses, question.id);


                    });
                });

                //  question + question.id

            }
        }

    });
    generateNewQuestion();
}









$(document).ready(function()
{

    'use strict';




    var frame = document.getElementById('game_iframe');



    function error(text) {
      var message =  {
        messageType: "ERROR",
        info: text
      };
      //send message to iframe
      frame.contentWindow.postMessage(message, "*");
    }


    $(window).on('message', function(evt) {

      var data = evt.originalEvent.data;

      if (data.messageType == 'SCORE') {

        var score = data.score;

        var title = $('#gameTitle').html();
        $.ajax({
          method: 'POST',
          url: 'score/',
          data: {csrfmiddlewaretoken: '{{ csrf_token }}',
          Score: score,
          Title: title
        },
        success: function (data) {

             $(".highscore").load(location.href + " .highscore");

           },
           error: function (data) {
             error("Something went wrong with submitting highscores :( ");
           }
         });








      }

      if (data.messageType == 'SAVE') {
        //implement SAVE

        var gamestate = JSON.stringify(data.gameState);
        var gametitle = $('#gameTitle').html();


        $.ajax({
          method: 'POST',
          url: 'save/',
          data: {csrfmiddlewaretoken: '{{ csrf_token }}',
          save_State: gamestate,
          Title: gametitle
        },

        success: function (data) {

             alert("game saved!");

           },
           error: function (data) {

             error("Something went wrong with saving the game :( ");
           }
         });

      }

      if (data.messageType == 'LOAD_REQUEST') {

        var Title = $('#gameTitle').html();

        $.ajax({
          method: 'POST',
          url: 'load/',
          data: { csrfmiddlewaretoken: '{{ csrf_token }}',
          Title: Title
        },

        success: function (data) {

             var message = {
                       messageType: "LOAD",
                       gameState: data
                     };


              frame.contentWindow.postMessage(message, "*");

           },
           error: function (data) {

             error("Something went wrong with loading the game :( ");
           }
         });






      }

      if (data.messageType == 'SETTING') {

        var width = data.options.width;

        var height = data.options.height;

        $('iframe').width(width)
        .height(height);

      }


    });



  });

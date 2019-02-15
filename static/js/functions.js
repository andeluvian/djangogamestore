$(document).ready( function() {
    'use strict';


    let frame = document.getElementById('game_iframe');
    function catchError(text) {
        let message =  {
            messageType: "ERROR",
            info: text
        };
        frame.contentWindow.postMessage(message, "*");
    }


    function communicate(url, data, success, error_msg) {
        $.ajax({
            method: 'POST',
            url: url,
            data: data,
            success: success,
            error: function() {
                catchError(error_msg);
            }
        });
    }


    function saveGame() {
        alert("Game saved!");
    }


    function loadGame(data) {
        frame.contentWindow.postMessage({ messageType: "LOAD", gameState: JSON.parse(data) }, "*");
    }


    function submitScore(data) {
        let scores = JSON.parse(data);
        $("#highscores").empty();

        let fragment = document.createDocumentFragment();
        for (let i = 0; i < scores.length; i++) {
            let highscore = scores[i].fields;
            let div = $('<li>' + highscore.username + ': ' + highscore.score + '</li>')[0];
            fragment.appendChild(div);
        }

        $("#highscores").append(fragment);
    }


    function changeSettings(options) {
        let width = options.width;
        let height = options.height;

        $('iframe').width(width)
            .height(height);
    }


    function parseMessage(event) {
        let message = event.originalEvent.data;

        if (message.messageType == 'LOAD_REQUEST') {
            communicate('load/', { csrfmiddlewaretoken: token }, loadGame, 'Unable to load game' );
        } 
        
        else if (message.messageType == 'SAVE') {
            let save_state = JSON.stringify(message.gameState);
            communicate('save/', { csrfmiddlewaretoken: token, save_state: save_state }, saveGame, 'Unable to save game' );
        } 
        
        else if (message.messageType == 'SCORE') {
            communicate('score/', { csrfmiddlewaretoken: token, score: message.score }, submitScore, 'Unable to submit score' );
        } 
        
        else if (message.messageType == 'SETTING') {
            changeSettings(message.options);
        }
    }


    $(window).on('message onmessage', parseMessage);
});

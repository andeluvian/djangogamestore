$(document).ready( function() {
    'use strict';


    let frame = document.getElementById('game-container');
    function sendError(text) {
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
                sendError(error_msg);
            }
        });
    }


    function saveGame() {
        alert("Game saved!");
    }


    function loadGame(data) {
        frame.contentWindow.postMessage({ messageType: "LOAD", gameState: JSON.parse(data) }, "*");
    }


    function updateScore() {
        $.ajax({
            method: 'GET',
            url: '/api/v1/game/' + gameId + '/score/?limit=5',
            data: { csrfmiddlewaretoken: token },
            success: function(data) {
                let scores = data.highscores;
                $("#highscores").empty();

                let fragment = document.createDocumentFragment();
                for (let i = 0; i < scores.length; i++) {
                    let highscore = scores[i];
                    let div = $('<li>' + highscore.username + ': ' + highscore.score + '</li>')[0];
                    fragment.appendChild(div);
                }

                $("#highscores").append(fragment);
            },
            error: function(data) {
                console.log('Leaderboard update failed');
            }
        });

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
            communicate('/api/v1/game/' + gameId + '/score/submit/', { csrfmiddlewaretoken: token, score: message.score }, updateScore, 'Unable to submit score' );
        } 
        
        else if (message.messageType == 'SETTING') {
            changeSettings(message.options);
        }
    }


    $(window).on('message onmessage', parseMessage);
});

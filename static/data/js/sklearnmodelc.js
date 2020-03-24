/*
 * @Descripttion: 
 * @Author: BerryBC
 * @Date: 2020-02-23 10:38:36
 * @LastEditors: BerryBC
 * @LastEditTime: 2020-03-10 23:12:32
 */
$(function() {
    $('#btnCreat')[0].onclick = function() {
        if ("WebSocket" in window) {
            var domain = window.location.host;
            wsSocks = new WebSocket("ws://" + domain + "/ws/data/sklcws/");

            $('#btnCreat').addClass('disabled');
            $('#btnCreat').attr('disabled', true);

            wsSocks.onopen = function() {
                $('#taContent').val($('#taContent').val() + ' Connected \n')
            };

            wsSocks.onmessage = function(evt) {
                var received_msg = JSON.parse(evt.data);
                received_msg = received_msg.message;

                $('#taContent').val($('#taContent').val() + received_msg + '\n')
                setTimeout(() => {
                    wsSocks.send(JSON.stringify({
                        'message': 1
                    }));
                }, 1000);
            };

            wsSocks.onclose = function() {
                $('#taContent').val($('#taContent').val() + ' Closed \n');

                $('#btnCreat').removeClass('disabled');
                $('#btnCreat').attr('disabled', false);
            };
        } else {
            $('#taContent').val('Your 浏览器 can\'t support Websocket!')
        }
    };
});
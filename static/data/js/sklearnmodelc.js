/*
 * @Descripttion: 
 * @Author: BerryBC
 * @Date: 2020-02-23 10:38:36
 * @LastEditors: BerryBC
 * @LastEditTime: 2020-03-29 16:24:36
 */
$(function() {
    $('#btnCreat')[0].onclick = function() {
        if ("WebSocket" in window) {
            var domain = window.location.host;
            wsSocks = new WebSocket("ws://" + domain + "/ws/data/sklcws/");

            $('#btnCreat').addClass('disabled');
            $('#btnCreat').attr('disabled', true);
            $('#taContent').val($('#taContent').val() + 'Try to connected \n')
            wsSocks.onopen = function() {
                $('#taContent').val($('#taContent').val() + ' - Connected \n');
            };

            wsSocks.onmessage = function(evt) {
                var jsonRevData = JSON.parse(evt.data);
                intCode = jsonRevData.code;
                strRev = jsonRevData.msg;

                if (intCode == 1) {
                    $('#taContent').val($('#taContent').val() + ' - Server confirm connected \n');
                    wsSocks.send(JSON.stringify({
                        'doCode': 0
                    }));
                } else if (intCode == 2) {
                    $('#taContent').val($('#taContent').val() + '  - - ' + strRev + '\n');
                } else if (intCode == 3) {
                    $('#taContent').val($('#taContent').val() + ' - Done creat classification\n');
                    wsSocks.close();
                };
            };

            wsSocks.onclose = function() {
                $('#taContent').val($('#taContent').val() + ' - Closed \n');

                $('#btnCreat').removeClass('disabled');
                $('#btnCreat').attr('disabled', false);
            };
        } else {
            $('#taContent').val('Your 浏览器 can\'t support Websocket!');
        }
    };
});
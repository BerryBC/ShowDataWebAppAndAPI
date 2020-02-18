/*
 * @Descripttion: 
 * @Author: BerryBC
 * @Date: 2020-02-18 21:43:52
 * @LastEditors: BerryBC
 * @LastEditTime: 2020-02-18 22:02:23
 */
$(function() {
    $('#btnSpy')[0].onclick = function() {
        if ($("#txtTag").val() == "" || $("#txtURL").val() == "") {
            ShowModal(false, 'Neither Tag and Key URL could not be BLANK!')
        } else {
            var formData = new FormData();
            formData.append('t', $("#txtTag").val());
            formData.append('u', $("#txtURL").val());
            $('#modalWait').modal({ backdrop: 'static', keyboard: false });
            $.ajax({
                url: "/data/spydatawithtag/",
                type: "POST",
                dataType: "json",
                data: formData,
                contentType: false,
                processData: false,
                success: function(data) {
                    $('#modalWait').modal('hide');
                    if (data.intBack == 0) {
                        ShowModal(false, 'Something wrong, unable to spy.')
                    } else if (data.intBack == 99) {
                        ShowModal(false, 'Request is wrong, please contact the administrator.')
                    } else if (data.intBack == 98) {
                        ShowModal(false, 'Request is wrong, please login again.')
                    } else if (data.intBack == 1) {
                        $("#taContent").val(data.strCT);
                        ShowModal(true, 'Spy Data success! Yeah!');
                    };
                },
                error: function(err) {
                    $('#modalWait').modal('hide');
                    ShowModal(false, 'Something goes wrong with the network, please check it out.')
                }
            });
        };
    };
});
/*
 * @Descripttion: 
 * @Author: BerryBC
 * @Date: 2020-02-07 13:28:45
 * @LastEditors  : BerryBC
 * @LastEditTime : 2020-02-07 15:09:17
 */
$(function() {
    $('#btnLoadLog')[0].onclick = function() {
        $.ajax({
            url: "/data/getdatacount/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.intBack == 0) {
                    ShowModal(false, 'Something wrong, unable to insert.')
                } else if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.')
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.')
                } else if (data.intBack == 1) {
                    ShowModal(true, 'Load Data success! Yeah!')
                    $("#taContent").val('----------------------------\n\n' + $("#taContent").val());
                    $("#taContent").val(data.strFB + $("#taContent").val());
                    $("#taContent").val('----   ' + new Date() + '   ------\n' + $("#taContent").val());
                };
            },
            error: function(err) {
                ShowModal(false, 'Something goes wrong with the network, please check it out.')
            }
        });
    };
});
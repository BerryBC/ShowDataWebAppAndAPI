/*
 * @Descripttion: 判断情绪问题
 * @Author: BerryBC
 * @Date: 2020-05-01 23:49:57
 * @LastEditors: BerryBC
 * @LastEditTime: 2020-05-01 23:53:50
 */
$(function() {
    $('#btnJud')[0].onclick = function() {
        var formData = new FormData();
        formData.append('ct', $("#taContent").val());
        $.ajax({
            url: "/data/judemo/",
            type: "POST",
            dataType: "json",
            data: formData,
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.intBack == 0) {
                    ShowModal(false, 'Something wrong, unable to judgment the emotion.')
                } else if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.')
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.')
                } else if (data.intBack == 1) {
                    ShowModal(true, 'Just judgment the emotion.')
                    $('#lbEMO').val(data.intEMO);
                };
            },
            error: function(err) {
                ShowModal(false, 'Something goes wrong with the network, please check it out.')
            }
        });
    };
});
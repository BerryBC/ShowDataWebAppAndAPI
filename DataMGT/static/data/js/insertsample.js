/*
 * @Descripttion: 上传样本
 * @Author: BerryBC
 * @Date: 2020-02-05 16:56:50
 * @LastEditors  : BerryBC
 * @LastEditTime : 2020-02-05 17:09:52
 */
$(function() {
    CleanSample();

    $('#btnAdd')[0].onclick = function() {
        var formData = new FormData();
        formData.append('e', $("#selEmo").val());
        formData.append('ct', $("#taContent").val());
        $.ajax({
            url: "/data/insertonesample/",
            type: "POST",
            dataType: "json",
            data: formData,
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.intBack == 0) {
                    ShowModal(false, 'Something wrong, unable to insert to Database.')
                } else if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.')
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.')
                } else if (data.intBack == 1) {
                    ShowModal(true, 'Insert success! Yeah!')
                    CleanSample();
                };
            },
            error: function(err) {
                ShowModal(false, 'Something goes wrong with the network, please check it out.')
            }
        });
    };
});

function CleanSample() {
    $('#taContent').val('');
    $('#selEmo').val(0);
    $('#lbID').val('This action is used to insert a new sample');
};
/*
 * @Descripttion: 查看结果
 * @Author: BerryBC
 * @Date: 2020-04-29 22:37:38
 * @LastEditors: BerryBC
 * @LastEditTime: 2020-04-29 23:03:32
 */

$(function() {
    LoadASample();
    $('#btnNext')[0].onclick = function() {
        LoadASample()
    };
});

function LoadASample() {
    $('#taContent').val('');
    $('#selEmo').val(0);
    $('#lbID').val('1024');
    $.ajax({
        url: "/data/clfeddata/",
        type: "POST",
        dataType: "json",
        contentType: false,
        processData: false,
        success: function(data) {
            if (data.intBack == 99) {
                ShowModal(false, 'Request is wrong, please contact the administrator.')
            } else if (data.intBack == 98) {
                ShowModal(false, 'Request is wrong, please login again.')
            } else if (data.intBack == 0) {
                ShowModal(false, 'Unable to find sample, please login again.')
            } else if (data.intBack == 1) {
                // console.log(data.listUsr);
                ShowSample(data.dictData);
            };
        },
        error: function(err) {
            ShowModal(false, 'Something goes wrong with the network, please check it out.')
        }
    });
};

function ShowSample(objSample) {
    $('#taContent').val(objSample.ct);
    $('#selEmo').val(objSample.e);
    $('#lbID').val(objSample._id);
};;
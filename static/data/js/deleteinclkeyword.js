/*
 * @Descripttion: 
 * @Author: BerryBC
 * @Date: 2020-02-07 11:12:51
 * @LastEditors  : BerryBC
 * @LastEditTime : 2020-02-07 12:51:27
 */
$(function() {
    CleanSample();
});

function CleanSample() {
    $('#taContent').val('');
};


$('#divDeleteKeyWord').on('show.bs.modal', function(event) {
    var strKW = $('#txtKeyWord').val();
    var modal = $(this)
    $("#h5DeleteKeyWordTitle").text("Delete Sample with Keyword '" + strKW + "'");
    $("#lbDeleteKeyWord").text("Sure Delete Keyword '" + strKW + "' ?");
    modal.find('#btnCDelete').click(function() {
        var formData = new FormData();
        modal.find('#btnCDelete').unbind("click");
        formData.append('kw', strKW);
        $.ajax({
            url: "/data/deletesamplewithkw/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                modal.modal('hide');
                if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.');
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.');
                } else if (data.intBack == 0) {
                    ShowModal(false, 'Error, please check it out.');
                } else if (data.intBack == 1) {
                    ShowModal(true, 'OK! You just delete ' + data.intDeleteCount + ' datas.');
                    CleanSample();
                } else {
                    ShowModal(false, 'You can\'t make it! Try it again!');
                };
            },
            error: function(err) {
                modal.modal('hide');
                ShowModal(false, 'Something goes wrong with the network, please check it out.');
            }
        });
    });
});
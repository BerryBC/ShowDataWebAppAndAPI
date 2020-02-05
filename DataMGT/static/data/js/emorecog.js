/*
 * @Descripttion: 
 * @Author: BerryBC
 * @Date: 2020-02-05 14:11:33
 * @LastEditors  : BerryBC
 * @LastEditTime : 2020-02-05 15:45:00
 */
$(function() {
    LoadASample();

    $('#btnAdd')[0].onclick = function() {
        var formData = new FormData();
        formData.append('e', $("#selEmo").val());
        formData.append('id', $("#lbID").val());
        $.ajax({
            url: "/data/confirmsample/",
            type: "POST",
            dataType: "json",
            data: formData,
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.intBack == 0) {
                    ShowModal(false, 'Something wrong, unable to update Database.')
                } else if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.')
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.')
                } else if (data.intBack == 1) {
                    ShowModal(true, 'Confirm success! Yeah!')
                    LoadASample();
                };
            },
            error: function(err) {
                ShowModal(false, 'Something goes wrong with the network, please check it out.')
            }
        });
    };
});

function LoadASample() {
    $('#taContent').val('');
    $('#selEmo').val(0);
    $('#lbID').val('1024');
    $.ajax({
        url: "/data/randdata/",
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
    $('#selEmo').val(0);
    $('#lbID').val(objSample._id);
};
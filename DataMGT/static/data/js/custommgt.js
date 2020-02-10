$(function() {
    LoadCustomInfo();


    $('#btnAdd')[0].onclick = function() {
        if ($("#txtTag").val() == "" && $("#txtKeyURL").val() == "") {
            ShowModal(false, 'Neither Tag and Key URL could not be BLANK!')
        } else {
            var formData = new FormData();
            formData.append('t', $("#txtTag").val());
            formData.append('u', $("#txtKeyURL").val());
            $.ajax({
                url: "/data/insertcustominfo/",
                type: "POST",
                dataType: "json",
                data: formData,
                contentType: false,
                processData: false,
                success: function(data) {
                    LoadCustomInfo();
                    if (data.intBack == 0) {
                        ShowModal(false, 'Something wrong, unable to insert.')
                    } else if (data.intBack == 1) {
                        ShowModal(false, 'The URL already exists, please double check the URL.')
                    } else if (data.intBack == 99) {
                        ShowModal(false, 'Request is wrong, please contact the administrator.')
                    } else if (data.intBack == 98) {
                        ShowModal(false, 'Request is wrong, please login again.')
                    } else if (data.intBack == 2) {
                        ShowModal(true, 'Insert success! Yeah!')
                        $("#txtTag").val('');
                        $("#txtKeyURL").val('');
                    };
                },
                error: function(err) {
                    ShowModal(false, 'Something goes wrong with the network, please check it out.')
                }
            });
        };
    };
});



function LoadCustomInfo() {
    var intCount = $('#tbCustom')[0].rows.length;
    if (intCount > 1) {
        for (var intI = 1; intI < intCount; intI++) {
            var tdEle = $('#tbCustom')[0].rows[1];
            tdEle.remove();
        };
    };
    $.ajax({
        url: "/data/getallcustominfo/",
        type: "POST",
        dataType: "json",
        contentType: false,
        processData: false,
        success: function(data) {
            if (data.intBack == 99) {
                ShowModal(false, 'Request is wrong, please contact the administrator.')
            } else if (data.intBack == 98) {
                ShowModal(false, 'Request is wrong, please login again.')
            } else if (data.intBack == 1) {
                ListAllCustomToTable(data.arrData)
            } else {
                ShowModal(false, 'Something wrong, unable to get site information.')
            };
        },
        error: function(err) {
            ShowModal(false, 'Something goes wrong with the network, please check it out.')
        }
    });
};


function ListAllCustomToTable(listAllSite) {
    var intNo = 1;
    listAllSite.forEach(function(eleLink) {
        var trRow = $('<tr></tr>');
        trRow.append($('<td></td>').text(intNo));
        trRow.append($('<td></td>').text(eleLink.tag));
        trRow.append($('<td></td>').text(eleLink.rURL));
        var btnDelete = $('<td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-id="' + eleLink._id + '" data-link="' + eleLink.rURL + '" data-target="#divDeleteCustom">Delete URL </button></td>');
        trRow.append(btnDelete);
        $("#tbCustom tbody").append(trRow);
        // console.log(trRow);
        intNo++;
    });
};


$('#divDeleteCustom').on('show.bs.modal', function(event) {
    var btnModalClick = $(event.relatedTarget) // Button that triggered the modal
    var strID = btnModalClick.data('id') // Extract info from data-* attributes
    var strLink = btnModalClick.data('link') // Extract info from data-* attributes
    var modal = $(this)
    $("#h5DeleteCustomTitle").text("Delete Key URL '" + strLink + "'");
    $("#lbDeleteCustom").text("Delete '" + strLink + "'");
    modal.find('#btnCDelete').click(function() {
        var formData = new FormData();
        modal.find('#btnCDelete').unbind("click");
        formData.append('i', strID);
        $.ajax({
            url: "/data/deletecustominfo/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                LoadCustomInfo();
                modal.modal('hide');
                if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.');
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.');
                } else if (data.intBack == 0) {
                    ShowModal(false, 'Wrong URL, please check it out.');
                } else if (data.intBack == 1) {
                    ShowModal(true, 'OK! You just delete the Custom Info.!');
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
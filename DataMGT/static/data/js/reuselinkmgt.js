/*
 * @Descripttion: 可重用链接的管理脚本
 * @Author: BerryBC
 * @Date: 2020-02-05 17:40:46
 * @LastEditors  : BerryBC
 * @LastEditTime : 2020-02-05 20:35:57
 */
$(function() {
    LoadSiteInfo();


    $('#btnAdd')[0].onclick = function() {
        if ($("#txtLink").val() == "") {
            ShowModal(false, 'Link could not be BLANK!')
        } else {
            var formData = new FormData();
            formData.append('u', $("#txtLink").val());
            $.ajax({
                url: "/data/insertnewreusablesite/",
                type: "POST",
                dataType: "json",
                data: formData,
                contentType: false,
                processData: false,
                success: function(data) {
                    LoadSiteInfo();
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
                        $("#txtLink").val('');
                    };
                },
                error: function(err) {
                    ShowModal(false, 'Something goes wrong with the network, please check it out.')
                }
            });
        };
    };
});



function LoadSiteInfo() {
    var intCount = $('#tbSite')[0].rows.length;
    if (intCount > 1) {
        for (var intI = 1; intI < intCount; intI++) {
            var tdEle = $('#tbSite')[0].rows[1];
            tdEle.remove();
        };
    };
    $.ajax({
        url: "/data/getallreuseablesite/",
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
                ListAllSiteToTable(data.arrSite)
            } else {
                ShowModal(false, 'Something wrong, unable to get site information.')
            };
        },
        error: function(err) {
            ShowModal(false, 'Something goes wrong with the network, please check it out.')
        }
    });
};


function ListAllSiteToTable(listAllSite) {
    var intNo = 1;
    listAllSite.forEach(function(eleLink) {
        var trRow = $('<tr></tr>');
        trRow.append($('<td></td>').text(intNo));
        trRow.append($('<td></td>').text(eleLink.url));
        var btnDelete = $('<td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-id="' + eleLink._id + '" data-link="' + eleLink.url + '" data-target="#divDeleteLink">Delete Link </button></td>');
        trRow.append(btnDelete);
        $("#tbSite tbody").append(trRow);
        // console.log(trRow);
        intNo++;
    });
};


$('#divDeleteLink').on('show.bs.modal', function(event) {
    var btnModalClick = $(event.relatedTarget) // Button that triggered the modal
    var strID = btnModalClick.data('id') // Extract info from data-* attributes
    var strLink = btnModalClick.data('link') // Extract info from data-* attributes
    var modal = $(this)
    $("#h5DeleteLinkTitle").text("Delete Site '" + strLink + "'");
    $("#lbDeleteLink").text("Delete Site '" + strLink + "'");
    modal.find('#btnCDelete').click(function() {
        var formData = new FormData();
        modal.find('#btnCDelete').unbind("click");
        formData.append('id', strID);
        $.ajax({
            url: "/data/deletereusablepage/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                LoadSiteInfo();
                modal.modal('hide');
                if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.');
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.');
                } else if (data.intBack == 0) {
                    ShowModal(false, 'Wrong URL, please check it out.');
                } else if (data.intBack == 1) {
                    ShowModal(true, 'OK! You just delete the URL!');
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
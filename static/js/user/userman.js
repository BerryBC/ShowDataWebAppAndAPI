/*
 * @Descripttion: 用户提交用户管理信息作用
 * @Author: BerryBC
 * @Date: 2019-10-26 10:32:26
 * @LastEditors: BerryBC
 * @LastEditTime: 2019-11-23 15:33:28
 */

$(function() {
    LoadUserDetail();


    $('#btnAdd')[0].onclick = function() {
        if ($("#txtUserName").val() == "" || $("#txtPW").val() == "") {
            ShowModal(false, 'User name and passwork could not be BLANK!')
        } else {
            var formData = new FormData();
            formData.append('u', $("#txtUserName").val());
            formData.append('p', md5($("#txtPW").val()));
            formData.append('pl', $("#selPower").val());
            $.ajax({
                url: "/user/userreg/",
                type: "POST",
                dataType: "json",
                data: formData,
                contentType: false,
                processData: false,
                success: function(data) {

                    LoadUserDetail();
                    if (data.intBack == 0) {
                        ShowModal(false, 'Something wrong, unable to register.')
                    } else if (data.intBack == 1) {
                        ShowModal(false, 'The user already exists, please double check the user name.')
                    } else if (data.intBack == 99) {
                        ShowModal(false, 'Request is wrong, please contact the administrator.')
                    } else if (data.intBack == 98) {
                        ShowModal(false, 'Request is wrong, please login again.')
                    } else if (data.intBack == 2) {
                        ShowModal(true, 'Register success! Yeah!')
                    };
                },
                error: function(err) {
                    ShowModal(false, 'Something goes wrong with the network, please check it out.')
                }
            });
        };
    };
});




function ShowModal(bolYoN, strContent) {
    if (bolYoN == true) {
        $('#pMsg').text(strContent);
        $('#modalSuccess').modal('show');
    } else {
        $('#pMsgW').text(strContent);
        $('#modalDanger').modal('show');
    };
};

function LoadUserDetail() {
    var intCount = $('#tbUser')[0].rows.length;
    if (intCount > 1) {
        for (var intI = 1; intI < intCount; intI++) {
            var tdEle = $('#tbUser')[0].rows[1];
            tdEle.remove();
        };
    };
    $.ajax({
        url: "/user/userlist/",
        type: "POST",
        dataType: "json",
        contentType: false,
        processData: false,
        success: function(data) {
            if (data.intBack == 99) {
                ShowModal(false, 'Request is wrong, please contact the administrator.')
            } else if (data.intBack == 98) {
                ShowModal(false, 'Request is wrong, please login again.')
            } else if (data.intBack == 2) {
                // console.log(data.listUsr);
                ListAllUserList(data.listUsr)
            };
        },
        error: function(err) {
            ShowModal(false, 'Something goes wrong with the network, please check it out.')
        }
    });

};



function ListAllUserList(listAllUser) {
    var intNo = 1;
    listAllUser.forEach(function(eleUser) {
        var trRow = $('<tr></tr>');
        trRow.append($('<td></td>').text(intNo));
        trRow.append($('<td></td>').text(eleUser.un));
        if (eleUser.pw == 0) {
            trRow.append($('<td></td>').text('Normal User'));
        } else {
            trRow.append($('<td></td>').text('Admin'));
        };
        var btnResetPW = $('<td><button type="button" class="btn btn-warning btn-sm" data-toggle="modal" data-user="' + eleUser.un + '" data-target="#divResetPasswork" > Reset Passwork </button > </td>');
        var btnResetPower = $('<td><button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-user="' + eleUser.un + '" data-target="#divResetPower"> Reset Power </button></td>');
        var btnDelete = $('<td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-user="' + eleUser.un + '" data-target="#divDeleteUser">Delete User </button></td>');
        trRow.append(btnResetPW);
        trRow.append(btnResetPower);
        trRow.append(btnDelete);
        $("#tbUser tbody").append(trRow);
        intNo++;
    });
};

$('#divResetPasswork').on('show.bs.modal', function(event) {
    var btnModalClick = $(event.relatedTarget) // Button that triggered the modal
    var strUser = btnModalClick.data('user') // Extract info from data-* attributes
    var modal = $(this)
    $("#h5ResetPassworkTitle").text("Reset '" + strUser + "' Passwork");
    $("#lbResetPasswork").text("Reset '" + strUser + "' Passwork");
    modal.find('#btnCReset').click(function() {
        var formData = new FormData();
        modal.find('#btnCReset').unbind("click");
        formData.append('u', strUser);
        formData.append('p', md5($("#inputPasswork").val()));
        $.ajax({
            url: "/user/userrspwd/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                LoadUserDetail();
                modal.modal('hide');
                if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.');
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.');
                } else if (data.intBack == 2) {
                    ShowModal(false, 'Wrong User Name, please check it out.');
                } else if (data.intBack == 1) {
                    ShowModal(true, 'OK! You just reset the password for this user!');
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


$('#divResetPower').on('show.bs.modal', function(event) {
    var btnModalClick = $(event.relatedTarget) // Button that triggered the modal
    var strUser = btnModalClick.data('user') // Extract info from data-* attributes
    var modal = $(this)
    $("#h5ResetPowerTitle").text("User '" + strUser + "' Reset Power to");
    modal.find('#btnCResetPow').click(function() {
        modal.find('#btnCResetPow').unbind("click");
        var formData = new FormData();
        formData.append('u', strUser);
        formData.append('pl', $("#selRePower").val());
        $.ajax({
            url: "/user/userrspw/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                LoadUserDetail();
                modal.modal('hide');
                if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.');
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.');
                } else if (data.intBack == 2) {
                    ShowModal(false, 'Wrong User Name, please check it out.');
                } else if (data.intBack == 3) {
                    ShowModal(false, 'The user cannot be downgrade when there is only one administrator account left!');
                } else if (data.intBack == 1) {
                    ShowModal(true, 'OK! You just reset the power for this user!');
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



$('#divDeleteUser').on('show.bs.modal', function(event) {
    var btnModalClick = $(event.relatedTarget) // Button that triggered the modal
    var strUser = btnModalClick.data('user') // Extract info from data-* attributes
    var modal = $(this)
    $("#h5DeleteUserTitle").text("Delete User '" + strUser + "'");
    $("#lbDeleteUser").text("Delete User '" + strUser + "'");
    modal.find('#btnCDelete').click(function() {
        var formData = new FormData();
        modal.find('#btnCDelete').unbind("click");
        formData.append('u', strUser);
        $.ajax({
            url: "/user/userdel/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                LoadUserDetail();
                modal.modal('hide');
                if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.');
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.');
                } else if (data.intBack == 2) {
                    ShowModal(false, 'Wrong User Name, please check it out.');
                } else if (data.intBack == 1) {
                    ShowModal(true, 'OK! You just delete the user!');
                } else if (data.intBack == 3) {
                    ShowModal(false, 'The user cannot be deleted when there is only one administrator account left!');
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
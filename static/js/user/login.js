/*
 * @Descripttion: 用户登录 JS 文件
 * @version: 0.1.0
 * @Author: BerryBC
 * @Date: 2019-11-18 10:49:25
 * @LastEditors: BerryBC
 * @LastEditTime: 2019-11-18 15:58:12
 */
function ShowModal(bolYoN, strContent) {
    if (bolYoN == true) {
        $('#pMsg').text(strContent);
        $('#modalSuccess').modal('show');
    } else {
        $('#pMsgW').text(strContent);
        $('#modalDanger').modal('show');
    };
};

$('#btnLogIn')[0].onclick = function () {
    if ($("#txtUserName").val() == "" || $("#txtPassword").val() == "") {
        ShowModal(false, 'User name and passwork could not be BLANK!');
    } else {
        var formData = new FormData();
        formData.append('u', $("#txtUserName").val());
        formData.append('p', md5($("#txtPassword").val()));
        $.ajax({
            url: "/user/userlog/",
            type: "POST",
            dataType: "json",
            data: formData,
            contentType: false,
            processData: false,
            success: function (data) {
                if (data.intBack == 0) {
                    ShowModal(false, 'Something wrong, unable to login.');
                } else if (data.intBack == 1) {
                    self.location.href="/";
                };
            },
            error: function (err) {
                ShowModal(false, 'Something goes wrong with the network, please check it out.');
            }
        });
    };
};
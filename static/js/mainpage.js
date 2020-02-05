/*
 * @Descripttion: 主页的 JS 程序
 * @version: 0.1.0
 * @Author: BerryBC
 * @Date: 2019-12-09 15:26:33
 * @LastEditors  : BerryBC
 * @LastEditTime : 2019-12-24 14:10:09
 */
function funLogout() {
    document.cookie = 'ut=0;path=/;expires=' + new Date(0).toUTCString();
    document.cookie = 'un=0;path=/;expires=' + new Date(0).toUTCString();
    window.location.href = "/user/login";
};

function ShowModal(bolYoN, strContent) {
    if (bolYoN == true) {
        $('#pMsg').text(strContent);
        $('#modalSuccess').modal('show');
    } else {
        $('#pMsgW').text(strContent);
        $('#modalDanger').modal('show');
    };
};
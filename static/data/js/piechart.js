/*
 * @Descripttion: 展示页面
 * @Author: BerryBC
 * @Date: 2020-05-21 22:13:31
 * @LastEditors: BerryBC
 * @LastEditTime: 2020-05-31 13:57:11
 */
var gobjData = {};
var chartPie = echarts.init(document.getElementById('divPieChart'));
$(function() {
    $('#btnSearch')[0].onclick = function() {
        var strKW = $('#txtKW').val();
        var formData = new FormData();
        formData.append('kw', strKW);
        $.ajax({
            url: "/data/kwemo/",
            type: "POST",
            dataType: "json",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                if (data.intBack == 99) {
                    ShowModal(false, 'Request is wrong, please contact the administrator.');
                } else if (data.intBack == 98) {
                    ShowModal(false, 'Request is wrong, please login again.');
                } else if (data.intBack == 0) {
                    ShowModal(false, 'Error, please check it out.');
                } else if (data.intBack == 1) {

                    InsertSelector(data.arrKWsEMO);
                } else {
                    ShowModal(false, 'You can\'t make it! Try it again!');
                };
            },
            error: function(err) {
                ShowModal(false, 'Something goes wrong with the network, please check it out.');
            }
        });
    };


    $('#selKW').change(function() { SelectKW() });
    $('#selKW').click(function() { SelectKW() });
});

function InsertSelector(arrKWs) {
    gobjData = {};
    var selKW = $('#selKW');
    selKW.empty();

    if (arrKWs.length > 0) {
        for (var intI = 0; intI < arrKWs.length; intI++) {
            gobjData[arrKWs[intI].kw] = arrKWs[intI].num;
            selKW.append('<option value="' + arrKWs[intI].kw + '">' + arrKWs[intI].kw + '</option>');
        };
    } else {
        ShowModal(false, 'None record for this keyword');
        selKW.append('<option value="-1" selected>Non of this Key Word in database</option>');
    };
};

function SelectKW() {

    if ($('#selKW').val() == "-1") {
        ShowModal(false, 'None record for this keyword');
    } else {
        optPie = {
            title: {
                text: $('#selKW').val(),
                left: 'center',
                top: 'center',
                textStyle: {
                    fontSize: 38
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%)'
            },

            series: [{
                name: '词语好坏',
                type: 'pie',
                hoverAnimation: true,
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    position: 'outer',
                    alignTo: 'labelLine',
                    bleedMargin: 5
                },
                data: [
                    { value: 0, name: '正面文章', itemStyle: { color: "#91c7ae" } },
                    { value: 0, name: '反面文章', itemStyle: { color: "#c23531" } },
                    { value: 0, name: '无意义文章', itemStyle: { color: "#2f4554" } }
                ]
            }]
        };
        chartPie.setOption(optPie);
        setTimeout(() => {
            optPie = {
                title: {
                    text: $("#selKW").val(),
                    left: 'center',
                    top: "center",
                    textStyle: {
                        fontSize: 38
                    }
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                series: [{
                    name: '词语好坏',
                    type: 'pie',
                    hoverAnimation: true,
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: false,
                    label: {
                        position: 'outer',
                        alignTo: 'labelLine',
                        bleedMargin: 5
                    },
                    data: [
                        { value: gobjData[$("#selKW").val()][2], name: '正面文章', itemStyle: { color: "#91c7ae" } },
                        { value: gobjData[$("#selKW").val()][0], name: '反面文章', itemStyle: { color: "#c23531" } },
                        { value: gobjData[$("#selKW").val()][1], name: '无意义文章', itemStyle: { color: "#2f4554" } }
                    ]
                }]
            };
            chartPie.setOption(optPie);
        }, 100);
    };
};
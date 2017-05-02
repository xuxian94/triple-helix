$(document).ready(function () {

    // 点击用户信息面板
    $('.panel-user').click(function () {
        var companyId = $(this).children('h3').attr('class');
        var data = {
            "companyId": companyId,
            "buff": '0'
        }
        if ($(this).hasClass('panel-user-check')) {
            $(this).removeClass('panel-user-check');
            data.buff = 0;
            $.ajax({
                type: 'GET',
                url: './order_confirm',
                data: data,
                dataType: 'json',
            })
        } else {
            $(this).addClass('panel-user-check');
            data.buff = 1;
            $.ajax({
                type: 'GET',
                url: './order_confirm',
                data: data,
                dataType: 'json',

            })
        }
    })



    // 点击“提交”按钮
    $('#submit-user').click(function () {
        location.href = './order_confirm';
    })
})
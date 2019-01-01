function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });
    $(".form-login").submit(function(e){
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();
        if (!mobile) {
            $("#mobile-err span").html("请填写正确的手机号！");
            $("#mobile-err").show();
            return;
        } 
        if (!passwd) {
            $("#password-err span").html("请填写密码!");
            $("#password-err").show();
            return;
        }
        // 调用ajax向后端发送注册请求
        var req_data = {
            mobile: mobile,
            password: passwd,
        }
        var req_json = JSON.stringify(req_data)
        $.ajax({
            url: "/api/v1.0/sessions",
            type: "post",
            data: req_json,
            contentType: "application/json",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },// 请求头,将csrf_token值放到请求头中，方便后端csrf进行验证
            success: function (resp) {
                if (resp.errno == "0") {
                    location.href = "/index.html"
                } else {
                    // 其他错误信息,在页面中展示
                    $("#password-err span").html(resp.errmsg)
                    $("#password-err").show()
                }
            }
        })
    });
})
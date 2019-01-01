function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

// 点击推出按钮时执行的函数
function logout() {
    $.ajax({
        url: "/api/v1.0/session",
        type: "delete",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        dataType: "json",
        success: function (resp) {
            if ("0" == resp.errno) {
                location.href = "/index.html";
            }
        }
    });
}

$(document).ready(function(){
})
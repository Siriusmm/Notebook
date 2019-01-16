$(function () {
    $username=$("#input_username");
    $info=$("#info");
    $username.blur(function () {
        var user_name=$username.val();
        $.ajax(
            {
                url:"/check/",
                data:{"username":user_name},
                dataType:'json',
                type:"get",
                async:'true',
                success:function (data,status,xhr) {
                    console.log(data);
                    var data=data.msg;
                    console.log(data);
                    if(data=="ok"){
                        $info.html("用户名可用");
                        $info.css({"color":"red","font-size":"12px"})
                    }else{
                            $info.html("该用户名已被占用");
                            $info.css("color","green");
                        }
                },
                error:function (xhr,status,erro) {
                    console.log(erro);
                }

            }
        )
    })
})
$(function () {
    content=$(".enter");
    content.click(function () {
        $id=$("#title");
        console.log(content.html());
        notes=$("#notes");
        $.ajax(
            {
                url:"/getcontent/",
                data:{"title":content.html()},
                dataType:'json',
                type:"get",
                async:'true',
                success:function (data,status,xhr) {
                    var data=data.content;
                    $title.val(content.html());
                    notes.html(data);
                },
                error:function (xhr,status,erro) {
                    console.log(erro);
                }

            }
        )
    });
})
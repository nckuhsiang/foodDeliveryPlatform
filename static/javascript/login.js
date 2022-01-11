$(function(){
    $("#login").click(function(){
        let account = $("#account").val();
        let password = $("#password").val();
        data = {
            account:account,
            password:password
        };
        url = 'loginUrl';
        $.post(url, data,function(data){
            console.log(data)
            if(data == "True"){
                alert("登入成功")
            }
            else{
                alert("帳號密碼錯誤")
            }
        });
    });

});

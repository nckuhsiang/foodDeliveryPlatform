$(function () {
    $("#register").click(function () {
        let name = $("#name").val()
        let gender = $("input[name=gender]:checked").val()
        let account = $("#account").val()
        let password = $("#password").val()
        let again = $("#again").val()
        let birthday = $("#birthday").val()
        let phone = $("#phone").val()
        let address = $("#address").val()
        let email = $("#email").val()
        let agree = $("#read").is(':checked')
        if(!checkAgreement(agree)){
            alert("請勾選下方同意")
            return
        }
        if(!checkAllData(name, gender, account, password, birthday, phone, address, email)) {
            alert("請確實填寫所有資料")
            return
        }
        if(!checkPassword(password, again)) {
            alert("請在確認一次密碼")
            return
        }
        let user = {
            name: name,
            gender: gender,
            account: account,
            password: password,
            birthday: birthday,
            phone: phone,
            address: address,
            email: email
        }
        let url = "registerUrl"
        $.post(url, user, function (data) {
            if(data=="success")
                alert("註冊成功")

            else
                alert("發生不可預期的錯誤")
        })
    });
    $("#test").click(function(){
        let account = $("#account").val()
        let data = { account: account }
        let url = 'checkAccountValid'
        var state = false
        $.get(url, data, function (data) {
            if (data == "True"){
                $("#result").text("------------------帳號已核准------------------")
                $("#result").css("color","white")
                $("#register").removeAttr('disabled');
            }
            else {
                $("#result").text("------------------帳號已存在------------------")
                $("#result").css("color","red")
                $("#register").attr('disabled',true);
            }
        })
    });
    // $.get doesn't return the return value of the callback function. It returns the XHR object. 
    // Second, the get function isn't synchronous, it's asynchronous so showGetResult will likely return before get completes. 
    // Third, you can't return something from inside the callback to the outer scope. You can, however, bind a variable in the outer scope and set it in the callback.
    function checkAllData(name, gender, account, password, birthday, phone, address, email) {
        if (name && account && password && birthday && phone && address && email && gender)
            return true
        return false
    }
    function checkPassword(password, again) {
        if (password == again)
            return true
        return false
    }
    function checkAgreement(agree) {
        if(agree == "1")
            return true
        return false
    }
    $("#test").click(function(){
        let account = $("#account").val()
        test = checkAccountValid(account)   
    }); 
});
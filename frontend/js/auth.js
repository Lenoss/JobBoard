
$(document).ready(function () {
    $("#society-form").hide();

    $("#society").click(function (e){
        $("#society-form").toggle();
    })

});

$("#login-form").submit(function(e) {
    e.preventDefault()
    var username = $("#username").val()
    var password = $("#password").val()
    
    var items = {};
    items["username"] = username;
    items["password"] = password;

    $.ajax({
        url: 'http://127.0.0.1:5000/api/auth/login',
        dataType: 'json',
        type: 'POST',
        crossDomain: true,
        data: items,
        success: function( data ){
            console.log(data);
        },
        error: function( error ){
            if(error.responseText != undefined)
                var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            else
                var msg = "Une erreur est survenue"
            noty(msg, "error")
        }
    });
})

$("#register-log").submit(function(e) {
    e.preventDefault()
    var username = $("#username").val()
    var password = $("#password").val()
    var confirme_password = $("#confirme_password")
    var email = $("#email").val()
    $cb = $('input#society');
    var company_title = $("#title").val();
    var phone = $("#phone").val();
    var logo = $("#logo").val();

    var items = {};
    items["username"] = username;
    items["password"] = password;
    items["confirme_password"] = confirme_password;
    items["email"] = email;
    items["company_is_valide"] = cb;
    items["company_title"] = company_title;
    items["phone"] = phone;
    items["logo"] = logo;

    $.ajax( {
        url:"http://127.0.0.1:5000/api/auth/",
        
        type:"POST",
        crossDomain:true,
        dataType:"json",
        ata:JSON.stringify($(this).serialize()),
    })
})
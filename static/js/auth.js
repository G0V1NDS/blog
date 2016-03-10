var auth = {
        afterLogin : function(response){
            console.log(response);
        }
    };

$('#login').validate({
       rules: {
            "text": {
                required: true,
            },
            "password": {
                required: true,
                minlength : 6
            }
       },
       submitHandler: function(form) {
            var data = {};
            alert('validating');
            $(form).serializeArray().map(function(x){data[x.name] = x.value;});

           var ajax_url = base_url+'/login/';
           //ajaxFactory.ajaxHandler(ajax_url, 'POST', data, auth.afterLogin)
           $.post()
       }

    });

$('#login_btn').on('click', function(){
        var signupModal = $('#signupModal');
        signupModal.modal('hide');
        signupModal.on('hidden.bs.modal',function(){
            $('#loginModal').modal('show')
        })
    });
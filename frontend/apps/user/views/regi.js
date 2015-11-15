define([
        'marionette',
],
function(
        Mn
) {
    var Regi = Mn.ItemView.extend({
        template: JST['regi'],
        ui: {
            name : '#name',
            email: '#email',
            password: '#password',
            submit: '#create',
        },
        events: {
            'click @ui.submit': 'submit',
        },

        submit: function(e){
            if(this.ui.name.val() == ''
                || this.ui.email.val() == ''
                || this.ui.password.val() == '')
            return;

            $.post('/user/create/',
            {
                name : this.ui.name.val(),
                email: this.ui.email.val(),
                password: this.ui.password.val()
            })
            .done(function(){
                alert('Added')
                app.router.navigate('login', { trigger : true})
            })
            .fail(function(response){
                if(response.status == 503)
                {
                    alert('user already exists')
                }
                else if (response.status == 500)
                {
                    alert('something went wrong')
                }
            })
        }
    })
    return Regi;
});

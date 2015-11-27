define([
        'marionette',
        'apps/user/models/session',
        'apps/user/models/user',

],
function(
        Mn,
        Session,
        User
) {
    var Login = Mn.ItemView.extend({
        template: JST['login'],
        model: new User(),
        ui: {
            email: '#email',
            password: '#password',
            submit: '#create',
        },
        events: {
            'click @ui.submit': 'submit',
        },

        submit: function(e){
            if(this.ui.email.val() == ''
                || this.ui.password.val() == '')
            return;
            var _this = this;
            $.post('/user/login/',
            {
                email: this.ui.email.val(),
                password: this.ui.password.val()
            })
            .done(function(response){
                response = JSON.parse(response)
                var session = new Session().set_token(access_token = response.access_token )
                _this.model.set_profile(profile = response.profile)

                app.router.navigate('leads/all', { trigger : true})
            })
            .fail(function(response){
                if(response.status == 503)
                {
                    alert('signup if not yet or try login again')
                }
                else if (response.status == 500)
                {
                    alert('something went wrong')
                }
            })
        }

    })
    return Login
});

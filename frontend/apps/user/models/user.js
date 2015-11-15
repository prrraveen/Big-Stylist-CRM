define([
        'backbone',
        'apps/user/models/session',
],
function(
        Backbone,
        Session
) {
    var User = Backbone.Model.extend({
        initialize: function () {
            this.session = new Session();
        },

        logged_in: function () {
            if (this.session.authenticated() && this.get_profile() !== undefined) {
                return true;
            } else {
                return false;
            }
        },

        get_profile: function () {
            return JSON.parse(window.localStorage.getItem('profile'));
        },

        set_profile: function (profile) {
            return window.localStorage.setItem('profile', JSON.stringify(profile));
        },

        get_name: function () {
            var profile = JSON.parse(window.localStorage.getItem('profile'));
            return profile.name;
        },

        logout: function () {
            var _this = this;
            $.ajax({
                url: '/logout/',
                type: 'GET',
                success: function (shortlist_response) {
                    _this.session.clean();
                    _this.clean_localstorage();
                },
            });
        },

        clean_localstorage: function () {
            window.localStorage.removeItem('profile');
        },

    })
    return User;
});

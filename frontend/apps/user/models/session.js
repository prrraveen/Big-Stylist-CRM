define(['backbone',
        'jquery',
        ],
function(Backbone,
        $
) {
    var Session = Backbone.Model.extend({
        defaults: {
            access_token:null,
        },
        initialize: function() {
            this.load();
        },

        load: function() {
            try {
                this.access_token = window.localStorage.getItem('access_token');
            }
            catch (e) {
                this.access_token = null;
            }
        },

        authenticated: function() {
            if (this.access_token) {
                return true;
            } else {
                return false;
            }
        },

        set_token: function(access_token) {
            window.localStorage.setItem('access_token', access_token);
            this.load();
        },

        clean: function() {
            window.localStorage.removeItem('access_token');
            this.load();
        },
    });
    return Session;
});

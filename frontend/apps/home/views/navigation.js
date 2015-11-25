define([
        'marionette',
        'apps/user/models/user',
        'bootstrap',
        'offcanvas',
],
function(
        Mn,
        User,
        Bootstrap,
        Offcanvas
) {
    var Navigation = Mn.ItemView.extend({
        model: new User(),
        template: JST['navigation'],
        templateHelpers: function() {
            return { user : this.model};
        },
        ui:{
            sidebar : '.main-sidebar',
            toggle:   '.sidebar-toggle',
        },

        events:{
            'click @ui.toggle': 'toggle',
        },

        toggle: function(){
            this.ui.sidebar.offcanvas('toggle')
        },
        onRender: function(){
            this.ui.sidebar.offcanvas('show')
        },

    })
    return Navigation;
});

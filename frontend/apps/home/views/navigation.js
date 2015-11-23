define([
        'marionette',
        'apps/user/models/user',
        'offcanvas',
],
function(
        Mn,
        User,
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
            toggle:   '.sidebar-toggle'
        },

        events:{
            'click @ui.toggle': 'toggle'
        },

        onRender: function(){
            this.ui.sidebar.offcanvas()
        },

        toggle: function(){
            this.ui.sidebar.offcanvas('toggle')
        }
    })
    return Navigation;
});

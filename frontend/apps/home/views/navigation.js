define([
        'marionette',
        'apps/user/models/user',
        'dashboard_theme',
],
function(
        Mn,
        User,
        Dashboard_theme
) {
    var Navigation = Mn.ItemView.extend({
        model: new User(),
        template: JST['navigation'],
        templateHelpers: function() {
            return { user : this.model};
        }
    })
    return Navigation;
});

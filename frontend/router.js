define([
        'marionette',
        'backbone',
        'apps/home/views/home',
        'apps/user/views/regi',
        'apps/user/views/login',

        'assets/templates',
        'bootstrap'
],
function(
        Mn,
        Backbone,
        Home,
        Regi,
        Login
) {
    var Router = Marionette.AppRouter.extend({
    // "someMethod" must exist at controller.someMethod
        // controller:  ,
        routes: {
            'regi':  function(){app.layout.main_region.show(new Regi())},
            'login': function(){app.layout.main_region.show(new Login())},
        },
    })
    return Router;
});

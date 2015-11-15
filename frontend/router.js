define([
        'marionette',
        'backbone',
        'apps/home/views/home',
        'apps/user/views/regi',

        'assets/templates',
        'bootstrap'
],
function(
        Mn,
        Backbone,
        Home,
        Regi
) {
    var Router = Marionette.AppRouter.extend({
    // "someMethod" must exist at controller.someMethod
        // controller:  ,
        routes: {
            'regi':  function(){window.app.layout.main_region.show(new Regi())},
            
        },
    })
    return Router;
});

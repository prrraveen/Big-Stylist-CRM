define([
        'marionette',
        'backbone',
        'apps/user/views/regi',
        'apps/user/views/login',
        'apps/home/views/navigation',
        'apps/home/views/dashboard',
        'apps/user/models/user',
        'apps/orders/views/orders',

        'assets/templates',
        'bootstrap'
],
function(
        Mn,
        Backbone,
        Regi,
        Login,
        Navigation,
        Dashboard,
        User,
        Orders
) {
    var Router = Marionette.AppRouter.extend({
    // "someMethod" must exist at controller.someMethod
        // controller:  ,
        routes: {
            'regi':  'regi',
            'login': 'login',
            'dashboard': 'dashboard',
            'logout': 'logout',
            'orders/:type': 'orders',
        },

        regi : function(){
            app.layout.navigation.empty();
            app.layout.main_region.show(new Regi())
        },

        login : function(){
            app.layout.navigation.empty();
            app.layout.main_region.show(new Login())
        },

        dashboard : function(){
            app.layout.navigation.show(new Navigation());
            app.layout.main_region.show(new Dashboard());
        },

        logout : function(){
            new User().logout();
            app.layout.navigation.empty();
            app.layout.main_region.empty();
            app.router.navigate('login', { trigger : true});
        },
        orders : function(type){
            app.layout.navigation.show(new Navigation());
            app.layout.main_region.show(new Orders({suffix : type}));
        }
    })
    return Router;
});

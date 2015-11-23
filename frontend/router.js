define([
        'marionette',
        'backbone',
        'apps/user/views/regi',
        'apps/user/views/login',
        'apps/home/views/navigation',
        'apps/user/models/user',
        'apps/orders/views/orders',
        'apps/detail/views/detail',
        'apps/orders/models/order',

        'assets/templates',
        'bootstrap'
],
function(
        Mn,
        Backbone,
        Regi,
        Login,
        Navigation,
        User,
        Orders,
        Detail,
        Order
) {
    var Router = Marionette.AppRouter.extend({
        routes: {
            'regi':  'regi',
            'login': 'login',
            'dashboard': 'dashboard',
            'logout': 'logout',
            'orders/:type': 'orders',
            'detail/:order_id': 'detail',
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
        },
        detail : function(order_id){
            app.layout.navigation.show(new Navigation());

            var order = new Order({id: order_id})
            order.fetch({
                success : function(model, response ,options){
                    // app.layout.main_region.show(new Detail({model : order}));
                }
            })
        }
    })
    return Router;
});

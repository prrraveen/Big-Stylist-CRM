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
        'apps/leads/views/leads',

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
        Order,
        Leads
) {
    var Router = Marionette.AppRouter.extend({
        routes: {
            '':     'home',
            'regi':  'regi',
            'login': 'login',
            'logout': 'logout',
            'orders/:type': 'orders',
            'detail/:order_id': 'detail',
            'leads/:type': 'leads',
        },

        home: function(){
            this.navigate('leads/all',{trigger:true})
            return
        },
        
        regi : function(){
            app.layout.navigation.empty();
            app.layout.main_region.show(new Regi())
        },

        login : function(){
            app.layout.navigation.empty();
            app.layout.main_region.show(new Login())
        },

        orders : function(type){
            if(!new User().logged_in()){
                this.navigate('login',{trigger:true})
                return
            }
            app.layout.navigation.show(new Navigation());
            app.layout.main_region.show(new Orders({suffix : type}));
        },

        leads: function(type){
            if(!new User().logged_in()){
                this.navigate('login',{trigger:true})
                return
            }
            app.layout.navigation.show(new Navigation());
            app.layout.main_region.show(new Leads({suffix: type}));
        },

        detail : function(order_id){
            if(!new User().logged_in()){
                this.navigate('login',{trigger:true})
                return
            }

            app.layout.navigation.show(new Navigation());

            var order = new Order({id: order_id})
            order.fetch({
                success : function(model, response ,options){
                    app.layout.main_region.show(new Detail({model : order}));
                }
            })
        },

        logout : function(){
            new User().logout();
            app.layout.navigation.empty();
            app.layout.main_region.empty();
            app.router.navigate('login', { trigger : true});
        },
    })
    return Router;
});

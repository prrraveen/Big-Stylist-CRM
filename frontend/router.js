define([
        'marionette',
        'assets/templates',
],
function(
        Mn
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
            require(['apps/user/views/regi',
            ],function(Regi){
                app.layout.navigation.empty();
                app.layout.main_region.show(new Regi())
            })
        },

        login : function(){
            require(['apps/user/views/login',
            ],function(Login){
                app.layout.navigation.empty();
                app.layout.main_region.show(new Login())
            })
        },

        orders : function(type){
            require([
                    'apps/home/views/navigation',
                    'apps/user/models/user',
                    'apps/orders/views/orders',
            ],function( Navigation,
                        User,
                        Orders
                      ){
                if(!new User().logged_in()){
                    this.navigate('login',{trigger:true})
                    return
                }
                app.layout.navigation.show(new Navigation());
                app.layout.main_region.show(new Orders({suffix : type}));
            })
        },

        leads: function(type){
            require([
                    'apps/home/views/navigation',
                    'apps/user/models/user',
                    'apps/leads/views/leads',
            ],function( Navigation,
                        User,
                        Leads
                      ){
                      if(!new User().logged_in()){
                          this.navigate('login',{trigger:true})
                          return
                      }
                      app.layout.navigation.show(new Navigation());
                      app.layout.main_region.show(new Leads({suffix: type}));
            })
        },

        detail : function(order_id){
            require([
                    'apps/home/views/navigation',
                    'apps/user/models/user',
                    'apps/detail/views/detail',
                    'apps/orders/models/order',
            ],function( Navigation,
                        User,
                        Detail,
                        Order
                      ){
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
            })

        },

        logout : function(){
            require([
                    'apps/user/models/user',
            ],function(
                        User
                      ){
              new User().logout();
              app.layout.navigation.empty();
              app.layout.main_region.empty();
              app.router.navigate('login', { trigger : true});
            })
        },
    })
    return Router;
});

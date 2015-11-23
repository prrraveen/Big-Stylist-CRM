define([
        'backbone',
        'apps/orders/models/order',
],
function(
        Backbone,
        Order
) {
    return Backbone.Collection.extend({
        model: Order,
        set_url : function(suffix){
            this.url = '/leads/'
        }
    })
});
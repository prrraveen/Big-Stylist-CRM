define([
        'backbone',
        'apps/orders/models/order',
],
function(
        Backbone,
        Order
) {
    var Orders = Backbone.Collection.extend({
        model: Order,
        set_url : function(suffix){
            this.url = '/orders/' + suffix + '/';
        }
    })
    return Orders;
});

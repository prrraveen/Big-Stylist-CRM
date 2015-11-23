define([
        'marionette',
        'apps/orders/views/order_itemView',
        'apps/orders/views/no_orders',
        'apps/orders/collections/orders_collection',
],
function(
        Mn,
        Order_itemView,
        No_orders,
        Orders_collection
) {
    var Orders = Mn.CompositeView.extend({
        initialize: function(options){
            this.collection = new Orders_collection();
            this.collection.set_url(suffix = options.suffix)
            this.collection.fetch();
        },
        childView: Order_itemView,
        // emptyView: No_orders,
        template: JST['orders'],
        childViewContainer: 'tbody',
    })

    return Orders;
});

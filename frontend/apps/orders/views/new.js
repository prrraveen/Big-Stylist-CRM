define([
        'marionette',
        'apps/orders/views/order_itemView',
        'apps/orders/views/no_orders',
        'apps/orders/collections/orders',
],
function(
        Mn,
        Order_itemView,
        No_orders,
        Orders
) {
    var New_orders = Mn.CompositeView.extend({
        initialize: function(){
            this.collection = new Orders();
            this.collection.set_url(suffix = 'new')
            this.collection.fetch();
        },
        childView: Order_itemView,
        emptyView: No_orders,
        template: JST['new_orders'],
        childViewContainer: 'tbody',
    })

    return New_orders;
});

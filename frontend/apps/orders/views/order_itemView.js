define([
        'marionette',
        'apps/orders/models/order',
],
function(
        Mn,
        Order
) {
    var Order_itemView = Mn.ItemView.extend({
        template: JST['order_itemView'],
        tagName: 'tr'
    })
    return Order_itemView;
});

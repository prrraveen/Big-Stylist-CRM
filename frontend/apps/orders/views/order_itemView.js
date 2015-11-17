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
        tagName: 'tr',
        attributes : function () {
           // Return model data
           return {
             id : this.model.get('id'),
             class: 'pointer'
           };
         }
    })
    return Order_itemView;
});

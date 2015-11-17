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
       },
       ui: {
           col: 'td'
       },
       events:{
           'click @ui.col': 'navigate_to_detail'
       },
       navigate_to_detail: function(){
           var fragment = 'detail/' + this.ui.col.parent()[0].id
           app.router.navigate(fragment , {trigger : true})
       }

    })
    return Order_itemView;
});

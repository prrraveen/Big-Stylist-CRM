define([
        'marionette',
        'apps/orders/models/order',
],
function(
        Mn,
        Order
) {
    return Mn.ItemView.extend({
        template: JST['lead_itemView'],
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
           'click @ui.col': 'navigate'
       },
       navigate: function(){
           var fragment = '/admin/agent/lead/' + this.ui.col.parent()[0].id + '/'
           document.location = fragment
       }

    })
});

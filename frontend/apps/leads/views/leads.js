define([
        'marionette',
        'apps/leads/views/lead_itemView',
        'apps/orders/views/no_orders',
        'apps/leads/collections/lead_collections',
],
function(
        Mn,
        Lead_itemView,
        No_orders,
        Lead_collection
) {
    return Orders = Mn.CompositeView.extend({
        initialize: function(options){
            this.collection = new Lead_collection();
            this.collection.fetch();
        },
        childView: Lead_itemView,
        emptyView: No_orders,
        template: JST['leads'],
        childViewContainer: 'tbody',
    })

});

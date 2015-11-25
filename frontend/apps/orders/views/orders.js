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
            this.collection.bind('reset', this.render);
            this.collection.set_url(suffix = options.suffix)
            var _this = this
            this.collection.fetch().then(function() {
               _this.render();
             });
        },
        childView: Order_itemView,
        emptyView: No_orders,
        template: JST['orders'],
        childViewContainer: 'tbody',

        templateHelpers: function(){
            return {
                state : this.collection.state
            }
        },

        ui:{
            search_name : '#search-name',
            search_contact : '#search-contact',
            name:    'input#name',
            contact: 'input#contact',
            remove_filters : '#remove-filters'
        },
        events:{
            'click @ui.search_name' : 'search_name',
            'click @ui.search_contact' : 'search_contact',
            'click @ui.remove_filters' : 'remove_filters',
        },

        search_name: function(){
            var name = this.ui.name.val().trim()
            if(!name)
                return

            var _this = this
            $.get('/search/orders/name/',
            {
                name: name,
            })
            .done(function(data){
                _this.collection.reset(data)
            })
            .fail(function(){
                alert('no result found with , Name ='+name)
            })
        },
        search_contact: function(){
            var contact = this.ui.contact.val().trim()
            if(!contact)
                return
            var _this = this
            $.get('/search/orders/contact/',
            {
                contact: contact,
            })
            .done(function(data){
                _this.collection.reset(data)
            })
            .fail(function(){
                alert('no result found with , Contact ='+contact)
            })
        },

        remove_filters: function(){
            debugger
            this.collection.fetch()
            this.render()
        }
    })

    return Orders;
});

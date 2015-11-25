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
            this.collection.bind('reset', this.render);
            this.collection.set_url(suffix = options.suffix)
            var _this = this
            this.collection.fetch().then(function() {
               _this.render();
            });
        },
        childView: Lead_itemView,
        emptyView: No_orders,
        template: JST['leads'],
        childViewContainer: 'tbody',
        templateHelpers: function(){
            return {
                state : this.collection.state,
                collection: this.collection
            }
        },

        ui:{
            search_name : '#search-name',
            search_contact : '#search-contact',
            name:    'input#name',
            contact: 'input#contact',
            remove_filters : '#remove-filters',
            page: '.page',
        },
        events:{
            'click @ui.search_name' : 'search_name',
            'click @ui.search_contact' : 'search_contact',
            'click @ui.remove_filters' : 'remove_filters',
            'click @ui.page' : 'get_page',
        },

        search_name: function(){
            var name = this.ui.name.val().trim()
            if(!name)
                return

            var _this = this
            $.get('/search/leads/name/',
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
            $.get('/search/leads/contact/',
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
            this.collection.fetch()
            this.render()
        },

        get_page: function(e){
            page = +e.target.id
            var _this = this
            this.collection.getPage(page).done(function(){
                _this.render()
            })
        }
    })

});

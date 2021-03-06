define([
        'backbone',
        'paginator',

        'apps/orders/models/order',
],
function(
        Backbone,
        paginator,

        Order
) {
    return Backbone.PageableCollection.extend({
        model: Order,
        set_url : function(suffix){
            this.url = '/leads/' + suffix + '/';
        },

        state: {
            firstPage: 1,
        },
        
        queryParams: {
          currentPage: "current_page",
        },

        parseState: function (response, queryParams, state, options) {
           return {totalRecords: response.state.totalRecords};
        },
        // get the actual records
        parseRecords: function (response, options) {
            return response.payload;
        }
    })
});

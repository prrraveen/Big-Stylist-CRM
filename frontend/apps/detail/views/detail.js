define([
        'marionette',
        'select2',
],
function(
        Mn,
        select2
) {
    var Detail = Mn.ItemView.extend({
        template: JST['detail'],
        templateHelpers:function(){
            return {
                order_status: this.get_order_status(),
                allocation_status_dict: this.get_allocation_data()
            }
        },
        ui : {
            search_beautician: '#search-beautician',
            status_change:     '#status-change',
            reallocation:      '#reallocation',
        },
        events: {
            'change @ui.search_beautician': 'allocate_manually',
            'change @ui.status_change':     'on_status_change',
            'click @ui.reallocation':       'reallocation',
        },
        onRender: function(){
            this.ui.search_beautician.select2({
                allowClear: true,
                width: '100%',
                ajax: {
                  url: "/search/beautician/",
                  dataType: 'json',
                  delay: 250,
                  data: function (params) {
                    return {
                      q: params.term, // search term
                    };
                  },
                  processResults: function (data, params) {
                    return {
                      results: data,
                    };
                  },
                  cache: true
                },
            });
        },//onRender

        allocate_manually: function(){
            var _this = this
            var beautician_id = +this.ui.search_beautician.val()
            if(!beautician_id)
                return
            $.get('/allocation/manual/',
            {
                order_id: this.model.id,
                beautician_id: beautician_id
            })
            .done(function(data){
                _this.model.attributes = data
                _this.render();
            })
            .fail(function(){
                alert('Failed')
            })
        },
        on_status_change: function(){
            if(this.ui.status_change.val() ==  _.invert(this.get_order_status())['Confirmed'] )
                this.auto_allocate()
        },

        static_data : JSON.parse(window.localStorage.getItem('static_data')),

        get_order_status : function(){
            return this.static_data.order_status
        },

        get_allocation_data : function(){
            return this.static_data.allocation_status
        },

        auto_allocate: function(){
            var _this = this
            $.get('/allocate/auto/',
            {
                order_id : this.model.id
            })
            .done(function(data){
                _this.model.attributes = data
                _this.render();
            })
            .fail(function(){
                alert('Failed , try reallocation or manual allocation')
                _this.ui.status_change.val(_this.model.get('status'))
            })
        },

        reallocation: function(){
            var _this = this
            $.get('/allocate/reallocate/',
            {
                order_id : _this.model.id
            })
            .done(function(data){
                _this.model.attributes = data
                _this.render();
            })
            .fail(function(){
                alert('Failed , try reallocation or manual allocation')
                _this.ui.status_change.val(_this.model.get('status'))
            })
        }

    })
    return Detail;
});

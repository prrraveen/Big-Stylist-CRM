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
            var static_data = JSON.parse(window.localStorage.getItem('static_data'))
            return {
                order_status: static_data.order_status,
                allocation_status_dict: static_data.allocation_status
            }
        },
        ui : {
            search_beautician: '#search-beautician',
        },
        events: {
            'change @ui.search_beautician' : 'allocate_manually'
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
        }
    })
    return Detail;
});

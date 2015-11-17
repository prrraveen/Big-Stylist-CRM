define([
        'backbone',
],
function(
        Backbone
) {
    var Order = Backbone.Model.extend({
        urlRoot: '/order/',
    });
    return Order;
});

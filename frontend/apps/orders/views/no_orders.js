define([
        'marionette',
],
function(
        Mn
) {
    var No_orders = Mn.ItemView.extend({
        template: JST['no-order-for-now']
    })
    return No_orders;
});

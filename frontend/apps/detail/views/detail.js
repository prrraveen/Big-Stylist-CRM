define([
        'marionette',
],
function(
        Mn
) {
    var Detail = Mn.ItemView.extend({
        template: JST['detail'],
    })
    return Detail;
});

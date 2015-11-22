define([
        'marionette',
        'jquery',
        'jasny',
        'assets/libs/jasny-bootstrap/js/offcanvas'
],
function(
        Mn
) {
    var Left_bar = Mn.ItemView.extend({
        template: JST['left_bar'],
    })
    return Left_bar;
});

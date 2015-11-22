define([
        'marionette',
],
function(
        Mn,
        $,
        Dashboard_theme
) {
    var Left_bar = Mn.ItemView.extend({
        template: JST['left_bar'],
    })
    return Left_bar;
});

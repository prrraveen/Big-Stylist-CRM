define([
        'marionette',
],
function(
        Mn
) {
    var Dashboard = Mn.ItemView.extend({
        template: JST['dashboard']
    })
    return Dashboard;
});

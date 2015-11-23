define([
        'marionette'
],
function(
        Mn
) {
    var Layout = Mn.LayoutView.extend({
        template: JST['layout'],
        // These are my visual regions: the "navigation" or
        // left hand list of categories, and the "main"
        // content area where the email list or contact list
        // is displayed.
        regions: {
          navigation: "#navigation",
          main_region: "#main"
        },
    });

    return Layout;
});

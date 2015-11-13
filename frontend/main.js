require.config({
    paths: {
        jquery:     'assets/libs/jquery/dist/jquery',
        underscore: 'assets/libs/underscore/underscore-min',
        backbone:   'assets/libs/backbone/backbone',
        marionette: 'assets/libs/backbone.marionette/lib/backbone.marionette',
        bootstrap:  'assets/libs/bootstrap/dist/js/bootstrap',
        templates:  'assets/js/templates',
    },
    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],

            //Once loaded, use the global 'Backbone' as the module value
            exports: 'Backbone',
        },
        'marionette': {
            deps: ['backbone'],

            //Once loaded, use the global 'Backbone' as the module value
            exports: 'Marionette',
        },
        'bootstrap': {
            deps: ['jquery'],
            exports: 'bootstrap',
        }
    },
});

require(['marionette',
],
function (Mn
) {
    // Create our Application
    var app = new Mn.Application();

});

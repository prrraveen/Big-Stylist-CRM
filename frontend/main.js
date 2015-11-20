require.config({
    paths: {
        jquery:     'assets/libs/jquery/dist/jquery',
        underscore: 'assets/libs/underscore/underscore-min',
        backbone:   'assets/libs/backbone/backbone',
        marionette: 'assets/libs/backbone.marionette/lib/backbone.marionette',
        bootstrap:  'assets/libs/bootstrap/dist/js/bootstrap',
        select2:    'assets/libs/select2/dist/js/select2.min',
        templates:  'assets/js/templates',

    },
    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],

            //Once loaded, use the global 'Backbone' as the module value
            exports: 'Backbone',
        },
        'marionette': {
            deps: ['backbone' , 'assets/extend'],

            //Once loaded, use the global 'Backbone' as the module value
            exports: 'Marionette',
        },
        'bootstrap': {
            deps: ['jquery'],
            exports: 'bootstrap',
        },
        'select2':{
            deps: ['jquery'],
            exports: 'select2'

        }
    },

    urlArgs: "bust=" + (new Date()).getTime()
});

require(['marionette',
         'backbone',
         'router',
         'layout'
],
function (  Mn,
            Backbone,
            Router,
            Layout
) {
    // Create our Application
    window.app = {};
    window.app = new Mn.Application();

    app.on("before:start", function(){
        app.router = new Router();
    });

    app.addInitializer(function(){
        // Render the layout and get it on the screen, first
        app.layout = new Layout();
        var layout_render = app.layout.render();
        $('body').prepend(app.layout.el);

        Backbone.history.start();
    })

    var get_static_data = function(){
        if(!window.localStorage.getItem('static_data'))
        {
            $.get('/static_data/')
            .done(function(data){
                window.localStorage.setItem('static_data', JSON.stringify(data))
            })
            .always(function(){
            })
        }
    }
    var add_ajax_loader = function(){
        var $loading = $('#ajax-spinner').hide();
        $(document)
          .ajaxStart(function () {
            $loading.show();
          })
          .ajaxStop(function () {
            $loading.hide();
          });
    }
    get_static_data();
    add_ajax_loader();
    app.start();
});

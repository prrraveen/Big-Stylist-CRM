require([
        'marionette',
        'backbone',
],
function(
        Mn,
        Backbone
) {
    Marionette.Renderer.render = function(template, data){
      return template(data);
    };
});

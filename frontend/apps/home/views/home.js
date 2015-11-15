define([
        'marionette',
],
function(
        Mn
) {
    var Home = Marionette.Object.extend({
      template: window['JST']['home.html'],
      homewards: function(){
          console.log('You and me Sunday driving , Not arriving ,On our way back home')
      }
    });

    return Home;
});

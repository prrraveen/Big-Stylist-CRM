this["JST"] = this["JST"] || {};

this["JST"]["dashboard"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<div class="container">\n    <div class="row">\n        <div class=\'col-sm-6 col-sm-offset-3\'>\n            <div class="list-group">\n              <a href="#orders/Received" class="list-group-item">New</a>\n              <a href="#orders/Confirmed" class="list-group-item">Confirmed</a>\n              <a href="#orders/Allocated" class="list-group-item">Allocated</a>\n              <a href="#orders/Delievered" class="list-group-item">Completed</a>\n              <a href="#orders/all" class="list-group-item">All</a>\n              <a href="#lead" class="list-group-item">Lead Data Table</a>\n              <a href="/admin/agent/order/" class="list-group-item">Edit Order Details</a>\n              <a href="/admin/agent/beautician/" class="list-group-item">Beauticians</a>\n              <a href="/admin/agent/service/" class="list-group-item">Services</a>\n            </div>\n        </div>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["layout"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<section id=\'navigation\'></section>\n\n<div class=\'row\'>\n    <div class="col-sm-12" id=\'main\'>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["navigation"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<nav class="navbar navbar-default">\n  <div class="container-fluid">\n    <!-- Brand and toggle get grouped for better mobile display -->\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="#dashboard">\n          <img src="frontend/assets/images/logo.png" id=\'brand-logo\' alt="Responsive image" class=\'img img-responsive\'/></a>\n    </div>\n\n    <!-- Collect the nav links, forms, and other content for toggling -->\n    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n      <ul class="nav navbar-nav navbar-right">\n        <li class="dropdown">\n          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"\n            aria-expanded="false">' +
((__t = ( user.get_name() )) == null ? '' : __t) +
'<span class="caret"></span></a>\n          <ul class="dropdown-menu">\n            <li><a href="#logout">logout</a></li>\n          </ul>\n        </li>\n      </ul>\n    </div><!-- /.navbar-collapse -->\n  </div><!-- /.container-fluid -->\n</nav>\n';

}
return __p
};

this["JST"]["no-order-for-now"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<div class="container">\n    <div class="row">\n        <div class=\'col-sm-12\'>\n            <h3>No Orders found in this category.</h3>\n        </div>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["order_itemView"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
function print() { __p += __j.call(arguments, '') }
with (obj) {
__p += '    <td>\n        ' +
((__t = ( customer.name )) == null ? '' : __t) +
'\n    </td>\n    <td>\n        ' +
((__t = ( customer.contact )) == null ? '' : __t) +
'\n    </td>\n    <td>\n        ' +
((__t = ( on )) == null ? '' : __t) +
'\n    </td>\n    <td>\n        ' +
((__t = ( at )) == null ? '' : __t) +
'\n    </td>\n    <td>\n        ';
 if (beautician != null) {  ;
__p += ' ' +
((__t = ( beautician.name )) == null ? '' : __t) +
' ';
};
__p += '\n    </td>\n    <td>\n        ' +
((__t = ( status )) == null ? '' : __t) +
'\n    </td>\n';

}
return __p
};

this["JST"]["orders"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<div class="container">\n    <div class="row">\n        <div class=\'col-sm-12\'>\n            <table class=\'table table-hover table-bordered\'>\n                <thead>\n                    <tr>\n                        <td>\n                            Customer\n                        </td>\n                        <td>\n                            Contact\n                        </td>\n                        <td>\n                            Date\n                        </td>\n                        <td>\n                            Time\n                        </td>\n                        <td>\n                            Beautician\n                        </td>\n                        <td>\n                            Status\n                        </td>\n                    </tr>\n                </thead>\n                <tbody>\n\n                </tbody>\n            </table>\n        </div>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["login"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<br>\n<div class="container">\n    <div class="row">\n        <div class=\'col-sm-4 col-sm-offset-4 well\' >\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                    <h3>Log in</h3>\n                </div>\n            </div>\n            <ul id=\'error\'>\n            </ul>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="email">Email</label>\n                    <input id=\'email\' class=\'form-control\' required></input>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="password">password</label>\n                    <input type=\'password\' id=\'password\' class=\'form-control\' required></input>\n                </div>\n            </div>\n             <button type="button" id=\'create\' class="btn btn-default">Submit</button>\n             <hr>\n             <div class="row">\n                 <div class=\'col-sm-12\'>\n                     <a href="#regi">Sign Up</a>\n                 </div>\n             </div>\n        </div>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["regi"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<br>\n<div class="container">\n    <div class="row">\n        <div class=\'col-sm-4 col-sm-offset-4 well\' >\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                    <h3>Add User</h3>\n                </div>\n            </div>\n            <ul id=\'error\'>\n            </ul>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="name">Name</label>\n                    <input id=\'name\' class=\'form-control\' required></input>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="email">Email</label>\n                    <input id=\'email\' class=\'form-control\' required></input>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="password">password</label>\n                    <input type=\'password\' id=\'password\' class=\'form-control\' required></input>\n                </div>\n            </div>\n             <button type="button" id=\'create\' class="btn btn-default">Submit</button>\n             <hr>\n             <div class="row">\n                 <div class=\'col-sm-12\'>\n                     <a href="#login">login</a>\n                 </div>\n             </div>\n        </div>\n    </div>\n</div>\n';

}
return __p
};
this["JST"] = this["JST"] || {};

this["JST"]["detail"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
function print() { __p += __j.call(arguments, '') }
with (obj) {
__p += '<div class="container">\n    <div class="row">\n        <div class=\'col-sm-6 well\'>\n            <h4>Customer Detail</h4>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <label for="Name">Name</label>\n                </div>\n                <div class=\'col-sm-9\'>\n                    ' +
((__t = ( customer.name )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <label for="Name">Contact</label>\n                </div>\n                <div class=\'col-sm-9\'>\n                    ' +
((__t = ( customer.contact )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <label for="Name">Locality</label>\n                </div>\n                <div class=\'col-sm-9\'>\n                    ';
 if(customer.locality != null) {;
__p += '\n                    ' +
((__t = ( customer.locality.name )) == null ? '' : __t) +
'\n                    ';
 } ;
__p += '\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <label for="Name">Pincode</label>\n                </div>\n                <div class=\'col-sm-9\'>\n                    ' +
((__t = ( customer.pincode.pincode )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <label for="Name">Address</label>\n                </div>\n                <div class=\'col-sm-9\'>\n                    ' +
((__t = ( customer.address )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                    <a href="/admin/agent/customer/' +
((__t = ( customer.id )) == null ? '' : __t) +
'/">Edit customer details</a>\n                </div>\n            </div>\n        </div>\n        <div class=\'col-sm-5 col-sm-offset-1 well\'>\n            <h4>Order Detail</h4>\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                <label for="">Services</label>\n                </div>\n                <ul>\n                    ';
 _.each(services, function(service){ ;
__p += '\n                        <a href="' +
((__t = ( service.lp )) == null ? '' : __t) +
'">' +
((__t = ( service.name )) == null ? '' : __t) +
'</a> ,\n                    ';
 }) ;
__p += '\n                </ul>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Amount</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ' +
((__t = ( amount )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Discount</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ' +
((__t = ( discount )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Placed On</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ';
 if(placedat != null) ;
__p += '\n                        ' +
((__t = ( placedat )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Scheduled On</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ';
 if(on != null) ;
__p += '\n                        ' +
((__t = ( on )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Scheduled at</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ';
 if(at != null) ;
__p += '\n                        ' +
((__t = ( at )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                    <a href="/admin/agent/order/' +
((__t = ( id )) == null ? '' : __t) +
'/">Edit Order Details</a>\n                </div>\n            </div>\n        </div>\n    </div>\n\n    <div class="row">\n        <div class=\'col-sm-6 well\'>\n            <h4>Allocation</h4>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <h5><label for="">Change To</label></h5>\n                </div>\n                <div class=\'col-sm-5\'>\n                    <select class="form-control" id=\'status-change\'>\n                        ';
 for(var i in order_status) { ;
__p += '\n                            <option value="' +
((__t = ( i )) == null ? '' : __t) +
'"\n                                ';
 if(status== order_status[i]) {;
__p += ' selected ';
};
__p += '\n\n                            >' +
((__t = ( order_status[i] )) == null ? '' : __t) +
'</option>\n                        ';
 } ;
__p += '\n                    </select>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <label for="">Allocation Status</label>\n                </div>\n                <div class=\'col-sm-9\'>\n                    <h5>\n                        ' +
((__t = ( allocation_status_dict[allocation_status] )) == null ? '' : __t) +
'\n                    </h5>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <h5><label for="">Reallocation</label></h5>\n                </div>\n                <div class=\'col-sm-9\'>\n                    <button id=\'reallocation\' class=\'btn btn-primary\'>Next Best Reallocation</button>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-3\'>\n                    <h5><label for="">Allocate Manually</label></h5>\n                </div>\n                <div class=\'col-sm-9\'>\n                    <select id="search-beautician" class=\'form-control form-input\'>\n                        <option id=\'-1\' selected="selected">Select a Beautician</option>\n                    </select>\n                </div>\n            </div>\n\n        </div>\n        <div class=\'col-sm-5 col-sm-offset-1 well\'>\n            <h4>Beautician</h4>\n            ';
 if(beautician) {;
__p += '\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Name</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ' +
((__t = ( beautician.name )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Contact</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ' +
((__t = ( beautician.phone_number )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Alternate</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ' +
((__t = ( beautician.alternate_number )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Locality</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ' +
((__t = ( beautician.locality )) == null ? '' : __t) +
'\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-4\'>\n                    <label for="">Allocation Distance</label>\n                </div>\n                <div class=\'col-sm-8\'>\n                    ' +
((__t = ( allocation_distance )) == null ? '' : __t) +
' Km\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                    <a href="/admin/agent/beautician/' +
((__t = ( beautician.id )) == null ? '' : __t) +
'/">Edit Beautician details</a>\n                </div>\n            </div>\n\n            ';
}else {;
__p += '\n                <div class="row">\n                    <div class=\'col-sm-12\'>\n                        Not allocated yet\n                    </div>\n                </div>\n            ';
};
__p += '\n\n        </div>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["layout"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<div id=\'navigation\'></div>\n<div id=\'main\'></div>\n';

}
return __p
};

this["JST"]["left_bar"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<aside class="main-sidebar">\n  <!-- sidebar: style can be found in sidebar.less -->\n  <section class="sidebar">\n    <!-- Sidebar user panel -->\n    <!-- sidebar menu: : style can be found in sidebar.less -->\n    <ul class="sidebar-menu">\n      <li class="header">MAIN NAVIGATION</li>\n      <li>\n        <a href="#orders/Received">\n          <i class="fa fa-th"></i> <span>New Orders</span> <small class="label pull-right bg-green">new</small>\n        </a>\n      </li>\n      <li>\n          <a href="#orders/Confirmed">\n            <i class="fa fa-th"></i> <span>Confirmed</span>\n          </a>\n      </li>\n      <li>\n          <a href="#orders/Allocated">\n            <i class="fa fa-th"></i> <span>Allocated</span>\n          </a>\n      </li>\n      <li>\n          <a href="#orders/Delievered">\n            <i class="fa fa-th"></i> <span>Completed</span>\n          </a>\n      </li>\n      <li>\n          <a href="#orders/all">\n            <i class="fa fa-th"></i> <span>All</span>\n          </a>\n      </li>\n      <li>\n          <a href="#lead">\n            <i class="fa fa-th"></i> <span>Leads</span>\n          </a>\n      </li>\n      <li>\n          <a href="/admin/agent/order/">\n            <i class="fa fa-th"></i> <span>Edit Order Details</span>\n          </a>\n      </li>\n      <li>\n          <a href="/admin/agent/beautician/">\n            <i class="fa fa-th"></i> <span>Beauticians</span>\n          </a>\n      </li>\n      <li>\n          <a href="/admin/agent/service/">\n            <i class="fa fa-th"></i> <span>Services</span>\n          </a>\n      </li>\n    </ul>\n  </section>\n  <!-- /.sidebar -->\n</aside>\n';

}
return __p
};

this["JST"]["navigation"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<header class="main-header">\n  <!-- Logo -->\n  <a href="#leads/all" class="logo">\n    <!-- mini logo for sidebar mini 50x50 pixels -->\n    <span class="logo-mini"><b>B</b>S</span>\n    <!-- logo for regular state and mobile devices -->\n    <span class="logo-lg">\n        <img src="frontend/assets/images/logo.png" id=\'brand-logo\' alt="Responsive image" class=\'img img-responsive\'/></a>\n    </span>\n  </a>\n  <!-- Header Navbar: style can be found in header.less -->\n  <nav class="navbar navbar-static-top" role="navigation">\n    <!-- Sidebar toggle button-->\n    <a class="sidebar-toggle"  role="button">\n      <span class="sr-only">Toggle navigation</span>\n    </a>\n    <div class="navbar-custom-menu">\n      <ul class="nav navbar-nav">\n          <li class="dropdown user user-menu">\n            <a href="#" class="dropdown-toggle" data-toggle="dropdown">\n              <span class="hidden-xs">' +
((__t = ( user.get_name() )) == null ? '' : __t) +
'</span>\n            </a>\n            <ul class="dropdown-menu">\n              <li class="user-footer">\n                  <a href="#logout" class="btn btn-default btn-flat">Sign out</a>\n              </li>\n            </ul>\n          </li>\n\n      </ul>\n    </div>\n  </nav>\n</header>\n<aside class="main-sidebar offcanvas">\n    <section class="sidebar">\n     <ul class="sidebar-menu">\n       <li class="header">MAIN NAVIGATION</li>\n       </li>\n       <li class="treeview">\n         <a role="button" data-toggle="collapse" href="#lead" aria-expanded="false" aria-controls="lead">\n           <i class="fa fa-laptop"></i>\n           <span>Leads</span>\n           <i class="fa fa-angle-left pull-right"></i>\n         </a>\n         <ul class="collapse" id="lead">\n           <li><a href="#leads/all" class=""><i class="fa fa-circle-o"></i> All Leads</a></li>\n           <li><a href="#leads/facebook"><i class="fa fa-circle-o"></i> Lead Facebook</a></li>\n           <li><a href="#leads/others"><i class="fa fa-circle-o"></i> Lead Others</a></li>\n           <li><a href="/admin/agent/lead/add/"><i class="fa fa-circle-o"></i> Add Lead</a></li>\n         </ul>\n       </li>\n       <li class="treeview">\n         <a role="button" data-toggle="collapse" href="#orders" aria-expanded="false" aria-controls="orders">\n           <i class="fa fa-laptop"></i>\n           <span>Orders</span>\n           <i class="fa fa-angle-left pull-right"></i>\n         </a>\n         <ul class="collapse" id=\'orders\'>\n           <li><a href="#orders/Received"><i class="fa fa-circle-o"></i> New/Received Orders</a></li>\n           <li><a href="#orders/Confirmed"><i class="fa fa-circle-o"></i> Confirmed Orders</a></li>\n           <li><a href="#orders/Allocated"><i class="fa fa-circle-o"></i> Allocated Orders</a></li>\n           <li><a href="#orders/Delievered"><i class="fa fa-circle-o"></i> Delievered Orders</a></li>\n           <li><a href="/admin/agent/order/"><i class="fa fa-circle-o"></i> + Add new orders</a></li>\n         </ul>\n       </li>\n\n       <li>\n           <a href="/admin/agent/service/">\n             <i class="fa fa-th"></i> <span>Manage Services</span>\n           </a>\n       </li>\n\n       <li>\n           <a href="/admin/agent/beautician/">\n             <i class="fa fa-th"></i> <span>Manage Beautician</span>\n           </a>\n       </li>\n       <li class="treeview">\n         <a role="button" data-toggle="collapse" href="#user" aria-expanded="false" aria-controls="user">\n           <i class="fa fa-laptop"></i>\n           <span>System</span>\n           <i class="fa fa-angle-left pull-right"></i>\n         </a>\n         <ul class="collapse" id=\'user\'>\n           <li><a href="/admin/agent/user/"><i class="fa fa-circle-o"></i> Manage Users</a></li>\n         </ul>\n       </li>\n\n     </ul>\n    </section>\n</aside>\n';

}
return __p
};

this["JST"]["lead_itemView"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
function print() { __p += __j.call(arguments, '') }
with (obj) {
__p += '<td>\n    ';
 if(source != null){;
__p += '\n        ' +
((__t = ( source.name )) == null ? '' : __t) +
'\n    ';
};
__p += '\n\n</td>\n<td>\n    ';
 if(customer != null){;
__p += '\n        ' +
((__t = ( customer.name )) == null ? '' : __t) +
'\n    ';
}else{;
__p += '\n        ' +
((__t = ( name )) == null ? '' : __t) +
'\n    ';
};
__p += '\n</td>\n<td>\n    ' +
((__t = ( contact )) == null ? '' : __t) +
'\n</td>\n<td>\n    ' +
((__t = ( app.static_data.lead_status[lead_status] )) == null ? '' : __t) +
'\n</td>\n<td>\n    ' +
((__t = ( app.static_data.next_step[next_step] )) == null ? '' : __t) +
'\n</td>\n';

}
return __p
};

this["JST"]["leads"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
function print() { __p += __j.call(arguments, '') }
with (obj) {
__p += '<div class="container">\n    <div class="row">\n        <div class=\'col-sm-6 col-sm-offset-5\'>\n            <h3> ' +
((__t = ( page)) == null ? '' : __t) +
' Leads </h3>\n        </div>\n    </div>\n    <div class="row">\n        <div class=\'col-sm-4\'>\n            <div class="input-group">\n                <span class="input-group-addon" id="basic-addon1">\n                    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>\n                </span>\n                <input type="text" id=\'name\' class=\'form-control\' placeholder="Search leads by customer name" />\n                <span class="input-group-btn">\n                    <button id=\'search-name\' class="search btn btn-default">Search</button>\n                </span>\n            </div>\n        </div>\n        <div class=\'col-sm-3\'>\n            <div class="input-group">\n                <span class="input-group-addon" id="basic-addon1">\n                    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>\n                </span>\n                <input type="text" class=\'form-control\' id=\'contact\' placeholder="Search leads by customer contact" />\n                <span class="input-group-btn">\n                    <button type="button" id=\'search-contact\'class="search btn btn-default">Search</button>\n                </span>\n            </div>\n        </div>\n        <div class=\'col-sm-2\'>\n            <button type="button" id=\'remove-filters\' class="btn btn-default">Remove filters</button>\n        </div>\n        <div class=\'col-sm-2\'>\n            <button type="button" data-toggle="modal" data-target="#myModal" class="btn btn-default">+ Add Lead</button>\n        </div>\n    </div>\n    <br>\n    <div class="row">\n        <div class=\'col-sm-12\'>\n            <table id=\'table\' class=\'table table-hover table-bordered\'>\n                <thead>\n                    <tr>\n                        <td>\n                            Source\n                        </td>\n                        <td>\n                            Name\n                        </td>\n                        <td>\n                            Contact\n                        </td>\n                        <td>\n                            Lead Status\n                        </td>\n                        <td>\n                            Next Step\n                        </td>\n                    </tr>\n                </thead>\n                <tbody>\n\n                </tbody>\n            </table>\n        </div>\n    </div>\n    <br>\n    <div class="row">\n        <div class=\'col-sm-12\'>\n            <h4>\n                ';
 for(var i =1; i <= state.totalPages; i++){;
__p += '\n                    <a class="page pointer" id=\'' +
((__t = ( i )) == null ? '' : __t) +
'\' >' +
((__t = ( i )) == null ? '' : __t) +
'</a>\n                ';
};
__p += '\n            </h4>\n        </div>\n    </div>\n\n</div>\n\n<!-- Modal -->\n<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n  <div class="modal-dialog modal-lg" role="document">\n    <div class="modal-content">\n      <div class="modal-body" id=\'modal-body\'>\n          <div class="embed-responsive embed-responsive-16by9">\n            <!-- <iframe class="embed-responsive-item" src="…"></iframe> -->\n            <iframe class="embed-responsive-item"src="/admin/agent/lead/add/">\n                <p>Your browser does not support iframes.</p>\n            </iframe>\n          </div>\n\n      </div>\n    </div>\n  </div>\n</div>\n';

}
return __p
};

this["JST"]["no-order-for-now"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<tr>\n    <td>\n        No Orders found in this category.\n    </td>\n</tr>\n';

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
var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
function print() { __p += __j.call(arguments, '') }
with (obj) {
__p += '<div class="container">\n    <div class="row">\n        <div class=\'col-sm-6 col-sm-offset-5\'>\n            <h3> ' +
((__t = ( page)) == null ? '' : __t) +
' Orders </h3>\n        </div>\n    </div>\n\n    <div class="row">\n        <div class=\'col-sm-4\'>\n            <div class="input-group">\n                <span class="input-group-addon" id="basic-addon1">\n                    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>\n                </span>\n                <input type="text" id=\'name\' class=\'form-control\' placeholder="Search leads by customer name" />\n                <span class="input-group-btn">\n                    <button id=\'search-name\' class="search btn btn-default">Search</button>\n                </span>\n            </div>\n        </div>\n        <div class=\'col-sm-4\'>\n            <div class="input-group">\n                <span class="input-group-addon" id="basic-addon1">\n                    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>\n                </span>\n                <input type="text" class=\'form-control\' id=\'contact\' placeholder="Search leads by customer contact" />\n                <span class="input-group-btn">\n                    <button type="button" id=\'search-contact\'class="search btn btn-default">Search</button>\n                </span>\n            </div>\n        </div>\n        <div class=\'col-sm-1\'>\n            <button type="button" id=\'remove-filters\' class="btn btn-default">Remove filters</button>\n        </div>\n    </div>\n    <br>\n    <div class="row">\n        <div class=\'col-sm-12\'>\n            <table class=\'table table-hover table-bordered\'>\n                <thead>\n                    <tr>\n                        <td>\n                            Customer\n                        </td>\n                        <td>\n                            Contact\n                        </td>\n                        <td>\n                            Date\n                        </td>\n                        <td>\n                            Time\n                        </td>\n                        <td>\n                            Beautician\n                        </td>\n                        <td>\n                            Status\n                        </td>\n                    </tr>\n                </thead>\n                <tbody>\n\n                </tbody>\n            </table>\n        </div>\n    </div>\n    <br>\n    <div class="row">\n        <div class=\'col-sm-12\'>\n            <h4>\n                ';
 for(var i =1; i <= state.totalPages; i++){;
__p += '\n                    <a class="page pointer" id=\'' +
((__t = ( i )) == null ? '' : __t) +
'\' >' +
((__t = ( i )) == null ? '' : __t) +
'</a>\n                ';
};
__p += '\n            </h4>\n        </div>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["login"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<br>\n<div class="container">\n    <div class="row">\n        <div class=\'col-sm-4 col-sm-offset-5\'>\n            <h3>Bigstylist CRM</h3>\n        </div>\n    </div>\n    <div class="row">\n        <div class=\'col-sm-4 col-sm-offset-4 well\' >\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                    <h3>Log in</h3>\n                </div>\n            </div>\n            <ul id=\'error\'>\n            </ul>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="email">Email</label>\n                    <input id=\'email\' class=\'form-control\' required></input>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="password">password</label>\n                    <input type=\'password\' id=\'password\' class=\'form-control\' required></input>\n                </div>\n            </div>\n             <button type="button" id=\'create\' class="btn btn-default">Submit</button>\n             <hr>\n             <div class="row">\n                 <div class=\'col-sm-12\'>\n                     <a href="#regi">Sign Up</a>\n                 </div>\n             </div>\n        </div>\n    </div>\n</div>\n';

}
return __p
};

this["JST"]["regi"] = function(obj) {
obj || (obj = {});
var __t, __p = '', __e = _.escape;
with (obj) {
__p += '<br>\n<div class="container">\n    <div class="row">\n        <div class=\'col-sm-4 col-sm-offset-5\'>\n            <h3>Bigstylist CRM</h3>\n        </div>\n    </div>\n    <div class="row">\n        <div class=\'col-sm-4 col-sm-offset-4 well\' >\n            <div class="row">\n                <div class=\'col-sm-12\'>\n                    <h3>Add User</h3>\n                </div>\n            </div>\n            <ul id=\'error\'>\n            </ul>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="name">Name</label>\n                    <input id=\'name\' class=\'form-control\' required></input>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="email">Email</label>\n                    <input id=\'email\' class=\'form-control\' required></input>\n                </div>\n            </div>\n            <div class="row">\n                <div class=\'col-sm-12 form-group\'>\n                     <label for="password">password</label>\n                    <input type=\'password\' id=\'password\' class=\'form-control\' required></input>\n                </div>\n            </div>\n             <button type="button" id=\'create\' class="btn btn-default">Submit</button>\n             <hr>\n             <div class="row">\n                 <div class=\'col-sm-12\'>\n                     <a href="#login">login</a>\n                 </div>\n             </div>\n        </div>\n    </div>\n</div>\n';

}
return __p
};
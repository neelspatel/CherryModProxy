def get(arg):
	#output = "<div style = 'width:100%; margin-left: -10px !important; padding-left: 15px !important; background-color:grey; position:fixed;top:0;z-index:999; display:block !important;'>Butucu - Doin Big Shit <button class = 'addCoupon'>Add!</button><div id = 'couponCount'>0</div></div>"	
	output = '<div class="navbar navbar-fixed-top navbar-inverse" style = "margin-left: 0px; margin-right: 0px; width: 100%;"><div class="navbar-inner"><a class="brand" href="#">The Coop</a><ul class = "nav pull-right"><li class="dropdown" ><a href="#" class="dropdown-toggle" data-toggle="dropdown" onclick = ""><i class="icon-tags icon-white"></i> Deals <span class="badge badge-important" id = "couponCount"></span> <b class="caret"></b></a><ul class="dropdown-menu  outerDropdown" style = "min-width:150px !important;"></ul></li></ul>      </div></div>'
	return output

	
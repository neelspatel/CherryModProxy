def get(arg):
	#output = "<div style = 'width:100%; margin-left: -10px !important; padding-left: 15px !important; background-color:grey; position:fixed;top:0;z-index:999; display:block !important;'>Butucu - Doin Big Shit <button class = 'addCoupon'>Add!</button><div id = 'couponCount'>0</div></div>"	
	output = '<div class="navbar navbar-fixed-top navbar-inverse" style = "margin-left: -10px !important; width: 100%;"><div class="navbar-inner"><a class="brand" href="#">Butucu</a><ul class="nav"><li class="active brand" id = "couponCount">0</li></ul><ul class = "nav pull-right"><li class="dropdown" ><a href="#" class="dropdown-toggle" data-toggle="dropdown" onclick = "">Your Coupons <b class="caret"></b></a><ul class="dropdown-menu  outerDropdown" style = "min-width:50px !important;"></ul></li></ul>      </div></div>'
	return output

	
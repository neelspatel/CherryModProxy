def get(arg):	
	output = "<script src='http://code.jquery.com/jquery-1.7.2.min.js'></script>"	
	output += " <script src='//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js'> </script>"
	output += " <link href='//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css' rel='stylesheet'>"
	#output += "<script src='http://code.jquery.com/ui/1.10.2/jquery-ui.js'></script>"
	#output += '<link href = "http://code.jquery.com/ui/1.10.2/themes/smoothness/jquery-ui.css" rel = "stylesheet">'
	#output += '<script>function addCoupon() {alert("in here");jQuery(#number).text("updated");}</script>'	
	output += " <script>jQuery(document).ready(function(){function addCoupon() {alert('in');jQuery('#couponCount').text(parseInt(jQuery('#couponCount').text())+1); return true;}jQuery('.addCoupon').click(addCoupon);});</script>"	
	return output
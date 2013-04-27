def get(arg):	
	output = "<script src='http://code.jquery.com/jquery-1.7.2.min.js'></script>"	
	output += " <script src='//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js'> </script>"
	output += " <link href='//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css' rel='stylesheet'>"
	#output += "<script src='http://code.jquery.com/ui/1.10.2/jquery-ui.js'></script>"
	#output += '<link href = "http://code.jquery.com/ui/1.10.2/themes/smoothness/jquery-ui.css" rel = "stylesheet">'
	#output += '<script>function addCoupon() {alert("in here");jQuery(#number).text("updated");}</script>'	
	
	addBook = '<li class="dropdown-submenu pull-left" style = "width:100px;"><a tabindex="-1" href="#">' + 'The Coop'  + '   <i class="icon-plus-sign"></i></a><ul class="dropdown-menu" style = "width:100px; padding: 0px 20px 10px 20px; left:-200% !important;"><h2 style = "text-align: center">The Coop</h2><img src = "http://www.graphicsfuel.com/wp-content/uploads/2012/07/red-book.png" style = "width:100px; margin:auto; display: block;"></img><p> Recieve $5 off books if you buy in the next 45 minutes! </p></ul></li>'
	addPrinter = '<li class="dropdown-submenu pull-left" style = "width:100px;"><a tabindex="-1" href="#">' + 'Staples'  + '   <i class="icon-plus-sign"></i></a><ul class="dropdown-menu" style = "width:100px; padding: 0px 20px 10px 20px; left:-200% !important;"><h2 style = "text-align: center">The Coop</h2><img src = "http://www.graphicsfuel.com/wp-content/uploads/2012/07/red-book.png" style = "width:100px; margin:auto; display: block;"></img><p> Recieve $5 off books if you buy in the next 45 minutes! </p></ul></li>'
	addBookFunction = "function addBook() {alert('upp'); jQuery('.outerDropdown').append('" + addBook+ "'); return true;}; jQuery('.addBook').click(addBook);"
	addPrinterFunction = "function addPrinter() {jQuery('.outerDropdown').append('" + addPrinter+ "'); return true;}; jQuery('.addPrinter').click(addPrinter);"
	#addBookFunction = "function addBook(){alert('inaddbook')}; jQuery('.addBook').click(addBook);"
	#addPrinterFunction = "function addPrinter(){alert('inaddprinter')}; jQuery('.addPrinter').click(addPrinter);"
	output += " <script>jQuery(document).ready(function(){function addCoupon() {jQuery('#couponCount').text(parseInt(jQuery('#couponCount').text(), 10)+1); return true;}	" + addBookFunction + addPrinterFunction  + "});</script>"	
	#output += " <script>jQuery(document).ready(function(){alert('in start'); function addCoupon() {alert('hey'); return true;} jQuery('.addCoupon').click(addCoupon);	});</script>"	
	return output
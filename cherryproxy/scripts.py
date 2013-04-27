def get(arg):	
	output = "<script src='http://code.jquery.com/jquery-1.7.2.min.js'></script>"	
	output += " <script src='//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js'> </script>"
	output += " <link href='//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css' rel='stylesheet'>"
	#output += "<script src='http://code.jquery.com/ui/1.10.2/jquery-ui.js'></script>"
	#output += '<link href = "http://code.jquery.com/ui/1.10.2/themes/smoothness/jquery-ui.css" rel = "stylesheet">'
	#output += '<script>function addCoupon() {alert("in here");jQuery(#number).text("updated");}</script>'	
	
	addBook = '<li class="dropdown-submenu pull-left" style = "width:125px;"><a tabindex="-1" href="#">' + 'The Coop'  + '   <i class="icon-plus-sign"></i></a><ul class="dropdown-menu" style = "width:250px; padding: 0px 20px 10px 20px; left:-130% !important;"><h2 style = "text-align: center">The Coop </h2><img src = "http://www.graphicsfuel.com/wp-content/uploads/2012/07/red-book.png" style = "width:100px; margin:auto; display: block;"></img><p>Buy your book in The Coop and get <b>$10 Coop Cash</b>.</p><p>Plus, get our one-of-a-kind book buyback program.</p></ul></li>'
	addPrinter = '<li class="dropdown-submenu pull-left" style = "width:150px;"><a tabindex="-1" href="#">' + 'Staples'  + '   <i class="icon-plus-sign"></i></a><ul class="dropdown-menu" style = "width:250px; padding: 0px 20px 10px 20px; left:-130% !important;"><h2 style = "text-align: center">Staples</h2><img src = "http://icons.iconarchive.com/icons/artua/dragon-soft/512/Printer-icon.png" style = "width:100px; margin:auto; display: block;"></img><p> Recieve free ink for a year if you buy in the next 45 minutes! </p></ul></li>'
	addBookFunction = "function addBook() {jQuery('.outerDropdown').append('" + addBook+ "'); jQuery('#couponCount').text('1'); return true;}; jQuery('.addBook').click(addBook);"
	addPrinterFunction = "function addPrinter() {jQuery('.outerDropdown').append('" + addPrinter+ "'); jQuery('#couponCount').text('1'); return true;}; jQuery('.addPrinter').click(addPrinter);"
	#addBookFunction = "function addBook(){alert('inaddbook')}; jQuery('.addBook').click(addBook);"
	#addPrinterFunction = "function addPrinter(){alert('inaddprinter')}; jQuery('.addPrinter').click(addPrinter);"
	output += " <script>jQuery(document).ready(function(){function addCoupon() {jQuery('#couponCount').text(parseInt(jQuery('#couponCount').text(), 10)+1); return true;}	" + addBookFunction + addPrinterFunction  + "});</script>"	
	output += '<style>select, textarea, input[type="text"], input[type="password"], input[type="datetime"], input[type="datetime-local"], input[type="date"], input[type="month"], input[type="time"], input[type="week"], input[type="number"], input[type="email"], input[type="url"], input[type="search"], input[type="tel"], input[type="color"], .uneditable-input {height: 30px !important;}</style>'
	output += '<style>body{padding: 0px !important;}</style>'
	#output += " <script>jQuery(document).ready(function(){alert('in start'); function addCoupon() {alert('hey'); return true;} jQuery('.addCoupon').click(addCoupon);	});</script>"	
	return output
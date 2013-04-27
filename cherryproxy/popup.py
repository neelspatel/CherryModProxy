import amazon

def choose(arg):
	print "\033[32m\033[1m" + arg + "\033[0m\033[0m\n\n"
	books = arg.count("book") + arg.count("Book") 
	printers = arg.count("printer") + arg.count("Printer")

	print "There are " + str(books) + " books and " + str(printers) + " printers"

	if arg.count("<title>Amazon</title>") > 0:
		return ("none", 0)
	elif books > printers and books > 1:
		return ("book", books)
	elif printers > 1:
		return ("printer", printers)
	else:
		return ("none", 0)

def get(arg):	

	#output = '<script>$(function() {$( "#dialog" ).dialog();});</script>'
	#output += '<div id="dialog" title="Basic dialog">Here</div>'

	#output = '<a href="#popupBasic" data-rel="popup">Open Popup</a><div data-role="popup" id="popupBasic"><p>This is a completely basic popup, no options set.<p></div>'	
	#output += '<script>$(document).ready(function() {$("#popup").click(function() {alert ("here"); ("#popup").hide();});});</script>'
	#output += '<script type="text/javascript">$(document).bind("mobileinit", function () {    $.mobile.ajaxEnabled = false;});</script>'
	
	#print "\033[32m\033[1m" + amazon.get(arg) + "\033[0m\033[0m\n\n"

	(choice, number) = choose(arg)

	print "Choice was " + choice

	output = ""

	if amazon.get(arg) != "":	
		#output = "<script>$(document).ready(function(){$('#myModal').modal('show')})</script>"
		#output = "<script>$(document).ready(function(){$('#myModal').modal('hide')})</script>"
		output = "<script>$(document).ready(function(){setTimeout(function() {$('#myModal').modal('show')},2000)})</script>"
		#output += '<div id="myModal" class="modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">This is the modal...</div>'
		if choice == "book":
			output += '<div id="myModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button><h3 id="myModalLabel">Special offer from The Coop!</h3></div><div class="modal-body"><p>' + amazon.get(arg) + '</p><p>Buy your book in The Coop instead and get <b>$10 Coop Cash</b>.</p><p>Plus, get our one-of-a-kind book buyback program.</p></div><div class="modal-footer"><button class="btn btn-primary addBook addCoupon" data-dismiss="modal" aria-hidden="true">Save deal </button></div></div>	'		
		elif choice == "printer":
			output += '<div id="myModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button><h3 id="myModalLabel">' + amazon.get(arg) + '</h3></div><div class="modal-body"><p>Special offer from Staples!.</p><p>Buy your printer in Staples instead and get free ink refills for a year!</p></div><div class="modal-footer"><button class="btn btn-primary addPrinter addCoupon" data-dismiss="modal" aria-hidden="true">Save deal </button></div></div>	'

	if choice == "book":
		output +=  "<div class = 'alert alert-success' style = 'width:100%;margin-top: -20px;'>Hey! Heard about our book buybacks? <b>Learn more.</b> </div>"
	elif choice == "printer":
		output +=  "<div class = 'alert alert-success' style = 'width:100%; margin-top: -20px;'>Buy from Staples and get a year of free ink.  <b>Learn more.</b></div>"
	else:
		output += "<div class = 'alert alert-success' style = 'width:100%; margin-top: -20px; font-size:115%'>Have you heard about our new warranty?  <b>Learn more.</b></div>"
	#output += '<link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.1/jquery.mobile-1.3.1.min.css" />'

	#output = '<script>$(document).ready(function(){alert("in"); $("#popup").popup("open");});</script>'

	#output += '<a href="#popupBasic" data-rel="popup">Open Popup</a><div data-role="popup" id="popupBasic" positionTo="window"><p>This is a completely basic popup, no options set.<p></div>'
	#output += '<div data-role="popup" id="popup" class="ui-content"><p>This is a popup</p></div>'
	#output += '<a href="#popupPadded" data-rel="popup" data-role="button">Popup with padding</a><div data-role="popup" id="popupPadded" class="ui-content"><p>This is a popup with the <code>ui-content</code> class added to the popup container.</p></div>'
	#output += "<script>$(document).ready(function(){alert('out5');});</script>"
	
	#output += '<a href="#popupDialog" data-rel="popup" data-position-to="window" data-role="button" data-inline="true" data-transition="pop">Dialog</a><div data-role="popup" id="popupDialog" data-overlay-theme="a" data-theme="c" style="max-width:400px;" class="ui-corner-all"><div data-role="header" data-theme="a" class="ui-corner-top"><h1>Delete Page?</h1></div><div data-role="content" data-theme="d" class="ui-corner-bottom ui-content"><h3 class="ui-title">Are you sure you want to delete this page?</h3><p>This action cannot be undone.</p></div></div>'
	#output += '<div id = "popup" style = "position:absolute;width:800px; height:100px; z-index:99; background-color: rgba(12,34,56,0.5); margin: auto" onclick = "$(#popup).hide();">'
	#output += '<h1>' + amazon.get(arg) + '</h1>'
	#output += '</div>'
	return output
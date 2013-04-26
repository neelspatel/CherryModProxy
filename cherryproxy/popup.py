def get(arg):	

	#output = '<script>$(function() {$( "#dialog" ).dialog();});</script>'
	#output += '<div id="dialog" title="Basic dialog">Here</div>'

	#output = '<a href="#popupBasic" data-rel="popup">Open Popup</a><div data-role="popup" id="popupBasic"><p>This is a completely basic popup, no options set.<p></div>'	
	#output += '<script>$(document).ready(function() {$("#popup").click(function() {alert ("here"); ("#popup").hide();});});</script>'
	#output += '<script type="text/javascript">$(document).bind("mobileinit", function () {    $.mobile.ajaxEnabled = false;});</script>'
	
	
	output = "<script>$(document).ready(function(){$('#myModal').modal('show')})</script>"
	#output += '<div id="myModal" class="modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">This is the modal...</div>'
	output += '<div id="myModal" class="modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button><h3 id="myModalLabel">Modal header</h3></div><div class="modal-body"><p>Hey There</p></div><div class="modal-footer"><button class="btn" data-dismiss="modal" aria-hidden="true">Close</button><button class="btn btn-primary addCoupon" data-dismiss="modal" aria-hidden="true">Save changes</button></div></div>	'
	output += "<button class = 'addCoupon'>Add!</button>"
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
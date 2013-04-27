jQuery(document).ready(function(){
	function addCoupon() {
		jQuery('#couponCount').text(parseInt(jQuery('#couponCount').text(), 10)+1); 
		return true;}	

	function addBook() {
		alert('upp'); 
		jQuery('.outerDropdown').append('<li class="dropdown-submenu pull-left" style = "width:100px;"><a tabindex="-1" href="#">The Coop   <i class="icon-plus-sign"></i></a><ul class="dropdown-menu" style = "width:100px; padding: 0px 20px 10px 20px; left:-200% !important;"><h2 style = "text-align: center">The Coop</h2><img src = "http://www.graphicsfuel.com/wp-content/uploads/2012/07/red-book.png" style = "width:100px; margin:auto; display: block;"></img><p> Recieve $5 off books if you buy in the next 45 minutes! </p></ul></li>'); 
		return true;}

	jQuery('.addBook').click(alert('adding'); addBook);

	function addPrinter() {
		jQuery('.outerDropdown').append('<li class="dropdown-submenu pull-left" style = "width:100px;"><a tabindex="-1" href="#">Staples   <i class="icon-plus-sign"></i></a><ul class="dropdown-menu" style = "width:100px; padding: 0px 20px 10px 20px; left:-200% !important;"><h2 style = "text-align: center">The Coop</h2><img src = "http://www.graphicsfuel.com/wp-content/uploads/2012/07/red-book.png" style = "width:100px; margin:auto; display: block;"></img><p> Recieve $5 off books if you buy in the next 45 minutes! </p></ul></li>'); 
		return true;} 

	jQuery('.addPrinter').click(addPrinter);
});
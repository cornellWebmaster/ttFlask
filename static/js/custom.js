/**
 * Organizes grid layout of images when loading the site.
 */
$(window).load(function () {
	var currentTallest = 0,
     currentRowStart = 0,
     rowDivs = new Array(),
     $el,
     topPosition = 0;

	 $('.blocks').delay(1200).each(function() {

	   $el = $(this);
	   topPosition = $el.position().top;

	   if (currentRowStart != topPosition) {

	     // we just came to a new row.  Set all the heights on the completed row
	     for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
	       rowDivs[currentDiv].height(currentTallest);
	     }

	     // set the variables for the new row
	     rowDivs.length = 0; // empty the array
	     currentRowStart = topPosition;
	     currentTallest = $el.height();
	     rowDivs.push($el);

	   } else {

	     // another div on the current row.  Add it to the list and check if it's taller
	     rowDivs.push($el);
	     currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);

	  }

	  // do the last row
	   for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
	     rowDivs[currentDiv].height(currentTallest);
	   }

	 });
});

/**
 * Enables spotlight's carousel.
 */
$(document).ready(function(){
	$('.spotlight').slick({
		autoplay: true,
		autoplaySpeed: 5000,
		arrows:true,
		adaptiveHeight: false,
		appendArrows: $('.spt-nav'),
		prevArrow: '<button style="margin-right:20px;"><</button>',
		nextArrow: '<button style="">></button>'
	});
});
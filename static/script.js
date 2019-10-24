function onlyBrand(checkbox) {
    var checkboxes = document.getElementsByName('brand')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}

function onlyCategory(checkbox) {
    var checkboxes = document.getElementsByName('category')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}



/*Results*/
function collapse(el) {
	$(el).parent().removeAttr('open');
	$(el).siblings(':not(summary)').removeAttr('style');
}
$(function(){
	//Set accessibility attributes
	$('summary').each(function(){
		$(this).attr('role', 'button');
		if ($(this).parent().is('[open]')) { $(this).attr('aria-expanded', 'true'); }
		else { $(this).attr('aria-expanded', 'false'); }
	});
	
	//Event handler
	$('summary').on('click', function(e){
		e.preventDefault();
		if ($(this).parent().is('[open]')) {
			$(this).attr('aria-expanded', 'false');
			$(this).siblings(':not(summary)').css('transform', 'scaleY(0)');
			window.setTimeout(collapse, 300, $(this));
		} else {
			$(this).parent().attr('open', '');
			$(this).attr('aria-expanded', 'true');
		}
	});
});

/*Results*/
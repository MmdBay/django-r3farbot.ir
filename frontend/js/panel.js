const check = document.getElementById('check-active');



const checkAcktive = () => {
   const checkEl = check.textContent;
   if(checkEl.includes('Active')){
    classActive(check)
   } else {
    classOnActive(check)
   }
}
const classActive = (check) => {
    const activeList = check;
    activeList.classList.add('active');
}
const classOnActive = (check) => {
    const activeList = check;
    activeList.classList.add('inactive');
}
checkAcktive()


// ----------------- panel slideToggle jquery --------------
$(function () {
    $("#nav-icon").click(function () {
        $(".youtobe").slideToggle();
    });
    $("#nav-icon1").click(function () {
        $(".insta").slideToggle();
    });
    $("#nav-icon2").click(function () {
        $(".url").slideToggle();
    });
});

$(document).ready(function(){
	$('#nav-icon,#nav-icon1,#nav-icon2').click(function(){
		$(this).toggleClass('open');
	});
});
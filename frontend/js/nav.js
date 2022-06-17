$(function () {
    $("#button1").click(function () {
        $("#topmenu ul").slideToggle();
        // $("#cats").css("right", "-300px");
    });
    $("#left-botton").click(function () {
        if ($("#cats").css("left") == "-600px") {
            $("#cats").css("left", "0");
            $("#topmenu ul").slideUp();
        } else {
            $("#cats").css("left", "-600px");
        }
    });
    $("#right-botton").click(function () {
        if ($("#cats").css("left") == "-600px") {
            $("#cats").css("left", "0");
            $("#topmenu ul").slideUp();
        } else {
            $("#cats").css("left", "-600px");
        }
    });
    $("#cats .plus").click(function (event) {
        $(this).parent().siblings("ul").slideToggle();
        event.preventDefault();
    });

    $(window).resize(function () {
        if ($("#cats").css("width") != "300px") {
            // $("#cats .submenu").slideUp();
        }
    });
});

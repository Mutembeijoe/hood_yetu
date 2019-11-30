$(document).ready(function () {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");

    });



    // neighbourhood tabs
    $('#tab_header ul li.item').on('click', function () {
        var number = $(this).data('option');
        $('#tab_header ul li.item').removeClass('is-active');
        $(this).addClass('is-active');
        $('#tab_container .container_item').removeClass('is-active');
        $('div[data-item="' + number + '"]').addClass('is-active');
    });

    // search form ajax

    $('#business_search').submit(function (e) {
        e.preventDefault();
        // form = $('#business_search')
        // console.log(form.serialize())
        // $.ajax({
        //     type: "GET",
        //     url: "/neighbourhoods/business/search/",
        //     data: form.serialize(),
        //     dataType: "json",
        //     success: function (response) {
        //         console.log('success')
        //     }
        // });
    });
});
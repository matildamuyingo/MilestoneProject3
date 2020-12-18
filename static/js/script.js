$(document).ready(function(){

// MaterializeCss JavaScript
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();


    // If the checkbox for 'finished reading' is clicked, the bottompart of the form is displayed
        $('#read-check').click(function() {
            $('.fin-read').removeClass('no-display').addClass('full-display');
        });

        $('#upload-img').click(function() {
            $('#upload-img-field').removeClass('no-display').addClass('full-display');
            $('#upload-url-field').addClass('no-display').removeClass('full-display');
        })

        $('#upload-url').click(function() {
            $('#upload-url-field').removeClass('no-display').addClass('full-display');
            $('#upload-img-field').addClass('no-display').removeClass('full-display');
        })

// Edit buttons on cards

    // When mouse enters a card the 'no-display' class will be removed and the edit buttons will be visible
        $('.card-stacked').mouseenter(function(){
            $('.sub-book-edit-buttons', this).addClass('full-display').removeClass('no-display');
        });

    // When mouse leaves a card the 'no-display' class will be added again and the edit buttons will disappear
        $('.card-stacked').mouseleave(function(){
            $('.sub-book-edit-buttons', this).removeClass('full-display').addClass('no-display');
        });

    // Check card height and set all heights to the max height
        var maxHeight = 0;
        $(".book-card-style").each(function(){
        if ($(this).height() > maxHeight) { maxHeight = $(this).height(); }
        });

        $(".book-card-style").height(maxHeight);


  });
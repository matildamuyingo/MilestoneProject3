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

// Edit buttons on cards

    // When mouse enters a card the 'no-display' class will be removed and the edit buttons will be visible
        $('.card-stacked').mouseenter(function(){
            $('.sub-book-edit-buttons', this).addClass('full-display').removeClass('no-display');
        });

    // When mouse leaves a card the 'no-display' class will be added again and the edit buttons will disappear
        $('.card-stacked').mouseleave(function(){
            $('.sub-book-edit-buttons', this).removeClass('full-display').addClass('no-display');
        });
    
    // When a card displaying a book is clicked
    $('.card-content').click(function(){

        // Check the card height and save it in a variable
        var cardHeight = $('.card-content').height();

        // If the card height is larger than 130px remove the maxheight for that card so the review paragraph is visible
        if (cardHeight > 130){
            $(this).toggleClass('max-height');
            $('.row', this).css('height', cardHeight);
        }
    });
    

  });
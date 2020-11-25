$(document).ready(function(){

    // MaterializeCss JavaScript
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();


    // If the checkbox for 'finished reading' is clicked, the bottompart of the form is displayed
    $('#read-check').click(function() {
        $('.fin-read').removeClass('no-display').addClass('full-display');
    });

    // When mouse enters a card the 'no-display' class will be removed and the edit buttons will be visible
    $('.card-stacked').mouseenter(function(){
        $('.sub-book-edit-buttons', this).addClass('full-display').removeClass('no-display')
    })

    // When mouse leaves a card the 'no-display' class will be added again and the edit buttons will disappear
    $('.card-stacked').mouseleave(function(){
        $('.sub-book-edit-buttons', this).removeClass('full-display').addClass('no-display')
    })
    
    /*
    $('delete-book-button').click(function(){
        $(this).removeClass('full-display').addClass('no-display')
    })
    */

  });
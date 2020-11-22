$(document).ready(function(){

    // MaterializeCss JavaScript
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();



    $('#read-check').click(function() {
        $('.fin-read').removeClass('no-display').addClass('full-display');
        /*
        var isCheck = $(this).hasClass('no-display');
        if (isCheck == true){
            $('.fin-read').removeClass('no-display').addClass('full-display');
            console.log("Removed, works fine");
        } 
        else {
            $('.fin-read').removeClass('full-display').addClass('no-display');
            console.log("Displayed, works fine");
        }
        */
    });

  });
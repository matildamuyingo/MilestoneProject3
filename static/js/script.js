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

// Edit buttons for reviews
    // When mouse enters a card the 'no-display' class will be removed and the edit buttons will be visible
        $('.review-card').mouseenter(function(){
            $('.sub-book-edit-buttons', this).addClass('full-display').removeClass('no-display');
        });

    // When mouse leaves a card the 'no-display' class will be added again and the edit buttons will disappear
        $('.review-card').mouseleave(function(){
            $('.sub-book-edit-buttons', this).removeClass('full-display').addClass('no-display');
        });

    // Check card height and set all heights to the max height
        var maxHeight = 0;
        $(".book-card-style").each(function(){
        if ($(this).height() > maxHeight) { maxHeight = $(this).height(); }
        });

        $(".book-card-style").height(maxHeight);


    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

  });
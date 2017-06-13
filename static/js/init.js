(function($){
    $(function(){

        $('.button-collapse').sideNav();
        $('.slider').slider({interval:3000});
        $('.materialboxed').materialbox();
        $('.modal').modal();
        $('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 15, // Creates a dropdown of 15 years to control year
            format: 'dd-mm-yyyy'
        });

    }); // end of document ready
})(jQuery); // end of jQuery name space
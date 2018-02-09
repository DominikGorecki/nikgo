$(document).ready(clickInit);

function clickInit(){ 
  $(".on-click").click(function(event) {
    event.preventDefault();

    $(this).toggleClass('clicked');
    setTimeout(function() {
        window.location.href= $(this).attr('href');


    }.bind(this), 200);
    
  });
}
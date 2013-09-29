$(function(){
  
  // SHOW/HIDE POPUP CREATE TASK
//(function() {
//    var popup = $('.js-popup-task-add'),
//        showPopup = $('.js-task-add');
//        //close = popup.find('.popup-close');
//        
//    showPopup.click('live', function(e) {
//      popup.hide();       
//      //popup.fadeIn('slow');
//      popup.animate({ height: "show"}, 500, function() {});
//      
//      e.preventDefault();    
//    });
//
//    /*close.click('live', function(e) {
//      popup.hide();   
//      e.preventDefault();    
//    });*/
//  })();
  
  //CHECKBOX
  (function(){
    var checkbox = $('.js-checkbox');
    
    checkbox.each(function(index,value){
      var input = $(this).children('[type=checkbox]');
      input.hide();
      var widget = $('<a class="checked" href="javascript:;"></a>' +'<a class="unchecked" href="javascript:;"></a>');
      widget.insertBefore($(input)).hide();
      
      var checked = widget.closest('.checked'),
      unchecked = widget.closest('.unchecked');
      if (input.attr('checked') === 'checked') {
        $(checked).show();
      } else {
        $(unchecked).show();
      }
      
      $(checked).on('click',function(e){
        $(this).hide();
        $(unchecked).show();
        $(input).attr('checked', null);
        $(input).change();
        e.preventDefault();
      });
     
     $(unchecked).on('click',function(e){
       $(this).hide();
       $(checked).show();
       $(input).attr('checked', 'checked');
       $(input).change();
       e.preventDefault();
     });
    });
  })(); 
  
  // SHOW/HIDE DESC
  (function() {
    var taskDesc = $('.js-task-desc'),
        toggleDesc= $('.js-toggle-task-desc');
    toggleDesc.click(function(e){
      //$(taskDesc).hide();
      $(this).closest('.task-item').find('.js-task-desc').animate({ height: "toggle"}, 500, function() {});
      e.preventDefault(); 
    });
  })();
  
  // POPUP AWARDS
  (function() {
    var popup = $('.js-popup-awards'),
        showPopup = $('.js-see-popup-awards'),
        close = popup.find('.popup-close'),
        outside = $(popup).find('.popup-overlay');
        
    showPopup.click('live', function(e) {
      popup.fadeIn('fast');
      e.preventDefault();    
    });
  
    $(document).keydown(function(e) {
      if (e.which == 27) {
         popup.hide();   
      } else {
        return true;
      }
      e.preventDefault();   
    });
    
    outside.click('live', function(e) {
      popup.hide();   
      e.preventDefault();    
    });
    
    close.click('live', function(e) {
      popup.hide();   
      e.preventDefault();    
    });
  })();
  
});

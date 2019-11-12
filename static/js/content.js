$(document).ready(function(){
   $('.btn').on('click', function() {
   $('.btn').toggleClass('btnc');

   var value=$('.book-mian').position().left;

   if(value>250){
   		$('.book-mian').css('leftsidebar',30);
   		$('.book-mian').css('width','100%');
   }
   
   
   $('.leftsidebar').toggleClass('leftsidebar-c');
   if(value<250){
   		$('.book-mian').css('margin-left',2);
   		$('.book-mian').css('width','90%');
   }  	

});
});
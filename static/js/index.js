(function chatInit(){
$(document).ready(function(){
        $.get("/chatdata", function(data, status){
          res_polling = JSON.stringify(data);
          console.log(res_polling)
          $('#chatbox').html(res_polling);
        });
    });
})();

(function pollMessages(){
    $(document).ready(function(){

        $.get("/chatdata", function(data, status){
          res_polling = JSON.stringify(data);
          chat_text = $('#chatbox').text();


          if (chat_text != res_polling)
          {
            $('#chatbox').html(res_polling);
          }
          setTimeout(pollMessages, 1000)
        });
//      });
    });
})()
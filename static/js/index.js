(function getChatData(){
//$(document).ready(function(){
        res_polling=""
        $.get("/chatdata", function(data, status){
          res_polling = JSON.stringify(data);

            chat_text = $('#chatbox').text();

            if (chat_text != res_polling)
              {
                    output = ""
                    parsed_json = JSON.parse(res_polling)["data"];
                    for (key in parsed_json) {
                       value = parsed_json[key];
                        console.log(key, value);
                        output+="<span>"
                        output+="<div>"+value["from"]+": ";
                        output+= value["contents"]+"</div>";
                        output+="</span>"
                    }
                    $('#chatbox').html(output);
              }
        });
         setTimeout(getChatData, 1000)

})();

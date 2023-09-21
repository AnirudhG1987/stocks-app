
var user_id

function UpdateUserID(){
    //console.log(user_id);
    //user_id = user_id;
    alert("hello");
}



$('.board button').on('click',function() {

  // Recognize what column was chosen
  var col = $(this).closest("td").index();
  var row = $(this).closest("tr").index();
  //$('.board').find('tr').eq(row).find('td').eq(col).find('button').text(row);
    console.log("{{user_id}}");
    user_id=$('#user_id').text();
  $.ajax({
        type: "POST",
        url: 'my-ajax-test/',
        data: {row:row,col:col,user_id:user_id}, /* Passing the text data */
        dataType: 'json' ,
        success:  function(response){
                for(let i=0;i<3;i++){
                    for(let j=0;j<3;j++)
                    {
                        $('.board').find('tr').eq(i)
                            .find('td').eq(j).find('button')
                            .text(response.board[3*i+j]);

                    }
                }
                $('#xscore').text("X Score " + response.x_score)
                $('#oscore').text("O Score " + response.o_score)
           }

});


});


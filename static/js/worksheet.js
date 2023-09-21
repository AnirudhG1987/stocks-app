$(document).ready(function () {
   populateChapters("../static/json/grade5.json");
});

function populateChapters(json) {
  fetch(json)
    .then(response => response.json())
    .then(data => {
      let select = document.getElementById("selChapter");
      //console.log(select);
      //console.log(data["Chapters"]);
      //console.log(data.length);
      for (const x in data["Chapters"]) {
        let option = document.createElement("option");
        //console.log(x);
        option.text = String(x);
        option.value = String(x);
        select.appendChild(option);
      }
    });
}

function populateTopics(json,chapter) {
  fetch(json)
    .then(response => response.json())
    .then(data => {
      $("#selTopic").find('option').remove().end().append('<option value = "null">Select Topic</option>');
      let select = document.getElementById("selTopic");
      //console.log(select);
      //console.log(select);
      //console.log(data["Chapters"]);
      //console.log(data.length);
      for (const x in data["Chapters"][chapter]) {
        let option = document.createElement("option");
        //console.log(x);
        option.text = String(x);
        option.value = String(x);
        select.appendChild(option);
      }
    });
}


function myTopicFunction() {
//console.log("i am here topics");
  var e = document.getElementById("selChapter");
  var chapter = e.options[e.selectedIndex].value;
  if (chapter!="null"){
    //console.log(chapter);
    populateTopics("../static/json/grade5.json",chapter);
  }
}

function generateWorksheetFunction(){
   // Recognize what column was chosen
    var chapter = document.getElementById('selChapter').value;
    var topic = document.getElementById('selTopic').value;

  $.ajax({
        type: "POST",
        url: 'ajax_ws/',
        data: {chapter:chapter,topic:topic}, /* Passing the text data */
        dataType: 'json' ,
        success:  function(response){
                //console.log(response.filename);

                var a = document.createElement('a');
                a.setAttribute('href','../static/pdf/' + response.filename[0]);
                a.innerHTML = "Worksheet 1";
                // apend the anchor to the body
                // of course you can append it almost to any other dom element
                document.getElementById('id_Easy_WS').appendChild(a);
                var b = document.createElement('a');
                b.setAttribute('href','../static/pdf/' + response.filename[1]);
                b.innerHTML = "Worksheet 2";
                // apend the anchor to the body
                // of course you can append it almost to any other dom element
                document.getElementById('id_Easy_WS').appendChild(b);

                //var link = document.getElementById('id_ws_link');
                //console.log(link)
                //link.href   = link.href + response.filename

                //console.log(response)
                //"data:" + strMimeType + ";base64," + escape(strData);
                //window.open("data:application/pdf,;base64," + escape(response));


                //var blob = new Blob([response], {type: 'application/pdf'});
                //console.log(blob)
                //var url = URL.createObjectURL(blob);
                //console.log(url);
                //var iframe = document.getElementById('id_frame');
                //iframe.src = url;
                //var pdfAsDataUri = "data:application/pdf;base64,"+response;
                //window.open(pdfAsDataUri);
                //window.open("data:application/pdf," + escape(response));
                //window.navigator.msSaveOrOpenBlob(blob, "sample.pdf");

        },
  });

}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function complete(id,klaar){


var http = new XMLHttpRequest();

var text = document.getElementById("process");
console.log("showing text");
console.log(text);
text.style.display = "block";
console.log(text);

var html = document.getElementById(id);
var full_id = html.textContent;
var params = 'id=' + full_id + '&klaar=' + klaar;
//var params = 'id=' + full_id + ',klaar='+ klaar;
const url='https://data.mb-server.com';

http.open('POST', url, true);

//Send the proper header information along with the request
http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

http.onreadystatechange = function() {//Call a function when the state changes.
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
    }
}
http.send(params);
await sleep(750)
window.location.reload(true)

}

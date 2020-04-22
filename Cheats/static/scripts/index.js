//This is the script for the landing page
//the code included here is to demonstrate how the landing page and search page relate. 

console.log("script file loaded");

var restuarantList = [];

function getLocation(geoLocation) {
    // console.log({
    //     "latitude" : geoLocation.coords.latitude,
    //     "longitude" : geoLocation.coords.longitude,
    // });
    
    let geoLocation2 = {
        latitude : geoLocation.coords.latitude,
        longitude : geoLocation.coords.longitude,
    }
    
    $.ajax({
        url : "/GetDB",
        type : 'POST',
        contentType: "application/json;charset=UTF-8",
        async: false,
        data: JSON.stringify(geoLocation2),
        success: function(response){
            console.log(response)
            //restuarantList = JSON.parse(response);
        },
        error: function(xhr) {
            console.log(xhr)
            console.log("error with location handeling");
        }
    });
};


function searchCarry(){
    var searchterms = document.getElementById('search-box').value;
    var searchterms = searchterms.trim();  
    var searchterms = encodeURIComponent(searchterms);

    window.location.href = ("http://127.0.0.1:5000/search/" + searchterms);
}

window.onload = function() {
    var searchTrigger = document.getElementById('submit-search');
    searchTrigger.addEventListener("click", searchCarry);

    navigator.geolocation.getCurrentPosition(getLocation);

    if(getCookie('storeId') != ""){
        var idList = getCookie('storeId').split(',');
        //getprevious(idList);
        //alert("sending: " + idList);
        
        $.ajax({
            type: 'POST',
            async: false,
            url: '/getInfo',
            contentType: "application/json; charset=utf-8",
            data:  JSON.stringify({ 
                'ids' : idList // <-- the $ sign in the parameter name seems unusual, I would avoid it
            }),
            success: function(msg){
                createPrevious(JSON.parse(msg));
                alert("previous created");
            }
        });


    }


}


//gets the cookie if it exsits
//will just append further ids on to the cookie after that
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

//creates the cards at the bottom of the screen
//needs to be style and altered so that it is visually appealing
function createPrevious(ids){
    console.log(ids);
    var rootForm = document.getElementById("root");
    for(i in ids){
        each = ids[i];

        var nameHolder = document.createElement('h1');
        nameHolder.innerText = each['name'];
        rootForm.appendChild(nameHolder)
    }
}
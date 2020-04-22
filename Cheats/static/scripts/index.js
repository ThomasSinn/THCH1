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
}

/*
document.getElementById("home").href = location.origin;
var a = str.concat(location.origin, '/about');
console.log(a);
let f = str.concat(location.origin, '/faq');
let c = str.concat(location.origin, '/contact');
document.getElementById("about").href = a;
document.getElementById("faq").href = f;
document.getElementById("contact").href = c;
*/

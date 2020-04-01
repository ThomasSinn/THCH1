//This is the script for the landing page
//the code included here is to demonstrate how the landing page and search page relate. 

console.log("script file loaded");

var restuarantList = [];

function getLocation(geoLocation) {
    console.log({
        "latitude" : geoLocation.coords.latitude,
        "longitude" : geoLocation.coords.longitude,
    });
    
    let geoLocation2 = {
        latitude : geoLocation.coords.latitude,
        longitude : geoLocation.coords.longitude,
    }
    
    $.ajax({
        url : "/GetDB",
        type : 'POST',
        contentType: "application/json;charset=UTF-8",
        async: false,
        data : JSON.parse(geoLocation2),
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

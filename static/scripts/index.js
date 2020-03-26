//This is the script for the landing page
//the code included here is to demonstrate how the landing page and search page relate. 

console.log("script file loaded");

window.onload = function() {
    var searchTrigger = document.getElementById('submit-search');
    searchTrigger.addEventListener("click", searchCarry);
}

function searchCarry(){
    var searchterms = document.getElementById('search-box').value;
    var searchterms = searchterms.trim();  
    var searchterms = encodeURIComponent(searchterms);

    window.location.href = ("http://127.0.0.1:5000/search/" + searchterms);
}
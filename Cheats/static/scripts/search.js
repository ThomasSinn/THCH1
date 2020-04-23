console.log("Loaded Script")

function makefeed(posts){
    let post;
    for (post in posts){
        makepost(posts[post]);
    }
}

function makepost(data){
    let feed = document.getElementById("searchPro");

    let newpost = document.createElement("li");
    newpost.setAttribute("class", "post");
    newpost.innerHTML = data;

    feed.appendChild(newpost);
}


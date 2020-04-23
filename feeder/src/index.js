function makefeed(posts){
    let root = document.getElementById("root");

    let main = document.createElement("main");
    main.setAttribute("class", "main");
    main.setAttribute("id", "main");
    root.appendChild(main);

    let post;
    for (post in posts){
        makepost(posts[post]);
    }
}

function makepost(data){
    let feed = document.getElementById("main");

    let newpost = document.createElement("li");
    newpost.setAttribute("class", "post");
    newpost.innerHTML = data;

    feed.appendChild(newpost);
}

makefeed(["somedata", "data2", "bruh", "somedata", "data2", "bruh","somedata", "data2", "bruh","somedata", "data2", "bruh","somedata", "data2", "bruh","somedata", "data2", "bruh","somedata", "data2", "bruh","somedata", "data2", "bruh","somedata", "data2", "bruh","somedata", "data2", "bruh",])
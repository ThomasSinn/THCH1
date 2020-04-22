//creates the cards for the results page.
//will allow for a redirect to a genuine compare page. 
var AUTH_KEY = "AIzaSyDHAlJ2Qs0KBhp4gWuJ2tl1JcNkwVvf5w4"

function populater(resResults){
    console.log(resResults);
    //console.log("this should be the list passed to the page by flask");
    navigator.geolocation.getCurrentPosition((pos) => {
                //userLocation = pos;
                //console.log(userLocation)
                getDistance(resResults, pos)
        });

    var rootForm = document.getElementById('theform');
    for(i in resResults){
        each = resResults[i]
        var mainDiv = document.createElement('div');
        mainDiv.setAttribute('class', "column");
        mainDiv.setAttribute('id', each.id)
        var cardDiv = document.createElement('div')
        cardDiv.setAttribute('class', 'card');
        var imgsrc = document.createElement('img');
        imgsrc.setAttribute('src', each.photopath);
        imgsrc.setAttribute('style', 'width:100%');
        cardDiv.appendChild(imgsrc);
        var container = document.createElement('div');
        container.setAttribute('class', 'container');

        var textTag = document.createElement('h4');
        //console.log("name as per the results list")
        //console.log(each.name)
        textTag.innerText = each.name;
        container.appendChild(textTag);

        var dis = document.createElement('p');
        dis.innerText="Distance";
        dis.setAttribute("id", each.id+"p")
        var rating = document.createElement('p');
        rating.innerText = "rating: " + each.rating;

        container.appendChild(dis);
        container.appendChild(rating);
        cardDiv.appendChild(container);

        mainDiv.setAttribute('onclick', 'click_handler(this.id)')

        mainDiv.appendChild(cardDiv);
        rootForm.appendChild(mainDiv);
        //console.log((document.getElementById(each.id).childNodes)[0].childNodes[1].childNodes[1].innerText);
    }
}

function click_handler(click_id){
    //alert(click_id)
    console.log("http://127.0.0.1:5000/store/" + click_id);
    window.location.href  = "http://127.0.0.1:5000/store/" + click_id;
        
}

function getDistance(resResults, userLocation){
    //dodgy coding 101
    
    for(i in resResults){
        lat = resResults[i].lat;
        lng = resResults[i].lng;
        id = resResults[i].id;
        var request = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metirc&origins="
        //console.log(userLocation)
        request = request + userLocation.coords.latitude + "," + userLocation.coords.longitude;
        request = request + "&destinations=" + lat + "," + lng;
        request = request + "&key=" + AUTH_KEY;
        console.log(request)
        //document.getElementById(each.id).childNodes)[0].childNodes[1].childNodes[1].innerText
        $.post(request, function(data){

            $(id+"p").replaceWith(data.rows[0].elements[0].distance.text);

            //document.getElementById(id+'p').innerText = data.rows[0].elements[0].distance.text;
            console.log(document.getElementById(id+'p'));
            
        });
    };
}
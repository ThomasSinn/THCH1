// This is a tester to try and convert html to JS

document.getElementById("home").href = location.origin;

function tryme() {
    // just to check if the files are linked properly 
    alert('hello');
};

/*
// make some ajax calls 
$(document).ready(function() {
    //alert('damn')
    $.ajax({
        type: 'GET', 
        url: '/shit'
    })
    .done(function(data){
        // alert('shit');
        // document.write('shitfuckfuckingwork');
        // document.write(data.result);
        $('#result').text(data.result);
    });
})
*/
/*
$(document).ready(function() {
    //alert('damn')
    $.ajax({
        type: 'GET', 
        headers: {  'Access-Control-Allow-Origin': `http://127.0.0.1:${port}/menuPricing/${cuisine}`},
        url: `http://127.0.0.1:${port}/menuPricing/${cuisine}`
    })
    .done(function(data){
        // alert('shit');
        // document.write('shitfuckfuckingwork');
        // document.write(data.result);
        console.log('the data is');
        console.log(data);
        $('#result').text(data.result);
        
    });
})
*/
/*
fetch(`http://127.0.0.1:${port}/menuPricing/${cuisine}`,{
    mode: 'no-cors',
    headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'Accept': 'application/json'
    }
}).then(function(response) {
    return response;
}).then(function (json) {
    console.log('GET response text:');
    let obj = JSON.parse(json.body);
    console.log(JSON.stringify(obj)); // Print the greeting as text
    console.log(JSON.stringify(json));
    console.log(json.body);
})
.catch(error => { console.log('request failed', error); }); // Syntax error: unexpected end of input
//console.log(obj)
*/


let port = 5001;
let cuisine = "cafe";
//var prices = [];
const asyncFuck = async function get_menu(port, cuisine){
    const res2 = await fetch(`http://127.0.0.1:${port}/menuPricing/${cuisine}`,{
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': 'application/json'
        }
    }).then((resp) => resp.json()).then((data) => {
        prices = data;
        return data;
    });
    console.log(res2)
}

const main = (port, cuisine) => {
    const result = asyncFuck(port, cuisine);
    return result;
}

let prices = main(port, cuisine);
console.log("Prices dict");
console.log(prices);



//This is the code for the boxes but not fully working so commented out 
/*
const container = document.getElementById("container");

function makeRows(rows, cols) {
    container.style.setProperty('--grid-rows', rows);
    container.style.setProperty('--grid-cols', cols);
    for (c = 0; c < (rows * cols); c++) {
        let cell = document.createElement("div");
        cell.innerText = (c + 1);
        container.appendChild(cell).className = "grid-item";
        if (c+1 == 1) {
            cell.innerHTML = "";
            cell.style.border = "none";
        }
        if (c+1 == 2) {
            var ubereatslogo = document.createElement("img");
            ubereatslogo.setAttribute("src", "../locationpics/5310383-uber-eats-logo-png-93-images-in-collection-page-1-uber-eats-png-1200_630_preview.png");
        // cell.appendChild("ubereatslogo");
    }
    if (c+1 == 7|| c+1 == 12 || c+1 == 17 || c+1 == 22) {
        cell.style.border = "solid black";
    }
    if (c+1 == 8|| c+1 == 13 || c+1 == 18 || c+1 == 23) {
        cell.style.border = "solid red";
    }
    if (c+1 == 9|| c+1 == 14 || c+1 == 19 || c+1 == 24) {
        cell.style.border = "solid green";
    }    
    if (c+1 == 10|| c+1 == 15 || c+1 == 20 || c+1 == 25) {
        cell.style.border = "solid blue";
    }
};
};

makeRows(5, 5);



<div class="ubereats">
<img class="ubereatslogo" src="{{ url_for('static', filename='5310383-uber-eats-logo-png-93-images-in-collection-page-1-uber-eats-png-1200_630_preview.png') }}">

</div>
<div class="doordash">
<img class="ubereatslogo" src="{{ url_for('static', filename='Doordash.png') }}">
                </div>
                <div class="menulog">
                <img class="ubereatslogo" src="{{ url_for('static', filename='menulog.png') }}">
                </div>
                <div class="deliveroo">
                <img class="ubereatslogo" src="{{ url_for('static', filename='deliveroo.png') }}">
                </div>
                */
               
function set_image(parent, url) { 
    var img = new Image(); 
    img.src = url; 
    parent.appendChild(img);   
}  
window.onload = function() {
    var body = document.getElementById("TBL");
    var table = document.createElement('TABLE');
    var tblB = document.createElement('TBODY');
    
    table.appendChild(tblB);
    row = 5;
    col = 5;
    for (var i=0; i<row; i++)
    {
        var tr = document.createElement('TR');
        tblB.appendChild(tr);
        
        for (var j=0; j<col; j++) {
            var td = document.createElement('TD');
            //td.style.borderRadius = '10px';
            
            if (i==0 && j==1) {
                //set_image(td, "/../static/5310383-uber-eats-logo-png-93-images-in-collection-page-1-uber-eats-png-1200_630_preview.png");    
                var l = document.getElementById("ubereatslogo");
                l.style.height = "50px";
                l.style.width = "80px";
                td.appendChild(l);
            } else if (i==0 && j==2) {
                //set_image(td, "{{ url_for('static', filename='Doordash.png') }}");
                var m = document.getElementById("doordashlogo");
                m.style.height = "50px";
                m.style.width = "80px";
                td.appendChild(m);
            } 
            else if (i==0 && j==3) {
                //set_image(td, "{{ url_for('static', filename='menulog.png') }}");
                var n = document.getElementById("menuloglogo");
                n.style.height = "50px";
                n.style.width = "80px";
                td.appendChild(n);
            } 
            else if (i==0 && j==4) {
                //set_image(td, "{{ url_for('static', filename='deliveroo.png') }}");
                var o = document.getElementById("deliveroologo");
                o.style.height = "50px";
                o.style.width = "80px";
                td.appendChild(o);
            } 
            
            if (i != 0) {
                if ((i*row + j)%5 == 0) {
                    console.log(prices[i-1]["item"]);
                    console.log(i-1);
                    td.innerHTML = prices[i-1]["item"];
                }
                if ((i*row + j - 1)%5 == 0) {
                    td.style.border = "solid black 2px";
                    td.innerHTML = prices[i-1]["prices"][0]["price"]
                }
                if ((i*row + j - 2)%5 == 0) {
                    td.style.border = "solid red 2px";
                    td.innerHTML = prices[i-1]["prices"][2]["price"]
                }
                if ((i*row + j - 3)%5 == 0) {
                    td.style.border = "solid rgb(8, 196, 8)  2px";
                    td.innerHTML = prices[i-1]["prices"][3]["price"]
                }
                if ((i*row + j - 4)%5 == 0) {
                    td.style.border = "solid rgb(54, 42, 231) 2px";
                    td.innerHTML = prices[i-1]["prices"][1]["price"]
                }
            }


            tr.appendChild(td);
        }
    }
    body.appendChild(table)
    //initMap();
}

// function updateInfo(info){
//     info = JSON.parse(info)
//     console.log(info)
//     return info
// }

// // window.onload = function(){
// //     initMap();
// // }

// function initMap(store){
//     var map;
//     console.log(store)
//     //console.log(storeInfo.lat + " " + storeInfo.lng)
//     map = new google.maps.Map(document.getElementById('map'), {
//         center: {lat: -34.397, lng: 150.644},
//         zoom: 8
//     });
// }

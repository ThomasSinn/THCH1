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

/*
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
*/
/* CHANGE THIS ONE FOR THE NEW API */
/*
//var prices = [];

var latlong = {}; // object of the lat and longitude 
const get_lat = async function lat(rid){
    const res6 = await fetch(`http://127.0.0.1:5000/ridlatlong/${r_id}`,{
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': 'application/json'
        }
    }).then((resp) => resp.json()).then((data) => {
        prices = data;
        return data;
    });
    console.log(res6)
    latlong = res6;
    latlong.lat = String(latlong.lat);
    latlong.lng = String(latlong.lng);
    latlong.lat = latlong.lat.replace(".", "%2E");
    latlong.lng = latlong.lng.replace(".","%2E");
    console.log(latlong.lng)
    get_menus(latlong);
}

const main6 = (r_id) => {
    const result = get_lat(r_id);
    return result;
}

var coord = main6(r_id);
console.log("co-ords dict");
console.log(coord);

var menu_items = {};
const get_menus = async function menus(latlong) {
    const menu_f = await fetch(`http://127.0.0.1:5001/menuPricing/?lat=${latlong.lat}&lng=${latlong.lng}`, {
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': 'application/json'
        }
    }).then((resp) => resp.json()).then((data) => {
        return data;
    });
    console.log(menu_f);
    menu_items = menu_f;
}
*/
/*
const main7 = (latlong) => {
    const result = get_menus(latlong);
    return result;
}
*/
/*
var m = main7(latlong);
console.log("menu items");
console.log(m);
*/

/*
var menu_url = new URL(),
params = {lat:35.696233, long:139.570431}
Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
fetch(url).then()
*/

/*
first update the database which will have the restaurant id 
    and the cuisine assign cuisine by keywords as they are loaded in
    
    query the backend with the id that is stripped from the url 
    returning the cuisine type

    then get the cuisine from the backend and do the next query for the food 
*/

// get the store id from the url then use it to call the backend 

/*
const main = (port, cuisine) => {
    const result = asyncFuck(port, cuisine);
    return result;
}


var prices = main(port, cuisine);
console.log("Prices dict");
console.log(prices);
*/

/*
const asyncFuck2 = async () => {
    const res3 = await fetch('http://api.exchangeratesapi.io/latest?base=AUD&symbols=USD,GBP,JPY,CNY,NZD,EUR',{
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': 'application/json'
        }
    }).then((resp) => resp.json()).then((data) => {
        return data;
    });
    console.log(res3)
}

const main2 = () => {
    const result1 = asyncFuck2();
    return result1;
}

let rates = main2();
console.log("rates dict");
console.log(rates);
*/
var url = window.location.href;
var n = url.indexOf("/store/");
var r_id = parseInt(url.substring(n + 7));
console.log(url);
console.log(r_id);

// I want to get the cuisine out of this 
var cuisine = "";
let port = 5001;
var prices = [];
//console.log(cuisine[0]);
var rates = {};
/*
const asyncCuisine = async function get_cuisine(r_id){
    const res5 = await fetch(`http://127.0.0.1:5000/getCuisine/${r_id}`,{
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': 'application/json'
        }
    }).then((resp) => resp.json()).then((data) => {
        cuisine = data;
        return data;
    });
    console.log(res5);
    asyncFuck(port, cuisine[0]);
}
asyncCuisine(r_id);
*/
c = 0;
const asyncFuck = async function get_menu(r_id){
    if (c == 0) {
        const res5 = await fetch(`http://127.0.0.1:5000/getCuisine/${r_id}`,{
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Accept': 'application/json'
            }
        }).then((resp) => resp.json()).then((data) => {
            cuisine = data;
            return data;
        });
        console.log(res5);
        //asyncFuck(port, cuisine[0]);

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
        //}
        //const asyncFuck2 = async () => {
        console.log('asyncFUCK2');
        const res3 = await fetch('http://127.0.0.1:5000/exchange',{
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Accept': 'application/json'
            }
        }).then((resp) => resp.json()).then((data) => {
            return data;
        });
        console.log(res3);
        rates = res3;
    }
    console.log('inside the async');
    change_ex(prices, rates);
    var e = document.createElement("div");    
    var ex_ = document.getElementById("list").value;
    ex_ = String(ex_);
    e.innerHTML = rates[ex_];
    var exch = document.getElementById('list');
    exch.appendChild(e);
    c=1;
}
console.log('outside async');
console.log(rates);
asyncFuck(r_id);

//console.log(rates);
/*
const main2 = () => {
    const result1 = asyncFuck2();
    return result1;
}

rates1 = main2();
console.log("rates dict");
console.log(rates1);
*/


/* 
change the exchange rate 
*/ 
/* NOW WE HAVE THE EXCHANGE RATES AND THE PRICES 
we need to make a click button maybe in the nav bar dropdown menu? to change the prices

*/
let change = 0;

// if change = 1 then it has been changed before
change_ex = (prices, rates) => {
    var curr = document.getElementById("list").value;
    console.log(curr);
    curr = String(curr);
    console.log(rates);
    if (rates[curr] != undefined) {
        console.log("CHANGING THE PRICES");
        //location.reload(true);
        var ex_prices = [];
        // multiply the prices dictionary 
        for (i=0;i<prices.length;i++) {
            let p_list = prices[i]["prices"];
            for (j=0; j < p_list.length; j++) {
                console.log(prices[i]["prices"][j]["price"]);
                console.log(rates[curr]);
                console.log(curr);
                prices[i]["prices"][j]["price"] = prices[i]["prices"][j]["price"] * rates[curr];
                prices[i]["prices"][j]["price"] = prices[i]["prices"][j]["price"].toFixed(2);
                console.log(prices[i]["prices"][j]["price"]);
            }
        }
        change = 1;
        console.log("the changed prices are");
        console.log(prices);
        console.log(curr);

        var body = document.getElementById("TBL");
        var table = document.getElementById('TAB');
        var tblB = document.getElementById('tblB');

        //table.appendChild(tblB);
        row = 5;
        col = 5;
        for (var i=0; i<row; i++)
        {
            var tr = document.getElementById('tr' + i);
            //tblB.appendChild(tr);
            
            for (var j=0; j<col; j++) {
                //var td = document.createElement('TD');
                var td = document.getElementById(i*row + j);
                //td.style.borderRadius = '10px';
                /*
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
                */
                if (i != 0 && change != 0) {
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
                //tr.appendChild(td);
            }
        }
    }
    //body.appendChild(table)
    change = 1;
    return prices;
    
    //var p = 1; 
    //p = p *rates[curr];
    //console.log(curr);
    //console.log(p);
   //return p;
}

               
function set_image(parent, url) { 
    var img = new Image(); 
    img.src = url; 
    parent.appendChild(img);   
}  

window.onload = function () {
    if(getCookie("storeId") == ""){
        createCookie(info);
    }else{
        var cur = getCookie('storeId');
        //alert(cur)
        document.cookie = "storeId=" + cur + "," + info.id + ";" + "path=/";
        //alert(getCookie('storeId'))
    }

    var body = document.getElementById("TBL");
    var table = document.createElement('TABLE');
    table.id = 'TAB';
    var tblB = document.createElement('TBODY');
    tblB.id = 'tblB';
    
    table.appendChild(tblB);
    row = 5;
    col = 5;
    for (var i=0; i<row; i++)
    {
        var tr = document.createElement('TR');
        tr.id = 'tr' + i;
        console.log(tr.id);
        tblB.appendChild(tr);
        
        for (var j=0; j<col; j++) {
            var td = document.createElement('TD');
            td.id = i*row + j;
            //td.style.borderRadius = '10px';
            if (i==0 && j==1) {
                //set_image(td, "/../static/5310383-uber-eats-logo-png-93-images-in-collection-page-1-uber-eats-png-1200_630_preview.png");    
                var l = document.getElementById("ubereatslogo");
                var link1 = document.getElementById('uber');
                link1.href = "https://www.ubereats.com/au";
                l.style.height = "50px";
                l.style.width = "80px";
                //link1.appendChild(l)
                td.appendChild(link1);
            } else if (i==0 && j==2) {
                //set_image(td, "{{ url_for('static', filename='Doordash.png') }}");
                var m = document.getElementById("doordashlogo");
                var link2 = document.getElementById('door');
                link2.href = "https://www.doordash.com/en-US";
                m.style.height = "50px";
                m.style.width = "80px";
                //link1.appendChild(m)
                td.appendChild(link2);
            } 
            else if (i==0 && j==3) {
                //set_image(td, "{{ url_for('static', filename='menulog.png') }}");
                var n = document.getElementById("menuloglogo");
                var link3 = document.getElementById('menu');
                link3.href = "https://www.menulog.com.au/";
                n.style.height = "50px";
                n.style.width = "80px";
                //link3.appendChild(n)
                td.appendChild(link3);
            } 
            else if (i==0 && j==4) {
                //set_image(td, "{{ url_for('static', filename='deliveroo.png') }}");
                var o = document.getElementById("deliveroologo");
                var link4 = document.getElementById('deli');
                link4.href = "https://deliveroo.com.au/";
                o.style.height = "50px";
                o.style.width = "80px";
                //link1.appendChild(o)
                td.appendChild(link4);
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

//creates a new cookie if required. 
function createCookie(Info){
    document.cookie = 'storeId=' + Info.id + ";" + "path=/";
}


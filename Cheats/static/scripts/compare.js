// This is a tester to try and convert html to JS

function tryme() {
    // just to check if the files are linked properly 
    document.write("hello");
};

// make some ajax calls 
$(document).ready(function() {
    //alert('damn')
    /*$.getJSON('/shit'), {
    }, function(data) {
        $("#result").text(data.result);
    }*/
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








/*
This is the code for the boxes but not fully working so commented out 

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
/*

/*

num = 5
str = "item " + num;
console.log(str);
*/


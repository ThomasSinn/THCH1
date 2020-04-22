function revealMessage() {
    document.getElementById("hiddenMessage").style.display = 'block';

}

function countDown() {
    var currentVal = document.getElementById("countDownButton").innerHTML;
    var newVal = 0;
    if (currentVal > 0) {
        var newVal = currentVal - 1;
        document.getElementById("countDownButton").innerHTML = newVal;
    }


}

/*
$(function() {

    alert("find an island");
    document.write("found it");

});
*/
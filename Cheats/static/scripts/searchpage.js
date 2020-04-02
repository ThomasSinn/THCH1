var x = document.getElementsByClassName("card");

let i;
for (i in x) {
    try {
    x[i].addEventListener("click", (event) => {
        window.location.href = "/store/pizza"
    });
    } catch {}
}
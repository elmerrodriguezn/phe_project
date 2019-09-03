let getYear;
(getYear = function () {
    const date = new Date();
    document.querySelector('.year').innerHTML = date.getFullYear();
})();

let menuIcon;
(menuIcon = function (x) {
    if (x) {
        x.classList.toggle("change");
    }
})();
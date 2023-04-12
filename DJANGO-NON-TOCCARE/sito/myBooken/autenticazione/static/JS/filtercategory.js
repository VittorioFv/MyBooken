const scrollmenu = document.querySelectorAll(".categoryscrollmenu a")
const scrollmenuclose = document.querySelectorAll(".categoryscrollmenufiltrata a")

function openfn(e) {
    var id = e.target.dataset.id
    var singlecategoryfiltrata = document.querySelector("#" + id);
    singlecategoryfiltrata.classList.remove('nascosto');
}

function closefn(e) {
    var id = e.target.dataset.id
    const singlecategoryfiltrata = document.querySelector("#" + id);
    singlecategoryfiltrata.classList.add('nascosto');
}


scrollmenu.forEach(element => {
    element.addEventListener('click', openfn)
});

scrollmenuclose.forEach(element => {
    element.addEventListener('click', closefn)
});

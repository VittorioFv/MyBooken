const overlay = document.querySelector("#overlay");

document.querySelector("#show-modal-btn").addEventListener("click", () => {
    overlay.style.display = 'block';
})

document.querySelector("#close-modal-btn").addEventListener("click", () => {
    overlay.style.display = 'none';
})

function myalert() {
    alert("La posizione è indicativa del paese nel quase si trova il libro.");
}
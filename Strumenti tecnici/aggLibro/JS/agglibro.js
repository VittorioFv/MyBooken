const overlay = document.querySelector("#overlaybook");

document.querySelector("#show-modalbook-btn").addEventListener("click", () => {
    overlay.style.display = 'block';
})

document.querySelector("#close-modalbook-btn").addEventListener("click", () => {
    overlay.style.display = 'none';
})

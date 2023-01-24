if (window.innerWidth > window.innerHeight){
  document.querySelector("body").classList.add("desktop");
}

function openNav() {
  document.getElementById("sidebar").style.width = "80vw";
  document.getElementById("close").style.display = "block";
  document.getElementById("close").style.opacity = "20%";
}

function closeNav() {
  document.getElementById("sidebar").style.width = "0";
  document.getElementById("close").style.display = "none";
  document.getElementById("close").style.opacity = "0%";
}

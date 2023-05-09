
/**** Mappa ***/

const mappa = document.querySelector(".mappa");
const libri = document.querySelector(".containerschedalibrimobile");

var mappaAttiva = false;
document.querySelector("#show-modal-btn").addEventListener("click", () => {
    if (!mappaAttiva) {
        mappa.style.bottom = '5vh';

        libri.classList.add("horizontal");
    } else {
        mappa.style.bottom = '-70vh';

        libri.classList.remove("horizontal");
    }

    mappaAttiva = !mappaAttiva;
})

data = document.querySelectorAll(".data")
var d = [];
data.forEach((e) => {
    var l = e.innerHTML.indexOf(",");
    d.push([parseFloat(e.innerHTML.substring(0, l)),
            parseFloat(e.innerHTML.substring(l+1, e.innerHTML.length))
          ]);
})

if (d.length > 0) {
  lon = 0;
  lat = 0;
  d.forEach( (e) => {
    lon += e[0];
    lat += e[1];
  });
  lon /= d.length;
  lat /= d.length;
} else {
  lon = 10.9924122;
  lat = 45.4384958;
}

var map = L.map('basicMap').setView([lat, lon], 12);
var markersArray = []

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//L.marker([45.4384958, 10.9924122]).addTo(map);
d.forEach((i) => {
  const marker = L.marker([i[1], i[0]]).addTo(map);
})


//INIZIO
function cercaCitta(cittaDaCercare) {
  var cittaDaCercare = document.getElementById("citta").value;

  var url = "https://nominatim.openstreetmap.org/search?format=json&q=" + cittaDaCercare;
  fetch(url)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      var lat = data[0].lat;
      var lon = data[0].lon;
      map.setView(new L.LatLng(lat, lon), 13);
      currentMarker = L.marker([lat, lon]).addTo(map);
      //map.fitBounds(marker.getBounds());
      document.getElementById("longitudine").value = lon;
      document.getElementById("latitudine").value = lat;
   
      document.getElementById('basicMap').style.left = "20%";
      document.getElementById('overlay').style.display = "block";
      document.getElementById('bottoneRicerca').style.display = "block";
      document.getElementById('domanda').style.display = "block";

    })
    .catch(function(error) {
      console.log(error);
    })
    .finally(() => {
      document.getElementById('basicMap').style.left = "20%";
      document.getElementById('overlay').style.display = "block";
      document.getElementById('bottoneRicerca').style.display = "block";
      document.getElementById('domanda').style.display = "block";
    });
}
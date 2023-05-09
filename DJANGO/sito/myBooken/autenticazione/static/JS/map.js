var map = L.map('basicMap').setView([45.4384958, 10.9924122], 13);
var markersArray = []
var currentMarker = null;
var open = null;

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

function updateDivPosition() {
  if(open == 1){
    if (window.innerWidth > 992) {
      document.getElementById('basicMap').style.left = "20%";
    } else {
      document.getElementById('basicMap').style.left = "10%";
    }
  }else{
    document.getElementById('basicMap').style.left = "-150vw";
  }
}

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
      open = 1;

    })
    .catch(function(error) {
      console.log(error);
    })
    .finally(() => {
      updateDivPosition();
      document.getElementById('overlay').style.display = "block";
      document.getElementById('bottoneRicerca').style.display = "block";
      document.getElementById('domanda').style.display = "block";
      open = 1;
    });
}

map.on('click', (event) => {
  // rimuovi il marker precedente se esiste
  if (currentMarker) {
    console.log("funziona quasi");
    map.removeLayer(currentMarker);
  }
  // aggiungi un nuovo marker alla mappa
  const marker = L.marker([event.latlng.lat, event.latlng.lng]).addTo(map);
  currentMarker = marker;

  document.getElementById("longitudine").value = event.latlng.lng;
  document.getElementById("latitudine").value = event.latlng.lat;
});

var conferma = false;
document.querySelector("form").addEventListener("submit", (e) => {
  if (!conferma) {
    e.preventDefault();    
    cercaCitta();
  }
});

document.querySelector("#bottoneRicerca").addEventListener("click", () => {
  conferma = true;
  document.querySelector("form").submit();
});




window.addEventListener('resize', updateDivPosition);
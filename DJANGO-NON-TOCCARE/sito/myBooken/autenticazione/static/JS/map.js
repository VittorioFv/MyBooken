var map = L.map('basicMap').setView([45.4384958, 10.9924122], 13);
var markersArray = []
var currentMarker = null;


  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//L.marker([45.4384958, 10.9924122]).addTo(map);


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
      console.log("Quello che mi interessa: "+ document.getElementById("longitudine").value);
      console.log("Quello che mi interessa: "+ document.getElementById("latitudine").value);

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

map.on('click', (event) => {
  // rimuovi il marker precedente se esiste
  if (currentMarker) {
    console.log("funziona quasi");
    map.removeLayer(currentMarker);
  }
  // aggiungi un nuovo marker alla mappa
  const marker = L.marker([event.latlng.lat, event.latlng.lng]).addTo(map);
  currentMarker = marker;
  console.log("Valore vecchio longitudine: " + document.getElementById("longitudine").value);
  console.log("Valore vecchio latitudine: " + document.getElementById("latitudine").value);

  document.getElementById("longitudine").value = event.latlng.lng;
  document.getElementById("latitudine").value = event.latlng.lat;

  console.log("New value longitudine: " + document.getElementById("longitudine").value);
  console.log("New value latitudine: " + document.getElementById("latitudine").value);


});

var conferma = false;
document.querySelector("form").addEventListener("submit", (e) => {
  if (!conferma) {
    e.preventDefault();
    console.log("hei");
    
    cercaCitta();

  } else {
    console.log("ciao");
  }
});

document.querySelector("#bottoneRicerca").addEventListener("click", () => {
  conferma = true;
  document.querySelector("form").submit();
});
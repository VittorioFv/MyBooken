//document.getElementById("bottoneRicerca").addEventListener("click", cercaCitta(document.getElementById("citta").value))
const zoom = 13;
var markers = new OpenLayers.Layer.Markers("Markers");
var markersArray = []

/********************* CREA LA MAPPA ************************/
map = new OpenLayers.Map("basicMap");
var mapnik = new OpenLayers.Layer.OSM();
var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
var toProjection = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
var position = new OpenLayers.LonLat(10.9, 45.5).transform(fromProjection, toProjection);

map.addLayer(mapnik);
map.addLayer(markers);
map.setCenter(position, zoom);

setCenterCoordinatesLonLat(10.9924122, 45.4384958);

function setCenterCoordinatesLonLat(lon, lat) // Sposta la mappa sulle cordinate longitudine latitudine
{
  var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
  var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
  var position       = new OpenLayers.LonLat(lon,lat).transform( fromProjection, toProjection);

  map.setCenter(position, zoom);

  document.getElementById("latitudine").value = lat;
  document.getElementById("longitudine").value = lon;
}

function createMarker(lon, lat) /**posiziona un marker e elimina i marker precedenti ***/
{
  var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
  var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
  var position       = new OpenLayers.LonLat(lon,lat).transform( fromProjection, toProjection);


  while (markersArray.length >= 1){
    markers.removeMarker(markersArray.pop());
  }

  markersArray.push(new OpenLayers.Marker(position))

  markers.addMarker(markersArray[0]);
}

function cercaCitta() {
    var cittaDaCercare = document.getElementById("citta").value;

    var url = "https://nominatim.openstreetmap.org/search?format=json&q=" + cittaDaCercare;

    var callNominatiumApi = fetch(url);

    callNominatiumApi.then(function (response) {
        return response.json();
    }).then(function (data) {
        if (data.length > 0) {
            var lat = data[0].lat;
            var lon = data[0].lon;
            setCenterCoordinatesLonLat(lon, lat)
            createMarker(lon, lat);
            console.log(lon, lat);
            document.getElementById('nascondiSotto').style.display = "block";
          document.getElementById('schedaMappa').style.display = "block";
        document.getElementById('schedaMappa').style.opacity = "100%";
        } else {
            alert("Non ho trovato niente")
        }
    }).catch(function (error) {
        alert(error);
    }).finally(() => {
      document.getElementById('nascondiSotto').style.display = "block";
      document.getElementById('schedaMappa').style.display = "block";
      document.getElementById('schedaMappa').style.opacity = "100%";
    });
}

function getCenterCoordinates() /****** ricava le coordinate centrali della posizione della mappa */
{
  var center = map.getCenter();
  var fromProjection = new OpenLayers.Projection("EPSG:900913"); // Spherical Mercator Projection
  var toProjection = new OpenLayers.Projection("EPSG:4326"); // Transform to WGS 1984
  var centerLonLat = center.transform(fromProjection, toProjection);
  var lat = centerLonLat.lat;
  var lon = centerLonLat.lon;
}

// nascondo i form non utilizzati
// let h = document.querySelectorAll(".inputHidden")
// for(let i of h){
//   i.parentNode.style.display = "none";
// }

document.getElementById("schedaMappa").style.display = "none";

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


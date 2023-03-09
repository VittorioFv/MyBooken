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

function setCenterCoordinatesLonLat(lon, lat) // Sposta la mappa sulle cordinate longitudine latitudine
{
  var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
  var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
  var position       = new OpenLayers.LonLat(lon,lat).transform( fromProjection, toProjection);

  map.setCenter(position, zoom);
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
        } else {
            alert("Non ho trovato niente")
        }
    }).catch(function (error) {
        alert(error);
    });
}


const zoom = 13;
var markers = new OpenLayers.Layer.Markers( "Markers" );
var markersArray = []

/********************* CREA LA MAPPA ************************/
function init() // Da richiamare onload sul body, crea la mappa, assegna i layer
{
  map = new OpenLayers.Map("basicMap");
  var mapnik         = new OpenLayers.Layer.OSM();
  var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
  var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
  var position       = new OpenLayers.LonLat(10.9,45.5).transform( fromProjection, toProjection);

  map.addLayer(mapnik);
  map.addLayer(markers);
  map.setCenter(position, zoom );
}

function setCenterCoordinatesLonLat(lon, lat) // Sposta la mappa sulle cordinate longitudine latitudine
{
  var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
  var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
  var position       = new OpenLayers.LonLat(lon,lat).transform( fromProjection, toProjection);

  map.setCenter(position, zoom);

  /*************** modifica l'html, non necessario per la funzione ********/
  document.getElementById("lat").innerHTML = lat;
  document.getElementById("lon").innerHTML = lon;
}

function getCenterCoordinates() /****** ricava le coordinate centrali della posizione della mappa */
{
  var center = map.getCenter();
  var fromProjection = new OpenLayers.Projection("EPSG:900913"); // Spherical Mercator Projection
  var toProjection = new OpenLayers.Projection("EPSG:4326"); // Transform to WGS 1984
  var centerLonLat = center.transform(fromProjection, toProjection);
  var lat = centerLonLat.lat;
  var lon = centerLonLat.lon;


  /****** Sposta il marker al centro *********/
  createMarker(lon, lat);
  /*****  Modifica l'html *****/
  document.getElementById("lat").innerHTML = lat;
  document.getElementById("lon").innerHTML = lon;
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

/********************* CERCA DA INDIRIZZO ************************/
function searchAddress() {
    var address = document.getElementById("address").value;
    var endpoint = "https://nominatim.openstreetmap.org/search?format=json&q=" + address;

    axios.get(endpoint)
        .then(function (response) {
            var data = response.data;
            if (data.length > 0) {
                var lat = data[0].lat;
                var lon = data[0].lon;
                setCenterCoordinatesLonLat(lon, lat)
                createMarker(lon, lat);
            } else {
                document.getElementById("result").innerHTML = "No results found.";
            }
        })
        .catch(function (error) {
            console.log(error);
            document.getElementById("result").innerHTML = "Error: " + error;
        });
}

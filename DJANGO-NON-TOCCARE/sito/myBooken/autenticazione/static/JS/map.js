
var map = L.map('map').setView([45.4384958, 10.9924122], 13);

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
L.marker([45.4384958, 10.9924122]).addTo(map);
map.on('click', (event) => {
    console.log(event.latlng)
    L.marker([event.latlng.lat, event.latlng.lng]).addTo(map);
});


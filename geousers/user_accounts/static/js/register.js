var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

var marker;

function onMapClick(e) {
  if (marker) {
    map.removeLayer(marker);
  }
  marker = L.marker(e.latlng).addTo(map);
  document.getElementById("location").value = "POINT(" + e.latlng.lng + " " + e.latlng.lat + ")";
}

map.on('click', onMapClick);
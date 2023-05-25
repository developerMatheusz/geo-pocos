function onEachFeature(feature, layer) {
    var popupContent = feature.properties.popup_content;
    layer.bindPopup(popupContent);
}

var gstreets = L.tileLayer('http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var satellite = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google'
});

var pit = L.geoJson([],
    {
        style: {
            fillColor: '#fff',
            weight: 2,
            opacity: 1,
            color: '#000000',
            fillOpacity: 1
        },
        pointToLayer: function (feature, latlng) {
            return new L.CircleMarker(latlng, { radius: 4 });
        },
        onEachFeature: onEachFeature
    }
);

var pit_url = $('#pit_geojson').val();

$.getJSON(pit_url, function (data) {
    pit.addData(data);
});

var heat = L.heatLayer(pitCoord, {
    radius: 22,
    blur: 30,
    max: $('#qmax').val(),
    minOpacity: 0.7
});

var map = L.map('map', {
    center: [-7.166300, -36.77673],
    zoom: 8,
    layers: [
        gstreets,
        pit,
        heat
    ]
});

var baseLayers = {
    'Google Streets': gstreets,
    'Google Satélite': satellite
};

var overlays = {
    'Poços': pit,
    'Mapa de calor': heat
};

var control = L.control.layers(baseLayers, overlays).addTo(map);

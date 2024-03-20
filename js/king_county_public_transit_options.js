// king_county_public_transit_options.js

mapboxgl.accessToken = 'MAPBOX_ACCESS_TOKEN';

var map = new mapboxgl.Map({
    container: 'king_county_public_transit_options', // The ID of the div where the map will be rendered
    style: 'mapbox://styles/mapbox/streets-v11', // Base map style
    center: [47.608013, -122.335167], // Centered on King County
    zoom_start:12, max_zoom:25
});



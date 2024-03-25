function initMap() {
    var mapOptions = {
        center: new google.maps.LatLng(47.5480, -121.9836), // King County coordinates
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        streetViewControl: false, // Disable Street View
        mapTypeControl: false // Disable Map/Satellite switch
    };
    var map = new google.maps.Map(document.getElementById('googlemap'), mapOptions);
}

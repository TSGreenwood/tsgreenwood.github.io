import folium
from folium.plugins import HeatMap, MarkerCluster

def create_map(location=[47.608013, -122.335167], zoom_start=12, max_zoom=25, 
               tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 
               attr='Esri', map_name='base_map', overlay=False, control=True):
    """Create and return a folium Map object initialized with specified parameters."""
    m = folium.Map(location=location, zoom_start=zoom_start, max_zoom=max_zoom, control_scale=True)
    folium.TileLayer(tiles=tiles, attr=attr, name=map_name, overlay=overlay, control=control).add_to(m)
    return m

def add_geojson_layer(m, gdf, layer_name, style):
    """Add a GeoJson layer to a folium map from a GeoDataFrame with specified styling."""
    folium.GeoJson(gdf, name=layer_name, style_function=lambda x: style).add_to(m)

def add_legend(m, legend_html):
    """Add a custom HTML legend to a folium map."""
    folium.Element(folium.Html(legend_html, script=True).render()).add_to(m)

def mark_locations(m, locations, icon_details):
    """Add markers for locations to a folium map."""
    for location in locations:
        folium.Marker(location=location, icon=folium.Icon(**icon_details)).add_to(m)

def create_heatmap(m, data):
    """Create a heatmap layer on a folium map from provided data."""
    HeatMap(data).add_to(m)

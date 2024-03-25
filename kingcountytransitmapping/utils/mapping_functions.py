import folium
from folium import plugins

def create_kc_map(location=[47.608013, -122.335167], 
                  zoom_start=12, max_zoom=25, min_zoom=10,
                  min_lat=47.0, max_lat=48.0, 
                  min_lon=-123.0, max_lon=-121.0):
    m = folium.Map(location=location, zoom_start=zoom_start, max_zoom=max_zoom, min_zoom=min_zoom,
                   min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon, max_bounds=True, control_scale=True)
    base_layer = folium.TileLayer(tiles=tiles, attr=attr, name=map_name, overlay=overlay, control=control)
    base_layer.add_to(m)
    return m


def add_express_routes(m):
    folium.GeoJson(
        express_routes_gdf,
        name='Express Routes',
        style_function=lambda x: {'color': '#32CD32', 'weight': 3, 'opacity': 0.7}
    ).add_to(m)

def add_local_routes(m):
    folium.GeoJson(
        local_routes_gdf,
        name='Local Routes',
        style_function=lambda x: {'color': 'darkred', 'weight': 2, 'opacity': 0.7}
    ).add_to(m)

# Add legend for route types
def add_route_legend(map_object):
  legend_html = '''
  <div style="position: fixed;
      bottom: 50px; left: 50px; width: 150px; height: 80px;
      border:2px solid grey; z-index:9999; font-size:14px;
      ">&nbsp; <b>Route Type:</b><br>
      &nbsp; Express &nbsp; <i style="background:brightgreen; width:20px; height:10px; display:inline-block;"></i><br>
      &nbsp; Local &nbsp; <i style="background:darkred; width:20px; height:10px; display:inline-block;"></i>
  </div>
  '''

  legend = folium.Html(legend_html, script=True)
  folium.Element(legend.render()).add_to(map_object)

  from folium.plugins import MarkerCluster
def mark_bus_stops(map_object, bus_stops_gdf):
  for _, row in bus_stops_gdf.iterrows():
    folium.Marker(
        location=[row['YCOORD'], row['XCOORD']],
        icon=folium.Icon(icon='bus', prefix='fa', color='orange')
    ).add_to(map_object)

from folium.plugins import HeatMap
def create_heatmap_bus_stops(map_object, bus_stops_gdf):
  heatmap_data = bus_stops_gdf[['YCOORD', 'XCOORD']].values.tolist()
  HeatMap(heatmap_data).add_to(map_object)

 
def display_zipcode_overlay(map_object, zip_codes_gdf, attribute='TOTAL_BUS_STOPS'):

    # Create a tooltip that dynamically fetches the ZIPCODE and the specified attribute
    folium.GeoJson(
        zip_codes_gdf,
        style_function=lambda x: {'color': 'blue', 'weight': 2, 'opacity': 0.5},
        tooltip=folium.GeoJsonTooltip(fields=['ZIPCODE', attribute],
                                      aliases=['ZIP Code:', f'{attribute}:'],
                                      localize=True)
    ).add_to(map_object)

    

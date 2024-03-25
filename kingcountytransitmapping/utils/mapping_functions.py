import folium
from folium import plugins

def create_anchored_kc_base_map(default_location=[47.608013, -122.335167],
                                default_zoom_start=12):
    m = folium.Map(location=default_location, zoom_start=default_zoom_start,
                   tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
                   attr='Esri', overlay=False, control_scale=True, min_zoom=9)

    # Define your boundary for King County or the specific area of interest
    boundary = {
        'north': 48,
        'south': 47.4,
        'east': -121.8,
        'west': -122.7
    }

    # Apply the max bounds to the map
    #m.fit_bounds([
     #   [boundary['south'], boundary['west']],
     #   [boundary['north'], boundary['east']]
   # ])

    # Ensure user cannot pan outside of the given boundary
    m.options['maxBounds'] = [
        [boundary['south'], boundary['west']],
        [boundary['north'], boundary['east']]
    ]

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

    
    

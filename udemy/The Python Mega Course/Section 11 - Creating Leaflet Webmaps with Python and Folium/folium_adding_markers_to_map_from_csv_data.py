"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 11: Creating Leaflet Webmaps with Python and Folium

Adding Markers to the map from CSV Data

Author: Jhesed Tacadena
Date: 2017-01-26

Section 11 Contents:
    66. Demonstration of Web Mapping Application
    67. Creating an Open Street Map with Python
    68. Adding Markers to the Map
    69. Adding Markers to the Map from CSV Data
    70. Rule-based COloring of Markers
    71. More on Rule-based Styling
    72. Calculating the Map Center from Input Data
    73. Adjusting the Code for the Latest Version of Folium
    74. Adding a Choropleth Map from GeoJson
    75. Adding a Layer Control Panel
    
"""

import pandas
import folium


# -----------------------------------------------------------------------------
def determine_color(elev):
    """
    Determines color based on elevation
    """

    # Decide the marker color
    if elev in range(1, 1000):
        marker_color = 'green'
    elif elev in range(1000, 3000):
        marker_color = 'orange'
    else:
        marker_color = 'red'                

    return marker_color


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    
    # Create the folium map object
    # location = <latitude, longitude>
    # zoom_start = lower means zoom out
    # tiles = to override default tile view 
    map = folium.Map(location=[45.372, -121.697], zoom_start=4,
                     tiles='Stamen Terrain')

    # Read the reference file for fetching coordinates
    df = pandas.read_csv('res/Volcanoes-USA.txt')

    # Adding map markers from csv

    for lat, lon, name, elev in zip(df['LAT'], df['LON'], 
                                    df['NAME'], df['ELEV']): 

        map.simple_marker(location=[lat, lon], popup=name,
                          marker_color=determine_color(elev))
    
    # Create the html file with the actual map
    map.create_map(path='folium_test.html')

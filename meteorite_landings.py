import folium
from folium.features import Icon
import pandas as pd

# Create Data Frame
df = pd.read_csv('Meteorite_Landings.csv')

# Remove all NaN Lines
df = df.dropna()

# Create Map
m = folium.Map(location = [45, -75], zoom_start=5, tiles="OpenStreetMap", prefer_canvas=True)

# Loop through data frame, adding a marker for each entry
for i in range(0, len(df)):
    if df.iloc[i]['mass (g)'] > 100000:
        if df.iloc[i]['fall'] == 'Found':
            folium.Marker(
            location = [df.iloc[i]['reclat'], df.iloc[i]['reclong']],
            popup = "<b>" + "Mass: " + str(df.iloc[i]['mass (g)']) + "g" + "\nClass: " + str(df.iloc[i]['recclass']) + "</b>",
            tooltip = "<i>" + df.iloc[i]['name'] + "</i>",
            icon = Icon(icon='map-marker', icon_color='green')
        ).add_to(m)
        elif df.iloc[i]['fall'] == 'Fell':
            folium.Marker(
            location = [df.iloc[i]['reclat'], df.iloc[i]['reclong']],
            popup = "<b>" + "Mass: " + str(df.iloc[i]['mass (g)']) + "g" + "\nClass: " + str(df.iloc[i]['recclass']) + "</b>",
            tooltip = df.iloc[i]['name'],
            icon = Icon(icon='map-marker', icon_color='red')
        ).add_to(m)    

m.save('meteorite_landings_map.html')
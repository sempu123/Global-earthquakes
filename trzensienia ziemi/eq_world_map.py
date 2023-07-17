import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'eq_data_past_Week.json'
with open(filename, encoding="utf8") as file:
    all_eq_data = json.load(file)

readable_file = 'readalbe_eq_data.json'
with open(readable_file, 'w') as file:
    json.dump(all_eq_data, file, indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    text = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(text)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [mag*5 for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Siła'}
    }, }]
tytul = all_eq_data['metadata']['title']
my_layout = Layout(title=tytul)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

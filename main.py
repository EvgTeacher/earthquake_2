import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
data = {'format': 'geojson', 'starttime': input('Input start time '), 'endtime': input('Input end time '),
        'latitude': input('Input latitude '), 'longitude': input('Input longitude '),
        'maxradiuskm': input('Input max radius in km '), 'minmagnitude': input('Input min magnitude ')}
response = requests.get(url, headers={'Accepr': 'application/json'}, params=data)
lst_features = response.json()['features']
result_lst = []
for elem in lst_features:
    if int(elem['properties']['mag']) >= int(data['minmagnitude']):
        result_lst.append(F"Place: {elem['properties']['place']}. Magnitude: {elem['properties']['mag']}")

for elem in enumerate(result_lst, 1):
    print(elem)
counter = 1
for elem in result_lst:
    print(f'{counter}. {elem}')
    counter += 1

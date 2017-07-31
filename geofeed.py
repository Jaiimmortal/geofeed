
import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
    
query = input('What kinda places you want me look up? ')
url = main_api + urllib.parse.urlencode({'query': query}) + '&key=some-rubbish-key-you-get-from-developes.google.com'
# for security and privacy concerns im nos sharing my API key

json_data = requests.get(url).json()

#print(url)

json_status = json_data['status']
print('\nAPI Status :' + json_status)

if json_status == 'OK':

    for i in range(len(json_data['results'])):

        print()
        formatted_address = json_data['results'][i]['formatted_address']
        name_of_place = json_data['results'][i]['name']
        rating = json_data['results'][i]['rating']
        location = json_data['results'][i]['geometry']['location']

        print('Name of the place : ' + name_of_place)
        print('Address : ' + formatted_address)
        print('Rating : ' + str(rating))
        print('Location : ' + str(location) + '\n')

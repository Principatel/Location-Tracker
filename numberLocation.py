import phonenumbers
import folium
from mynumber import number

from phonenumbers import geocoder

samnumber = phonenumbers.parse(number)
yourlocation = geocoder.description_for_number(samnumber,"en")
print(yourlocation)

from phonenumbers import carrier
yourservice = phonenumbers.parse(number)
print(carrier.name_for_number(yourservice,"en"))

from opencage.geocoder import OpenCageGeocode
key = '63690d40fa1342c781e21c91f3b36071'
geocoder = OpenCageGeocode(key)
query = str(yourlocation)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']

lng = result[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=yourlocation).add_to(myMap)
myMap.save("mylocation.html")
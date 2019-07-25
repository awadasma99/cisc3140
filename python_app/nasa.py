import urllib.request
import json

url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
urlobj = urllib.request.urlopen(url)
apodread = urlobj.read()
data = json.loads(apodread.decode('utf-8'))

print(data["date"])


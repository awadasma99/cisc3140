import time
import urllib.request
import json


t0 = time.time()  # start time
# the code to time goes here
foo = "bar"
t1 = time.time() # end time
print(t1 - t0)

# another example
t2 = time.time()
url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
urlobj = urllib.request.urlopen(url)
apodread = urlobj.read()
data = json.loads(apodread.decode('utf-8'))

img = data['hdurl']

t3 = time.time()
print(t3 - t2)


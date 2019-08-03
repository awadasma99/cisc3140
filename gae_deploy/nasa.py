import urllib.request
import json


# This function connects to the NASA picture of the day API endpoint
# It parses the JSON blob and returns a dictionary with content from the API endpoint.

def connect(**extra):
  url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
 
  # check to see if additional parameters are needed
  if len(list(extra)) > 0:
    if extra["date"]:
      url += '&date=' + extra['date']

  urlobj = urllib.request.urlopen(url)
  apodread = urlobj.read()
  data = json.loads(apodread.decode('utf-8'))

  return data


# This is a test function to check the data returned from the connect() function
# This is how we know that today's data is the one returned.
def test_connect(data):
  return data["date"]

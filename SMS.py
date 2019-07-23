import urllib # Python URL functions
import urllib.parse 
import urllib.request
import json


authkey = "2830A1bqIVR0OIlL5d349688" # Your authentication key.

mobiles = "4698897876" # Multiple mobiles numbers separated by comma.

message = "HI Mal, Are you feelin lucky today!?" # Your message to send.

sender = "112233" # Sender ID,While using route4 sender id should be 6 characters long.

route = "4" # Define route

# Prepare you post parameters
values = {
          'authkey' : authkey,
          'mobiles' : mobiles,
          'message' : message,
          'sender' : sender,
          'route' : route
          }


url = "http://world.msg91.com/api/sendhttp.php" # API URL

postdata = urllib.parse.urlencode(values).encode("utf-8") # URL encoding the data here.
req = urllib.request.urlopen(url, postdata)


response = urllib.request.Request(req)
output = response.read() # Get response

print(output) #print respone


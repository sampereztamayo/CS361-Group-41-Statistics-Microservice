# CS361-Group-41-Statistics-Microservice

## Requesting data:
* Main program sends a HTTP POST request to the url of the public server corresponding to the statistic they want, in this case hosted via Render. The numbers that the statistics are to be done on are stored in a JSON object, which is sent during the request.

* Example call in Python (sum calculation):
```
import json 

# select url of desired statistic
url_server = 'https://cs361-group-41-statistics-microservice-2.onrender.com/stats/sum'

# package data of interest
request_data = {'numbers': [1, 3, 5, 3, 9]}

# send request and save response
response = requests.post(url_server, json = request_data)

    *** continued below ***
 ```

## Receiving data:
* The microservice returns a JSON object containing the status of the request and the requested statistical value.
* Example call in Python (sum calculation):

```
    *** continued from above ***
    
# parse data into a dictionary
incoming_data = response.json()

# statistic (sum) is held in 'return_value' key 
if incoming_data.get('status') == 'success':
    print(f"Sum successfully calculated: {incoming_data.get('return_value')}")
```

## UML sequence diagram:

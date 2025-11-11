import requests

url_sum = 'https://cs361-group-41-statistics-microservice-2.onrender.com/stats/sum'
url_average = 'https://cs361-group-41-statistics-microservice-2.onrender.com/stats/average'

def test_sum(data):
    # send JSON data to Render server
    response = requests.post(url_sum, json = data)

    incoming_data = response.json()

    if incoming_data.get('status') == 'success':
        print(f"Sum successfully calculated: {incoming_data.get('return_value')}")


def test_average(data):
    # send JSON data to Render server
    response = requests.post(url_average, json = data)

    incoming_data = response.json()

    if incoming_data.get('status') == 'success':
        print(f"Average successfully calculated: {incoming_data.get('return_value')}")




# Testing
numbers = [1, 3, 5, 9, 12]

test_sum({'numbers': numbers})
test_average({'numbers': numbers})

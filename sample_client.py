import requests

url_sum = 'https://cs361-group-41-statistics-microservice-2.onrender.com/stats/sum'
url_average = 'https://cs361-group-41-statistics-microservice-2.onrender.com/stats/average'
url_percentage = 'https://cs361-group-41-statistics-microservice-2.onrender.com/stats/percentage'
url_median = 'https://cs361-group-41-statistics-microservice-2.onrender.com/stats/median'


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


def test_percentage(data):
    # send JSON data to Render server
    response = requests.post(url_percentage, json = data)

    incoming_data = response.json()

    if incoming_data.get('status') == 'success':
        print(f"Percentage successfully calculated: {incoming_data.get('return_value')}")


def test_median(data):
    # send JSON data to Render server
    response = requests.post(url_median, json = data)

    incoming_data = response.json()

    if incoming_data.get('status') == 'success':
        print(f"Median successfully calculated: {incoming_data.get('return_value')}")



# Testing
numbers = [2, 4, 3, 5, 9, 9, 12, 22]

test_sum({'numbers': numbers})
test_average({'numbers': numbers})
test_percentage({'numbers': numbers})
test_median({'numbers': numbers})

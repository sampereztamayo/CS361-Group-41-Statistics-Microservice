from flask import Flask, jsonify, request

app = Flask(__name__)

# health check
@app.route('/health', methods = ['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/stats/sum', methods = ['POST'])
def calculate_sum():
    incoming_data = request.get_json()
    numbers = incoming_data.get('numbers', [])

    # empty list; error
    if not numbers:
        return jsonify({'status': 'error',
                       'error_message': 'cannot calculate using empty list'}), 400

    # success
    total = sum(numbers)
    return jsonify({'status': 'success',
                    'return_value': total}), 200

@app.route('/stats/average', methods = ['POST'])
def calculate_average():
    incoming_data = request.get_json()
    numbers = incoming_data.get('numbers', [])

    # empty list; error
    if not numbers:
        return jsonify({'status': 'error',
                       'error_message': 'cannot calculate using empty list'}), 400

    # success
    average = sum(numbers)/len(numbers)
    return jsonify({'status': 'success',
                    'return_value': average}), 200


@app.route('/stats/percentage', methods = ['POST'])
def calculate_percentage():
    incoming_data = request.get_json()
    numbers = incoming_data.get('numbers', [])

    # empty list; error
    if not numbers:
        return jsonify({'status': 'error',
                       'error_message': 'cannot calculate using empty list'}), 400

    # success
    percentage = (numbers[0] / numbers[1]) * 100
    return jsonify({'status': 'success',
                    'return_value': percentage}), 200








#
# if __name__ == '__main__':
#     app.run
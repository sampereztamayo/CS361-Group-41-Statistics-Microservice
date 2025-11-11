from flask import Flask, jsonify, request

app = Flask(__name__)

# health check
@app.route('/health', methods = ['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/stats/sum', methods = ['POST'])
def sum():
    incoming_data = request.get_json()
    numbers = incoming_data.get('numbers', [])

    # empty list; error
    if not numbers:
        return jsonify({'status': 'error',
                       'error_message': 'cannot calculate using empty list'}), 400

    # success
    summation = sum(numbers)
    return jsonify({'status': 'success',
                    'return_value': summation}), 200













#
# if __name__ == '__main__':
#     app.run
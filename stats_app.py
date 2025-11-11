from flask import Flask, jsonify, request

app = Flask(__name__)

# health check
@app.route('/health', methods = ['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200





#
# if __name__ == '__main__':
#     app.run
from utils import get_remote_address
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from flask_limiter import Limiter
import os

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

# Hashed passwords for comparison
hashed_passwords = [
    'scrypt:32768:8:1$2oTbzKNmYVeUf5by$30c84d1e31e9818e7fb14c2ad16692eaab43a49ae3e717df7159376bfba1d9296a27d4f85d997f6d0d38bcf469fe0f5748fee4990f2fa4e3d01b173b92d71628', 'scrypt:32768:8:1$EQxEZuRxX4TsHlXh$f45c29a5da1afc48e918ee41bd7d397f0c1f897a4b72bb14f097b00298d0ffb17bd9468bebfa2ac1a664c0b8f22890d49c53e5e6414122a50e0f56522f7ffd7f', 'scrypt:32768:8:1$LZ2LlAXe96KotOS6$cda1fdfb92307c15992e503716760e5d94aabd340be8feacfacca3008ae3d2ec893a67d7a866721d0c237c9a5d1a9c7931994d546842fa4e86bed11b995354a1', 'scrypt:32768:8:1$TNicH9lUO9KjjUQN$aa1f7071907cefec328a161d5b4ff1c1a12ca1d1ac7fdd6050017b5fa70c66c8e39c66432dade0aee3dcdb9f1ea58598ccb7b48fe3148a0594e0f0f58bcd6d78'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    return send_from_directory(directory='.', path='Challenge.zip')

@app.route('/submit', methods=['POST'])
@limiter.limit("5 per minute")  # rate limit to 5 requests per minute per IP
def submit():
    data = request.json
    received_passwords = data.get('passwords', [])

    # Check the number of passwords received
    if len(received_passwords) != 4:
        return jsonify({"success": False, "reason": "Invalid number of passwords"}), 400

    # Check each received password against the hashed ones
    if all(check_password_hash(hp, rp) for hp, rp in zip(hashed_passwords, received_passwords)):
        try:
            with open('notes.txt', 'r') as f:
                content = f.read()
            return jsonify({"success": True, "content": content, "dns": "shadow.wargame.esd"}), 200
        except FileNotFoundError:
            return jsonify({"success": False, "reason": "notes.txt not found"}), 500
    else:
        return jsonify({"success": False, "reason": "Invalid passwords"}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)

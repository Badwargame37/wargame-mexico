from flask import Flask, request, jsonify, render_template, send_from_directory
import hashlib
import os
from flask_limiter import Limiter


def get_remote_address():
    return request.remote_addr

def check_sha256_hash(stored_hash, input_password):
    hashed_input = hashlib.sha256(input_password.encode('utf-8')).hexdigest()
    return hashed_input == stored_hash

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)
hashed_passwords = ('4c3e683ce66f9525ab8cf5c9abe2a0a47f653a34d2fa4c19fca2ac1601dc6626,3b0fe0d342e9fa16a5c68dbba33f2e63c024f72a9d4c1ce1028570101d5229ff,1cfa6b030017a1bf5d20ee50f59b65ab0aea02d062a8e914ba2eea6e3e4686db,02317af5040dfbf07670ec23673a98f9f8e83c82a185a6ebf7c0b3bf9fec5a5f').split(',')
print(hashed_passwords)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('./static', filename)
@app.route('/download')
def download():
    return send_from_directory(directory='.', path='Challenge.zip')

@app.route('/submit', methods=['POST'])
@limiter.limit("5 per minute")
def submit():
    data = request.json
    received_passwords = data.get('passwords', [])
    
    if len(received_passwords) != 4:
        return jsonify({"success": False, "reason": "Invalid number of passwords"}), 400
    if all(check_sha256_hash(hp, rp) for hp, rp in zip(hashed_passwords, received_passwords)):
        try:
            with open('notes.txt', 'r') as f:
                content = f.read()
            return jsonify({"success": True, "content": content, "dns": "check http://bastion.esd37.com/guacamole/#/"}), 200
        except FileNotFoundError:
            return jsonify({"success": False, "reason": "notes.txt not found"}), 500
    else:
        return jsonify({"success": False, "reason": "Invalid passwords"}), 401


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)

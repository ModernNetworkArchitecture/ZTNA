from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rahasia-fashion'  # Ganti untuk produksi

# Simulasi database user
users = {
    "batikjogja": "batik123",
    "ecobali": "eco123",
    "modestbandung": "modest123",
    "resellerjakarta": "reseller123"
}

# Middleware ZTNA - JWT required
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split(" ")[1]
            except IndexError:
                return jsonify({"message": "Token tidak valid"}), 401

        if not token:
            return jsonify({"message": "Token tidak ditemukan"}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user']
        except Exception as e:
            return jsonify({"message": "Token salah atau expired"}), 403

        return f(current_user, *args, **kwargs)
    return decorated

# Endpoint login
@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    username = auth.get('username')
    password = auth.get('password')

    if username in users and users[username] == password:
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})

    return jsonify({'message': 'Username/password salah'}), 401

# Endpoint secure (ZTNA protected)
@app.route('/produk', methods=['GET'])
@token_required
def produk(current_user):
    return jsonify({
        'user': current_user,
        'produk': ['Batik Etnik', 'Gamis Bandung', 'Tas Ecoprint', 'Hijab Jersey']
    })

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

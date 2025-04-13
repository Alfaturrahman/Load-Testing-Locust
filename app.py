from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email dan kata sandi harus diisi"}), 400

    if email == "user@example.com" and password == "Password123":
        return jsonify({"message": "Login berhasil"}), 200
    else:
        return jsonify({"message": "Email atau kata sandi salah"}), 401

if __name__ == "__main__":
    app.run(debug=True)

from flask import jsonify

class UserController:
    def get_users(self):
        # Dummy data pengguna
        users = [
            {"id": 1, "username": "user1", "email": "user1@example.com"},
            {"id": 2, "username": "user2", "email": "user2@example.com"},
            {"id": 3, "username": "user3", "email": "user3@example.com"},
        ]
        
        # Mengembalikan daftar pengguna dalam format JSON
        return jsonify(users)

class AuthController:
    def login(self, username, password):
        # Dummy logic untuk autentikasi pengguna
        if username == "admin" and password == "admin":
            # Jika autentikasi berhasil, arahkan pengguna ke halaman utama
            return redirect(url_for("home"))
        else:
            # Jika autentikasi gagal, kembalikan pengguna ke halaman login dengan pesan kesalahan
            return render_template("login.html", error="Invalid username or password.")

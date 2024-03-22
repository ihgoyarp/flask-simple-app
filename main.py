from flask import Flask, render_template, request, redirect, url_for, session
from controllers import UserController, AuthController

app = Flask(__name__, template_folder="templates")
app.secret_key = 'your_secret_key'

user_controller = UserController()
auth_controller = AuthController()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/login', methods=["GET","POST"])
def login():
    # Periksa apakah pengguna sudah login
    if 'logged_in' in session and session['logged_in']:
        # Jika sudah login, arahkan langsung ke halaman dashboard
        return redirect('/home')

    if request.method == 'POST':
        # Periksa apakah username dan password sesuai
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            # Jika sesuai, set sesi login dan arahkan ke halaman lain
            session['logged_in'] = True
            return redirect('/home')
        else:
            # Jika tidak, tampilkan pesan kesalahan
            return render_template('login.html', error='Invalid username or password')
    else:
        # Jika metode request adalah GET, tampilkan halaman login
        return render_template('login.html')

@app.route("/home")
def home():
    # Periksa apakah pengguna sudah login
    if 'logged_in' in session and session['logged_in']:
        # Jika sudah login, tampilkan halaman dashboard
        return 'Welcome to the Dashboard!'
    else:
        # Jika belum login, arahkan kembali ke halaman login
        return redirect('/login')
    
@app.route('/logout')
def logout():
    # Hapus session login jika ada
    session.pop('logged_in', None)
    # Alihkan pengguna ke halaman login
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
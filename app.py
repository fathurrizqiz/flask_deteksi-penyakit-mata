from flask import Flask, render_template, request, session, send_file, redirect, url_for


app = Flask(__name__) 

pesan_sebelumnya = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/cek_kesehatan')
def cek_kesehatan():
    return render_template('cek_kesehatan.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        if 'user_input' in request.form:
            user_input = request.form['user_input']
            response = process_input(user_input)
            return render_template('chatbot.html', response=response)
        else:
            return 'Error: user_input field is missing', 400
    return render_template('chatbot.html')

def process_input(user_input):
    if user_input.lower() == 'hello':
        return 'hallo, ada yang bisa dibantu?'
    elif user_input.lower() == 'bantu saya menyelesaikan case ini':
        return 'baiklah, apa masalahmu hari ini'
    else:
        return 'saya tidak mengerti mohon di ulang'

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def Profile():
    return render_template('profile.html')
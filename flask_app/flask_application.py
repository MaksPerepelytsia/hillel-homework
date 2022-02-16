from flask import Flask, request
import string, time, random

app = Flask(__name__)


@app.route('/whoami/')
def whoami():
    browser = request.user_agent.browser
    ip_address = request.remote_addr
    time_server = time.strftime('%H:%M:%S')
    return f'Client browser: {browser}, Client IP adress: {ip_address}, Current time on the server: {time_server}'


@app.route('/source_code/')
def source_code():
    with open('flask_application.py') as fl:
       code = fl.read()
       return f'<pre>{code}</pre>'


@app.route('/random/')
def m_random():
    try:
        length: int = int(request.values.get('length', 0))
    except Exception:
        length = 0
    try:
        specials: int = int(request.values.get('specials', 0))
    except Exception:
        specials = 0
    try:
        digits: int = int(request.values.get('digits', 0))
    except Exception:
        digits = 0
    alp = string.ascii_letters
    sp = '!"№;%:?*()_+'
    dig = string.digits
    rez = []
    if specials == 1:
        alp += sp
    if digits == 1:
        alp += dig
    if 0 < length < 100:
        for i in range(length):
            rez.append(random.choice(alp))
    result = ''.join(rez)
    return f'{result}'


app.run(debug=True)



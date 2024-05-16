from flask import Flask, render_template, request
from hash import Algo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hash-function', methods=['GET', 'POST'])
def hash_function():
    if request.method == 'POST':
        message = request.form['message']
        salt = request.form['salt']
        hash_value = Algo(message, salt)  # Calling the Algo function with message and salt
        return render_template('hash_function.html', message=message, salt=salt, hash_value=hash_value)
    return render_template('hash_function.html')

@app.route('/collision-attack', methods=['GET', 'POST'])
def collision_attack():
    if request.method == 'POST':
        message1 = request.form['message1']
        message2 = request.form['message2']
        salt = request.form['salt']
        hash_value1 = Algo(message1, salt)  # Calling the Algo function with message1 and salt
        hash_value2 = Algo(message2, salt)  # Calling the Algo function with message2 and salt
        return render_template('collision_attack.html', message1=message1, message2=message2, salt=salt, hash_value1=hash_value1, hash_value2=hash_value2)
    return render_template('collision_attack.html')
if __name__ == '__main__':
    app.run(debug=True)

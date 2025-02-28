import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    conn = mysql.connector.connect(
        host='mysql',
        user ='root',
        password='root',
        database='db'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=result)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

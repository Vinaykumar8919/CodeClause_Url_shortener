from flask import Flask, render_template, request, redirect
import string
import random
import mysql.connector
from mysql.connector import Error
from validators import url as validate_url

app = Flask(__name__)
app.config['BASE_URL'] = 'http://localhost:5000/'

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user='root',
        password='Vinay@#23',
        database='url'
    )
    mycursor = mydb.cursor()
except Error as e:
    print("Error connecting to MySQL:", e)

mycursor.execute("CREATE TABLE IF NOT EXISTS url (shortcode VARCHAR(225), original_url VARCHAR(225), shorturl VARCHAR(225))")

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']

        if not validate_url(original_url):
            return render_template('index.html', error="Invalid URL")

        short_code = generate_short_code()
        short_url = app.config['BASE_URL'] + short_code
        
        try:
            insert = "INSERT INTO url (shortcode, original_url, shorturl) VALUES (%s, %s, %s)"
            values = (short_code, original_url, short_url)
            mycursor.execute(insert, values)
            mydb.commit()
        except Error as e:
            print("Error inserting data:", e)
            mydb.rollback()

        return render_template('index.html', short_url=short_url)
    
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    try:
        mycursor.execute("SELECT original_url FROM url WHERE shortcode = %s", (short_code,))
        res = mycursor.fetchone()
        if not res:
            return "Invalid URL"
        return redirect(res[0])
    except Error as e:
        print("Error fetching data:", e)
        return "An error occurred"

if __name__ == '__main__':
    app.run(debug=True)
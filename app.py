from flask import *
import string
import random

app = Flask(__name__)
app.config['BASE_URL'] = 'http://localhost:5000/'

# Database to store shortened URLs (You can replace it with a proper database like MySQL or PostgreSQL)
url_db = {}

def generate_short_code():
    """Generate a random alphanumeric code for the shortened URL."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        short_url = app.config['BASE_URL'] + short_code
        url_db[short_code] = original_url
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect to the original URL based on the provided short code."""
    if short_code in url_db:
        return redirect(url_db[short_code])
    return 'Invalid URL'

if __name__ == '__main__':
    app.run(debug=True)

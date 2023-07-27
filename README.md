# CodeClause_Url_shortener
1. Import necessary libraries:
   - `Flask`: A web framework for Python used to create web applications.
   - `string` and `random`: These standard Python libraries are used to generate random alphanumeric codes for the shortened URLs.

2. Create a Flask application instance:
   - The `Flask` class is used to create an instance of the web application. It is assigned to the variable `app`.

3. Set the base URL:
   - `app.config['BASE_URL']` is set to the base URL of the application. In this example, it is set to `'http://localhost:5000/'`. This will be used to construct the shortened URLs.

4. Define a function to generate a short code:
   - `generate_short_code()` is a function that generates a random alphanumeric code of length 6 using `string.ascii_letters` (lowercase and uppercase letters) and `string.digits` (digits 0-9).

5. Create two routes using the `@app.route` decorator:
   - `'/'`: The home route, used to handle both GET and POST requests.
   - `'/<short_code>'`: A dynamic route that accepts a short code as part of the URL.

6. Define the `home()` function for the '/' route:
   - For POST requests, the function receives the original URL from the submitted form data.
   - It calls `generate_short_code()` to create a short code for the URL and constructs the short URL using the base URL and the generated short code.
   - The original URL and the short code are stored in the `url_db` dictionary, which acts as a simple in-memory database to store the shortened URLs.
   - The function renders the 'index.html' template and passes the short URL to be displayed on the page.
   - For GET requests, it simply renders the 'index.html' template without any short URL.

7. Define the `redirect_to_url()` function for the '/<short_code>' route:
   - When a user accesses a shortened URL like 'http://localhost:5000/abc123', the function receives 'abc123' as the `short_code` parameter.
   - If the `short_code` exists in the `url_db` dictionary, it means a valid short URL was provided, and the user is redirected to the original URL associated with that short code using the `redirect()` function.
   - If the `short_code` doesn't exist in the `url_db`, the function returns 'Invalid URL'.

8. Run the application:
   - The `if __name__ == '__main__':` block ensures that the application is run only when executed directly (not when imported as a module).
   - The application is started using `app.run(debug=True)`, which runs the Flask development server with debug mode enabled.

To use this URL shortener, run the Python script, and it will start the Flask development server on `http://localhost:5000/`. Visit this URL in your web browser, and you'll see a form to submit a long URL. Upon submitting the form, the application will generate a shortened URL, which you can use to access the original URL. For example, entering `http://www.example.com` in the form might generate a short URL like `http://localhost:5000/abc123`, and accessing the short URL will redirect you to `http://www.example.com`.

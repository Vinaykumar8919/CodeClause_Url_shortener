# URL Shortener Application

This is a simple Flask application that provides URL shortening functionality. The application allows users to input a long URL, and it generates a short code that redirects to the original URL when accessed. The short URL is constructed based on the base URL of the application.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python
- Flask
- MySQL server
- `mysql-connector-python` package
- `validators` package

## Installation and Setup

1. Clone the repository or download the source code:

   ```bash
   git clone <repository_url>
   ```

2. Install the required packages using pip:

   ```bash
   pip install Flask mysql-connector-python validators
   ```

3. Set up the MySQL database:

   - Create a database named 'url'.
   - Update the `user` and `password` values in the code to match your MySQL configuration.

4. Run the Application:

   Navigate to the project directory and run the following command:

   ```bash
   python app.py
   ```

   The application will start, and you should see output indicating that the server is running.

5. Access the Application:

   Open a web browser and navigate to `http://localhost:5000/` to access the URL shortener application.

## How the Application Works

1. **Homepage:**

   When you access the root URL (`http://localhost:5000/`), you'll see a form where you can input a long URL.

2. **Shortening a URL:**

   - Enter a long URL in the input field and submit the form.
   - The application validates the URL using the `validators` package.
   - If the URL is valid, a short code is generated using the `generate_short_code` function.
   - The short URL is constructed using the base URL and the generated short code.
   - The original URL, short code, and short URL are stored in the MySQL database.

3. **Accessing a Shortened URL:**

   - When you access a short URL (e.g., `http://localhost:5000/<short_code>`), the application retrieves the original URL associated with the short code from the database.
   - If the short code is found, the application redirects you to the original URL.
   - If the short code is not found, you'll see an "Invalid URL" message.

## Customization

- You can customize the base URL by modifying the `BASE_URL` configuration in the code.
- The length of the generated short code can be adjusted by changing the value in the `generate_short_code` function.

## Error Handling

- The application handles errors related to MySQL database connections and data insertion.
- Invalid URLs are detected using the `validators` package.

## Note

- This code is for educational purposes and may require additional security and optimization for production use.

Feel free to modify, enhance, and deploy this application as needed for your specific use case.

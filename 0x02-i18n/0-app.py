#!/usr/bin/env python3
"""A Basic Flask App with a Custom Welcome Message."""
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Make trailing slashes in URLs optional
app.url_map.strict_slashes = False


# Define a route for the home page
@app.route('/')
def home():
    """Render the home page with a custom welcome message."""
    return render_template('0-index.html')


if __name__ == '__main__':
    # Run the Flask app on all available network interfaces
    app.run(host='0.0.0.0', port=5000)

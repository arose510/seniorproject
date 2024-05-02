from flask import redirect, url_for
from website import create_app
from website.auth import auth  # Import the auth blueprint

# Create the Flask application instance using create_app function from website module
app = create_app()

# Register the auth blueprint with the new client ID
app.register_blueprint(auth, url_prefix="/auth")

# Route to handle the authentication callback from Microsoft
@app.route('/getAToken')
def handle_microsoft_callback():
    # Process the authentication token from Microsoft
    # This could involve validating the token, extracting user information, etc.
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)

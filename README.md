# Flask Project Setup Walkthrough

This walkthrough provides a basic setup for a Python Flask project, including the folder structure, a "Hello, World!" application, and instructions on setting up a virtual environment.

## Step 1: Create the Project Directory

Create the main project directory:

```bash
mkdir flask_project
cd flask_project
```

## Step 2: Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

## Step 3: Install Flask

With the virtual environment activated, install Flask:

```bash
pip install Flask
```

## Step 4: Create the Folder Structure

Create the following folder structure:

```
flask_project/
│
├── app/
│   ├── __init__.py
│   └── routes.py
│
├── venv/
│
├── .gitignore
├── config.py
└── run.py
```

## Step 5: Create the Flask Application Files

### 1. `run.py`

This is the entry point of your application. It will run the Flask app.

```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

### 2. `app/__init__.py`

This file initializes the Flask application.

```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app
```

### 3. `app/routes.py`

This file contains the routes (views) for your application.

```python
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return "Hello, World!"
```

### 4. `config.py`

This file can hold configuration settings for your application. For now, you can leave it empty or add some basic settings.

```python
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
```

### 5. `.gitignore`

If you plan to use Git, create a `.gitignore` file to exclude certain files and directories from version control.

```plaintext
venv/
__pycache__/
instance/
*.pyc
*.pyo
*.pyd
*.db
```

## Step 6: Run the Application

With the virtual environment activated, you can run your Flask application:

```bash
python run.py
```

Your Flask app should now be running, and you can view it in your browser at `http://127.0.0.1:5000/`.

## Adding Templates and Static Files

### Updated Folder Structure

```
flask_project/
│
├── app/
│   ├── __init__.py          # Initializes the Flask app
│   ├── routes.py            # Contains the routes (views) of the app
│   ├── templates/           # Folder for HTML or EJS templates
│   │   └── index.html       # Example template file
│   └── static/              # Folder for static files (CSS, JS, images)
│       ├── css/
│       │   └── style.css    # Example CSS file
│       ├── js/
│       │   └── script.js    # Example JavaScript file
│       └── img/
│           └── logo.png     # Example image file
│
├── venv/                    # Virtual environment
│
├── .gitignore               # Files and directories to ignore in Git
├── config.py                # Configuration settings
└── run.py                   # Entry point of the application
```

### Step 1: Create the `templates` and `static` Folders

Within the `app` directory, create the `templates` and `static` folders:

```bash
mkdir -p app/templates app/static/css app/static/js app/static/img
```

### Step 2: Create a Template (HTML/EJS) File

Create an `index.html` file inside the `templates` folder:

```html
<!-- app/templates/index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello, World!</title>
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/style.css') }}"
    />
  </head>
  <body>
    <h1>Hello, World!</h1>
    <img src="{{ url_for('static', filename='img/logo.png') }}" alt="Logo" />
  </body>
</html>
```

### Step 3: Create Static Files (CSS, JS, Images)

You can create some example static files:

1. **CSS File:** `app/static/css/style.css`

   ```css
   /* app/static/css/style.css */
   body {
     font-family: Arial, sans-serif;
     text-align: center;
     background-color: #f0f0f0;
   }

   h1 {
     color: #333;
   }
   ```

2. **JavaScript File:** `app/static/js/script.js`

   ```javascript
   // app/static/js/script.js
   console.log("Hello, World!");
   ```

3. **Image File:** `app/static/img/logo.png`

   You can add any image to this folder.

### Step 4: Update the Route to Render the Template

Update `routes.py` to render the HTML template:

```python
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return render_template('index.html')
```

### Step 5: Run the Application

Run your Flask app again:

```bash
python run.py
```

### Access the App

Visit `http://127.0.0.1:5000/` in your browser, and you should see the "Hello, World!" message styled with the CSS you added and any images you included.

## Summary

This expanded folder structure allows you to organize your templates and static files separately:

- **`templates/`:** For HTML (or EJS) files that define the structure of your web pages.
- **`static/`:** For CSS, JavaScript, images, and other static files used by your web pages.

This setup is commonly used in Flask projects and provides a clean separation of concerns, making your project easier to maintain as it grows.

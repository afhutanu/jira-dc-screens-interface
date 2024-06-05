# Flask API for Screen Management

This repository contains a Flask API for managing screens, including login, renaming screens, and copying screens.

## Requirements

- Python 3.x
- Flask
- requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/afhutanu/JIRA-DC-SCREENS-UI
    cd yourrepository
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## API Endpoints

### 1. Login

- **URL:** `/login`
- **Method:** `POST`
- **Form Data:**
    - `auth_type`: `basic` or `bearer`
    - If `basic`: `username` and `password`
    - If `bearer`: `token`
- **Response:**
    - On success: Renders the `screens.html` template with screens data.
    - On failure: Returns `401` status code.

### 2. Rename Screen

- **URL:** `/edit_screen_name`
- **Method:** `POST`
- **JSON Payload:**
    - `name`: New name for the screen
    - `screenId`: ID of the screen to rename
- **Response:**
    - On success: Returns a JSON response with updated screens data.
    - On failure: Returns appropriate status code and message.

### 3. Copy Screen

- **URL:** `/copy_screen`
- **Method:** `POST`
- **JSON Payload:**
    - `name`: New name for the copied screen
    - `screenId`: ID of the screen to copy
- **Response:**
    - On success: Returns a JSON response with updated screens data.
    - On failure: Returns appropriate status code and message.

## Usage

1. Run the Flask application:
    ```sh
    export FLASK_APP=api.py
    flask run
    ```

2. Access the API at `http://127.0.0.1:5000`.

## Example Requests

### Login

```sh
curl -X POST http://127.0.0.1:5000/login \
    -F 'auth_type=basic' \
    -F 'username=yourusername' \
    -F 'password=yourpassword'
```

## Notes
Requires Jira data center
Requires ScriptRunner"# jira-dc-screens-interface" 
"# jira-dc-screens-interface" 
"# jira-dc-screens-interface" 

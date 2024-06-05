from flask import Blueprint, render_template, request, jsonify, session
import requests

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/login', methods=['POST'])
def login():
    auth_type = request.form['auth_type']
    headers = {}

    if auth_type == 'basic':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
        session['auth_type'] = 'basic'
        headers['Authorization'] = f'{requests.auth._basic_auth_str(username, password)}'
    elif auth_type == 'bearer':
        token = request.form['token']
        session['token'] = token
        session['auth_type'] = 'bearer'
        headers['Authorization'] = f'Bearer {token}'

    print(f"Auth type: {session['auth_type']}")

    if(session['auth_type'] == 'basic'):
        print(f"Basic auth: {session['username']}:{session['password']}")

    if(session['auth_type'] == 'bearer'):
        print(f"Bearer token: {session['token']}")

    response = requests.post('https://dev.instance-name/rest/scriptrunner/latest/custom/createOrFetchScreens?action=fetch', headers=headers)

    if response.status_code == 200:
        data = response.json()
        return render_template('screens.html', screens=data)
    else:
        return "Login failed", 401
    
@api_blueprint.route('/edit_screen_name', methods=['POST'])
def renameScreen():
    data = request.get_json()
    newName = data['name']
    screenId = data['screenId']

    # https://dev.instance-name/rest/scriptrunner/latest/custom/createOrFetchScreens?action=edit&screenId=92807
    # #{
    #   "name": "TEAH: CLOSED RENAME"
    # }

    # screenId = request.form['screenId']
    # newName = request.form['newName']
    headers = {}
    if(session['auth_type'] == 'basic'):
        headers['Authorization'] = f"{requests.auth._basic_auth_str(session['username'], session['password'])}"
    elif(session['auth_type'] == 'bearer'):
        headers['Authorization'] = f"Bearer {session['token']}"
    
    headers['Content-Type'] = 'application/json'
    payload = {
        "name": newName
    }
    response = requests.post(f'https://dev.instance-name/rest/scriptrunner/latest/custom/createOrFetchScreens?action=edit&screenId={screenId}', headers=headers, json=payload)

    if response.status_code == 200:
        # Fetch the updated list of screens
        fetch_response = requests.post('https://dev.instance-name/rest/scriptrunner/latest/custom/createOrFetchScreens?action=fetch', headers=headers)
        print(fetch_response.status_code)
        if fetch_response.status_code == 200:
            updated_data = fetch_response.json()
            # return render_template('screens.html', screens=updated_data)
            return jsonify({'status': 'success', 'message': 'Screen renamed successfully', 'screens': updated_data})
        else:
            return jsonify({'status': 'success', 'message': 'Screen renamed, but failed to refresh data'}), 200
    else:
        return jsonify({'status': 'fail', 'message': 'Failed to rename screen'}), response.status_code
    
@api_blueprint.route('/copy_screen', methods=['POST'])
def copyScreen():
    data = request.get_json()
    screenId = data['screenId']
    newName = data['newName']

    headers = {}
    if(session['auth_type'] == 'basic'):
        headers['Authorization'] = f"{requests.auth._basic_auth_str(session['username'], session['password'])}"
    elif(session['auth_type'] == 'bearer'):
        headers['Authorization'] = f"Bearer {session['token']}"
    
    headers['Content-Type'] = 'application/json'
    payload = {
        "name": newName
    }
    response = requests.post(f'https://dev.instance-name/rest/scriptrunner/latest/custom/createOrFetchScreens?action=copy&screenId={screenId}', headers=headers, json=payload)

    if response.status_code == 200:
        # Fetch the updated list of screens
        fetch_response = requests.post('https://dev.instance-name/rest/scriptrunner/latest/custom/createOrFetchScreens?action=fetch', headers=headers)
        print(fetch_response.status_code)
        if fetch_response.status_code == 200:
            updated_data = fetch_response.json()
            return jsonify({'status': 'success', 'message': 'Screen copied successfully', 'screens': updated_data})
        else:
            return jsonify({'status': 'success', 'message': 'Screen copied, but failed to refresh data'}), 200
    else:
        return jsonify({'status': 'fail', 'message': 'Failed to copy screen'}), response.status_code
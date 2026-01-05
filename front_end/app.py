from flask import Flask, render_template, request, redirect, session
import requests
from functools import wraps
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_this'

API_URL = 'http://127.0.0.1:5000'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/auth')
        return f(*args, **kwargs)
    return decorated_function

# ===== AUTH ROUTES =====
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    error = ''
    
    if request.method == 'POST':
        is_login = request.form.get('is_login') == 'true'
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if is_login:
            try:
                res = requests.get(f'{API_URL}/users/username/{username}')  
                data = res.json()
                print(f"API Response: {data}")
    
                if data['status'] == 'success':
                    stored_hash = data['user']['password']
                    print(f"Stored hash: {stored_hash}")
                    print(f"Input password: {password}")
        
                    result = check_password_hash(stored_hash, password)
                    print(f"Password match: {result}")
        
                    if result:
                        session['user_id'] = data['user']['id']
                        session['username'] = username
                        return redirect('/dashboard')
                    else:
                        error = 'Invalid password'
                else:
                    error = 'User not found'
            except Exception as e:
                print(f"Login error: {e}")
                import traceback
                traceback.print_exc()
                error = 'Error connecting to server'
        else:
            try:
                res = requests.post(f'{API_URL}/users/', json={
                    'username': username,
                    'email': email,
                    'password': password
                })
                data = res.json()
                
                if data['status'] == 'success':
                    session['user_id'] = data['user']['id']
                    session['username'] = username
                    return redirect('/dashboard')
                else:
                    error = data.get('message', 'Sign up failed')
            except Exception as e:
                error = 'Error connecting to server'
    
    return render_template('auth.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/auth')

# ===== DASHBOARD ROUTES =====
@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    error = ''
    pockets = []
    
    try:
        res = requests.get(f'{API_URL}/users/{user_id}/pockets')
        data = res.json()
        if data['status'] == 'success':
            pockets = data.get('pockets', [])
            print(f"Pockets: {pockets}")
    except Exception as e:
        error = 'Error fetching pockets'
    
    return render_template('dashboard.html', pockets=pockets, error=error)

@app.route('/pocket/create', methods=['POST'])
@login_required
def create_pocket():
    user_id = session['user_id']

    pocket_name = request.form.get('pocket_name')
    description = request.form.get('description')
    goal = request.form.get('goal')
    balance = request.form.get('balance')
    currency = request.form.get('currency')

    try:
        res = requests.post(
            f'{API_URL}/users/{user_id}/pockets',
            json={
                "pocket_name": pocket_name,                         # API-level field
                "description": description,
                "balance": float(balance or 0),
                "goal": float(goal),
                "currency": currency or "USD"
            }
        )

        print(f"Status code: {res.status_code}")
        print(f"Response: {res.text}")

        data = res.json()
        print(f"JSON: {data}")

        if data.get('status') != 'success':
            return redirect(
                f'/dashboard?error={data.get("message", "Error creating pocket")}'
            )

    except Exception as e:
        print(f"Exception: {e}")
        import traceback
        traceback.print_exc()
        return redirect('/dashboard?error=Error creating pocket')

    return redirect('/dashboard')

@app.route('/pocket/<int:pocket_id>')
@login_required
def pocket_detail(pocket_id):
    user_id = session['user_id']
    pocket = None
    error = ''
    
    try:
        res = requests.get(f'{API_URL}/users/{user_id}/pockets')
        data = res.json()
        if data['status'] == 'success':
            pockets = data.get('pockets', [])
            pocket = next((p for p in pockets if p['id'] == pocket_id), None)
            
            if not pocket:
                error = 'Pocket not found'
    except Exception as e:
        error = 'Error fetching pocket'
    
    if not pocket:
        return redirect('/dashboard')
    
    return render_template('pocket_detail.html', pocket=pocket, error=error)

@app.route('/pocket/<int:pocket_id>/update', methods=['POST'])
@login_required
def update_pocket(pocket_id):
    user_id = session['user_id']
    name = request.form.get('name')
    goal = request.form.get('goal')
    
    try:
        res = requests.put(f'{API_URL}/users/{user_id}/pockets/{pocket_id}', json={
            'name': name,
            'goal': float(goal)
        })
        data = res.json()
        
        if data['status'] != 'success':
            return redirect(f'/pocket/{pocket_id}?error={data.get("message", "Error")}')
    except Exception as e:
        return redirect(f'/pocket/{pocket_id}?error=Error updating pocket')
    
    return redirect('/dashboard')

@app.route('/pocket/<int:pocket_id>/delete', methods=['POST'])
@login_required
def delete_pocket(pocket_id):
    user_id = session['user_id']
    
    try:
        res = requests.delete(f'{API_URL}/users/{user_id}/pockets/{pocket_id}')
        data = res.json()
        
        if data['status'] != 'success':
            return redirect(f'/dashboard?error={data.get("message", "Error")}')
    except Exception as e:
        return redirect(f'/dashboard?error=Error deleting pocket')
    
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
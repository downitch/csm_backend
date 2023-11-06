import sys
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))

userProfiles = os.path.join(current_dir, 'controllers', 'userProfiles')
sys.path.append(userProfiles)
roles = os.path.join(current_dir, 'controllers', 'roles')
sys.path.append(roles)
timeslots = os.path.join(current_dir, 'controllers', 'timeslots')
sys.path.append(timeslots)
bids = os.path.join(current_dir, 'controllers', 'bids')
sys.path.append(bids)

from handleAuthentication import HandleAuthentication
from handleCreateUserProfile import HandleCreateUser
from handleReadUserProfile import HandleReadUser
from handleUpdateUserProfile import HandleUpdateUser
from handleDeleteUserProfile import HandleDeleteUser
from handleSearchUserProfile import HandleSearchUser

from handleCreateRole import HandleCreateRole 
from handleReadRole import HandleReadRole 
from handleUpdateRole import HandleUpdateRole 
from handleDeleteRole import HandleDeleteRole 
from handleSearchRole import HandleSearchRole

from handleCreateTimeslot import HandleCreateTimeslot  
from handleReadTimeslot import HandleReadTimeslot  
from handleUpdateTimeslot import HandleUpdateTimeslot  
from handleDeleteTimeslot import HandleDeleteTimeslot  
from handleSearchTimeslot import HandleSearchTimeslot

from handleCreateBid import HandleCreateBid
from handleReadBid import HandleReadBid
from handleUpdateBid import HandleUpdateBid
from handleDeleteBid import HandleDeleteBid
from handleSearchBid import HandleSearchBid

app = Flask(__name__)
CORS(app)

auth_controller = HandleAuthentication('database/database.db')
create_user_controller = HandleCreateUser('database/database.db')
read_user_controller = HandleReadUser('database/database.db')
update_user_controller = HandleUpdateUser('database/database.db')
delete_user_controller = HandleDeleteUser('database/database.db')
search_user_controller = HandleSearchUser('database/database.db')

create_role_controller = HandleCreateRole('database/database.db')
read_role_controller = HandleReadRole('database/database.db')
update_role_controller = HandleUpdateRole('database/database.db')
delete_role_controller = HandleDeleteRole('database/database.db')
search_role_controller = HandleSearchRole('database/database.db')

create_timeslot_controller = HandleCreateTimeslot('database/database.db')
read_timeslot_controller = HandleReadTimeslot('database/database.db')  
update_timeslot_controller = HandleUpdateTimeslot('database/database.db')  
delete_timeslot_controller = HandleDeleteTimeslot('database/database.db')  
search_timeslot_controller = HandleSearchTimeslot('database/database.db')

create_bid_controller = HandleCreateBid('database/database.db')
read_bid_controller = HandleReadBid('database/database.db')
update_bid_controller = HandleUpdateBid('database/database.db')
delete_bid_controller = HandleDeleteBid('database/database.db')
search_bid_controller = HandleSearchBid('database/database.db')

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email and password:
        token = auth_controller.auth(email, password)
        if token:
            return jsonify({"token": token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    else:
        return jsonify({"error": "Missing email or password"}), 400

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    if token:
        # You can implement token validation and invalidation logic here
        result = auth_controller.unauth(token)
        if result:
            return jsonify({"message": "Logged out"}), 200
        else:
            return jsonify({"error": "Invalid token"}), 401
    else:
        return jsonify({"error": "Missing token in headers"}), 400

# Create User endpoint (Create)
@app.route('/user_profiles', methods=['POST'])
def create_user():
    data = request.get_json()
    login = data.get('login')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    dob = data.get('dob')
    role_id = data.get('role_id')

    user_id = create_user_controller.create_user(login, email, password, first_name, last_name, dob, role_id)
    return jsonify({"user_id": user_id}), 201

# Get User Profile by ID endpoint (Read)
@app.route('/user_profiles/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = read_user_controller.read_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Update User Profile by ID endpoint (Update)
@app.route('/user_profiles/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    login = data.get('login')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    dob = data.get('dob')
    role_id = data.get('role_id')

    update_user_controller.update_user(user_id, login, email, password, first_name, last_name, dob, role_id)
    return jsonify({"message": "User profile updated"}), 200

# Delete User Profile by ID endpoint (Delete)
@app.route('/user_profiles/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    delete_user_controller.delete_user(user_id)
    return jsonify({"message": "User profile deleted"}), 200

# Search User Profiles by Email endpoint (Search)
@app.route('/user_profiles', methods=['GET'])
def search_user():
    email = request.args.get('email')
    users = search_user_controller.search_user(email)
    return jsonify(users), 200

# Create Role endpoint (Create)
@app.route('/roles', methods=['POST'])
def create_role():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    role_id = create_role_controller.create_role(name, description)
    return jsonify({"role_id": role_id}), 201

# Get Role by ID endpoint (Read)
@app.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    role = read_role_controller.read_role(role_id)
    if role:
        return jsonify(role), 200
    else:
        return jsonify({"error": "Role not found"}), 404

# Update Role by ID endpoint (Update)
@app.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    update_role_controller.update_role(role_id, name, description)
    return jsonify({"message": "Role updated"}), 200

# Delete Role by ID endpoint (Delete)
@app.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    delete_role_controller.delete_role(role_id)
    return jsonify({"message": "Role deleted"}), 200

# Search Roles by Name endpoint (Search)
@app.route('/roles', methods=['GET'])
def search_role():
    name = request.args.get('name')
    roles = search_role_controller.search_role(name)
    return jsonify(roles), 200

# Create Timeslot endpoint (Create)
@app.route('/timeslots', methods=['POST'])
def create_timeslot():
    data = request.get_json()
    frame = data.get('frame')
    exact_date = data.get('exact_date')

    timeslot_id = create_timeslot_controller.create_timeslot(frame, exact_date)
    return jsonify({"timeslot_id": timeslot_id}), 201

# Get Timeslot by ID endpoint (Read)
@app.route('/timeslots/<int:timeslot_id>', methods=['GET'])
def get_timeslot(timeslot_id):
    timeslot = read_timeslot_controller.read_timeslot(timeslot_id)
    if timeslot:
        return jsonify(timeslot), 200
    else:
        return jsonify({"error": "Timeslot not found"}), 404

# Update Timeslot by ID endpoint (Update)
@app.route('/timeslots/<int:timeslot_id>', methods=['PUT'])
def update_timeslot(timeslot_id):
    data = request.get_json()
    frame = data.get('frame')
    exact_date = data.get('exact_date')

    update_timeslot_controller.update_timeslot(timeslot_id, frame, exact_date)
    return jsonify({"message": "Timeslot updated"}), 200

# Delete Timeslot by ID endpoint (Delete)
@app.route('/timeslots/<int:timeslot_id>', methods=['DELETE'])
def delete_timeslot(timeslot_id):
    delete_timeslot_controller.delete_timeslot(timeslot_id)
    return jsonify({"message": "Timeslot deleted"}), 200

# Search Timeslots by Frame endpoint (Search)
@app.route('/timeslots', methods=['GET'])
def search_timeslot():
    frame = request.args.get('frame')
    timeslots = search_timeslot_controller.search_timeslot(frame)
    return jsonify(timeslots), 200

# Create Bid endpoint (Create)
@app.route('/bids', methods=['POST'])
def create_bid():
    data = request.get_json()
    timeslot_id = data.get('timeslot_id')
    user_account_id = data.get('user_account_id')
    reviewed = data.get('reviewed')
    approved = data.get('approved')

    bid_id = create_bid_controller.create_bid(timeslot_id, user_account_id, reviewed, approved)
    return jsonify({"bid_id": bid_id}), 201

# Get Bid by ID endpoint (Read)
@app.route('/bids/<int:bid_id>', methods=['GET'])
def get_bid(bid_id):
    bid = read_bid_controller.read_bid(bid_id)
    if bid:
        return jsonify(bid), 200
    else:
        return jsonify({"error": "Bid not found"}), 404

# Update Bid by ID endpoint (Update)
@app.route('/bids/<int:bid_id>', methods=['PUT'])
def update_bid(bid_id):
    data = request.get_json()
    timeslot_id = data.get('timeslot_id')
    user_account_id = data.get('user_account_id')
    reviewed = data.get('reviewed')
    approved = data.get('approved')

    update_bid_controller.update_bid(bid_id, timeslot_id, user_account_id, reviewed, approved)
    return jsonify({"message": "Bid updated"}), 200

# Delete Bid by ID endpoint (Delete)
@app.route('/bids/<int:bid_id>', methods=['DELETE'])
def delete_bid(bid_id):
    delete_bid_controller.delete_bid(bid_id)
    return jsonify({"message": "Bid deleted"}), 200

# Search Bids by Timeslot and User Account IDs endpoint (Search)
@app.route('/bids', methods=['GET'])
def search_bid():
    timeslot_id = request.args.get('timeslot_id')
    user_account_id = request.args.get('user_account_id')
    bids = search_bid_controller.search_bid(timeslot_id, user_account_id)
    return jsonify(bids), 200

if __name__ == '__main__':
    app.run(debug=True)

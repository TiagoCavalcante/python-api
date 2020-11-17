from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

users = []

# routes
@app.route('/users', methods=['GET'])
def get_users():
	return jsonify(users), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
	for user in users:
		if user['id'] == id:
			return jsonify(user), 200
	
	return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
	if not request.json:
		return jsonify({'message': '\'application/json\' body missing or empty'}), 400
	if not 'name' in request.json:
		return jsonify({'message': '\'name\' property missing'}), 400
	if not 'email' in request.json:
		return jsonify({'message': '\'email\' property missing'}), 400

	users.append({
		'id': len(users),
		'name': request.json['name'],
		'email': request.json['email']
	})

	return jsonify({'id': len(users) - 1}), 201    	

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
	if not request.json:
		return jsonify({'message': '\'application/json\' body missing or empty'}), 400

	for i, user in enumerate(users):
		if user['id'] == id:
			if 'name' in request.json:
				users[i]['name'] = request.json['name']
			if 'email' in request.json:
				users[i]['email'] = request.json['email']

			return jsonify({}), 200
	
	return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
	for i, user in enumerate(users):
		if user['id'] == id:
			del users[i]

			return jsonify({}), 200
	
	return jsonify({'message': 'User not found'}), 404

# run
if __name__ == '__main__':
    app.run()
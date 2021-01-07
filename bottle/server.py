from bottle import run, route, request, response
import json

users = []

@route('/users', method='GET')
def get_users():
	response.status = 200
	return json.dumps(users)

@route('/users/<user_id:int>', method='GET')
def get_user(user_id):
	for user in users:
		if user['id'] == user_id:
			response.status = 200
			return json.dumps(user)

	response.status = 404
	return json.dumps({'message': 'User not found'})

@route('/users', method='POST')
def create_user():
	if request.json is None:
		response.status = 400
		return json.dumps({'message': '\'application/json\' body missing'})

	if not 'name' in request.json:
		response.status = 400
		return json.dumps({'message': '\'name\' property missing'})
	if not 'email' in request.json:
		response.status = 400
		return json.dumps({'message': '\'email\' property missing'})

	users.append({
		'id': len(users),
		'name': request.json['name'],
		'email': request.json['email']
	})

	response.status = 201
	return json.dumps({'id': len(users) - 1})

@route('/users/<user_id:int>', method='PUT')
def update_user(user_id):
	if request.json is None:
		response.status = 400
		return json.dumps({'message': '\'application/json\' body missing'})

	for i, user in enumerate(users):
		if user['id'] == user_id:
			if 'name' in request.json:
				users[i]['name'] = request.json['name']
			if 'email' in request.json:
				users[i]['email'] = request.json['email']

			response.status = 200
			return json.dumps({})

	response.status = 404
	return json.dumps({'message': 'User not found'})

@route('/users/<user_id:int>', method='DELETE')
def delete_user(user_id):
	for i, user in enumerate(users):
		if user['id'] == user_id:
			del users[i]

			response.status = 200
			return json.dumps({})

	response.status = 404
	return json.dumps({'message': 'User not found'})

run()
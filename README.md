# python-api
An API to register users wrote in Python with 2 versions: Flask and Bottle

## Install dependencies
Search how to install Flask and Bottlo on your system

## Run
To run the Flask API: ```python flask/server.py```

![flask](https://user-images.githubusercontent.com/62714153/99418577-ef231480-28d9-11eb-93ac-051f925401d1.gif)

To run the Bottle API: ```python bottle/server.py```

![bottle](https://user-images.githubusercontent.com/62714153/99418594-f5b18c00-28d9-11eb-8c72-430301145cc0.gif)

## Routes
| method | path          | description                                                                                                                              |
|--------|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| GET    | `/users`      | return the users and their information                                                                                                   |
| GET    | `/users/<id>` | return the information about the user with the id `id`                                                                                   |
| POST   | `/users`      | create a user, receives a `application/json` body with the required parameters `name` and `email`, return the created user's id          |
| PUT    | `/users/<id>` | edit the information about the user with the id `id`, receives a `application/json` body with the optional parameters `name` and `email` |
| DELETE | `/users/<id>` | delete the user with the id `id`                                                                                                         |
# flask-boilerplate
Minimal setup for building a Python API running with Flask and MongoDB, inside Docker Containers

### On machines with Docker and Docker Compose installed, simply run:

```
docker-compose build
docker-compose up
```

### Otherwise, you'll need to:

* install MongoDB
* install Python 3
* install `pip`
* run `pip install -r requirements.txt`
* run `FLASK_APP=app.py flask run` to start the server (or `python app.py`)
* change the line:
```
client = MongoClient('mongodb://db:27017/')
```
to wherever your Mongo DB is running (`localhost` for instance)
```
client = MongoClient('mongodb://localhost:27017/')
```

You can test the endpoints with:
```bash
curl localhost:5000  # Hello World
curl localhost:5000/users  # Retrieves all users
curl --data "name=John Doe"  localhost:5000/users  # Adds new "John Doe" user
```

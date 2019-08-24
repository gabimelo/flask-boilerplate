# flask-boilerplate
Minimal setup for building a Python API running with Flask and MongoDB, inside Docker Containers. Some more info can be found in [this medium post](https://medium.com/@gabimelo/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e).

## Running it:

Make sure Docker and Docker Compose are installed, and then simply run:

```
docker-compose up --build -d
```

## Testing it:

You can test the endpoints with:
```bash
curl localhost:5000  # Hello World
curl localhost:5000/users  # Retrieves all users
curl --data "name=John Doe"  localhost:5000/users  # Adds new "John Doe" user
```

For unit testing, `pip install pytest pytest-cov` and then you can run:
```bash
make test
``` 

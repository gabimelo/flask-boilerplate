test:
	docker exec -it flaskboilerplate_app_1 python -m pytest --cov=src tests/

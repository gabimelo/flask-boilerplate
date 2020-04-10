#### Base

docker_compose_test_file = docker-compose -p flask_boilerplate_tests -f docker-compose.test.yml
docker_up = $(docker_compose_test_file) up --abort-on-container-exit

build-image:
	# given that all our services in docker-compose.test.yml use the same image, we'll just call build on the first one
	$(docker_compose_test_file) build lint || exit 1

#### Lint

.SILENT lint: build-image
	$(docker_up) lint || exit 1

#### Tests

unit-test: build-image
	$(docker_up) unit_test || exit 1

integration-test: build-image
	$(docker_compose_test_file) up -d db
	$(docker_up) integration_test || (docker rm -f flask_boilerplate_tests_db_1; exit 1)
	docker rm -f flask_boilerplate_tests_db_1

test: unit-test integration-test

#### Local development helpers

dev-up:
	docker-compose up --build -d

ping:
	curl localhost:5010/ping

get-users:
	curl localhost:5010/users

add-user:  # pass it the name argument, eg `make add-user name='John Doe'`
	curl --data "name=$(name)"  localhost:5010/users

#### Dev Helpers

config-githooks:
	git config core.hooksPath githooks
	chmod +x githooks/pre-commit

clean-pycache:
	sudo find . -type f -name "*.py[co]" -delete
	sudo find . -type d -name "__pycache__" -exec rm -rv {} +
	sudo find . -type d -name ".pytest_cache" -exec rm -rv {} +

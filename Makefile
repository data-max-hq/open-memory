build:
	docker-compose build

run:
	docker-compose up

clean:
	docker rm jinaai-demo
	
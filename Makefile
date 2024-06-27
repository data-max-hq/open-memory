build:
	docker build -t jinaai .

run:
	docker run -p 9876:9876 -p 11434:11434 jinaai
build:
	docker build -t jinaai .

run:
	docker run -it -p 9876:9876 jinaai /bin/bash
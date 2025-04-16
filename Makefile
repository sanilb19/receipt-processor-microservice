# Makefile for FastAPI Receipt Processor

APP_NAME=receipt-app
CONTAINER_NAME=receipt-container

# Load environment variables from .env file
include .env
export

.PHONY: build run stop test clean

build:
	docker build -t $(APP_NAME) .

run:
	docker run -d -p $(PORT):$(PORT) -e PORT=$(PORT) --name $(CONTAINER_NAME) $(APP_NAME)

stop:
	docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME)

test:
	PORT=$(PORT) pytest tests/

clean: stop
	docker rmi $(APP_NAME)
	find . -type d -name '__pycache__' -exec rm -r {} +

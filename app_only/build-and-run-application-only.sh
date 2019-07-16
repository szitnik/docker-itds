#!/bin/bash
docker build -t docker-app ./application

docker run -p 8787:8787 -it docker-app docker-app
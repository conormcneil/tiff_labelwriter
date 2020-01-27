#!/bin/bash

docker-compose build 

docker-compose up -d

docker container logs -f tiff-labelwriter
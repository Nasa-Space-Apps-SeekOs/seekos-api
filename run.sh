#!/bin/bash

docker run -it --rm --name seekos-api -v ./app:/var/app -p 8001:8001 seekos-api

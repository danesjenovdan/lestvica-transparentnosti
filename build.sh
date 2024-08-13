#!/bin/bash

docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH api
docker build ./api -t lestvica-transparentnosti:latest
docker tag lestvica-transparentnosti:latest rg.fr-par.scw.cloud/djnd/lestvica-transparentnosti:latest
docker push rg.fr-par.scw.cloud/djnd/lestvica-transparentnosti:latest

# BUILD AND PUBLISH front
docker build ./front -t lestvica-transparentnosti-front:latest
docker tag lestvica-transparentnosti-front:latest rg.fr-par.scw.cloud/djnd/lestvica-transparentnosti-front:latest
docker push rg.fr-par.scw.cloud/djnd/lestvica-transparentnosti-front:latest

#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH PRAVNA MREZA
sudo docker build -f api/Dockerfile -t lestvica-transparentnosti:latest ./api
sudo docker tag lestvica-transparentnosti:latest rg.fr-par.scw.cloud/djnd/lestvica-transparentnosti:latest
sudo docker push rg.fr-par.scw.cloud/djnd/lestvica-transparentnosti:latest

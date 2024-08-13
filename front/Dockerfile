# build stage image
FROM node:16-alpine AS build-stage

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn

COPY . .

RUN mv .env.example .env

RUN yarn generate

# actual image
FROM nginx:alpine

# copy built files to nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# copy custom nginx config to support client-side routing
COPY nginx.conf /etc/nginx/conf.d/default.conf

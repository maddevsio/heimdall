FROM node:9.11.1
COPY . /heimdall
WORKDIR /heimdall
RUN npm i && npm run build

FROM nginx:latest
COPY --from=0  /heimdall/dist /usr/share/nginx/html

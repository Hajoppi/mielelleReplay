FROM node:10 as build_stage

WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . .
RUN npm run build

FROM nginx:1.19
EXPOSE 80
COPY --from=build_stage /app/dist /usr/share/nginx/html

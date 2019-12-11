FROM nginx:1.14.1-alpine
RUN apk add --no-cache bash

ENV APP ./api
RUN mkdir $APP
WORKDIR $APP

## Copy our default nginx config which will replace the existing default.conf
COPY default.conf /etc/nginx/conf.d/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
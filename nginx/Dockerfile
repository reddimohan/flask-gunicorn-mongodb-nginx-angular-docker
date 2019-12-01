FROM nginx:1.11.8-alpine

# Removing the defualt .conf file
RUN rm /etc/nginx/conf.d/default.conf

# Copying application specific nginx .conf files
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
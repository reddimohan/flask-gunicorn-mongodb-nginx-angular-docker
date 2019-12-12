### Docker
```sh
$ docker --version
Docker version 19.03.4, build 9013bf583a
```

### Dockercompose
```sh
$ docker-compose --version
docker-compose version 1.25.0, build 0a186604
```

##### Setup
- Can be found 

##### Docker commands used in the project
Build image:
`$ docker build --tag image_name .`

Docker run the image on container
`$ docker run --name container_name --detach -p HOST_PORT:Container_PORT image_name`

Docker run image and ssh to the container and remove container on terminal Exit 
`$ docker run -it --rm image_name /bin/bash`

Dockercompose command to build and run the container
`$ docker-compose up --build --detach`

##### Create new mongodb user for the flask API to use
```sh
## Create DB name before calling the Flask APIs based on your docker-compose.yml file configuration at 'flask-api' service

use mo
db.createUser(
  {
    user: "test",
    pwd: "test",
    roles: [ { role: "readWrite", db: "mo" } ]
  }
)
```


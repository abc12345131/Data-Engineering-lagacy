# Some general command with docker

## check the docker version
```
docker version
```

## check the docker information
```
docker info
```

## Might be Your first container run 
```
docker container run --publish 80:80 nginx
```

## Run container in a detach mode
```
docker container run --publish 80:80 --detach nginx
```

## Run container with a name
```
➜  ~ docker container run --publish 80:80 --name webserver --detach nginx
```

## Check the logs of the container
```
docker logs webserver
```

## Check the process running within a container
```
docker container top webserver
```

## Ok, let's clean the container (introduce -f also)
```
docker container rm container_id
```

## Check the logs of the running container
```
docker container logs container_name
```

# Hands on 
## requirement
1) Run a nginx, mysql, httpd (apache) server
2) Run them in a detach mode, and name them with --name
3) Nginx listen on port 80:80, httpd on 8080:80, myql on 3306:3306
4) Give mysql env for the password, MYSQL_RANDOM_ROOT_PASSWORD=yes with --env(or -e)
5) Use docker logs on the mysql container to check the instance's password
6) Remove the containers after you successfully lauch the them




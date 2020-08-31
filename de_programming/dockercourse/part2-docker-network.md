
## Access shell within a container

### Start a new container with interactive shell
```
docker container run -it ${container_name} 
```

### Hack into a existing contianer
```
docker container exec -it ${container_name} ?the bash command for your linux distribution?
```


## Docker networks
```
docker container run -p 80:80 --name web -d nginx

docker container port web

docker inspect web|grep IPAddress      // or you can do `docker inspect --format '{{ .NetworkSettings.IPAddress }}'  web`
```

```
docker network ls

docker network inspect bridge

docker network create my_virtual_net
```

bridge is the default

host is the host machine network

none is no network


### create container within my_virtual_net network
```
docker container run -d -p 80:80 --name webb --network=my_virtual_net nginx
```

### Connect/disconnect a container to a different network
```
docker container run -d -p 8011:80 --name webnew nginx

docker network connect my_virtual_net webnew

docker network disconnect  bridge webnew
```


## Docker DNS, don't use IP, it's anti-pattern and you shouldn't rely on IP for communication
```
docker exec -it webnew ping webb
```
### Default network has disadvantage that has not DNS server, in order to let two container talk to each other within the default bridge,
### you have to link the two instances which are very inconvenient. And this feature will be removed wihtin docker release.
### So, always create a new network for your containers.




## 1) Using container for CLI testing to have a container as a environment that only 
##    available during the interactive period, and after it's finish, terminate automatically.
## 2) Understand basics of what a Linux distribution is, like Ubuntu and Centos
## 3) Know how to run a container
## 4) Understand the basics of DNS records and DNS round robin https://en.wikipedia.org/wiki/Round-robin_DNS


### distro centos
```
docker container run --rm -it centos:7 bash
yum install -y curl
```

### distro ubuntu
```
docker container run --rm -it ubuntu:14.04 bash
apt-get update && apt-get install -u curl
```

## Assignment
## 1) Create a new virtual network
## 2) Create two containers from elasticsearch:2 image
## 3) Research and use --net-alias search when creating them to give
##    them an additional DNS name to respond to
## 4) Run apline nslookup search with --net to see the two containers list for the same DNS name
## 5) Run curl --s search:9200 with --net several times



## Tips
```
https://github.com/WeCloudData-Academy/de_programming/wiki/Docker---part2-netowrk
```

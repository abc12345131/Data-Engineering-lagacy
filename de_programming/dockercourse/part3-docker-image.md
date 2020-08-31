## User docker hub image

### Official image, good public image
```
docker images -a
```

### Check how the docker image is being layered up
```
docker history nginx:latest
```

### Create an account in docker hub
```
https://hub.docker.com
```

### Tag your own image
```
docker tag nginx edwinguo123/nginx
docker login
docker push edwinguo123/nginx
```

### build you own image
```
cd part3-dockerfile-stage1 
docker image build -t edwinnginx .
```

### build a custom nginx with a html file
```
cd part3-dockerfile-stage2
docker build -t nginxwithhtml .
docker container run --rm -d -p 80:80 nginxwithhtml
```

### Assignment: Build your own image
### This process will be iterative, build, test, modify, retest etc.
```
1) Take existing Node.js app and dockerize it
2) Create a Dockerfile , build it, test it push it, rm it and run it!
3) Use the apline version of the official 'node' 6.x image
4) Check your result at http://localhost
5) Tag and push your Docker hub account.
6) Remove your miage from your local cache and run again from docker hub.
```

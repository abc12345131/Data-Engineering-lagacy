## Using a single YAML file to describe your components for your project, including containers, networks and volumes.
## You can configure your own docker-compose file version.
## Check docker-compose-sample.yml file under this directory.

## There are two commands that you will use the most

```
docker-compose up -d
docker-compose down
```

## Class walk through
```
part4-dockercompose/jekyll-serve/
part4-dockercompose/compose-web-server/
```

## you can also check docker-compose through
```
docker-compose ps
docker-compose top
```


# Assignment: Writing a Compose File

##
> Goal: Create a compose config for a local Drupal CMS website

- This empty directory is where you should create a docker-compose.yml
- Use the `drupal` image along with the `postgres` image
- Set the version to 2
- Use `ports` to expose Drupal on 8080
- Be sure to setup POSTGRES_PASSWORD on postgres image
- Walk though Drupal config in browser at http://localhost:8080
- Tip: Drupal assumes DB is localhost, but it will actually be on the compose service name you give it
- Use Docker Hub documentation to figure out the right environment and volume settings
```


## Adding Image Building to Compose Files 
```
under part4-bonus-dockercompose
docker-compose up
```

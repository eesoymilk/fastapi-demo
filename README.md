# Docker tutorial

> Refer to [official documentations](https://docs.docker.com/) for more.

## Usage

### Build the image

```zsh
docker build -t fastapi-demo .
```

### Run the container

```zsh
docker run --name fastapi-demo-1 -p 8000:8000 fastapi-demo
```

## Useful Commands

```zsh
# list images
docker images

# list all images (including dangling ones)
docker images -a

# list containers
docker ps

# list all containers (including dangling ones)
docker ps -a

# build images
docker build -t <image-name>:<tag> <context>

# run a container with a given image
docker run -t --name fastapi-demo-1 -p 8000:8000 fastapi-demo

# remove containers
docker rm <selector-string>

# remove images
docker rmi <selector-string>

# clean your dockers
docker system prune
```

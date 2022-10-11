# Dockerfile

## Build docker image

```shell
docker build --build-arg UID=$(id -u) --build-arg GID=$(id -g) -t pybind11-example .
```

## Launch docker container

```shell
docker run -it --rm -v $HOME:$HOME pybind11-example bash
```

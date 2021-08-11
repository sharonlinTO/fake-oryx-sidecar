# Setup Instructions

## Create a Network
`docker network create testnetwork`

## Building the API
In the folder /flask-hello-world:

`docker build -t test-flask .`

`docker run --name=flask --net=testnetwork -dp 5000:5000 --mount type=volume,source=govolume,destination=/data test-flask`

## Building the caller/client
In the folder /caller-hello-world:

`docker build -t test-caller .`

`docker run --name=caller --net=testnetwork -dp 5324:5324 --mount type=volume,source=govolume,destination=/data test-flask`

Note: Make sure that the Flask API is running before you run the client, or else the client will not launch

## Check that containers are connected
`docker exec -it caller ping flask`

`docker exec -it flask ping caller`

## Binding a local volume as a docker volume
`docker run --name=flask --net=testnetwork -dp 5000:5000 -v "$PWD/binary":"/data" test-flask`

## Copy main.go to volumes
`docker cp ../data/main.go flask:/data`

`docker volume prune`
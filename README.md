# Setup Instructions

## Create a Network
`docker network create testnetwork`

## Building the API (Fake Oryx)

`docker build -t test-fake-oryx .`

`docker run --name=fake-oryx --net=testnetwork -dp 5000:5000 -v /tmp/kuduhome:/home test-fake-oryx`

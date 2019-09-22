[![](https://images.microbadger.com/badges/version/arunramakani/stream-server.svg)](https://microbadger.com/images/arunramakani/stream-server "Get your own version badge on microbadger.com") [![](https://img.shields.io/docker/pulls/arunramakani/stream-server.svg)](https://img.shields.io/docker/pulls/arunramakani/stream-server.svg) [![](https://img.shields.io/docker/stars/arunramakani/stream-server.svg)](https://img.shields.io/docker/stars/arunramakani/stream-server.svg)

# Stream Server

This is an example of unidirectional streaming using gRPC where the client streams data. This Stream server also uses metadata based authentication 

## Deploy to Kubernetes 

To deploy the application in kubernetes use 

```kubectl apply -f https://raw.githubusercontent.com/ArunRamakani/StreamServer/master/StreamServer.yaml```

Please note that you need ambassador setup in your k8s befor running this. If you choose to expose differently StreamServer.yaml needs modification. 

## Build 

checkout the repository and run the below command to build the docker image in your local  

```docker build -t arunramakani/stream-server```

Alternatively we can pull the docker image from the Docker Hub directly using the below command

```docker pull arunramakani/stream-server```

## Run 

Once you have the image you can run the image using the command

```docker run arunramakani/stream-server```

This make the server start looking for any new gRPC connections. See datastream.proto file in this repository for gRPC contarct details. 




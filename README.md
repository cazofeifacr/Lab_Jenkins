# Lab_Jenkins


# Define Docker Infra 
```
    docker network create jenkins
    docker network list
    docker network inspect jenkins
```

# Define Docker image 

```

ARG VERSION_SERVER="2.426.3-jdk17"

FROM --platform=linux/amd64 jenkins/jenkins:$VERSION_SERVER
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

```

# Build Docker image 

```
docker build -t myjenkins-blueocean:2.426.3-jdk17 -t myjenkins-blueocean:latest .
```

# Host Container Locally

```
VERSION_SERVER="2.426.3-jdk17"

docker run \
  --name myjenkins-blueocean \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:$VERSION_SERVER

```

# Accessing Server

```
docker exec -it myjenkins-blueocean bash
```

# Setup Server 

From Browser 

> http://localhost:8080

From Container 

> cat /var/jenkins_home/secrets/initialAdminPassword

or 

> docker exec myjenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword

From Browser 

> Copy Password *********

# Setup Docker Agent 

## Setup A Dockerfile 

File located at ```/Docker_Agent/Dockerfile```

## Create build and push image 

> docker login -u "cazofeifacr" -p "********" docker.io

```
VERSION_CLIENT="alpine-jdk17"
docker build -t cazofeifacr/myjenkins-agent-python:$VERSION_CLIENT -t cazofeifacr/myjenkins-agent-python:latest .
```

```
 docker push cazofeifacr/myjenkins-agent-python:latest
 docker push cazofeifacr/myjenkins-agent-python:alpine-jdk17
```

# Installation Docker Reference:
https://www.jenkins.io/doc/book/installing/docker/

## Bridge 
https://hub.docker.com/r/alpine/socat/


```
docker pull alpine/socat
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
```

>  docker inspect <Container_ID> | grep IPAddress


### alpine/socat container to forward traffic from Jenkins to Docker Desktop on Host Machine
https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin
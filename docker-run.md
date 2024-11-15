docker network create jenkins

```
VERSION_SERVER="2.484-jdk17"

docker run \
  --name jenkins-blueocean \
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

  Notice:
- To run the container in the **background** insert ``` --detach ``` after docker run.
- To automatically **start the container on restart** insert ```--restart always``` after docker run.
- To automatically **start the container unless it has been stopped** explicitly insert ```--restart unless-stopped``` after docker run.


# Setup Docker Agent 

> docker pull alpine/socat
> 
> docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock

> docker inspect <container_id> | grep IPAddress

> docker pull cazofeifacr/myjenkinsagents:python
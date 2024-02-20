ARG VERSION_CLIENT="alpine-jdk17"
FROM --platform=linux/amd64 jenkins/agent:$VERSION_CLIENT
USER root

# cmd tools
RUN apk update && apk upgrade && apk add --update alpine-sdk && \
    apk add --no-cache make cmake

# NPM
RUN apk add --no-cache nodejs npm \
    && npm install -g yarn --unsafe-perm

# Update packages
RUN apk update && \
    apk add --upgrade apk-tools && \
    apk upgrade --available && \
    sync

# PYTHON
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add py3-pip

WORKDIR /home/jenkins
USER jenkins
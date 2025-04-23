# Docker

## Share local Network with docker Network

Docker network outbound defintion example, which will enalbe to access services in the mapped network with docker services attached to the network.

```bash
docker network create --attachable --opt 'com.docker.network.bridge.name=bridge-tb' --opt 'com.docker.network.bridge.enable_ip_masquerade=false' bridge-tb
sudo iptables -t nat -A POSTROUTING -s 172.20.0.0/16 -o bridge-tb -j SNAT --to-source 192.168.0.23
```

## Portainer

To download the image from GitHub Packages, Docker must be logged in.  
Here is the command to do this:

```bash
export GITHUB_TOKEN=<dein_github_token>

echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_USER --password-stdin
```

Afterward, the Docker image can be downloaded from the GitHub repository.

## Watchtower

WatchTower is deployed, which automatically checks for newer versions. This will keep our app up-to-date while we are developing.  
Here is the documentation for WatchTower: [https://containrrr.dev/watchtower/](https://containrrr.dev/watchtower/)

To ensure that not all Docker images are updated indiscriminately, WatchTower is configured with the flag **WATCHTOWER_LABEL_ENABLE: "true"**. This means that only containers with a WatchTower label `enable=true` will be considered for updates. This allows us to precisely control which services should automatically receive updates. Documentation link here: [https://containrrr.dev/watchtower/container-selection/](https://containrrr.dev/watchtower/container-selection/)

Sample Config:

```yaml
version: "3"
services:
  someimage:
    container_name: someimage
    labels:
      - "com.centurylinklabs.watchtower.enable=true"
```
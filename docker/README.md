# Docker

## Share local Network with docker Network

Docker network outbound defintion example
```bash
docker network create --attachable --opt 'com.docker.network.bridge.name=bridge-tb' --opt 'com.docker.network.bridge.enable_ip_masquerade=false' bridge-tb
sudo iptables -t nat -A POSTROUTING -s 172.20.0.0/16 -o bridge-tb -j SNAT --to-source 192.168.0.23
```

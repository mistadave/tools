# Docker Sample MQTT

Here are some docker compose for mqtt to spin up.

## Compose using Cert

The `docker-compose-mqtt-cert.yaml` just defines a simple compose script for mosquitto mqtt which exposes two ports.

- 8883 (requires certificat)
- 1883 (no auth required)

Also will be a ca and server certificate be required for this example, which alloes only clients with a valid certificate to connect.

Cert Certificate: [TLS](../../TLS/README.md)

External example: [MQTT TLS Setup](http://www.steves-internet-guide.com/mosquitto-tls/)

## MQTT bridge example

The bridge example allows to access the mqtt using a password.txt file.
This mqtt is exposed using the port 8884, assuming that already a mqtt is running on 8883.
In the configuration it can be bridged to another mqtt using cert.
The bridge will forward all messages on a specifed topic: `mydevices/#` in the config to the destination mqtt.

# Generate tls

## Using Script

use the script `generate-CA.sh`, which automates the whole process of creating a certificate.

## By Hand

1. Create a **CA key pair**
2. Create **CA certificate** and use the CA key from step 1 to sign it.
3. Create a **broker key pair** don’t password protect.
4. Create a **broker certificate request** using key from step 3
5. Use the **CA certificate to sign the broker certificate request** from step 4.
6. Now we should have a **CA key file**,a **CA certificate file**, a **broker key file**, and a **broker certificate file**.

### Step 1

First create a key pair for the CA

```bash
openssl genrsa -des3 -out ca.key 2048
```

### Step 2

Now Create a certificate for the CA using the CA key that we created in step 1

```bash
openssl req -new -x509 -days 1826 -key ca.key -out ca.crt
Enter pass phrase for ./ca.key:
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CH
State or Province Name (full name) [Some-State]:St.Gallen
Locality Name (eg, city) []:Grabs
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Gateway Uno
Organizational Unit Name (eg, section) []:MQTT
Common Name (e.g. server FQDN or YOUR name) []:GatewayUno
Email Address []:admin@gateway.uno
```

### Step 3

Now we create a server key pair that will be used by the broker

```bash
openssl genrsa -out server.key 2048
```

### Step 4

Now we create a certificate request .csr. When filling out the form the common name is important and is usually the domain name of the server.

```bash
openssl req -new -out ./server.csr -key ./server.key
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CH
State or Province Name (full name) [Some-State]:St.Gallen
Locality Name (eg, city) []:Grabs
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Gateway Uno
Organizational Unit Name (eg, section) []:MQTT
Common Name (e.g. server FQDN or YOUR name) []:GatewayUno
Email Address []:admin@gateway.uno

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

### Step 5

Now we use the *CA key* to verify and sign the server certificate. This creates the *server.crt* file

```bash
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 1826
Signature ok
subject=C = CH, ST = St.Gallen, L = Grabs, O = Gateway Uno, OU = MQTT, CN = GatewayUno, emailAddress = admin@gateway.uno
Getting CA Private Key
Enter pass phrase for ca.key:
140525545760128:error:28069065:UI routines:UI_set_result:result too small:../crypto/ui/ui_lib.c:765:You must type in 4 to 1023 characters
Enter pass phrase for ca.key:
```

### Step 6

The above steps created various files. This is what the directory looks like now:
Required is the *ca.crt*, *server.crt* and *server.key* file for the mqtt.

```bash
-rw-r--r-- 1 admin admin 1428 Dec 17 09:36 ca.crt
-rw------- 1 admin admin 1751 Dec 17 09:34 ca.key
-rw-r--r-- 1 admin admin   17 Dec 17 09:39 ca.srl
-rw-r--r-- 1 admin admin 1306 Dec 17 09:39 server.crt
-rw-r--r-- 1 admin admin 1058 Dec 17 09:37 server.csr
-rw------- 1 admin admin 1679 Dec 17 09:36 server.key
```

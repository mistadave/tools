# Linux Tricks

## Add self signed Certificate

You've got a self signed certificate for your local servcies.

General docs: <https://alexanderzeitler.com/articles/Fixing-Chrome-missing_subjectAltName-selfsigned-cert-openssl/>

### Ubuntu install custom certificate

Replace school with your wanted name.

```bash
cd /usr/local/share/ca-certificates/
# Create a new folder, i.e.
sudo mkdir school
# Copy the .crt file into the school folder
cp ~/Downloads/school.crt /usr/local/share/ca-certificates/school/school.crt
# Make sure the permissions are OK (755 for the folder, 644 for the file)
sudo chmod 755 /usr/local/share/ca-certificates/school
sudo chmod 644 /usr/local/share/ca-certificates/school/school.crt
# update certs
sudo update-ca-certificates
```

## Failed2ban

install failed2ban on a linux server system, helps to reduce the rate of incorrect authentication attempts.

[https://github.com/fail2ban/fail2ban](https://github.com/fail2ban/fail2ban)

Config files can be found at the following paths

```bash
sudo nano /etc/fail2ban/jail.d/defaults-debian.conf
sudo nano /etc/fail2ban/jail.conf
```

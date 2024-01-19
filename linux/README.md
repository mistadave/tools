# Linux Tricks

## Add self signed Certificate

You've got a self signed certificate for your local servcies.

General docs: https://alexanderzeitler.com/articles/Fixing-Chrome-missing_subjectAltName-selfsigned-cert-openssl/

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

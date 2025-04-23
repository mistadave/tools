# Postgres

Postgres is a opensource object-relational DB.

Docker image: [https://hub.docker.com/_/postgres](https://hub.docker.com/_/postgres)

## Configuration

Enable to access psql from any host, not just localhost

```bash
sed "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/12/main/postgresql.conf

cat /etc/postgresql/12/main/pg_hba.conf
```

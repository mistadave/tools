# Running in the background

added app to crontab

```bash
sudo crontab -e

#insert
@reboot python3 {path-to-projekt}/modbus-ch341/flask-modbus.py >> /var/log/flask.log 2>&1 &
```

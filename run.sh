#!/bin/bash

# python manage.py migrate

# python manage.py collectstatic
./cloud_sql_proxy -instances=xcode111:us-central1:slammad=tcp:6543 -credential_file=secrets/db-proxy.json &
# wait for the proxy to spin up
sleep 1
# Start the server



/usr/local/bin/gunicorn src.wsgi:application -w 2 -b :8888



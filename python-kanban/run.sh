#!/usr/bin/with-contenv bashio

echo "Serving flask!"
waitress-serve --call 'main:create_app'

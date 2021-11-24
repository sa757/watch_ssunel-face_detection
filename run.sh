#!/usr/bin/env bash
export IS_DEBUG=${DEBUG:-false}
export APP_PORT=$1
exec gunicorn -b :$APP_PORT run:application

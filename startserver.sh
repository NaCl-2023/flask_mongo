#!/usr/bin/env bash
source ./venv/bin/activate
gunicorn wsgi:app -c config/gconfig.py --preload

#!/usr/bin/env bash
source ./venv/bin/activate
gunicorn wsgi:app -c conf/gconfig.py --preload

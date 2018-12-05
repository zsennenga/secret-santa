#! /bin/bash
gunicorn --bind 127.0.0.1:5000 --workers=8 "app.app:init_default_app()" --reload --log-level debug
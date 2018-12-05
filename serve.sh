#! /bin/bash
gunicorn --bind 0.0.0.0:5000 --workers=8 "app.app:init_default_app()" --reload --log-level debug
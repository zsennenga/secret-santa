# Secret Santa
Secret Santa Webapp in Flask and shitty jquery

# Install
1. Generate a config by copying `app/config/config_example.py` to `app/config/config.py`
2. Set up a database, a simple sqlite database works for local testing. `app/config/config_dev.py` has examples; feel free to use this instead of `config_example.py` as the basis for your config.
3. Run scripts/create_db.py
3. Run serve.sh

# TODO
Security/Registration
Templates and routes for home page, view santa page, and registration page
Tests (lol whatever)
Set up gunicorn, and maybe nginx?
Set up database/server

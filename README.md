# Secret Santa
Secret Santa Webapp in Flask and shitty jquery (FOR NOW?)

# Install
1. Generate a config by copying `config_example.py` or `config_dev.py` to `config.py`
2. Run serve.sh

# TODO
1. Auth Layer
* Login, register FE
* Hashing Algo
* Tests
2. Shared/general
* Pretty landing page/header/etc
* Project structure iterations
* Deploy procedure
3. Exchange functionality
The goal is to build a framework that can support multiple exchanges
To that end we need 3 pages:

1. View all existing exchanges, basic info (name, # signed up, etc), and their status (registration open/closed, matched, gifts exchanged)
2. Register for a given exchange
3. View detailed status of an exchange (rules, exchange date, who's signed up, etc)


4. Admin panel
* basic admin auth
* view exchange status
* view (anonomous) matching status
* kick off matching progess
* open/close registration

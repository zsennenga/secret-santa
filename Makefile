.PHONY: install serve

VIRTUALENV = $(shell which virtualenv)

ifeq ($(strip $(VIRTUALENV)),)
  VIRTUALENV = /usr/local/python/bin/virtualenv
endif

venv:
	$(VIRTUALENV) -p $(shell which python3) venv

clean:
	rm -rf venv __pycache__ .cache *.pyc

install: venv
	. venv/bin/activate; pip install -r requirements.txt

serve:
	. venv/bin/activate; sh serve.sh

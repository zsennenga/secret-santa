from app.app import init_default_app
from model.table.exchange import Exchange


def main():
    app = init_default_app()

    with app.app_context():
        Exchange.create()


if __name__ == '__main__':
    main()

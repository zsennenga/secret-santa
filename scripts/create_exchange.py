from datetime import datetime

from app.app import init_default_app
from model.table.exchange import Exchange


def main():
    app = init_default_app()

    with app.app_context():
        Exchange.create(
            name='test',
            ends_at=datetime.utcnow()
        )


if __name__ == '__main__':
    main()

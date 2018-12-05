from flask import render_template
from flask_login import current_user

from app.blueprint.base_blueprint import BaseBlueprint
from constant.blueprint_name import BlueprintName


class SharedPages(BaseBlueprint):
    def __init__(self):
        super(SharedPages, self).__init__(
            import_name=__name__,
            name=BlueprintName.SHARED.value,
        )

    def build_routes(self):
        @self.route('/', methods=['GET'])
        def home_get():
            return render_template('shared/home.html', user=current_user)

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
        def home():
            # HTML form showing 5 things:
            # Name, email, what to get me, what not to get me, who to ask for help with my gift
            return "Hewwo world"

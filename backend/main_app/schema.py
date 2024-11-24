import importlib
import graphene
from graphene import ObjectType

import os


from hackathon.settings import APP_NAME, BASE_DIR
from main_app.accounts.schema import UserType, get_me
from main_app.health.schema import HealthType
from main_app.parkings.schema import (
    ParkingType,
    get_parking,
    get_parkings,
    get_prediction,
)


class Query(ObjectType):
    me = graphene.Field(UserType, required=True)
    health = graphene.Field(HealthType, required=True)
    all_parkings = graphene.List(ParkingType, required=True)
    parking = graphene.Field(ParkingType, identifier=graphene.String(required=True))
    predict_parking = graphene.String(
        required=True, datetime=graphene.DateTime(required=True)
    )

    def resolve_me(self, info):
        return get_me(info)

    def resolve_health(self, info):
        return HealthType.get_health()

    def resolve_all_parkings(self, info):
        return get_parkings(info)

    def resolve_parking(self, info, identifier):
        return get_parking(info, identifier)

    def resolve_predict_parking(self, info, datetime):
        return get_prediction(info, datetime)


def _find_and_import_schema_modules():
    all_mutations = {}
    package_path = BASE_DIR
    for root, _, files in os.walk(package_path):
        if "schema.py" in files:
            module_name = os.path.relpath(os.path.join(root, "schema.py"), package_path)
            module_name = module_name.replace(os.sep, ".").replace(".py", "")
            if not APP_NAME in module_name:
                continue
            try:
                module = importlib.import_module(module_name)
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, graphene.Mutation):
                        mutation_name = name[0].lower() + name[1:]
                        mutation_name = mutation_name.replace("Mutation", "")
                        all_mutations[mutation_name] = obj
            except Exception as e:
                print(f"Error importing from {module_name}: {e}")
    return all_mutations


Mutation = type(
    "Mutation",
    (graphene.ObjectType,),
    {
        name: mutation.Field(required=True)
        for name, mutation in _find_and_import_schema_modules().items()
    },
)


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)

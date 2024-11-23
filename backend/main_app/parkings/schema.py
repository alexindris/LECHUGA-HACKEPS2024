import graphene

from main_app.parkings.actions import create_parking
from main_app.parkings.getter import get_all_parkings
from main_app.parkings.models import Parking


class ParkingID(graphene.Scalar):
    @staticmethod
    def serialize(value):
        return str(value.unique_id)

    @staticmethod
    def parse_literal(node):
        return ParkingID.parse_value(node.value)

    @staticmethod
    def parse_value(value):
        return Parking.objects.get(unique_id=value)


class ParkingType(graphene.ObjectType):
    identifier = graphene.Field(ParkingID, required=True)
    name = graphene.String(required=True)
    address = graphene.String(required=True)
    total_lots = graphene.Int(required=True)
    occupied_lots = graphene.Int(required=True)

    @staticmethod
    def get_from_parking(parking):
        return ParkingType(
            identifier=parking,
            name=parking.name,
            address=parking.address,
            total_lots=parking.total_lots,
            occupied_lots=parking.occupied_lots,
        )


def get_parkings(info):
    viewer_context = info.context.viewer_context

    output = [
        ParkingType.get_from_parking(parking)
        for parking in get_all_parkings(viewer_context)
    ]

    return output


class CreateParkingMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        total_lots = graphene.Int(required=True)

    parking = graphene.Field(ParkingType, required=True)

    @staticmethod
    def mutate(root, info, name, address, total_lots):
        viewer_context = info.context.viewer_context
        parking = create_parking(viewer_context, name, address, total_lots)
        return CreateParkingMutation(parking=ParkingType.get_from_parking(parking))

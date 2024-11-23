import graphene

from main_app.parkings.actions import create_parking
from main_app.parkings.getter import get_all_parkings, get_parking_by_id
from main_app.parkings.models import Parking


class ParkingStatusEnum(graphene.Enum):
    ENTRANCE = "ENTRANCE"
    EXIT = "EXIT"


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


class ParkingEntry(graphene.ObjectType):
    entry_type = graphene.Field(ParkingStatusEnum, required=True)
    created_at = graphene.DateTime(required=True)

    @staticmethod
    def get_from_entry(entry):
        return ParkingEntry(entry_type=entry.entry_type, created_at=entry.created_at)


class ParkingType(graphene.ObjectType):
    identifier = graphene.Field(ParkingID, required=True)
    name = graphene.String(required=True)
    address = graphene.String(required=True)
    total_lots = graphene.Int(required=True)
    occupied_lots = graphene.Int(required=True)
    entries = graphene.List(ParkingEntry, required=True)

    @staticmethod
    def get_from_parking(parking):
        return ParkingType(
            identifier=parking,
            name=parking.name,
            address=parking.address,
            total_lots=parking.total_lots,
            occupied_lots=parking.occupied_lots,
        )

    def resolve_entries(self, info):

        return [
            ParkingEntry.get_from_entry(entry)
            for entry in self.identifier.get_entries()
        ]


def get_parkings(info):
    viewer_context = info.context.viewer_context

    output = [
        ParkingType.get_from_parking(parking)
        for parking in get_all_parkings(viewer_context)
    ]

    return output


def get_parking(info, identifier):
    viewer_context = info.context.viewer_context

    return ParkingType.get_from_parking(get_parking_by_id(viewer_context, identifier))


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

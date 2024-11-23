import graphene

from infrastructure.errors.errors import NotAuthorizedActionError
from main_app.accounts.actions import create_user, create_user_token
from main_app.accounts.models import User


class UserID(graphene.Scalar):
    @staticmethod
    def serialize(user):
        return str(user.username)

    @staticmethod
    def parse_literal(node):
        return UserID.parse_value(node.value)

    @staticmethod
    def parse_value(value):
        return User.objects.get(username=value)


class UserType(graphene.ObjectType):
    identifier = graphene.Field(UserID, required=True)
    name = graphene.String(required=True)
    email = graphene.String(required=True)

    @staticmethod
    def get_from_user(viewer_context, user):
        return UserType(
            identifier=user,
            name=user.name,
            email=user.email,
        )


def get_me(info):
    viewer_context = info.context.viewer_context
    if not viewer_context.is_identified():
        raise NotAuthorizedActionError()

    return UserType.get_from_user(viewer_context, viewer_context.identified_user())


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType, required=True)

    @staticmethod
    def mutate(root, info, name, email, password):
        viewer_context = info.context.viewer_context
        user = create_user(viewer_context, name, email, password)
        return CreateUserMutation(
            user=UserType.get_from_user(info.context.viewer_context, user)
        )


class LoginUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String(required=True)

    def mutate(self, info, email, password):
        token = create_user_token(info.context.viewer_context, email, password)

        return LoginUserMutation(token=token)

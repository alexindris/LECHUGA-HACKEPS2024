import graphene

from main_app.device.action import _unregister_device, register_device


class RegisterDeviceMutation(graphene.Mutation):
    class Arguments:
        push_token = graphene.String(required=True)

    success = graphene.Boolean(required=True)

    def mutate(self, info, push_token: str):
        register_device(
            info.context.viewer_context,
            push_token,
        )
        return RegisterDeviceMutation(success=True)


class UnregisterDeviceMutation(graphene.Mutation):
    class Arguments:
        push_token = graphene.String(required=True)

    success = graphene.Boolean(required=True)

    def mutate(self, info, push_token: str):
        _unregister_device(
            info.context.viewer_context,
            push_token,
        )
        return UnregisterDeviceMutation(success=True)

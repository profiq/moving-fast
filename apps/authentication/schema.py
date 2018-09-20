import graphene
from graphene_django.types import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        only_fields = ("id", "username", "email", "first_name", "last_name")


class Query:
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int(), username=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        user_id = kwargs.get("id")
        username = kwargs.get("username")

        if user_id is not None:
            return User.objects.get(id=user_id)

        if username is not None:
            return User.objects.get(username=username)

        return None

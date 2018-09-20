import graphene

from apps.authentication.schema import Query as AuthenticationQuery
from apps.chat.schema import Query as ChatQuery


class Query(AuthenticationQuery, ChatQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

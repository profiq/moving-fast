import graphene

import apps.authentication.schema
import apps.chat.schema


class Query(apps.authentication.schema.Query, apps.chat.schema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

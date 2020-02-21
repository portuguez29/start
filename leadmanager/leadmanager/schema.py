import graphene
from leads.schema import Query as iQuery


class Query(iQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
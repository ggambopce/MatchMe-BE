# graphql_router/schema.py

import strawberry
from graphql_router.profile.mutation import Mutation
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        return "pong"

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))
graphql_app = GraphQLRouter(schema)

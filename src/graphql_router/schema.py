import strawberry
from graphql_router.profile.query import Query
from graphql_router.profile.mutation import Mutation
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

# Strawberry를 사용해서 GraphQL 스키마를 정의하고
# 이를 FastAPI 라우터(GraphQLRouter)로 등록할 수 있게 해줌

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))
graphql_app = GraphQLRouter(schema)

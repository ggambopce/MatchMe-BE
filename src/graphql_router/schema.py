import strawberry
from graphql_router.profile.query import Query
from graphql_router.profile.mutation import ProfileMutation
from graphql_router.match.mutation import MatchMutation
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

# GraphQL 전체 스키마를 정의하고 query, mutation 등을 통합한다.
# Strawberry를 사용해서 GraphQL 스키마를 정의하고
# 이를 FastAPI 라우터(GraphQLRouter)로 등록할 수 있게 해줌
# 각 타입, 리졸버를 묶어 하나의 Schema 객체로 생성
@strawberry.type
class Mutation(ProfileMutation, MatchMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))
graphql_app = GraphQLRouter(schema)

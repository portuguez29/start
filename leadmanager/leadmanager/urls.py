from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False, schema=schema))),
    path('graphiql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

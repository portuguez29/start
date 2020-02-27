from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
    path('Dadmin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False, schema=schema))),
    path('graphiql/', GraphQLView.as_view(graphiql=True, schema=schema)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

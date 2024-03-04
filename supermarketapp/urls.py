from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from rest_framework.routers import DefaultRouter    
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

router.register('category', CategoryViewset)
router.register('subcategory', SubcategoryViewset)
router.register('item', ItemViewset)
router.register('userregistration', MyUserViewset)


schema_view = get_schema_view(
   openapi.Info(
      title="Supermarket API",
      default_version='v1',
      description="Supermarket api description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('',include(router.urls)),
    path('auth', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    

]    



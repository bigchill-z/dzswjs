"""
URL configuration for dzswjs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions, routers
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView, SpectacularSwaggerView

# schema_view = get_schema_view(
#     openapi.Info(
#         title="电子商务技术作业接口文档",
#         default_version="v1",
#         description="电子商务技术作业接口文档",
#         terms_of_service="",
#         contact=openapi.Contact(email="zmrenwu@163.com"),
#         license=openapi.License(name="GPLv3 License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.ranks.urls')),
    path('swagger/json/', SpectacularJSONAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('swagger/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

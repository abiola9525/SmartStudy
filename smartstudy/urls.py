from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views

from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="SmartStudy API",
        default_version="v1.0.0",
        description="API for SmartStudy.",
        contact= openapi.Contact(email="omotoso.rauf@oratech.com.ng"),
        license= openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    
    path('api/account/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/account/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc'), name='schema-redoc'),
]

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from maqolalar.views import MaqolalarAPIView, MaqolalarimAPIView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),

    path('maqolalar/', MaqolalarAPIView.as_view()),
    path('maqolalarim/', MaqolalarimAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

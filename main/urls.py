from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import main, login, sign_up, learning, panel, logout


urlpatterns = [
    path('', main),
    path('account/login/', login),
    path('account/signup/', sign_up),
    path('account/logout/', logout),
    path('panel/', panel),
    path('learning/', learning),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

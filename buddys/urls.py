from django.conf.urls import url
from django.contrib import admin
from buddysapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^dispensary/sign-in/$', auth_views.login,
    {'template_name': 'dispensary/sign-in.html'},
    name = 'dispensary-sign-in'),
    url(r'^dispensary/sign-out', auth_views.logout,
    {'next_page': '/'},
    name = 'dispensary-sign-out'),
    url(r'^dispensary/signup', views.dispensary_sign_up,
    name = 'dispensary-signup'),
    url(r'^dispensary/$', views.dispensary_home, name = 'dispensary-home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url, include
from django.contrib import admin
from buddysapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    #Dispensaries
    url(r'^dispensary/sign-in/$', auth_views.login,
    { 'template_name': 'dispensary/sign-in.html'},
    name = 'dispensary-sign-in'),
    url(r'^dispensary/sign-out', auth_views.logout,
    {'next_page': '/'},
    name = 'dispensary-sign-out'),
    url(r'^dispensary/signup', views.dispensary_sign_up,
    name = 'dispensary-signup'),
    url(r'^dispensary/$', views.dispensary_home, name = 'dispensary-home'),

    url(r'^dispensary/account/$', views.dispensary_account, name = 'dispensary-account'),
    url(r'^dispensary/products/$', views.dispensary_products, name = 'dispensary-products'),
    url(r'^dispensary/products/add/$', views.dispensary_add_products, name = 'dispensary-add-products'),
    url(r'^dispensary/orders/$', views.dispensary_orders, name = 'dispensary-orders'),
    url(r'^dispensary/reports/$', views.dispensary_reports, name = 'dispensary-reports'),

    #SignIn/Signout
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    #/convert-token (signin/Sign Up)
    #/revoke-token (signout)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

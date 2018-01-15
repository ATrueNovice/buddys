from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from buddysapp import views, apis


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
    url(r'^dispensary/product/$', views.dispensary_product, name = 'dispensary-product'),
    url(r'^dispensary/product/add/$', views.dispensary_add_product, name = 'dispensary-add-product'),
    url(r'^dispensary/product/edit/(?P<product_id>\d+)/$', views.dispensary_edit_product, name = 'dispensary-edit-product'),
    url(r'^dispensary/orders/$', views.dispensary_orders, name = 'dispensary-orders'),
    url(r'^dispensary/reports/$', views.dispensary_reports, name = 'dispensary-reports'),

    #SignIn/Signout
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    #/convert-token (signin/Sign Up)
    #/revoke-token (signout)

    url(r'^api/customer/dispensary/$', apis.customer_get_dispensary)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

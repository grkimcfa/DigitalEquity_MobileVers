from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Need to specify my urls to be used within this project
urlpatterns = [
    path('', views.index, name='index'),
    # Pages for forms
    path('address', views.address, name='address'),
    path('account', views.account, name='account'),
    path('finances', views.finances, name='finances'),
    path('programs', views.programs, name='programs'),
    

    # Available/NotAvailable Digital equity in your area
    path('available', views.available, name='available'),
    path('notAvailable', views.notAvailable, name='notAvailable'),
    path('addressCorrection', views.addressCorrection, name='addressCorrection'),
    path('n2n', views.n2n, name='n2n'),
    path('GRQuickApply', views.GRQuickApply, name='GRQuickApply'),
    # May qualify page
    path('mayQualify', views.mayQualify, name='mayQualify'),
    path('takeUSPSaddress', views.takeUSPSaddress, name='takeUSPSaddress'),
    path('privacyPolicy', views.privacyPolicy, name='privacyPolicy'),
    path('dependentInfo', views.dependentInfo, name='dependentInfo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #this is needed to get file uploads to work! 

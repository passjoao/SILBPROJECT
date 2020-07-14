"""silb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()

router.register(r'api/v1/request', RequestViewset)
router.register(r'api/v1/authority', AuthorityViewset)
router.register(r'api/v1/captaincy', CaptaincyViewset)
router.register(r'api/v1/confirmation', ConfirmationViewset)
router.register(r'api/v1/deferment', DefermentViewset)
router.register(r'api/v1/demands', DemandsViewset)
router.register(r'api/v1/files', FilesViewset)
router.register(r'api/v1/image', ImageViewset)
router.register(r'api/v1/justifications', JustificationViewset)
router.register(r'api/v1/landrecord', LandRecordViewset)
router.register(r'api/v1/owner', OwnerViewset)
router.register(r'api/v1/religiousorder', ReligiousOrderViewset)
router.register(r'api/v1/tramitations', TramitationsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('core.urls')),
    path('', include(router.urls)),
]

urlpatterns += [
    path('conta/', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

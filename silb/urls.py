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
    path('', include(router.urls)),
]

urlpatterns += [
    path('conta/', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
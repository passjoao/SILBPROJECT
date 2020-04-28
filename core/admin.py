from django.contrib import admin

from core.models import (Owner, ReligiousOrder, Captaincy, LandRecord,
                         Request, Justification, Demands, Authority,
                         Confirmation, Deferment, Demands, LandHistory,
                         ReligiousOrder, Titles, Tramitations)

admin.site.register(Tramitations)
admin.site.register(Authority)
admin.site.register(Confirmation)
admin.site.register(Deferment)
admin.site.register(Owner)
admin.site.register(ReligiousOrder)
admin.site.register(Captaincy)
admin.site.register(Justification)
admin.site.register(Demands)
@admin.register(LandRecord)
class LandRecordAdmin(admin.ModelAdmin):
    verbose_name = "Sesmaria"

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    filter_horizontal = ('justification', 'demands', 'owners')
    verbose_name = "Requisição"

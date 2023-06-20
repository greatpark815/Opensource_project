from django.contrib import admin
from .models import NC_skyField
from .models import FC_football_Center
from .models import Jangseong_Field
# Register your models here.

class NC_skyFieldAdmin(admin.ModelAdmin):
    search_fields=['match_Time']
    
class FC_football_CenterAdmin(admin.ModelAdmin):
    search_fields=['match_Time']
    
class Jangseong_FieldAdmin(admin.ModelAdmin):
    search_fields=['match_Time']

admin.site.register(NC_skyField,NC_skyFieldAdmin)
admin.site.register(FC_football_Center,FC_football_CenterAdmin)
admin.site.register(Jangseong_Field,Jangseong_FieldAdmin)
 
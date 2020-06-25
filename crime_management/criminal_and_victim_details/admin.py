from django.contrib import admin
from criminal_and_victim_details.models import VictimDetail,CriminalDetail,CriminalDetailAddress,VictimDetailAddress
# Register your models here.


admin.site.register(VictimDetail)

admin.site.register(CriminalDetail)

admin.site.register(CriminalDetailAddress)

admin.site.register(VictimDetailAddress)
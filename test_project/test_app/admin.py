from django.contrib import admin
from .models import TypesOfWorkDO, TransgazList, ActivitiesDO, StructuralSubdivision, ReportingYear, AccountBalance, \
    Bookkeeping, Lpumg, ProductionDepartment

admin.site.register(TypesOfWorkDO)
admin.site.register(TransgazList)
admin.site.register(ActivitiesDO)
admin.site.register(StructuralSubdivision)
admin.site.register(ReportingYear)
admin.site.register(AccountBalance)
admin.site.register(Bookkeeping)
admin.site.register(Lpumg)
admin.site.register(ProductionDepartment)

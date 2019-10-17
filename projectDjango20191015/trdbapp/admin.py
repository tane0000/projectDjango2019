from django.contrib import admin

# Register your models here.
from .models import Trouble
from .models import Product, Bruser, Brmachine
from .models import Acceptedmethod, Actioncategory, Suspendcategory, Disposalcategory
from .models import TroubleStatus, ControlStatus

@admin.register(Trouble)
@admin.register(Product)
@admin.register(Bruser)
@admin.register(Brmachine)
@admin.register(Acceptedmethod)
@admin.register(Actioncategory)
@admin.register(Suspendcategory)
@admin.register(Disposalcategory)
@admin.register(TroubleStatus)
@admin.register(ControlStatus)

class TroubleAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class BruserAdmin(admin.ModelAdmin):
    pass

class BrmachineAdmin(admin.ModelAdmin):
    pass

class AcceptedmethodAdmin(admin.ModelAdmin):
    pass

class ActioncategoryAdmin(admin.ModelAdmin):
    pass

class SuspendcategoryAdmin(admin.ModelAdmin):
    pass

class DisposalcategoryAdmin(admin.ModelAdmin):
    pass

class TroubleStatusAdmin(admin.ModelAdmin):
    pass

class ControlStatusAdmin(admin.ModelAdmin):
    pass


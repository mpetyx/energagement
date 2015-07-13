from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Plug, BuildingCounter, StreetLightingCounter, ElectricVehicleCounter, Sensor, Value, Buffer, Building, StreetLighting, ElectricVehicle, StreetLighting1

class ValueAdmin(admin.ModelAdmin):
    pass

class PlugAdmin(admin.ModelAdmin):
    pass

class BuildingCounterAdmin(admin.ModelAdmin):
    pass

class StreetLightingCounterAdmin(admin.ModelAdmin):
    pass

class ElectricVehicleCounterAdmin(admin.ModelAdmin):
    pass

class SensorAdmin(admin.ModelAdmin):
    pass

class BufferAdmin(admin.ModelAdmin):
    pass

class BuildingAdmin(admin.ModelAdmin):
    pass

class StreetLightingAdmin(admin.ModelAdmin):
    pass

class ElectricVehicleAdmin(admin.ModelAdmin):
    pass

class StreetLighting1Admin(admin.ModelAdmin):
    pass


admin.site.register(Value, ValueAdmin)
admin.site.register(Plug, PlugAdmin)
admin.site.register(BuildingCounter, BuildingCounterAdmin)
admin.site.register(StreetLightingCounter, StreetLightingCounterAdmin)
admin.site.register(ElectricVehicleCounter, ElectricVehicleCounterAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Buffer, BufferAdmin)
admin.site.register(Building, SensorAdmin)
admin.site.register(ElectricVehicle, ElectricVehicleAdmin)
admin.site.register(StreetLighting, StreetLightingAdmin)
admin.site.register(StreetLighting1, StreetLighting1Admin)

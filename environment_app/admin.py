from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Sw, Ip, Plataforma, Hw, Responsable, Departamento, Modulo, Submodulo,ResponsableSistema, Sistema
# Clase ModelAdmin para Departamento
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id_departamento','nombre_departamento']
    search_fields = ['nombre_departamento']

admin.site.register(Departamento, DepartamentoAdmin)

# Clase ModelAdmin para Hw
class HwAdmin(admin.ModelAdmin):
    list_display = ['id_hw', 'url_hw', 'user_hw','password_hw', 'puerto_hw','direccion_fisica']
    search_fields = ['ip_hw','url_hw', 'user_hw','password_hw', 'puerto_hw','direccion_fisica']
    list_filter = ['ip_hw','url_hw', 'user_hw','password_hw', 'puerto_hw','direccion_fisica']

admin.site.register(Hw, HwAdmin)

# Clase ModelAdmin para Ip
class IpAdmin(admin.ModelAdmin):
    list_display = ['id_ip','ip','puerto']
    search_fields = ['ip','puerto']
    list_filter = ['ip','puerto']

admin.site.register(Ip, IpAdmin)

# Clase ModelAdmin para Plataforma
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['nombre_plataforma', 'tipo_ambiente_plataforma','tipo_servidor_plataforma', 'tipo_motor_bd', 'nombre_esquema_bd','nombre_instancia_bd']
    search_fields = ['nombre_plataforma', 'tipo_ambiente_plataforma','tipo_servidor_plataforma', 'tipo_motor_bd', 'nombre_esquema_bd','nombre_instancia_bd']
    list_filter = ['nombre_plataforma','nombre_esquema_bd', 'nombre_instancia_bd']

admin.site.register(Plataforma, PlataformaAdmin)


# Clase ModelAdmin para Modulo
class ModuloAdmin(admin.ModelAdmin):
    list_display = ['id_modulo', 'nombre_modulo']
    search_fields = ['nombre_modulo']
    list_filter = ['nombre_modulo']

admin.site.register(Modulo, ModuloAdmin)

# Clase ModelAdmin para Responsable
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ['id_responsable','nombre_responsable']
    search_fields = ['nombre_responsable']
    list_filter = ['nombre_responsable']

admin.site.register(Responsable, ResponsableAdmin)


# Clase ModelAdmin para Sistema
class SistemaAdmin(admin.ModelAdmin):
    list_display = ['id_sistema','nombre_sistema']
    search_fields = ['nombre_sistema']
    list_filter = ['nombre_sistema']

admin.site.register(Sistema, SistemaAdmin)

# Clase ModelAdmin para Submodulo
class SubmoduloAdmin(admin.ModelAdmin):
    list_display = ['id_submodulo', 'nombre_submodulo']
    search_fields = ['nombre_submodulo']
    list_filter = ['nombre_submodulo']

admin.site.register(Submodulo, SubmoduloAdmin)

# Clase ModelAdmin para Sw
class SwAdmin(admin.ModelAdmin):

    list_display = ['id_sw', 'tipo_sw', 'endpoint_sw', 'url_sw',]
    search_fields = ['tipo_sw', 'endpoint_sw', 'url_sw', 'user_sw', 'password_sw']
    list_filter = ['tipo_sw', 'endpoint_sw', 'url_sw', 'user_sw', 'password_sw']

admin.site.register(Sw, SwAdmin)
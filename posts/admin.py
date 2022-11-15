from django.contrib import admin
from users.models import Profile

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.



"""
Documentación
https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
"""
#admin.site.register(Profile)

#Decorador
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','phone_number', 'website', 'picture')#Listado de informacion
    list_editable=('website','picture') #Editarlos desde la lista mostrada
    list_display_links=('user', 'phone_number')#Leva al detalle
    search_fields = ('user__email', 'user__first_name')
    list_filter = ('created', 'modified','user__is_active', 'user__is_staff')
    fieldsets = (
        ('Profile',{
            'fields':('user','picture'),
        }),
        #Puede ser none y asi no muestra un separador con titulo
        ('Extra info',{
            'fields':(('website','phone_number'),
                    ('biography'))
        })
    )

    readonly_fields = (
        'created', 'modified', 'user'
    )

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete=False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email'
        'first_name'
        'last_name',
        'is_active',
        'is_staff'
    )

"""
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
"""
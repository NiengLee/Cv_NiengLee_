from django.contrib import admin
from .models import msg_user

# Register your models here.
class msg_userAdmin(admin.ModelAdmin):
    list_display=("nombre", "mail", "asunto")
    search_fields=("nombre", "mail")

admin.site.register(msg_user, msg_userAdmin)
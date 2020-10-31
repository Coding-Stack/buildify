from django.contrib import admin

# Register your models here.
from .models import Client,Worker,Admin,Plan,Construction,Material

admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Admin)
admin.site.register(Plan)
admin.site.register(Construction)
admin.site.register(Material)
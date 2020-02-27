from django.contrib import admin

# Register your models here.
from .models import Permission, Role, User, Lawyer, Assistant, Client, Type_case, Case, Schedule, Record, Payment

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Lawyer)
admin.site.register(Assistant)
admin.site.register(Client)
admin.site.register(Type_case)
admin.site.register(Case)
admin.site.register(Schedule)
admin.site.register(Record)
admin.site.register(Payment)
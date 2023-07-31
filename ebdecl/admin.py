from django.contrib import admin

from .models import *
admin.site.register(Decl)
admin.site.register(Firm)
admin.site.register(Decl_type)
admin.site.register(Decl_status)
admin.site.register(Payment_invoice_status)
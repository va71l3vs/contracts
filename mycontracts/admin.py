from django.contrib import admin

from django.contrib import admin
from .models import Post, Departments, Contracts, Published_contracts, Revisor


admin.site.register(Post)
admin.site.register(Departments)
admin.site.register(Contracts)
admin.site.register(Published_contracts)
admin.site.register(Revisor)


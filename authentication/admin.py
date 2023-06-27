from django.contrib import admin

from authentication.models import User, Location
from ads.models import Ad, Category

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Ad)
admin.site.register(Category)

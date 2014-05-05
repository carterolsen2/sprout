from django.contrib import admin
from .models import *


''' Register Admin layouts into django'''
# admin.site.register(__MODEL-NAME__)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
# admin.site.register(Photo)
#below line12; I added that because it seemed like a good idea...
# admin.site.register(Favorite)
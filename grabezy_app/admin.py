from django.contrib import admin
from django.db import models
from .models import Electronic,Grocery,Fashion,Contact
# Register your models here.
admin.site.register(Contact),
admin.site.register(Fashion),
admin.site.register(Grocery),
admin.site.register(Electronic)
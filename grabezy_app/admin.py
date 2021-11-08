from django.contrib import admin
from django.db import models
from .models import Electronic,Feedback,Grocery,Fashion,Contact, Order, OrderUpdate
# Register your models here.
admin.site.register(Contact),
admin.site.register(Fashion),
admin.site.register(Grocery),
admin.site.register(Electronic),
admin.site.register(Order),
admin.site.register(OrderUpdate),
admin.site.register(Feedback)
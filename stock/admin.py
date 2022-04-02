from django.contrib import admin

# Register your models here.
from .models import CoAction, StockData, CorpActionRecord, UserPhone

admin.site.register(CoAction)
admin.site.register(StockData)
admin.site.register(CorpActionRecord)
admin.site.register(UserPhone)

from django.contrib import admin
from .models import SampleModel,BlogModel, Category


admin.site.register(SampleModel)
admin.site.register(BlogModel)
admin.site.register(Category)
from django.contrib import admin
from django.apps import apps




admin.site.site_header = 'LookCut'

app = apps.get_app_config('api')

for model_name, model in app.models.items():
    admin.site.register(model)
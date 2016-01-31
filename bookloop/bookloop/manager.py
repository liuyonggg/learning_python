from django.contrib.admin import ModelAdmin

class ModelManager(ModelAdmin):
    def __init__(self, model):

model_manager = ModelManager()
